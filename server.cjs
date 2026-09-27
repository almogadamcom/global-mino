// Load local server credentials without exposing them to static pages.
const envPath=require('node:path').join(__dirname,'.env');
if(require('node:fs').existsSync(envPath))process.loadEnvFile(envPath);
const http=require('node:http'),fs=require('node:fs/promises'),path=require('node:path');
const root=path.join(__dirname,'dist');
const {saveEnquiry}=require('./lib/enquiries.cjs');
const interests=['gold-mining','mineral-exploration','mining-consultancy','investment-opportunity','partnership','other'];
const json=(res,status,data)=>{res.writeHead(status,{'Content-Type':'application/json'});res.end(JSON.stringify(data))};
const server=http.createServer(async(req,res)=>{
try{
const url=new URL(req.url,'http://localhost');
if(url.pathname==='/api/contact'){
if(req.method!=='POST')return json(res,405,{error:'Method not allowed'});
let raw='';for await(const chunk of req){raw+=chunk;if(Buffer.byteLength(raw)>16000)return json(res,413,{error:'Request too large'})}
let data;try{data=JSON.parse(raw)}catch{return json(res,400,{error:'Invalid request'})}
if(!data||typeof data!=='object'||['name','email','country','interest','message'].some(k=>typeof data[k]!=='string'||!data[k].trim())||!/^\S+@\S+\.\S+$/.test(data.email)||data.message.trim().length<10||data.message.length>5000||!interests.includes(data.interest)||!['sudan','cameroon','central-african-republic','other'].includes(data.country))return json(res,400,{error:'Please check required fields'});
if(['name','email'].some(k=>data[k].length>200)||['company','phone'].some(k=>data[k]!==undefined&&(typeof data[k]!=='string'||data[k].length>200)))return json(res,400,{error:'Please check field lengths'});
const payload=Object.fromEntries(['name','company','email','phone','country','interest','message'].map(k=>[k,(data[k]||'').trim()]));
const result=await saveEnquiry(payload);
return json(res,result.status,result.ok?{ok:true}:{error:result.error});
}
if(!['GET','HEAD'].includes(req.method)){res.writeHead(405);return res.end()}
let file=path.resolve(root,'.'+decodeURIComponent(url.pathname));
if(file!==root&&!file.startsWith(root+path.sep)){res.writeHead(403);return res.end()}
try{if((await fs.stat(file)).isDirectory())file=path.join(file,'index.html')}catch{}
let data;try{data=await fs.readFile(file)}catch{res.statusCode=404;file=path.join(root,'404.html');data=await fs.readFile(file)}
res.setHeader('Content-Type',({'.html':'text/html; charset=utf-8','.css':'text/css','.js':'text/javascript','.jpg':'image/jpeg','.svg':'image/svg+xml','.png':'image/png','.xml':'application/xml','.txt':'text/plain','.woff2':'font/woff2'})[path.extname(file)]||'application/octet-stream');
res.setHeader('X-Content-Type-Options','nosniff');res.setHeader('Referrer-Policy','strict-origin-when-cross-origin');res.setHeader('Cache-Control',['.jpg','.png','.svg','.woff2'].includes(path.extname(file))?'public, max-age=86400':'no-cache');res.end(req.method==='HEAD'?undefined:data);
}catch{json(res,500,{error:'Request could not be completed'})}
});
server.listen(process.env.PORT||4173,'127.0.0.1',()=>console.log(`Local: http://127.0.0.1:${process.env.PORT||4173}`));
