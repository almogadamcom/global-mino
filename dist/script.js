const header=document.querySelector('header');
const menu=document.querySelector('.menu-toggle');
const nav=document.querySelector('nav');
const backdrop=document.querySelector('.menu-backdrop');
const mobile=matchMedia('(max-width: 760px)');
function updateHeader(){header.classList.toggle('solid',scrollY>30)}
addEventListener('scroll',updateHeader,{passive:true});updateHeader();
function closeMenu(){
 nav.classList.remove('open');document.body.classList.remove('menu-open');backdrop.hidden=true;
 menu.setAttribute('aria-expanded','false');menu.setAttribute('aria-label','Open navigation');
 nav.querySelectorAll('details').forEach(d=>d.open=false);
}
menu.addEventListener('click',()=>{
 if(nav.classList.contains('open'))return closeMenu();
 nav.classList.add('open');document.body.classList.add('menu-open');backdrop.hidden=false;
 menu.setAttribute('aria-expanded','true');menu.setAttribute('aria-label','Close navigation');
});
backdrop.addEventListener('click',closeMenu);mobile.addEventListener('change',closeMenu);
nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',closeMenu));
nav.querySelectorAll('details').forEach(d=>d.addEventListener('toggle',()=>{if(d.open)nav.querySelectorAll('details').forEach(other=>{if(other!==d)other.open=false})}));
document.addEventListener('click',e=>{if(!header.contains(e.target))closeMenu()});
document.addEventListener('keydown',e=>{
 if(e.key==='Escape'){
  const opened=nav.querySelector('details[open]');
  if(opened){opened.open=false;opened.querySelector('summary').focus()}
  else if(nav.classList.contains('open')){closeMenu();menu.focus()}
 }
 if(e.key==='Tab'&&mobile.matches&&nav.classList.contains('open')){
  const elements=[menu,...nav.querySelectorAll('a,summary')].filter(el=>el.getClientRects().length);
  const first=elements[0],last=elements.at(-1);
  if(e.shiftKey&&document.activeElement===first){e.preventDefault();last.focus()}
  else if(!e.shiftKey&&document.activeElement===last){e.preventDefault();first.focus()}
 }
});
nav.addEventListener('focusout',()=>setTimeout(()=>{if(!nav.contains(document.activeElement))nav.querySelectorAll('details').forEach(d=>d.open=false)},0));
document.querySelector('#credits-open').addEventListener('click',()=>document.querySelector('#credits-dialog').showModal());
document.querySelectorAll('dialog').forEach(dialog=>{
 dialog.querySelector('.dialog-close').addEventListener('click',()=>dialog.close());
 dialog.addEventListener('click',event=>{if(event.target===dialog){const r=dialog.getBoundingClientRect();if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom)dialog.close()}});
});
if(!matchMedia('(prefers-reduced-motion: reduce)').matches&&'IntersectionObserver'in window){
 const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('visible');observer.unobserve(entry.target)}}),{threshold:.08});
 document.querySelectorAll('.about-grid,.section-heading,.service,.project').forEach(element=>{element.classList.add('reveal');observer.observe(element)});
}
const filters=[...document.querySelectorAll('[data-filter]')];
function filterProjects(value,updateURL=false){
 if(!filters.some(button=>button.dataset.filter===value))value='all';
 filters.forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.filter===value)));
 let count=0;document.querySelectorAll('.listing .project').forEach(p=>{p.hidden=value!=='all'&&p.dataset.country!==value;if(!p.hidden)count++});
 document.querySelector('#filter-status').textContent=`${count} project placeholder${count===1?'':'s'} shown.`;
 if(updateURL){const url=new URL(location.href);if(value==='all')url.searchParams.delete('country');else url.searchParams.set('country',value);history.pushState(null,'',url)}
}
if(filters.length){filterProjects(new URLSearchParams(location.search).get('country')||'all');filters.forEach(button=>button.addEventListener('click',()=>filterProjects(button.dataset.filter,true)));addEventListener('popstate',()=>filterProjects(new URLSearchParams(location.search).get('country')||'all'))}
// Let the complete project image open the same detail page as its text link.
document.querySelectorAll('.project').forEach(project=>{
 const target=project.querySelector('a.text-link'),picture=project.querySelector('.project-image');
 if(target&&picture){const anchor=document.createElement('a');anchor.href=target.href;anchor.setAttribute('aria-label',`View ${project.querySelector('h3').textContent} — ${project.querySelector('.eyebrow').textContent}`);picture.replaceWith(anchor);anchor.append(picture)}
});
const form=document.querySelector('#contact-form');
if(form){
 const params=new URLSearchParams(location.search),status=document.querySelector('#form-status');
 for(const name of ['country','interest'])if([...form.elements[name].options].some(o=>o.value===params.get(name)))form.elements[name].value=params.get(name);
 if(/^project-0[1-3]$/.test(params.get('project')||''))form.elements.message.value=`I would like to discuss ${params.get('project')}.`;
 const fields=[...form.querySelectorAll('input,select,textarea')];
 form.noValidate=true;
 function validate(field){
  field.setCustomValidity('');
  if(field.required&&!field.value.trim())field.setCustomValidity('Please complete this field.');
  if(field.name==='message'&&field.value.trim().length<10)field.setCustomValidity('Please enter at least 10 characters.');
  let error=field.parentElement.querySelector('.field-error');
  if(!error){error=document.createElement('span');error.className='field-error';error.id=field.name+'-error';field.parentElement.append(error);field.setAttribute('aria-describedby',[field.getAttribute('aria-describedby'),error.id].filter(Boolean).join(' '))}
  error.textContent=field.validity.valid?'':field.validationMessage;
  field.setAttribute('aria-invalid',String(!field.validity.valid));return field.validity.valid;
 }
 fields.forEach(field=>{field.addEventListener('blur',()=>{if(field.value||field.hasAttribute('aria-invalid'))validate(field)});field.addEventListener('input',()=>{if(field.getAttribute('aria-invalid')==='true')validate(field)})});
 form.addEventListener('submit',async e=>{
  e.preventDefault();if(form.getAttribute('aria-busy')==='true')return;
  const valid=fields.map(validate);if(valid.includes(false)){status.className='error';status.textContent='Please check the highlighted fields.';fields[valid.indexOf(false)].focus();return}
  const button=form.querySelector('button[type=submit]');button.disabled=true;button.textContent='SENDING…';status.className='';status.textContent='Submitting your enquiry…';form.setAttribute('aria-busy','true');
  // Keep submitted data stable while the request is in flight.
  const payload=Object.fromEntries(new FormData(form));fields.forEach(field=>field.disabled=true);
  try{
   const response=await fetch('/api/contact',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload),signal:AbortSignal.timeout(15000)});
   if(!response.ok)throw Error(response.status===400?'Please check your enquiry details and try again.':'Your enquiry has not been sent. Please try again or email hashim@globalmino.com.');
   const result=await response.json();if(result.ok!==true)throw Error('Your enquiry could not be confirmed. Please contact hashim@globalmino.com.');
   status.className='success';status.textContent='Your enquiry has been received. Thank you for contacting Global Mino.';form.reset();fields.forEach(f=>f.removeAttribute('aria-invalid'));
  }catch(error){status.className='error';status.textContent=error.name==='TimeoutError'?'We could not confirm receipt. Please contact hashim@globalmino.com before resending. Your message remains in the form.':error.message.includes('enquiry')?error.message:'Your enquiry could not be confirmed. Please contact hashim@globalmino.com. Your message remains in the form.'}
  finally{fields.forEach(field=>field.disabled=false);button.disabled=false;button.innerHTML='SEND ENQUIRY <span>↗</span>';form.removeAttribute('aria-busy');status.focus()}
 });
}
