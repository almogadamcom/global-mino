const {test,expect}=require('@playwright/test');
const {default:AxeBuilder}=require('@axe-core/playwright');
const routes=['/','/about','/team','/team/hashim-sulieman','/team/huzaifa-ahmed-salih','/team/muhammad-abdul-rahman','/team/abdelrazig-ahmed','/team/rawi-elamin','/team/mona-ahmed-yagoub-mohammed','/team/bushra-babiker-ahmed-babiker','/operations','/gallery','/countries/sudan','/countries/cameroon','/countries/central-african-republic','/services','/services/gold-mining','/services/mineral-exploration','/services/mining-consultancy','/services/occupational-health-safety','/projects','/projects/project-01','/projects/project-02','/projects/project-03','/contact'];
for(const width of [1440,1280,1024,768,390])test(`all routes at ${width}px`,async({page})=>{for(const route of routes){await page.setViewportSize({width,height:950});const response=await page.goto(route);expect(response.status()).toBe(200);await expect(page.locator('h1')).toHaveCount(1);expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBe(true);expect(await page.locator('img').evaluateAll(async imgs=>{await Promise.all(imgs.map(i=>{i.loading='eager';return i.decode().catch(()=>{})}));return imgs.every(i=>i.naturalWidth>0)})).toBe(true);expect(await page.locator('link[rel=canonical]').getAttribute('href')).toBe('https://globalmino.com'+route)}});
test('links and accessibility',async({page,request})=>{await page.emulateMedia({reducedMotion:'reduce'});const links=new Set();for(const route of routes){await page.goto(route);for(const href of await page.locator('a[href^="/"]').evaluateAll(as=>as.map(a=>a.getAttribute('href'))))links.add(href);const results=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa']).analyze();expect(results.violations.map(v=>({id:v.id,nodes:v.nodes.map(n=>n.target)}))).toEqual([])}for(const href of links)expect((await request.get(href)).status()).toBe(200)});
test('navigation, filters, contact and fallback',async({page})=>{await page.goto('/');await expect(page.locator('main>section')).toHaveCount(7);await page.locator('summary').filter({hasText:'Countries'}).click();await expect(page.locator('.dropdown a').filter({hasText:'Explore Sudan'})).toBeVisible();await page.keyboard.press('Escape');await page.setViewportSize({width:390,height:844});await page.locator('.menu-toggle').click();await expect(page.locator('nav')).toBeVisible();await page.keyboard.press('Escape');await expect(page.locator('nav')).not.toBeVisible();await page.goto('/projects');await page.locator('[data-filter=cameroon]').click();await expect(page.locator('.listing .project:visible')).toHaveCount(1);await page.route('**/api/contact',r=>r.fulfill({status:502,contentType:'application/json',body:'{"error":"Enquiry could not be saved"}'}));await page.goto('/contact?country=cameroon&interest=mineral-exploration');await expect(page.locator('[name=country]')).toHaveValue('cameroon');await page.locator('[name=name]').fill('Test Person');await page.locator('[name=email]').fill('test@example.com');await page.locator('[name=message]').fill('A test enquiry about mineral exploration.');await page.locator('button[type=submit]').click();await expect(page.locator('#form-status')).toContainText('has not been sent');await page.route('**/api/contact',r=>r.fulfill({status:200,contentType:'application/json',body:'{"ok":true}'}));await page.locator('button[type=submit]').click();await expect(page.locator('#form-status')).toContainText('has been received');expect((await page.goto('/projects/unknown')).status()).toBe(404)});
test('local fonts, filter history and mobile keyboard focus',async({page})=>{
 await page.goto('/projects?country=sudan');
 await page.evaluate(()=>document.fonts.ready);
 expect(await page.evaluate(()=>document.fonts.check('16px "DM Sans"')&&document.fonts.check('600 16px "DM Sans"'))).toBe(true);
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
 await expect(page.locator('.ohs-home-banner a')).toHaveAttribute('href','/services/occupational-health-safety');
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
 const lightbox=page.locator('#lightbox');
 await page.locator('#visit-cameroon .shot').first().click();
 await expect(lightbox).toBeVisible();
 await expect(lightbox.locator('[data-lightbox-collection]')).toHaveText('Cameroon site visit');
 await expect(lightbox.locator('[data-lightbox-count]')).toHaveText('01 / 05');
 await page.locator('[data-lightbox-next]').click();
 await expect(lightbox.locator('[data-lightbox-count]')).toHaveText('02 / 05');
 await expect(lightbox.locator('[data-lightbox-caption]')).toContainText('Photograph 02');
 await page.keyboard.press('ArrowLeft');
 await expect(lightbox.locator('[data-lightbox-count]')).toHaveText('01 / 05');
 // Navigation wraps inside the visit that was opened and never leaves it.
 await page.keyboard.press('ArrowLeft');
 await expect(lightbox.locator('[data-lightbox-count]')).toHaveText('05 / 05');
 await page.keyboard.press('Escape');
 await expect(lightbox).toBeHidden();
 await expect(page.locator('body')).not.toHaveClass(/lightbox-open/);
 await expect(page.locator('#visit-cameroon .shot').last()).toBeFocused();
});
