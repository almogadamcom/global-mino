// Interface text for the French and Arabic editions; English is the fallback.
// Page copy is translated at build time, so only text written here needs entries.
const rtl=document.documentElement.dir==='rtl';
const TEXT={
 fr:{
  'Open navigation':'Ouvrir la navigation','Close navigation':'Fermer la navigation',
  '{0} project placeholder shown.':'{0} projet provisoire affiché.','{0} project placeholders shown.':'{0} projets provisoires affichés.',
  'View {0} — {1}':'Voir {0} — {1}','I would like to discuss {0}.':'Je souhaite discuter du {0}.',
  'Please complete this field.':'Veuillez remplir ce champ.','Please enter a valid email address.':'Veuillez saisir une adresse e-mail valide.','Project {0}':'projet {0}','Please enter at least 10 characters.':'Veuillez saisir au moins 10 caractères.',
  'Please check the highlighted fields.':'Veuillez vérifier les champs signalés.',
  'SENDING…':'ENVOI…','SEND ENQUIRY':'ENVOYER LA DEMANDE','Submitting your enquiry…':'Envoi de votre demande…',
  'Please check your enquiry details and try again.':'Veuillez vérifier les informations de votre demande et réessayer.',
  'Your enquiry has not been sent. Please try again or email info@globalmino.com.':'Votre demande n’a pas été envoyée. Veuillez réessayer ou écrire à info@globalmino.com.',
  'Your enquiry could not be confirmed. Please contact info@globalmino.com.':'Votre demande n’a pas pu être confirmée. Veuillez écrire à info@globalmino.com.',
  'Your enquiry has been received. Thank you for contacting Global Mino.':'Votre demande a bien été reçue. Merci d’avoir contacté Global Mino.',
  'We could not confirm receipt. Please contact info@globalmino.com before resending. Your message remains in the form.':'Nous n’avons pas pu confirmer la réception. Veuillez écrire à info@globalmino.com avant de renvoyer votre demande. Votre message reste dans le formulaire.',
  'Your enquiry could not be confirmed. Please contact info@globalmino.com. Your message remains in the form.':'Votre demande n’a pas pu être confirmée. Veuillez écrire à info@globalmino.com. Votre message reste dans le formulaire.',
  'This photograph has not been supplied yet. The frame is reserved for it.':'Cette photographie n’a pas encore été fournie. L’emplacement lui est réservé.'
 },
 ar:{
  'Open navigation':'فتح القائمة','Close navigation':'إغلاق القائمة',
  '{0} project placeholder shown.':'عرض مشروع واحد قيد الإعداد.','{0} project placeholders shown.':'عرض {0} مشاريع قيد الإعداد.',
  'View {0} — {1}':'عرض {0} — {1}','I would like to discuss {0}.':'أرغب في مناقشة {0}.',
  'Please complete this field.':'يُرجى تعبئة هذا الحقل.','Please enter a valid email address.':'يُرجى إدخال بريد إلكتروني صحيح.','Project {0}':'المشروع {0}','Please enter at least 10 characters.':'يُرجى إدخال 10 أحرف على الأقل.',
  'Please check the highlighted fields.':'يُرجى مراجعة الحقول المحدّدة.',
  'SENDING…':'جارٍ الإرسال…','SEND ENQUIRY':'أرسل الاستفسار','Submitting your enquiry…':'جارٍ إرسال استفسارك…',
  'Please check your enquiry details and try again.':'يُرجى مراجعة بيانات استفسارك والمحاولة مرة أخرى.',
  'Your enquiry has not been sent. Please try again or email info@globalmino.com.':'لم يُرسَل استفسارك. يُرجى المحاولة مرة أخرى أو مراسلتنا على info@globalmino.com.',
  'Your enquiry could not be confirmed. Please contact info@globalmino.com.':'تعذّر تأكيد استفسارك. يُرجى التواصل معنا على info@globalmino.com.',
  'Your enquiry has been received. Thank you for contacting Global Mino.':'تم استلام استفسارك. شكرًا لتواصلك مع جلوبال مينو.',
  'We could not confirm receipt. Please contact info@globalmino.com before resending. Your message remains in the form.':'تعذّر تأكيد الاستلام. يُرجى التواصل معنا على info@globalmino.com قبل إعادة الإرسال. رسالتك ما زالت في النموذج.',
  'Your enquiry could not be confirmed. Please contact info@globalmino.com. Your message remains in the form.':'تعذّر تأكيد استفسارك. يُرجى التواصل معنا على info@globalmino.com. رسالتك ما زالت في النموذج.',
  'This photograph has not been supplied yet. The frame is reserved for it.':'لم تُقدَّم هذه الصورة بعد، والإطار محجوز لها.'
 }
}[document.documentElement.lang]||{};
const t=(text,...values)=>(TEXT[text]||text).replace(/\{(\d)\}/g,(_,i)=>values[i]);
const header=document.querySelector('header');
const menu=document.querySelector('.menu-toggle');
const nav=document.querySelector('nav');
const backdrop=document.querySelector('.menu-backdrop');
const mobile=matchMedia('(max-width: 760px)');
function updateHeader(){header.classList.toggle('solid',scrollY>30)}
addEventListener('scroll',updateHeader,{passive:true});updateHeader();
function closeMenu(){
 nav.classList.remove('open');document.body.classList.remove('menu-open');backdrop.hidden=true;
 menu.setAttribute('aria-expanded','false');menu.setAttribute('aria-label',t('Open navigation'));
 nav.querySelectorAll('details').forEach(d=>d.open=false);
}
menu.addEventListener('click',()=>{
 if(nav.classList.contains('open'))return closeMenu();
 nav.classList.add('open');document.body.classList.add('menu-open');backdrop.hidden=false;
 menu.setAttribute('aria-expanded','true');menu.setAttribute('aria-label',t('Close navigation'));
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
document.querySelector('#credits-open')?.addEventListener('click',()=>document.querySelector('#credits-dialog').showModal());
document.querySelectorAll('dialog').forEach(dialog=>{
 dialog.querySelector('.dialog-close').addEventListener('click',()=>dialog.close());
 dialog.addEventListener('click',event=>{if(event.target===dialog){const r=dialog.getBoundingClientRect();if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom)dialog.close()}});
});
if(!matchMedia('(prefers-reduced-motion: reduce)').matches&&'IntersectionObserver'in window){
 const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('visible');observer.unobserve(entry.target)}}),{threshold:.08});
 document.querySelectorAll('.about-grid,.section-heading,.service,.project,.safety-card,.home-banner-copy').forEach(element=>{element.classList.add('reveal');observer.observe(element)});
}
const filters=[...document.querySelectorAll('[data-filter]')];
function filterProjects(value,updateURL=false){
 if(!filters.some(button=>button.dataset.filter===value))value='all';
 filters.forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.filter===value)));
 let count=0;document.querySelectorAll('.listing .project').forEach(p=>{p.hidden=value!=='all'&&p.dataset.country!==value;if(!p.hidden)count++});
 document.querySelector('#filter-status').textContent=t(count===1?'{0} project placeholder shown.':'{0} project placeholders shown.',count);
 if(updateURL){const url=new URL(location.href);if(value==='all')url.searchParams.delete('country');else url.searchParams.set('country',value);history.pushState(null,'',url)}
}
if(filters.length){filterProjects(new URLSearchParams(location.search).get('country')||'all');filters.forEach(button=>button.addEventListener('click',()=>filterProjects(button.dataset.filter,true)));addEventListener('popstate',()=>filterProjects(new URLSearchParams(location.search).get('country')||'all'))}
// Let the complete project image open the same detail page as its text link.
document.querySelectorAll('.project').forEach(project=>{
 const target=project.querySelector('a.text-link'),picture=project.querySelector('.project-image');
 if(target&&picture){const anchor=document.createElement('a');anchor.href=target.href;anchor.setAttribute('aria-label',t('View {0} — {1}',project.querySelector('h3').textContent,project.querySelector('.eyebrow').textContent));picture.replaceWith(anchor);anchor.append(picture)}
});
const form=document.querySelector('#contact-form');
if(form){
 const params=new URLSearchParams(location.search),status=document.querySelector('#form-status');
 for(const name of ['country','interest'])if([...form.elements[name].options].some(o=>o.value===params.get(name)))form.elements[name].value=params.get(name);
 if(/^project-0[1-4]$/.test(params.get('project')||''))form.elements.message.value=t('I would like to discuss {0}.',t('Project {0}',params.get('project').slice(-2)));
 const fields=[...form.querySelectorAll('input,select,textarea')];
 form.noValidate=true;
 function validate(field){
  field.setCustomValidity('');
  if(field.required&&!field.value.trim())field.setCustomValidity(t('Please complete this field.'));
  else if(field.validity.typeMismatch)field.setCustomValidity(t('Please enter a valid email address.'));
  if(field.name==='message'&&field.value.trim().length<10)field.setCustomValidity(t('Please enter at least 10 characters.'));
  let error=field.parentElement.querySelector('.field-error');
  if(!error){error=document.createElement('span');error.className='field-error';error.id=field.name+'-error';field.parentElement.append(error);field.setAttribute('aria-describedby',[field.getAttribute('aria-describedby'),error.id].filter(Boolean).join(' '))}
  error.textContent=field.validity.valid?'':field.validationMessage;
  field.setAttribute('aria-invalid',String(!field.validity.valid));return field.validity.valid;
 }
 fields.forEach(field=>{field.addEventListener('blur',()=>{if(field.value||field.hasAttribute('aria-invalid'))validate(field)});field.addEventListener('input',()=>{if(field.getAttribute('aria-invalid')==='true')validate(field)})});
 form.addEventListener('submit',async e=>{
  e.preventDefault();if(form.getAttribute('aria-busy')==='true')return;
  const valid=fields.map(validate);if(valid.includes(false)){status.className='error';status.textContent=t('Please check the highlighted fields.');fields[valid.indexOf(false)].focus();return}
  const button=form.querySelector('button[type=submit]');button.disabled=true;button.textContent=t('SENDING…');status.className='';status.textContent=t('Submitting your enquiry…');form.setAttribute('aria-busy','true');
  // Keep submitted data stable while the request is in flight.
  const payload=Object.fromEntries(new FormData(form));fields.forEach(field=>field.disabled=true);
  try{
   const response=await fetch('/api/contact',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload),signal:AbortSignal.timeout(15000)});
   const shown=message=>Object.assign(Error(t(message)),{shown:true});
   if(!response.ok)throw shown(response.status===400?'Please check your enquiry details and try again.':'Your enquiry has not been sent. Please try again or email info@globalmino.com.');
   const result=await response.json();if(result.ok!==true)throw shown('Your enquiry could not be confirmed. Please contact info@globalmino.com.');
   status.className='success';status.textContent=t('Your enquiry has been received. Thank you for contacting Global Mino.');form.reset();fields.forEach(f=>f.removeAttribute('aria-invalid'));
  }catch(error){status.className='error';status.textContent=error.name==='TimeoutError'?t('We could not confirm receipt. Please contact info@globalmino.com before resending. Your message remains in the form.'):error.shown?error.message:t('Your enquiry could not be confirmed. Please contact info@globalmino.com. Your message remains in the form.')}
  finally{fields.forEach(field=>field.disabled=false);button.disabled=false;button.innerHTML=t('SEND ENQUIRY')+(rtl?' <span>↖</span>':' <span>↗</span>');form.removeAttribute('aria-busy');status.focus()}
 });
}
// Site visits gallery: each visit's frames open in a shared lightbox, which
// navigates within that visit's collection only. Frames without a supplied
// photograph open too, showing the reserved slot rather than an empty screen.
const lightbox=document.querySelector('#lightbox');
if(lightbox){
 const stage=lightbox.querySelector('[data-lightbox-stage]');
 const caption=lightbox.querySelector('[data-lightbox-caption]');
 const collection=lightbox.querySelector('[data-lightbox-collection]');
 const counter=lightbox.querySelector('[data-lightbox-count]');
 const pad=number=>String(number).padStart(2,'0');
 let group=[],current=0;
 function render(){
  const shot=group[current];
  stage.replaceChildren();
  if(shot.dataset.full){const photo=new Image();photo.src=shot.dataset.full;photo.alt=shot.dataset.caption;stage.append(photo)}
  else{
   const pending=document.createElement('p');pending.className='lightbox-pending';
   const number=document.createElement('b');number.textContent=pad(current+1);
   const note=document.createElement('i');note.textContent=t('This photograph has not been supplied yet. The frame is reserved for it.');
   pending.append(number,note);stage.append(pending);
  }
  caption.textContent=shot.dataset.caption;
  collection.textContent=shot.dataset.collection;
  counter.textContent=`${pad(current+1)} / ${pad(group.length)}`;
  stage.classList.remove('is-entering');void stage.offsetWidth;stage.classList.add('is-entering');
 }
 function step(move){current=(current+move+group.length)%group.length;render()}
 document.querySelectorAll('.shot').forEach(shot=>shot.addEventListener('click',()=>{
  group=[...shot.closest('.visit').querySelectorAll('.shot')];current=group.indexOf(shot);
  render();lightbox.showModal();document.body.classList.add('lightbox-open');
 }));
 lightbox.querySelector('[data-lightbox-prev]').addEventListener('click',()=>step(-1));
 lightbox.querySelector('[data-lightbox-next]').addEventListener('click',()=>step(1));
 // In Arabic the collection reads right to left, so the arrow keys and swipes swap.
 lightbox.addEventListener('keydown',event=>{
  if(event.key==='ArrowRight')step(rtl?-1:1);
  else if(event.key==='ArrowLeft')step(rtl?1:-1);
  else if(event.key==='Home'||event.key==='End'){event.preventDefault();current=event.key==='Home'?0:group.length-1;render()}
 });
 // A click beside the photograph closes; a horizontal drag moves through the collection.
 lightbox.addEventListener('click',event=>{if(['lightbox','lightbox-inner','lightbox-figure'].some(name=>event.target.classList.contains(name)))lightbox.close()});
 let startX=null;
 stage.addEventListener('pointerdown',event=>{startX=event.clientX});
 stage.addEventListener('pointerup',event=>{if(startX!==null&&Math.abs(event.clientX-startX)>45)step((event.clientX<startX)!==rtl?1:-1);startX=null});
 stage.addEventListener('pointercancel',()=>{startX=null});
 // Return focus to the frame that was last on screen, not the one first opened.
 lightbox.addEventListener('close',()=>{document.body.classList.remove('lightbox-open');stage.replaceChildren();group[current]?.focus()});
}
