// Read-only enquiry feed for the /admin dashboard.
// The Supabase service key never leaves the server; the browser only ever
// sees rows it has already authenticated for.
const {timingSafeEqual}=require('node:crypto');

function authorised(req){
 const expected=process.env.ADMIN_TOKEN;
 if(!expected||expected.length<16)return false;
 const header=req.headers.authorization||'';
 const supplied=header.startsWith('Bearer ')?header.slice(7):'';
 const a=Buffer.from(supplied),b=Buffer.from(expected);
 return a.length===b.length&&timingSafeEqual(a,b);
}

module.exports=async(req,res)=>{
 res.setHeader('Cache-Control','no-store');
 res.setHeader('X-Robots-Tag','noindex, nofollow');
 if(req.method!=='GET')return res.status(405).json({error:'Method not allowed'});
 if(!authorised(req))return res.status(401).json({error:'Not authorised'});

 const url=process.env.SUPABASE_URL,key=process.env.SUPABASE_SERVICE_ROLE_KEY;
 const table=process.env.SUPABASE_ENQUIRIES_TABLE||'enquiries';
 if(!url||!key||!/^[a-z_][a-z0-9_]*$/.test(table))return res.status(503).json({error:'Enquiry storage is not configured'});

 try{
  const endpoint=new URL(`/rest/v1/${table}?select=*&order=created_at.desc&limit=500`,url);
  if(endpoint.protocol!=='https:')return res.status(503).json({error:'Enquiry storage is not configured'});
  const response=await fetch(endpoint,{
   headers:{apikey:key,...(key.startsWith('eyJ')?{Authorization:`Bearer ${key}`}:{}),Accept:'application/json'},
   signal:AbortSignal.timeout(10000)
  });
  if(!response.ok)return res.status(502).json({error:'Enquiries could not be loaded'});
  return res.status(200).json({rows:await response.json()});
 }catch{return res.status(502).json({error:'Enquiries could not be loaded'})}
};
