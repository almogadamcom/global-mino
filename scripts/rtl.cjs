// Mirrored stylesheets for the Arabic edition.
// The layout CSS lives in dist/ and positions things with left/right, so the
// Arabic pages load a flipped copy from dist/rtl/ instead (build.py points
// them there). Run after build.py; re-run whenever a layout stylesheet changes.
const fs=require('node:fs'),path=require('node:path'),rtlcss=require('rtlcss');
const dist=path.join(__dirname,'..','dist'),out=path.join(dist,'rtl');
const sheets=['style.css','pages.css','countries.css','gallery.css','ceo-message.css','brand.css','site.css','home.css'];
fs.mkdirSync(out,{recursive:true});
// The small tracked capitals used for labels (8–11px) are unreadable in Arabic
// script, which has no capitals to carry them; those sizes are raised to 12px.
const legible=css=>css.replace(/font-size:\s*(\d+(?:\.\d+)?)px/g,(match,size)=>Number(size)<12?'font-size:12px':match);
for(const name of sheets){
 const source=fs.readFileSync(path.join(dist,name),'utf8');
 fs.writeFileSync(path.join(out,name),`/* Generated from /${name} by scripts/rtl.cjs. Do not edit. */\n`+legible(rtlcss.process(source)));
}
console.log(`Mirrored ${sheets.length} stylesheets into dist/rtl/.`);
