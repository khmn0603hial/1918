// Parse the shipped scripts without running the game or loading network assets.
const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
const root=path.resolve(__dirname,'..'),html=fs.readFileSync(path.join(root,'index.html'),'utf8');
let count=0;
for(const match of html.matchAll(/<script\b[^>]*>([\s\S]*?)<\/script>/gi)){
  new vm.Script(match[1],{filename:`index.html:inline-${++count}`});
}
if(!count)throw Error('No inline scripts found');
console.log(`${count} inline scripts parsed successfully.`);
