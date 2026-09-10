function configuration(env=process.env){
 const key=env.SUPABASE_SERVICE_ROLE_KEY,url=env.SUPABASE_URL,table=env.SUPABASE_ENQUIRIES_TABLE||'enquiries';
 if(!key||!url||! /^[a-z_][a-z0-9_]*$/.test(table))return null;
 try{const endpoint=new URL('/rest/v1/'+table,url);if(endpoint.protocol!=='https:')return null;return {endpoint,key}}catch{return null}
}
async function saveEnquiry(payload,{env=process.env,fetcher=fetch}={}){
 const config=configuration(env);if(!config)return {status:503,error:'Enquiry storage is not configured'};
 try{
 const response=await fetcher(config.endpoint,{method:'POST',headers:{apikey:config.key,...(config.key.startsWith('eyJ')?{Authorization:`Bearer ${config.key}`} : {}),'Content-Type':'application/json',Prefer:'return=minimal'},body:JSON.stringify(payload),signal:AbortSignal.timeout(10000)});
 return response.ok?{status:200,ok:true}:{status:502,error:'Enquiry could not be saved'};
 }catch{return {status:502,error:'Enquiry could not be saved'}}
}
module.exports={saveEnquiry,configuration};
