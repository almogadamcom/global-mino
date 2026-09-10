const fs=require('node:fs');const path=require('node:path');
const root=path.join(__dirname,'..');
if(fs.existsSync(path.join(root,'.env')))process.loadEnvFile(path.join(root,'.env'));
async function main(){
 const token=process.env.SUPABASE_ACCESS_TOKEN;
 if(!token)throw Error('Add SUPABASE_ACCESS_TOKEN to your local .env to apply the migration.');
 const url=new URL(process.env.SUPABASE_URL);const ref=url.hostname.split('.')[0];
 if(!/^[a-z0-9]+$/.test(ref)||!url.hostname.endsWith('.supabase.co'))throw Error('Expected your Supabase project URL.');
 if((process.env.SUPABASE_ENQUIRIES_TABLE||'enquiries')!=='enquiries')throw Error('This migration creates enquiries; set SUPABASE_ENQUIRIES_TABLE=enquiries.');
 const endpoint=`https://api.supabase.com/v1/projects/${ref}/database/query`;
 async function query(sql){const r=await fetch(endpoint,{method:'POST',headers:{Authorization:`Bearer ${token}`,'Content-Type':'application/json'},body:JSON.stringify({query:sql}),signal:AbortSignal.timeout(30000)});if(!r.ok)throw Error(`Supabase migration request failed (HTTP ${r.status}). Check the token's project and database permissions.`);return r.json()}
 const existing=await query("select to_regclass('public.enquiries') as table_name");
 if(existing[0]?.table_name){console.log('The enquiries table already exists; no schema changes applied.');return}
 const sql=fs.readFileSync(path.join(root,'supabase/migrations/202609110001_create_enquiries.sql'),'utf8');
 await query(sql);
 const check=await query("select relrowsecurity from pg_class where oid='public.enquiries'::regclass");
 if(check[0]?.relrowsecurity!==true)throw Error('Table created but row security verification failed.');
 console.log('Created enquiries table and verified row level security.');
}
main().catch(error=>{console.error(error.message);process.exitCode=1});
