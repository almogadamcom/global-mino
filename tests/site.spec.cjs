const {test,expect}=require('@playwright/test');
const {default:AxeBuilder}=require('@axe-core/playwright');
const routes=['/','/about','/team','/team/hashim-sulieman','/team/huzaifa-ahmed-salih','/team/muhammad-abdul-rahman','/team/abdelrazig-ahmed','/team/rawi-elamin','/team/bushra-babiker-ahmed-babiker','/team/abdalla-adam-younis-mohammed','/team/ogba-adam-edris-ali','/team/ezzeldin-ali-suleiman-omar','/team/shaker-adam-idrees','/operations','/gallery','/ceo-message','/countries/sudan','/countries/cameroon','/countries/central-african-republic','/countries/ethiopia','/services','/services/gold-mining','/services/mineral-exploration','/services/mining-consultancy','/services/occupational-health-safety','/projects','/projects/project-01','/projects/project-02','/projects/project-03','/projects/project-04','/contact'];
for(const width of [1440,1280,1024,768,390])test(`all routes at ${width}px`,async({page})=>{for(const route of routes){await page.setViewportSize({width,height:950});const response=await page.goto(route);expect(response.status()).toBe(200);await expect(page.locator('h1')).toHaveCount(1);expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBe(true);expect(await page.evaluate(()=>{const h=document.querySelector('header');return [...h.children].filter(e=>e.getClientRects().length).every(e=>{const r=e.getBoundingClientRect();return r.left>=0&&r.right<=innerWidth})})).toBe(true);expect(await page.locator('img').evaluateAll(async imgs=>{await Promise.all(imgs.map(i=>{i.loading='eager';return i.decode().catch(()=>{})}));return imgs.every(i=>i.naturalWidth>0)})).toBe(true);expect(await page.locator('link[rel=canonical]').getAttribute('href')).toBe('https://globalmino.com'+route)}});
test('links and accessibility',async({page,request})=>{await page.emulateMedia({reducedMotion:'reduce'});const links=new Set();for(const route of routes){await page.goto(route);for(const href of await page.locator('a[href^="/"]').evaluateAll(as=>as.map(a=>a.getAttribute('href'))))links.add(href);const results=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa']).analyze();expect(results.violations.map(v=>({id:v.id,nodes:v.nodes.map(n=>n.target)}))).toEqual([])}for(const href of links)expect((await request.get(href)).status()).toBe(200)});
test('navigation, filters, contact and fallback',async({page})=>{await page.goto('/');await expect(page.locator('main>section')).toHaveCount(6);await page.locator('summary').filter({hasText:'Countries'}).click();await expect(page.locator('.dropdown a').filter({hasText:'Explore Sudan'})).toBeVisible();await page.keyboard.press('Escape');await page.setViewportSize({width:390,height:844});await page.locator('.menu-toggle').click();await expect(page.locator('nav')).toBeVisible();await page.keyboard.press('Escape');await expect(page.locator('nav')).not.toBeVisible();await page.goto('/projects');await page.locator('[data-filter=cameroon]').click();await expect(page.locator('.listing .project:visible')).toHaveCount(1);await page.route('**/api/contact',r=>r.fulfill({status:502,contentType:'application/json',body:'{"error":"Enquiry could not be saved"}'}));await page.goto('/contact?country=cameroon&interest=mineral-exploration');await expect(page.locator('[name=country]')).toHaveValue('cameroon');await page.locator('[name=name]').fill('Test Person');await page.locator('[name=email]').fill('test@example.com');await page.locator('[name=message]').fill('A test enquiry about mineral exploration.');await page.locator('button[type=submit]').click();await expect(page.locator('#form-status')).toContainText('has not been sent');await page.route('**/api/contact',r=>r.fulfill({status:200,contentType:'application/json',body:'{"ok":true}'}));await page.locator('button[type=submit]').click();await expect(page.locator('#form-status')).toContainText('has been received');expect((await page.goto('/projects/unknown')).status()).toBe(404)});
test('local fonts, filter history and mobile keyboard focus',async({page})=>{
 await page.goto('/projects?country=sudan');
 await page.evaluate(()=>document.fonts.ready);
 expect(await page.evaluate(()=>document.fonts.check('16px "Inter"')&&document.fonts.check('600 16px "Inter"'))).toBe(true);
 expect(await page.locator('link[href*="fonts.googleapis.com"]').count()).toBe(0);
 await expect(page.locator('.listing .project:visible')).toHaveCount(1);
 await page.locator('[data-filter=cameroon]').click();await page.reload();
 await expect(page.locator('[data-filter=cameroon]')).toHaveAttribute('aria-pressed','true');
 await page.locator('[data-filter=all]').click();await page.goBack();
 await expect(page.locator('[data-filter=cameroon]')).toHaveAttribute('aria-pressed','true');
 await page.setViewportSize({width:390,height:844});await page.locator('.menu-toggle').click();
 await expect(page.locator('body')).toHaveClass(/menu-open/);
 await page.locator('nav>a').last().focus();await page.keyboard.press('Tab');
 await expect(page.locator('.menu-toggle')).toBeFocused();
 await page.locator('summary').filter({hasText:'Services'}).click();
 await expect(page.locator('.dropdown a[href="/services/gold-mining"]')).toBeVisible();
 await page.keyboard.press('Escape');await page.keyboard.press('Escape');
 await expect(page.locator('body')).not.toHaveClass(/menu-open/);
});
test('OHS page and home banner expose the safety framework without unsupported metrics',async({page})=>{
 await page.goto('/');
 await expect(page.locator('.ohs-home-banner')).toBeVisible();
 await expect(page.locator('.ohs-home-banner a.button')).toHaveAttribute('href','/services/occupational-health-safety');
 await page.goto('/services/occupational-health-safety');
 for(const id of ['mining-safety','field-safety','emergency','wellbeing','training','compliance'])await expect(page.locator('#'+id)).toHaveCount(1);
 await expect(page.getByText('No company accident rate, certification status or achievement figure is displayed')).toBeVisible();
 await expect(page.locator('.kpi-grid article')).toHaveCount(6);
});
test('form validation, pending state and unconfirmed response',async({page,request})=>{
 await page.goto('/contact');await page.locator('button[type=submit]').click();
 await expect(page.locator('[name=name]')).toBeFocused();await expect(page.locator('#form-status')).toContainText('highlighted');
 await page.locator('[name=name]').fill('Test Person');await page.locator('[name=email]').fill('test@example.com');
 await page.locator('[name=country]').selectOption('sudan');await page.locator('[name=interest]').selectOption('gold-mining');await page.locator('[name=message]').fill('A test enquiry that must be retained.');
 let release;const pending=new Promise(resolve=>release=resolve);
 await page.route('**/api/contact',async route=>{await pending;await route.fulfill({status:200,contentType:'application/json',body:'{}'})});
 await page.locator('button[type=submit]').click();await expect(page.locator('button[type=submit]')).toBeDisabled();release();
 await expect(page.locator('#form-status')).toContainText('could not be confirmed');await expect(page.locator('[name=message]')).toHaveValue('A test enquiry that must be retained.');
 expect((await request.post('/api/contact',{data:{name:' '}})).status()).toBe(400);
 expect((await request.get('/.env')).status()).toBe(404);
});

test('site visit galleries and lightbox',async({page})=>{
 await page.goto('/gallery');
 await expect(page.locator('.visit')).toHaveCount(3);
 await expect(page.locator('#visit-sudan .shot')).toHaveCount(5);
 await expect(page.locator('#visit-cameroon .shot')).toHaveCount(3);
 await expect(page.locator('#visit-cameroon .visit-meta dd').last()).toHaveText('3 of 3 supplied');
 // The Central African Republic visit carries supplied photographs, not reserved frames.
 await expect(page.locator('#visit-central-african-republic .shot')).toHaveCount(4);
 await expect(page.locator('#visit-central-african-republic .shot img')).toHaveCount(4);
 expect(await page.locator('#visit-central-african-republic .shot img').evaluateAll(async imgs=>{
  await Promise.all(imgs.map(i=>{i.loading='eager';return i.decode().catch(()=>{})}));
  return imgs.every(i=>i.naturalWidth>0&&i.getAttribute('src').startsWith('/assets/visits/'));
 })).toBe(true);
 await expect(page.locator('#visit-central-african-republic .visit-meta dd').last()).toHaveText('4 of 4 supplied');
 const lightbox=page.locator('#lightbox');
 await page.locator('#visit-cameroon .shot').first().click();
 await expect(lightbox).toBeVisible();
 await expect(lightbox.locator('[data-lightbox-collection]')).toHaveText('Cameroon site visit');
 await expect(lightbox.locator('[data-lightbox-count]')).toHaveText('01 / 03');
 await page.locator('[data-lightbox-next]').click();
 await expect(lightbox.locator('[data-lightbox-count]')).toHaveText('02 / 03');
 await expect(lightbox.locator('[data-lightbox-caption]')).toContainText('airstairs');
 await page.keyboard.press('ArrowLeft');
 await expect(lightbox.locator('[data-lightbox-count]')).toHaveText('01 / 03');
 // Navigation wraps inside the visit that was opened and never leaves it.
 await page.keyboard.press('ArrowLeft');
 await expect(lightbox.locator('[data-lightbox-count]')).toHaveText('03 / 03');
 await page.keyboard.press('Escape');
 await expect(lightbox).toBeHidden();
 await expect(page.locator('body')).not.toHaveClass(/lightbox-open/);
 await expect(page.locator('#visit-cameroon .shot').last()).toBeFocused();
});

test('CEO message page carries the supplied letter and footer link',async({page})=>{
 await page.goto('/ceo-message');
 await expect(page.locator('h1')).toContainText('Message from the Founder');
 await expect(page.locator('.ceo-portrait img')).toBeVisible();
 await expect(page.locator('.ceo-quote')).toContainText('no mineral resource is more valuable than human life');
 await expect(page.locator('.ceo-letter-body h2')).toHaveCount(2);
 await expect(page.locator('.ceo-signoff-name')).toHaveText('Dr. Hashim Sulieman');
 // Reached from the footer of any page, which is where it is linked.
 await page.goto('/');
 await page.locator('footer a[href="/ceo-message"]').click();
 await expect(page).toHaveURL(/\/ceo-message$/);
});

test('Ethiopia country page and navigation',async({page})=>{
 await page.goto('/countries/ethiopia');
 await expect(page.locator('h1')).toHaveText('Ethiopia');
 await expect(page.locator('.profile-overview dd').first()).toContainText('Gold');
 await expect(page.locator('.profile-cards article')).toHaveCount(3);
 await expect(page.locator('.profile-sources a')).toHaveCount(2);
 // Reachable from the home page country panels and listed in the footer.
 await page.goto('/');
 await expect(page.locator('.country-grid a[href="/countries/ethiopia"]')).toHaveCount(1);
 await page.locator('footer a[href="/countries/ethiopia"]').click();
 await expect(page).toHaveURL(/\/countries\/ethiopia$/);
 // The enquiry form still offers only the countries the database accepts.
 await page.goto('/contact');
 await expect(page.locator('[name=country] option')).toHaveCount(5);
});

// French and Arabic editions: every English route has a counterpart under /fr and /ar.
const editions={fr:{dir:'ltr'},ar:{dir:'rtl'}};
const localized=lang=>routes.map(route=>'/'+lang+(route==='/'?'':route));
for(const [lang,{dir}] of Object.entries(editions))for(const width of [1440,1024,768,390])test(`${lang} routes at ${width}px`,async({page})=>{for(const route of localized(lang)){await page.setViewportSize({width,height:950});const response=await page.goto(route);expect(response.status()).toBe(200);await expect(page.locator('html')).toHaveAttribute('lang',lang);await expect(page.locator('html')).toHaveAttribute('dir',dir);await expect(page.locator('h1')).toHaveCount(1);expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBe(true);expect(await page.evaluate(()=>{const h=document.querySelector('header');return [...h.children].filter(e=>e.getClientRects().length).every(e=>{const r=e.getBoundingClientRect();return r.left>=0&&r.right<=innerWidth})})).toBe(true);expect(await page.locator('link[rel=canonical]').getAttribute('href')).toBe('https://globalmino.com'+route);expect(await page.locator('main a[href^="/"]').evaluateAll((as,lang)=>as.every(a=>a.getAttribute('href').startsWith('/'+lang)),lang)).toBe(true)}});
test('translated editions are accessible',async({page})=>{await page.emulateMedia({reducedMotion:'reduce'});for(const route of [...localized('fr'),...localized('ar')]){await page.goto(route);const results=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa']).analyze();expect(results.violations.map(v=>({route,id:v.id,nodes:v.nodes.map(n=>n.target)}))).toEqual([])}});
test('language switcher keeps the current page',async({page})=>{
 await page.goto('/countries/sudan');
 await expect(page.locator('.lang-switch a[aria-current]')).toHaveText('EN');
 await page.locator('.lang-switch a[hreflang=ar]').click();
 await expect(page).toHaveURL(/\/ar\/countries\/sudan$/);
 await expect(page.locator('h1')).toHaveText('السودان');
 await expect(page.locator('link[rel=alternate][hreflang=fr]')).toHaveAttribute('href','https://globalmino.com/fr/countries/sudan');
 await page.locator('.lang-switch a[hreflang=fr]').click();
 await expect(page).toHaveURL(/\/fr\/countries\/sudan$/);
 await expect(page.locator('h1')).toHaveText('Soudan');
 await page.locator('.lang-switch a[hreflang=en]').click();
 await expect(page).toHaveURL(/\/countries\/sudan$/);
 await page.goto('/ar');await expect(page.locator('.lang-switch a[aria-current]')).toHaveText('ع');
 await page.goto('/fr/team/rawi-elamin');await expect(page.locator('.lang-switch a[hreflang=en]')).toHaveAttribute('href','/team/rawi-elamin');
});
test('Arabic form, filters and lightbox speak Arabic and read right to left',async({page})=>{
 await page.goto('/ar/contact');await page.locator('button[type=submit]').click();
 await expect(page.locator('#form-status')).toHaveText('يُرجى مراجعة الحقول المحدّدة.');
 await expect(page.locator('[name=country] option[value=sudan]')).toHaveText('السودان');
 await page.locator('[name=name]').fill('Test Person');await page.locator('[name=email]').fill('test@example.com');
 await page.locator('[name=country]').selectOption('sudan');await page.locator('[name=interest]').selectOption('gold-mining');await page.locator('[name=message]').fill('A test enquiry in Arabic.');
 await page.route('**/api/contact',r=>r.fulfill({status:200,contentType:'application/json',body:'{"ok":true}'}));
 await page.locator('button[type=submit]').click();
 await expect(page.locator('#form-status')).toHaveText('تم استلام استفسارك. شكرًا لتواصلك مع جلوبال مينو.');
 await page.goto('/ar/projects');await page.locator('[data-filter=cameroon]').click();
 await expect(page.locator('#filter-status')).toHaveText('عرض مشروع واحد قيد الإعداد.');
 await page.goto('/ar/gallery');await page.locator('#visit-cameroon .shot').first().click();
 await expect(page.locator('[data-lightbox-collection]')).toHaveText('زيارة ميدانية إلى الكاميرون');
 await page.keyboard.press('ArrowLeft');
 await expect(page.locator('[data-lightbox-count]')).toHaveText('02 / 03');
 await page.keyboard.press('ArrowRight');
 await expect(page.locator('[data-lightbox-count]')).toHaveText('01 / 03');
 await page.keyboard.press('Escape');
 expect(await page.evaluate(()=>document.fonts.check('16px "IBM Plex Sans Arabic"','عربي'))).toBe(true);
});
test('French interface text and localized not-found pages',async({page})=>{
 await page.goto('/fr/projects?country=sudan');
 await expect(page.locator('#filter-status')).toHaveText('1 projet provisoire affiché.');
 await page.goto('/fr/contact');await page.locator('button[type=submit]').click();
 await expect(page.locator('#form-status')).toHaveText('Veuillez vérifier les champs signalés.');
 for(const [route,lang,text] of [['/fr/nope','fr','Page introuvable'],['/ar/nope','ar','الصفحة غير موجودة'],['/nope','en','Page not found']]){
  const response=await page.goto(route);expect(response.status()).toBe(404);
  await expect(page.locator('html')).toHaveAttribute('lang',lang);await expect(page).toHaveTitle(new RegExp(text));
 }
});
test('form messages, project prefill and link previews follow the page language',async({page,request})=>{
 for(const [lang,email,prefill] of [['fr','Veuillez saisir une adresse e-mail valide.','Je souhaite discuter du projet 02.'],['ar','يُرجى إدخال بريد إلكتروني صحيح.','أرغب في مناقشة المشروع 02.'],['en','Please enter a valid email address.','I would like to discuss Project 02.']]){
  const base=lang==='en'?'':'/'+lang;
  await page.goto(base+'/contact?project=project-02');
  await expect(page.locator('[name=message]')).toHaveValue(prefill);
  await page.locator('[name=email]').fill('not-an-email');await page.locator('[name=email]').blur();
  await expect(page.locator('#email-error')).toHaveText(email);
  await expect(page.locator('meta[property="og:locale"]')).toHaveAttribute('content',{en:'en_GB',fr:'fr_FR',ar:'ar_AR'}[lang]);
 }
 // The not-found page names no translated alternates, and the sitemap pairs every edition.
 await page.goto('/fr/nope');expect(await page.locator('link[rel=alternate][hreflang]').count()).toBe(0);
 const sitemap=await (await request.get('/sitemap.xml')).text();
 expect(sitemap).toContain('<loc>https://globalmino.com/ar/countries/sudan</loc><xhtml:link rel="alternate" hreflang="en" href="https://globalmino.com/countries/sudan"/>');
});
