// Vercel serverless equivalent of the /api/contact route in server.cjs.
// Validation is kept identical so local and deployed behaviour match.
const {saveEnquiry}=require('../lib/enquiries.cjs');
const interests=['gold-mining','mineral-exploration','mining-consultancy','investment-opportunity','partnership','other'];
const countries=['sudan','cameroon','central-african-republic','other'];

async function readBody(req){
 if(req.body!==undefined&&req.body!==null){
  if(typeof req.body==='object')return req.body;
  try{return JSON.parse(req.body)}catch{return null}
 }
 let raw='';
 for await(const chunk of req){raw+=chunk;if(Buffer.byteLength(raw)>16000)return 413}
 try{return JSON.parse(raw)}catch{return null}
}

module.exports=async(req,res)=>{
 const json=(status,data)=>res.status(status).json(data);
 if(req.method!=='POST')return json(405,{error:'Method not allowed'});
 try{
  const data=await readBody(req);
  if(data===413)return json(413,{error:'Request too large'});
  if(!data||typeof data!=='object')return json(400,{error:'Invalid request'});
  if(['name','email','country','interest','message'].some(k=>typeof data[k]!=='string'||!data[k].trim())
   ||!/^\S+@\S+\.\S+$/.test(data.email)
   ||data.message.trim().length<10||data.message.length>5000
   ||!interests.includes(data.interest)||!countries.includes(data.country))return json(400,{error:'Please check required fields'});
  if(['name','email'].some(k=>data[k].length>200)
   ||['company','phone'].some(k=>data[k]!==undefined&&(typeof data[k]!=='string'||data[k].length>200)))return json(400,{error:'Please check field lengths'});
  const payload=Object.fromEntries(['name','company','email','phone','country','interest','message'].map(k=>[k,(data[k]||'').trim()]));
  const result=await saveEnquiry(payload);
  return json(result.status,result.ok?{ok:true}:{error:result.error});
 }catch{return json(500,{error:'Request could not be completed'})}
};
