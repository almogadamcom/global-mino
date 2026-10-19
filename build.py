from pathlib import Path
import re, html
from country_content import INFO, GOLD, PROFILES
from team_profiles import TEAM_PROFILES
from site_visits import VISITS
import ceo_message as ceo
import i18n
root=Path(__file__).parent
out=root/'dist'
source=(root/'src/home.html').read_text(encoding='utf-8')
countries=[('Sudan','sudan','sudan','Gold Mining & Mineral Opportunities','Gold Mining|Mineral Exploration|Geological Services|Mining Consultancy|Technical Support|Responsible Resource Development'),('Cameroon','cameroon','cameroon','Geological Intelligence & Mineral Opportunity Development','Geological Mapping|Mineral Resource Intelligence|Mining Concession Identification|License & Legal Status Verification|Field Exploration|Sampling|Geochemical Investigation|Geophysical Investigation|Exploration Target Development|Prospective Area Identification|ASM Opportunity Assessment|GIS & Digital Deliverables|Technical Opportunity Reports'),('Central African Republic','central-african-republic','fieldwork','Mineral Exploration & Mining Opportunities','Mineral Exploration|Mining Consultancy|Geological Assessment|Opportunity Identification|Technical Support|Responsible Resource Development'),('Ethiopia','ethiopia','hero','Gold, Industrial & Strategic Minerals','Mineral Exploration|Gold Mining|Geological Assessment|Mining Consultancy|Technical Support|Responsible Resource Development')]
services=[('Gold Mining','gold-mining','hero','Developing opportunity.<br>Creating responsible value.','Mining Opportunity Assessment|Technical Evaluation|Mining Development Support|Operational Advisory|Safety Considerations|Environmental Considerations|Responsible Resource Development','Opportunity|Assessment|Planning|Development|Operations Support'),('Mineral Exploration','mineral-exploration','geologist','Understanding what<br>lies beneath.','Geological Mapping|Reconnaissance|Field Mapping|Rock Sampling|Soil Sampling|Stream Sediment Sampling|Trenching|Geochemical Investigation|Geophysical Investigation|Historical Data Review|Target Generation|Prospective Area Ranking','Field|Sample|Analysis|Interpretation|Target|Opportunity'),('Mining Consultancy','mining-consultancy','fieldwork','Technical insight.<br>Strategic perspective.','Technical Advisory|Geological Assessment|Opportunity Evaluation|Mining Project Evaluation|Risk Assessment|Operational Support|Investment Intelligence|Market Entry Support|Regulatory Coordination Support|Environmental Considerations|Occupational Health & Safety','Context|Assessment|Technical Review|Recommendation'),('Occupational Health & Safety','occupational-health-safety','fieldwork','Protecting people.<br>Strengthening operations.','Occupational Health Services|Health Risk Assessments|Health Surveillance|Industrial Hygiene|Emergency Preparedness|Dynamic Risk Management','Assess|Measure|Control|Monitor|Respond|Improve')]
alts={'hero':'Illustrative terraced open-pit mine','sudan':'Arid landscape south of Port Sudan','cameroon':'Rainforest in Bodiman, Cameroon','geologist':'Illustrative granite examination in Alaska','fieldwork':'Illustrative geophysical field survey in Hawaii'}
def link(text,url,cls='text-link'): return f'<a class="{cls}" href="{url}">{text} <span>↗</span></a>'
def image(name): return f'<img src="/assets/{name}.jpg" alt="{alts[name]}" loading="lazy" width="1200" height="800">'
def dropdown(label,items,base):
 return '<details data-navigation-group="'+base+'"><summary>'+label+'</summary><div class="dropdown"><p class="eyebrow">'+label.upper()+'</p>'+''.join(f'<a href="/{base}/{x[1]}">{x[0]}<small>{("Gold Mining & Exploration" if x[1]=="sudan" else "Mineral Exploration & Consultancy") if base=="countries" else x[3].replace("<br>"," ")}</small><span>Explore {x[0]} ↗</span></a>' for x in items)+(link('ALL SERVICES','/services') if base=='services' else '')+'</div></details>'
header=re.search(r'<header.*?</header>',source).group()
nav='<nav id="main-navigation" aria-label="Main navigation">'+''.join(f'<a href="{p}">{n}</a>' for n,p in [('Home','/'),('About','/about'),('Team','/team'),('Operations','/operations'),('Gallery','/gallery')])+dropdown('Countries',countries,'countries')+dropdown('Services',services,'services')+link('Projects','/projects','nav-link')+link('Contact','/contact','nav-link')+'</nav>'
header=re.sub(r'<nav.*?</nav>',lambda m:nav,header).replace('href="#home"','href="/"').replace('href="#contact"','href="/contact"').replace('class="menu-toggle"','class="menu-toggle" aria-controls="main-navigation"').replace('<button class="menu-toggle"','<!--lang-switch--><button class="menu-toggle"')
footer=re.search(r'<footer>.*?</footer>',source).group()
credits=re.search(r'<dialog id="credits-dialog".*?</dialog>',source).group()
paths={'home':'/','about':'/about','team':'/team','operations':'/operations','gallery':'/gallery','services':'/services','projects':'/projects','contact':'/contact','sudan':'/countries/sudan','cameroon':'/countries/cameroon','car':'/countries/central-african-republic','gold-mining':'/services/gold-mining','exploration':'/services/mineral-exploration','consultancy':'/services/mining-consultancy','project-list':'/projects'}
def routes(s):
 for a,b in paths.items(): s=s.replace(f'href="#{a}"',f'href="{b}"')
 return s
footer=routes(footer).replace('<a href="/about">About</a>','<a href="/about">About</a><a href="/ceo-message">CEO Message</a>').replace('<a href="/countries/central-african-republic">Central African Republic</a>','<a href="/countries/central-african-republic">Central African Republic</a><a href="/countries/ethiopia">Ethiopia</a>').replace('<a href="/operations">Operations</a>','<a href="/operations">Operations</a><a href="/team">Team</a><a href="/gallery">Gallery</a>').replace('href="/">BACK TO TOP','href="#top">BACK TO TOP')
def hero(label,title,copy,img='hero'):
 return f'''<section class="site-hero">
 <div class="site-hero-heading"><div class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><span>{label.title()}</span></div><p class="eyebrow">{label.upper()}</p><h1>{title}</h1><p class="site-hero-copy">{copy}</p></div>
 <figure class="site-hero-photo" style="background-image:linear-gradient(90deg,#10141922,#10141955),url(/assets/{img}.jpg)"></figure>
 </section>'''
def section(label,title,content,cls=''):
 return f'<section class="section {cls}"><div class="section-top"><p class="eyebrow">{label}</p></div><h2>{title}</h2>{content}</section>'
def blocks(items): return '<div class="type-grid">'+''.join(f'<article><span class="eyebrow">{i:02}</span><h3>{s}</h3></article>' for i,s in enumerate(items.split('|'),1))+'</div>'
def process(items): return section('OUR APPROACH','From knowledge to opportunity.', '<ol class="process">'+''.join(f'<li><span>{i:02}</span><h3>{s}</h3></li>' for i,s in enumerate(items.split('|'),1))+'</ol>','services')
def country_info(slug,img):
 d=INFO.get(slug)
 if not d: return ''
 s=section('GEOLOGICAL SETTING',d['setting_title'],'<div class="about-grid editorial"><div>'+''.join(f'<p>{x}</p>' for x in d['setting'])+'</div><figure class="about-image">'+image(img)+'</figure></div>')
 s+=section('MINERAL ENDOWMENT',d['commodities_title'],'<div class="safety-grid">'+''.join(f'<article class="safety-card"><span class="safety-no">{i:02}</span><h3>{n}</h3><p>{c}</p></article>' for i,(n,c) in enumerate(d['commodities'],1))+'</div>','services')
 s+='<section class="section project-detail"><div><article class="detail-block"><p class="eyebrow">OPERATING CONTEXT</p><h2>'+d['context_title']+'</h2>'+''.join(f'<p>{x}</p>' for x in d['context'])+'</article><p class="form-note">This page describes the documented mineral geology and operating context of '+d['country']+'. It does not describe Global Mino licences, concessions, holdings or production.</p></div><aside><p class="eyebrow">AT A GLANCE</p><dl>'+''.join(f'<dt>{a}</dt><dd>{b}</dd>' for a,b in d['facts'])+'</dl></aside></section>'
 return s
def dblocks(items): return '<div class="type-grid">'+''.join(f'<article><span class="eyebrow">{i:02}</span><h3>{n}</h3><p>{d}</p></article>' for i,(n,d) in enumerate(items,1))+'</div>'
def cards(items): return '<div class="safety-grid">'+''.join(f'<article class="safety-card"><span class="safety-no">{i:02}</span><h3>{n}</h3><p>{d}</p></article>' for i,(n,d) in enumerate(items,1))+'</div>'
def gold_detail(slug,img):
 g=GOLD.get(slug)
 if not g: return ''
 s=section(g['eyebrow'],g['title'],f'<p class="intro-copy">{g["intro"]}</p>')
 s+=section('GOLDFIELDS',g['districts_title'],dblocks(g['districts']))
 s+=section('DEPOSIT STYLES',g['styles_title'],cards(g['styles']),'services')
 s+=section('ARTISANAL AND SMALL-SCALE MINING',g['asm_title'],'<div class="about-grid editorial"><div>'+''.join(f'<p>{x}</p>' for x in g['asm'])+'</div><figure class="about-image">'+image(img)+'</figure></div>')
 s+=section('MINERAL TITLES',g['titles_title'],dblocks(g['titles'])+f'<p class="form-note">{g["titles_note"]}</p>')
 s+=section('THE OPPORTUNITY',g['opportunity_title'],cards(g['opportunity'])+f'<p class="form-note">{g["opportunity_note"]}</p>','services')
 return s
def cta(text='Discuss an opportunity',url='/contact'):
 return '<section class="contact"><div class="contact-intro"><p class="eyebrow">PARTNER WITH GLOBAL MINO</p><h2>Natural resources.<br>Real impact.</h2><p>Connect with Global Mino to discuss mining, exploration and technical consultancy across Africa.</p><div class="actions">'+link(text.upper(),url,'button gold')+'</div></div></section>'
def panels(large=False):
 return '<div class="country-grid'+(' immersive' if large else '')+'">'+''.join(f'<a class="country {"featured" if i==0 else ""}" href="/countries/{c[1]}">{image(c[2])}<span class="country-no">0{i+1} / {c[0].upper()}</span><div class="country-body"><p>{c[3]}</p><h3>{c[0]}</h3><span class="country-link">EXPLORE {c[0].upper()} <b>↗</b></span></div></a>' for i,c in enumerate(countries))+'</div>'
def projects():
 return '<div class="project-grid listing">'+''.join(f'<article class="project" data-country="{c[1]}"><div class="project-image">{image(c[2])}<span>PROJECT PLACEHOLDER / 0{i+1}</span></div><p class="eyebrow">{c[0].upper()} · {"Gold Mining" if i==0 else "Exploration"}</p><h3>Project 0{i+1}</h3><p>Project information coming soon.</p>{link("VIEW PROJECT",f"/projects/project-0{i+1}")}</article>' for i,c in enumerate(countries))+'</div>'
pages={}
home=re.search(r'<main>(.*?)</main>',source,re.S).group(1)
home=routes(home)
# Home hero: two image panels side by side (company introduction and the
# occupational health & safety framework) over the approach rail; home.css.
home_hero='''<section class="home-split" id="home">
 <article class="home-split-panel" style="--panel-image:url(/assets/hero-gold-mining-v2.jpg)" aria-labelledby="home-title">
  <div class="home-split-copy">
   <p class="eyebrow"><span></span>AFRICA-FOCUSED MINING &amp; EXPLORATION</p>
   <h1 id="home-title">Unlocking Africa’s<br><em>mineral potential.</em></h1>
   <p>Global Mino brings geological knowledge, field intelligence and technical consultancy together to move mineral opportunities forward responsibly.</p>
   <div class="actions"><a class="button gold" href="/operations">EXPLORE OUR OPERATIONS <span>↗</span></a><a class="text-link" href="/services">DISCOVER OUR EXPERTISE <span>↗</span></a></div>
  </div>
 </article>
 <article class="home-split-panel ohs-home-banner" style="--panel-image:url(/assets/ohs-mining-safety.jpg);--panel-position:82% center" aria-labelledby="home-ohs-title">
  <div class="home-split-copy">
   <p class="eyebrow"><span></span>OCCUPATIONAL HEALTH &amp; SAFETY</p>
   <h2 id="home-ohs-title">Every person.<br><em>Every task. Every shift.</em></h2>
   <p>A practical framework for managing critical risks, protecting worker health and preparing mining and exploration teams to respond when conditions change.</p>
   <div class="actions">'''+link('EXPLORE OUR OHS APPROACH','/services/occupational-health-safety','button gold')+'''<span class="home-split-note">Mining · Exploration · Field Operations</span></div>
  </div>
 </article>
 <div class="home-hero-rail" aria-label="Our approach"><p>AFRICAN PERSPECTIVE</p><p>FIELD-LED KNOWLEDGE</p><p>RESPONSIBLE DEVELOPMENT</p><a href="#about">SCROLL TO DISCOVER <span>↓</span></a></div>
 </section>'''
home=re.sub(r'<section class="hero" id="home">.*?</section>',home_hero,home,count=1,flags=re.S)
home=re.sub(r'<div class="country-grid">.*?</div></section>',lambda m:panels()+'</section>',home,count=1,flags=re.S)
home=home.replace('href="/contact">DISCOVER GLOBAL MINO','href="/about">DISCOVER GLOBAL MINO')
home=home.replace('Three markets.<br>One African vision.','Four markets.<br>One African vision.')
for s,text in zip(services,['DISCOVER GOLD MINING','EXPLORE OUR CAPABILITIES','VIEW CONSULTANCY']): home=home.replace(f'href="/contact">{text}',f'href="/services/{s[1]}">{text}')
i=iter(range(1,4))
home=re.sub(r'<button class="text-link project-open".*?</button>',lambda m:link('VIEW PROJECT',f'/projects/project-0{next(i)}'),home)
home=re.sub(r'<footer>.*?</footer>',lambda m:footer,home).replace('href="mailto:hashim@globalmino.com?subject=Discuss%20an%20opportunity"','href="/contact"')
home=home.replace('src="assets/','src="/assets/').replace('href="/about">SCROLL','href="#about">SCROLL')
# Home page only: drop the section/service counters, the hero index and the
# "01 / " prefix on the country tiles. The shared helpers keep their numbering
# so the inner pages are unaffected.
home=re.sub(r'<span class="(?:number|service-no|hero-index)">.*?</span>','',home)
home=re.sub(r'(<span class="country-no">)\s*\d+\s*/\s*','\\1',home)
# The homepage uses labels rather than decorative sequence numbers. Inner
# project and service pages retain their useful ordered steps.
home=re.sub(r'<span>\d{2}</span>(MINING|EXPLORATION|CONSULTANCY)',r'\1',home)
home=re.sub(r'PROJECT PLACEHOLDER\s*/\s*\d+','PROJECT PLACEHOLDER',home)
# Home page only: remove the photography-credits link from the footer.
home=home.replace('<button id="credits-open">Photography credits</button>','')
pages['/']=('Global Mino | Mining, Exploration & Consultancy',home)
about=hero('About Global Mino','Building value<br>beneath the surface.','An Africa-focused mining, mineral exploration and technical consultancy company.','geologist')
about+=section('WHO WE ARE','Mining expertise.<br>African perspective.','<div class="about-grid editorial"><div><p>Global Mino combines mining expertise, geological knowledge and technical consultancy to identify, evaluate and support mineral opportunities across Africa.</p><p>Our focus connects geological understanding with responsible development and strategic collaboration across Sudan, Ethiopia, Cameroon and the Central African Republic.</p></div><figure class="about-image">'+image('geologist')+'</figure></div>')
about+=section('OUR PURPOSE','Turning mineral potential<br>into sustainable value.','<div class="type-grid"><article><p class="eyebrow">VISION</p><p>To position Global Mino as a trusted African partner in responsible mining, mineral exploration and technical consultancy.</p></article><article><p class="eyebrow">MISSION</p><p>To support mineral opportunities through geological knowledge, technical expertise, responsible practices and strategic collaboration.</p></article></div>','services')
about+=section('OUR VALUES','The principles beneath our work.',blocks('Technical Excellence|Integrity|Safety|Environmental Responsibility|Data Integrity|Partnership|Community Value'))+section('AFRICAN PRESENCE','Four markets. One African vision.',panels(),'operations')+cta('Discover our operations','/operations')
pages['/about']=('About Global Mino | African Mining & Exploration',about)
employees=[
 ('Dr. Hashim Sulieman','Founder & Chief Executive Officer','Founder and CEO of Almogadam Multi Activities Company Ltd, overseeing its Global Mining and Global Health businesses. An occupational medicine physician and business leader with more than 15 years of experience across Europe, Africa and the Middle East.','team-hashim.jpg','hashim-sulieman','MBBS, University of Khartoum · LFOM & MFOM, RCPI Faculty of Occupational Medicine · MRCGP (UK) · MBA International Business & MSc Healthcare Management, Swiss Business School · Higher Diploma in Diabetes, Plymouth University'),
 ('Eng. Muhammad Abdul Rahman Abdul Wahab','Senior Geologist & Data Analyst','A senior geologist and data analyst with more than 20 years of experience, focused on gold mining and mineral exploration alongside oil and gas operations.','team-muhammad.jpg','muhammad-abdul-rahman','B.Sc. Theoretical Geology & Chemistry, Faculty of Science, University of Khartoum'),
 ('Eng. Abdelrazig Ahmed Abdelrazig Ahmed','Technical Consultant & Geologist','A geologist and mining professional with more than 10 years of experience across exploration, production, processing systems, technical consulting and mining-project management.','team-abdelrazig.jpg','abdelrazig-ahmed','B.Sc. Geology, specialising in Petroleum Geology, College of Petroleum and Minerals, Al-Neelain University'),
 ('Eng. Huzaifa Ahmed Salih Mohamed','Processing Engineer','A chemical engineer with more than six years of experience across cement and mining operations, specialising in mineral processing, production quality control and project delivery. He spent three years with Ariab Mining Company, the largest mining company in Sudan.','team-huzaifa.jpg','huzaifa-ahmed-salih','B.Sc. (Honours) in Chemical Engineering'),
 ('Dr. Rawi Elamin','Public Health Epidemiologist','A public health epidemiologist and global health security specialist with 16 years of experience supporting the World Health Organization (WHO) and national Ministries of Health across multiple regions.','team-rawi.jpg','rawi-elamin','MPH Epidemiology & Biostatistics, American University of Beirut · B.Sc. Public Health, University of Bahri'),
 ('Dr. Mona Mohammed','Public & Environmental Health Specialist','A multidisciplinary public and environmental health professional with more than 10 years of experience, focused on occupational health and safety and EHS/HSE management, alongside epidemiology and disease prevention.',None,'mona-mohammed','M.Sc. Public & Environmental Health, University of Gezira · B.Sc. Health & Environmental Sciences, University of Gezira'),
 ('Bushra Babiker Ahmed Babiker','Project Manager','An accounting and project management professional with experience in administration, organisational leadership, publishing and community organisations in Sudan and Lebanon.','team-bushra.jpg','bushra-babiker-ahmed-babiker','MBA Project Management, Sudan International University · B.Sc. Accounting, Omdurman Islamic University'),
 ('Dr. Ahmed Omar','Medical Doctor & Public Health Professional','A medical doctor and public health professional advancing stronger, data-led health systems across Africa and the Caribbean.','team-ahmed-omar.jpg',None,'MPH, KIT Royal Tropical Institute and Vrije Universiteit Amsterdam'),
 ('Dr. Shaker Adam Idrees','Medical Doctor — Emergency & Occupational Medicine','A medical doctor with experience in emergency medicine, occupational medicine and public health across Sudan, Libya and Saudi Arabia since 2009.','team-shaker.jpg','shaker-adam-idrees','MBBS, University of Gadarif · Higher Diploma in Clinical Documentation Improvement, Capilano Consulting Center · Diploma in Occupational Medicine, Royal College of Physicians of Ireland'),
 ('Abdalla Adam Younis Mohammed','Biotechnology & Humanitarian Partnerships Professional','A biotechnology and microbiology graduate with more than 15 years of experience across national and international organisations, emergency response, field operations and NGO partnership coordination.','team-abdalla-adam.jpg','abdalla-adam-younis-mohammed','M.Sc. Disaster Management, International University of Africa · B.Sc. Biotechnology & Microbiology, Omdurman Islamic University'),
 ('Eng. Ogba Adam Edris Ali','Civil Engineer','A civil-engineering professional with experience in project management, infrastructure supervision, quality control, road maintenance and materials testing across Sudan and Saudi Arabia.','team-ogba-adam.jpg','ogba-adam-edris-ali','B.Sc. Civil Engineering · Mini MBA, British International Academy'),
 ('Eng. Ezzeldin Ali Suleiman Omar','Civil Engineer & Infrastructure Supervisor','A civil engineer whose experience spans roads, bridges, public infrastructure, materials supervision and municipal projects in Sudan and Saudi Arabia.','team-ezzeldin-ali.jpg','ezzeldin-ali-suleiman-omar','B.Sc. Civil Engineering — Roads & Transport, Sudan University of Science and Technology'),
]
def portrait(cls,name,photo,lazy=False):
 # A member without a supplied photograph gets an initials tile, hidden from
 # screen readers since the name is already the heading beside it.
 if not photo:
  initials=''.join(w[0] for w in re.sub(r'^(Dr|Eng)\.\s+','',name).split()[:2]).upper()
  return f'<figure class="{cls} portrait-initials" aria-hidden="true"><span>{initials}</span></figure>'
 return f'<figure class="{cls}"><img src="/assets/{photo}" alt="Portrait of {html.escape(name)}"'+(' loading="lazy"' if lazy else '')+'></figure>'
def team_education(text):
 return f'<p class="team-education"><span>Education</span>{html.escape(text)}</p>' if text else ''
def team_bio(content):
 paragraphs=content if isinstance(content,list) else [content]
 return '<div class="team-bio">'+''.join(f'<p>{html.escape(paragraph)}</p>' for paragraph in paragraphs)+'</div>'
team_cards=''.join(f'''<article class="team-card{' leadership-profile' if i==1 else ''}">
 {portrait('team-portrait',name,photo,True)}
 <div class="team-card-body"><h3>{html.escape(name)}</h3><p class="team-role">{html.escape(role)}</p>{team_bio(bio)}{team_education(edu)}{link('VIEW FULL CV PROFILE','/team/'+slug) if slug else ''}</div>
</article>''' for i,(name,role,bio,photo,slug,edu) in enumerate(employees,1))
team=hero('Our Team','Knowledge in the field.<br><em>Leadership with purpose.</em>','Meet the people guiding Global Mino’s work across mining, mineral exploration and technical consultancy.','geologist')
team+=section('OUR PEOPLE','Expertise that moves<br>opportunity forward.','<div class="team-intro"><p>Our work is shaped by technical understanding, local context and a clear responsibility to the people and places connected to every opportunity.</p><p>Across geology, processing, public health, environmental health and project delivery, our team brings complementary expertise to each engagement.</p></div><div class="team-grid">'+team_cards+'</div>','team-section')
team+=cta('Work with our team','/contact')
pages['/team']=('Our Team | Global Mino',team)
def profile_items(items):
 return '<div class="credential-list">'+''.join('<article><h3>'+html.escape(item.get('qualification',item.get('title','')))+' </h3>'+(f'<p class="credential-place">{html.escape(item["institution"])}</p>' if item.get('institution') else '')+(f'<p>{html.escape(item["provider"])}</p>' if item.get('provider') else '')+'<p class="credential-meta">'+' · '.join(html.escape(x) for x in [item.get('location',''),item.get('date',''),item.get('status','')] if x)+'</p>'+(f'<p>{html.escape(item["details"])}</p>' if item.get('details') else '')+'</article>' for item in items)+'</div>'
def profile_tags(items):
 return '<div class="profile-tags">'+''.join(f'<span>{html.escape(item)}</span>' for item in items)+'</div>'
def member_profile(slug,data):
 body=f'''<section class="member-hero">
 <div class="member-heading"><div class="breadcrumb"><a href="/team">Our team</a><span aria-hidden="true">/</span><span>{html.escape(data['name'])}</span></div><p class="eyebrow">PROFESSIONAL PROFILE</p><h1>{html.escape(data['name'])}</h1><p class="member-role">{html.escape(data['role'])}</p><p class="member-summary">{html.escape(data['summary'])}</p></div>
 {portrait('member-photo',data['name'],data['photo'])}
 </section>
 <nav class="member-nav" aria-label="Profile sections"><a href="#education">Education</a><a href="#experience">Experience</a>{'<a href="#certifications">Certifications</a>' if data.get('certifications') else ''}</nav>
 <div class="member-profile-content">
 <section class="profile-section" id="education"><div class="profile-section-heading"><p class="eyebrow">EDUCATION</p><h2>Academic background.</h2></div>{profile_items(data['education'])}</section>'''
 if data.get('certifications'):
  body+=f'<section class="profile-section soft" id="certifications"><div class="profile-section-heading"><p class="eyebrow">PROFESSIONAL DEVELOPMENT</p><h2>Certifications and training.</h2></div>{profile_items(data["certifications"])}</section>'
 body+='<section class="profile-section" id="experience"><div class="profile-section-heading"><p class="eyebrow">CAREER HISTORY</p><h2>Professional experience.</h2></div><div class="career-timeline">'
 for job in data['experience']:
  details=''.join(f'<li>{html.escape(detail)}</li>' for detail in job.get('details',[]))
  body+=f'''<article><div class="career-when"><span>{html.escape(job.get('date',''))}</span><small>{html.escape(job.get('location',''))}</small></div><div class="career-detail"><h3>{html.escape(job['role'])}</h3><p class="career-company">{html.escape(job['company'])}</p>{'<ul>'+details+'</ul>' if details else ''}</div></article>'''
 body+='</div></section>'
 extras=[('expertise','CORE EXPERTISE','Areas of practice.'),('affiliations','AFFILIATIONS & COMMUNITY','Professional participation.'),('publications','PUBLICATIONS & REPORTS','Selected published work.'),('research','RESEARCH','Research activity.'),('projects','INNOVATION & PROJECTS','Selected initiatives.')]
 for key,label,title in extras:
  if data.get(key): body+=f'<section class="profile-section compact"><div class="profile-section-heading"><p class="eyebrow">{label}</p><h2>{title}</h2></div>{profile_tags(data[key])}</section>'
 body+='</div>'
 return body+cta('Work with our team','/contact')
for slug,data in TEAM_PROFILES.items():
 pages['/team/'+slug]=(data['name']+' | Global Mino Team',member_profile(slug,data))
# Mining site visits gallery. Photographs have not been supplied yet, so each
# frame renders as a reserved slot rather than an <img>; site_visits.py holds
# the per-visit record and every pending value is labelled as pending on the
# page itself. Adding a file name and caption there is enough to publish a
# photograph — the grid, the counters and the lightbox all read the same data.
def visit_photo(visit,index,total,photo):
 number=f'{index:02}'
 caption=photo.get('caption') or f'Photograph {number} · caption to be supplied'
 collection=visit['country']+' site visit'
 label=f'Open photograph {index} of {total} from the {collection}'
 if photo.get('src'):
  media=f'<img src="/assets/{photo["src"]}" alt="{html.escape(caption,quote=True)}" loading="lazy" width="1400" height="1050">'
  source=f' data-full="/assets/{photo["src"]}"'
 else:
  media=f'<span class="shot-pending" aria-hidden="true"><b>{number}</b><i>Awaiting photograph</i></span>'
  source=''
 # The lead frame covers a 2x2 area. When the remaining frames would leave a
 # single empty cell at the end of the grid, the last one widens to close it.
 shape=' feature' if index==1 else (' wide' if index==total and (total+3)%4==3 else '')
 return (f'<button class="shot{shape}" type="button"{source} data-caption="{html.escape(caption,quote=True)}"'
  f' data-collection="{html.escape(collection,quote=True)}" aria-label="{html.escape(label,quote=True)}">{media}'
  '<span class="shot-hint" aria-hidden="true">VIEW <b>↗</b></span></button>')
def visit_section(index,visit):
 total=len(visit['photos'])
 supplied=sum(1 for photo in visit['photos'] if photo.get('src'))
 meta=[('Location',visit['site']),('Visit date',visit['date']),('Visiting team',visit['party']),('Focus of work',visit['focus']),('Photographs',f'{supplied} of {total} supplied' if supplied else f'{total} frames reserved')]
 return f'''<article class="visit" id="visit-{visit['slug']}" aria-labelledby="visit-{visit['slug']}-title">
 <div class="visit-head">
 <div class="visit-headline"><p class="eyebrow">VISIT {index:02} / {html.escape(visit['country'].upper())}</p><h2 id="visit-{visit['slug']}-title">{html.escape(visit['country'])}</h2></div>
 <p class="visit-copy">{visit['description']}</p>
 <dl class="visit-meta">{''.join(f'<div><dt>{a}</dt><dd>{html.escape(b)}</dd></div>' for a,b in meta)}</dl>
 </div>
 <div class="visit-grid{' cols-3' if total==3 else ''}">{''.join(visit_photo(visit,n,total,photo) for n,photo in enumerate(visit['photos'],1))}</div>
 </article>'''
lightbox='''<dialog id="lightbox" class="lightbox" aria-label="Site visit photograph viewer">
 <div class="lightbox-inner">
 <div class="lightbox-bar"><p class="lightbox-collection" data-lightbox-collection></p><button class="lightbox-close dialog-close" type="button">CLOSE <span aria-hidden="true">✕</span></button></div>
 <figure class="lightbox-figure"><div class="lightbox-stage" data-lightbox-stage></div><figcaption class="lightbox-caption" data-lightbox-caption aria-live="polite"></figcaption></figure>
 <div class="lightbox-foot"><p class="lightbox-count" data-lightbox-count></p><div class="lightbox-nav"><button type="button" data-lightbox-prev aria-label="Previous photograph"><span aria-hidden="true">‹</span></button><button type="button" data-lightbox-next aria-label="Next photograph"><span aria-hidden="true">›</span></button></div></div>
 </div>
 </dialog>'''
gallery=hero('Gallery','Inside the field.<br><em>Site by site.</em>','Photographs from our team’s visits to mining locations across Sudan, Cameroon and the Central African Republic.','sudan')
gallery+=section('FIELD RECORD','A record of our visits<br>to mining locations.','<p class="intro-copy">Site visits are where the geological, processing and occupational health work actually happens. This page gathers the photography from those visits, grouped by location, so each set can be opened and viewed as a complete collection.</p>')
gallery+='<div class="visits">'+''.join(visit_section(i,visit) for i,visit in enumerate(VISITS,1))+'</div>'+lightbox
gallery+=cta('Discuss a site visit','/contact')
pages['/gallery']=('Gallery | Global Mino',gallery)
# Message from the Founder & Chief Executive Officer. The letter is reproduced
# from the supplied text in ceo_message.py; the module records where that text
# breaks off. Nothing here writes company statements of its own.
letter=''
for part in ceo.SECTIONS:
 if part['heading']: letter+=f'<h2>{html.escape(part["heading"])}</h2>'
 if part.get('quote'): letter+=f'<blockquote class="ceo-quote"><p>{html.escape(part["quote"])}</p></blockquote>'
 letter+=''.join(f'<p>{html.escape(paragraph)}</p>' for paragraph in part['paragraphs'])
message=f'''<section class="ceo-hero">
 <div class="ceo-hero-copy">
 <div class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><span>CEO message</span></div>
 <p class="eyebrow">CEO MESSAGE</p>
 <h1>Message from the Founder<br><em>&amp; Chief Executive Officer</em></h1>
 <p class="ceo-company">{html.escape(ceo.COMPANY)}</p>
 <p class="ceo-lead">{html.escape(ceo.LEAD)}</p>
 </div>
 <figure class="ceo-portrait">
 <img src="/assets/{ceo.PHOTO}" alt="Portrait of {html.escape(ceo.NAME,quote=True)}, {html.escape(ceo.ROLE,quote=True)}" width="{ceo.PHOTO_SIZE[0]}" height="{ceo.PHOTO_SIZE[1]}">
 <figcaption><b>{html.escape(ceo.NAME)}</b><span>{html.escape(ceo.ROLE)}</span></figcaption>
 </figure>
 </section>
 <section class="section ceo-letter"><div class="ceo-letter-body">{letter}</div>
 <div class="ceo-signoff"><p class="ceo-signoff-name">{html.escape(ceo.NAME)}</p><p class="ceo-signoff-role">{html.escape(ceo.ROLE)}</p>{link("VIEW FULL CV PROFILE",ceo.PROFILE)}</div>
 </section>'''
pages['/ceo-message']=('CEO Message | Global Mino',message+cta())
pages['/operations']=('Operations | Global Mino',hero('Operations','Across Africa.<br>Closer to opportunity.',"Global Mino’s operations connect geological understanding, mineral opportunities and technical expertise across selected African markets.",'sudan')+section('COUNTRY EXPERIENCE','Grounded in African opportunity.',panels(True),'operations')+cta())
for name,slug,img,title,caps in countries:
 d=PROFILES[slug]
 country_links=''.join(f'<a href="/countries/{c[1]}"'+(' aria-current="page"' if c[1]==slug else '')+f'>{c[0]}</a>' for c in countries)
 opportunities=''.join(f'<article><span class="profile-number">0{i}</span><h3>{html.escape(label)}</h3><p>{html.escape(copy)}</p></article>' for i,(label,copy) in enumerate(d['opportunities'],1))
 sources=''.join(f'<li><a href="{url}">{html.escape(label)} ↗</a></li>' for label,url in d['sources'])
 body=f'''<div class="country-profile">
 <section class="profile-hero">
 <div class="profile-heading"><div class="breadcrumb"><a href="/operations">Our countries</a><span aria-hidden="true">/</span><span>{name}</span></div>
 <p class="eyebrow">GOLD, MINING &amp; OPPORTUNITIES</p><h1>{name}</h1><p class="profile-intro">{d['intro']}</p>
 <a class="button gold" href="/contact?country={slug}">DISCUSS AN OPPORTUNITY <span>↗</span></a></div>
 <figure class="profile-photo">{image(img)}</figure>
 </section>
 <div class="profile-country-switch" role="navigation" aria-label="Explore countries">{country_links}</div>
 <div class="profile-content">
 <section class="profile-overview" aria-labelledby="overview"><div><p class="eyebrow">COUNTRY OVERVIEW</p><h2 id="overview">Mining at a glance.</h2></div><dl><div><dt>Key minerals</dt><dd>{d['minerals']}</dd></div><div><dt>Geographic focus</dt><dd>{d['regions']}</dd></div></dl></section>
 <section class="profile-mining" aria-label="Gold and mining"><article><span class="profile-label">01 / GOLD</span><h2>Gold in {name}.</h2><p>{d['gold']}</p></article><article><span class="profile-label">02 / MINING</span><h2>The wider mining sector.</h2><p>{d['mining']}</p></article></section>
 <section class="profile-opportunities" aria-labelledby="opportunities"><p class="eyebrow">03 / OPPORTUNITIES</p><h2 id="opportunities">Where to explore potential.</h2><p class="profile-section-intro">Areas for technical assessment, subject to site verification and feasibility.</p><div class="profile-cards">{opportunities}</div></section>
 <aside class="profile-note"><h3>Before moving forward</h3><p>{d['consideration']}</p></aside>
 <section class="profile-support"><div><p class="eyebrow">HOW GLOBAL MINO CAN HELP</p><h2>Start with a clearer picture.</h2><p>Geological review, exploration planning and technical assessment to help you understand your next step.</p></div><a class="button gold" href="/contact?country={slug}&amp;interest=mineral-exploration">TALK TO OUR TEAM <span>↗</span></a></section>
 <details class="profile-sources"><summary>Sources &amp; country notes</summary><p>Country background is based on the sources below. Opportunity themes are proposed areas of assessment, not verified projects, available concessions or a statement of Global Mino ownership.</p><ul>{sources}</ul></details>
 </div></div>'''
 pages['/countries/'+slug]=(name+' Gold, Mining & Opportunities | Global Mino',body)
body=hero('Our Services','Expertise across the<br>mining lifecycle.','Mining, exploration and technical advice connected by geological knowledge.')
body+='<section class="section services">'
for i,s in enumerate(services): body+=f'<article class="service {"reverse" if i%2 else ""}"><div class="service-image">{image(s[2])}</div><div class="service-copy"><span class="service-no">0{i+1}</span><p class="eyebrow">{s[0].upper()}</p><h2>{s[3]}</h2><p>Supporting {s[0].lower()} opportunities through geological knowledge, technical expertise and responsible practices.</p>{link("EXPLORE "+s[0].upper(),"/services/"+s[1])}</div></article>'
pages['/services']=('Services | Global Mino',body+'</section>'+cta())
for s in services:
 pages['/services/'+s[1]]=(s[0]+' | Global Mino',hero(s[0],s[3],f'{s[0]} expertise supporting informed decisions and responsible mineral opportunity development.',s[2])+section('TECHNICAL CAPABILITIES','Knowledge that supports<br>better decisions.',blocks(s[4]))+process(s[5])+cta('Discuss '+('a gold mining opportunity' if s[1]=='gold-mining' else s[0]),'/contact?interest='+s[1]))
# Occupational Health & Safety gets a bespoke, claim-safe body. It describes
# Global Mino's management approach and intended controls; it does not claim
# certification, performance results or an incident record.
def safety_icon(kind):
 paths={
  'shield':'<path d="M12 3 5 6v5c0 4.6 2.8 8 7 10 4.2-2 7-5.4 7-10V6l-7-3Z"/><path d="m9 12 2 2 4-4"/>',
  'mine':'<path d="M3 20h18L17 5H7L3 20Z"/><path d="M6 15h12M8 10h8M12 5v15"/>',
  'field':'<path d="M4 20c2-6 5-9 8-9s6 3 8 9M12 11V4m0 0-3 3m3-3 3 3"/>',
  'medical':'<path d="M9 3h6v6h6v6h-6v6H9v-6H3V9h6V3Z"/>',
  'training':'<path d="M3 5.5A3.5 3.5 0 0 1 6.5 2H11v17H6.5A3.5 3.5 0 0 0 3 22V5.5ZM21 5.5A3.5 3.5 0 0 0 17.5 2H13v17h4.5A3.5 3.5 0 0 1 21 22V5.5Z"/>',
  'compliance':'<path d="M6 3h12v18H6z"/><path d="M9 8h6m-6 4h6m-6 4h3"/>',
  'alert':'<path d="m12 3 10 18H2L12 3Z"/><path d="M12 9v5m0 3v.1"/>',
  'equipment':'<circle cx="8" cy="18" r="3"/><circle cx="18" cy="18" r="3"/><path d="M3 18V9h9l3 5h4l2 4M6 9l2-4h5l2 9"/>',
 }
 return f'<svg class="ohs-icon" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{paths[kind]}</svg>'
def ohs_cards(items):
 return '<div class="ohs-card-grid">'+''.join(f'<article class="ohs-card">{safety_icon(icon)}<h3>{title}</h3><p>{copy}</p></article>' for icon,title,copy in items)+'</div>'

ohs='''<section class="ohs-hero">
 <img src="/assets/ohs-mining-safety.jpg" alt="Mine safety team conducting a pre-shift inspection at an open-pit mine" width="1536" height="1024">
 <div class="ohs-hero-shade"></div><div class="ohs-hero-content"><div class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><a href="/services">Services</a><span aria-hidden="true">/</span><span>Occupational Health &amp; Safety</span></div><p class="eyebrow">OCCUPATIONAL HEALTH &amp; SAFETY</p><h1>Safe work is<br><em>the only work.</em></h1><p>Global Mino’s OHS approach is built for gold mining, mineral exploration and remote field operations—protecting employees, contractors, visitors and neighbouring communities through planned controls, clear accountability and readiness to respond.</p><div class="actions"><a class="button gold" href="#ohs-framework">EXPLORE OUR OHS FRAMEWORK <span>↓</span></a></div></div>
 <div class="ohs-hero-note"><span>01</span><p>Identify hazards</p><span>02</span><p>Control exposure</p><span>03</span><p>Verify &amp; improve</p></div>
 </section>'''
ohs+='''<nav class="ohs-local-nav" aria-label="Occupational health and safety sections"><a href="#mining-safety">Mining sites</a><a href="#field-safety">Exploration &amp; field</a><a href="#emergency">Emergency</a><a href="#wellbeing">Health &amp; wellbeing</a><a href="#training">Training</a><a href="#compliance">Standards &amp; compliance</a></nav>'''
ohs+='''<section class="section ohs-intro" id="ohs-framework"><div><p class="eyebrow">OUR COMMITMENT</p><h2>Everyone goes to work<br>with the right to return safe.</h2></div><div><p class="ohs-lede">Our objective is to prevent injury and work-related ill health by planning safe work, consulting the people who perform it and acting when conditions are unsafe.</p><p>The same expectations extend to employees, contractors and visitors. Site controls also consider traffic, dust, water, blasting, access and emergency scenarios that could affect surrounding communities.</p><div class="ohs-commitments"><span>Stop-work authority</span><span>Visible leadership</span><span>Worker consultation</span><span>No retaliation for reporting</span></div></div></section>'''
policy_items=[
 ('shield','Leadership & accountability','Managers define responsibilities, provide resources and verify critical controls. Supervisors confirm work is understood before it starts; every individual remains responsible for following controls and raising concerns.'),
 ('alert','Risk before task','Baseline assessments, task risk reviews and pre-start checks identify hazards, affected people and credible worst-case outcomes before work is authorised.'),
 ('medical','Fit for work','Fitness, fatigue, heat strain, exposure and wellbeing are considered alongside task capability, with personal health information handled confidentially.'),
 ('field','Inclusive protection','Inductions, permits, traffic plans, exclusion zones and emergency information apply to employees, contractors and visitors; off-site impacts are considered for neighbouring communities.'),
]
ohs+=section('OHS POLICY','Principles that guide<br>every operating decision.',ohs_cards(policy_items),'ohs-soft')
ohs+='''<section class="section ohs-risk"><div class="section-top"><p class="eyebrow">RISK ASSESSMENT &amp; HAZARD IDENTIFICATION</p></div><div class="ohs-risk-heading"><h2>See the risk.<br>Set the control.<br>Check it holds.</h2><p>Risk management begins before mobilisation and continues as ground, weather, people and equipment change. Controls follow the hierarchy: eliminate the hazard where practicable, then substitute, engineer, administrate and use PPE for remaining exposure.</p></div><ol class="ohs-flow" aria-label="OHS risk management process"><li><span>01</span><strong>Identify</strong><small>People, task, energy and environment</small></li><li><span>02</span><strong>Assess</strong><small>Likelihood, consequence and exposure</small></li><li><span>03</span><strong>Control</strong><small>Prioritise higher-order controls</small></li><li><span>04</span><strong>Communicate</strong><small>Brief, authorise and confirm understanding</small></li><li><span>05</span><strong>Verify</strong><small>Inspect critical controls in the field</small></li><li><span>06</span><strong>Improve</strong><small>Learn from work, change and events</small></li></ol><aside class="ohs-stop"><strong>STOP WORK</strong><p>Anyone should pause a task when controls are absent, conditions change or the work is not understood. Work resumes only after the risk is reassessed and controls are restored.</p></aside></section>'''
mining_items=[
 ('equipment','Mobile equipment & traffic','Separate people and vehicles through traffic plans, designated walkways, positive communication, speed controls, lighting, berms and exclusion zones. Seat belts and pre-start inspections are mandatory expectations.'),
 ('mine','Ground control & excavations','Inspect benches, faces, highwalls, stockpiles, trenches and access routes. Establish stand-off distances, edge protection and barricades, and reassess after rain, blasting or visible change.'),
 ('alert','Energy isolation','Identify every energy source before maintenance. Isolation, lockout, verification and controlled return to service are completed by authorised, competent people.'),
 ('shield','Processing & hazardous materials','Guard moving parts, control stored energy, maintain ventilation and manage chemicals through labels, safety data, compatible storage, spill controls and task-specific protection.'),
]
ohs+=f'''<section class="section ohs-dark" id="mining-safety"><div class="section-top"><p class="eyebrow">MINING SITE SAFETY</p></div><div class="ohs-split-heading"><h2>Critical controls<br>where energy is highest.</h2><p>Mining hazards can have severe consequences. The operating focus is on controlling interactions between people, vehicles, unstable ground, machinery, electricity, explosives and process materials.</p></div>{ohs_cards(mining_items)}<div class="ohs-equipment-strip"><div>{safety_icon('equipment')}<h3>Mining equipment safety</h3></div><ul><li>Competent, authorised operators</li><li>Documented pre-start inspections</li><li>Guarding and safety devices</li><li>Defect isolation and escalation</li><li>Planned maintenance controls</li><li>Pedestrian–vehicle separation</li></ul></div></section>'''
ohs+='''<section class="ohs-field" id="field-safety"><figure><img src="/assets/ohs-field-safety.jpg" alt="Exploration team checking communications and first-aid equipment before remote fieldwork" loading="lazy" width="1536" height="1024"></figure><div class="ohs-field-copy"><p class="eyebrow">EXPLORATION &amp; FIELD SAFETY</p><h2>Prepared beyond<br>the last paved road.</h2><p>Remote exploration requires the same discipline as an operating mine, with added attention to isolation, travel and delayed access to care.</p><ul class="ohs-check-list"><li><strong>Journey management</strong><span>Route, driver, vehicle, weather, check-in schedule and overdue action agreed before departure.</span></li><li><strong>Remote communications</strong><span>Primary and backup communication, tested coverage and location-sharing appropriate to the work.</span></li><li><strong>Field hazards</strong><span>Terrain, heat, lightning, wildlife, water, manual handling, sampling tools and community access assessed daily.</span></li><li><strong>Buddy system</strong><span>No isolated work without an approved lone-work control and reliable escalation method.</span></li></ul></div></section>'''
ohs+='''<section class="section ohs-ppe"><div class="section-top"><p class="eyebrow">PERSONAL PROTECTIVE EQUIPMENT</p></div><div class="ohs-split-heading"><h2>The last line of defence.<br>Never the first plan.</h2><p>PPE is selected from the task and exposure assessment, provided in suitable sizes, inspected before use and replaced when damaged. Training covers fit, limitations, cleaning and storage.</p></div><div class="ppe-list"><article><span>01</span><h3>Core site PPE</h3><p>Hard hat, safety eyewear, high-visibility clothing and protective footwear where site rules require them.</p></article><article><span>02</span><h3>Exposure-specific PPE</h3><p>Hearing, respiratory, hand, face, fall and chemical protection matched to the identified hazard.</p></article><article><span>03</span><h3>Fit &amp; compatibility</h3><p>Respirator fit and compatibility between multiple items are checked; facial hair and damaged seals are addressed.</p></article><article><span>04</span><h3>Visitor controls</h3><p>Visitors receive an induction, escort and correctly sized PPE before entering controlled operating areas.</p></article></div></section>'''
emergency_items=[
 ('alert','Scenario planning','Plans address credible events such as vehicle incidents, fire, medical emergencies, ground failure, hazardous release, severe weather, security events and missing persons.'),
 ('medical','On-site response','Alarm methods, trained responders, first-aid resources, rescue capability and incident command are proportionate to site risk and remoteness.'),
 ('field','Evacuation & coordination','Muster points, evacuation routes, medevac triggers and contact arrangements with transport providers, receiving facilities and relevant authorities are defined and tested.'),
]
ohs+=f'''<section class="section ohs-emergency" id="emergency"><div class="section-top"><p class="eyebrow">EMERGENCY PREPAREDNESS</p></div><div class="ohs-split-heading"><h2>Ready before<br>the alarm sounds.</h2><p>Emergency plans are site-specific, accessible and practiced. Drills test the full chain—from detection and first actions to accountability, communication, evacuation and recovery.</p></div>{ohs_cards(emergency_items)}<div class="emergency-sequence"><span>Detect</span><i></i><span>Raise alarm</span><i></i><span>Stabilise</span><i></i><span>Account</span><i></i><span>Escalate</span><i></i><span>Recover</span></div><p class="community-note"><strong>Community interface:</strong> Where an operational emergency could extend beyond a site boundary, planning includes warning methods, liaison responsibilities, access controls and coordination with community representatives and public responders.</p></section>'''
ohs+='''<section class="section ohs-health" id="wellbeing"><div><p class="eyebrow">EMPLOYEE HEALTH &amp; WELLBEING</p><h2>Protect health across<br>the full working life.</h2><p>Occupational health programmes should connect exposure information with confidential health monitoring so early signs of harm can trigger better controls—not blame.</p></div><div class="health-matrix"><article><strong>Health risk assessment</strong><span>Dust and silica · noise · vibration · heat · chemicals · ergonomics · biological hazards</span></article><article><strong>Fitness for task</strong><span>Role demands · work restrictions · fatigue and shift patterns · safe return to work</span></article><article><strong>Health surveillance</strong><span>Risk-based baseline and periodic checks where exposure indicates a need</span></article><article><strong>Wellbeing support</strong><span>Mental health awareness · hydration · nutrition · fatigue reporting · respectful workplace</span></article><article><strong>Confidentiality</strong><span>Clinical information protected; management receives only fit-for-work guidance and anonymised trends where appropriate</span></article></div></section>'''
ohs+=f'''<section class="section ohs-training" id="training"><div class="section-top"><p class="eyebrow">SAFETY TRAINING</p></div><div class="ohs-split-heading"><h2>Competence is shown<br>in the field.</h2><p>Training is role- and risk-based. Understanding is checked through observation, demonstration and supervision—not attendance alone.</p></div><div class="training-path"><article><span>01</span><h3>Induct</h3><p>Site rules, hazards, emergency actions, reporting and stop-work expectations.</p></article><article><span>02</span><h3>Train</h3><p>Task procedures, permits, equipment, PPE and critical controls for the role.</p></article><article><span>03</span><h3>Verify</h3><p>Competency assessment before unsupervised or safety-critical work.</p></article><article><span>04</span><h3>Refresh</h3><p>Retraining after change, extended absence, an event or identified performance gap.</p></article></div><div class="toolbox-callout">{safety_icon('training')}<div><h3>Every shift starts with context.</h3><p>Pre-start and toolbox conversations cover today’s work, interactions, changing conditions, lessons from recent events and the controls people must verify.</p></div></div></section>'''
ohs+='''<section class="section ohs-reporting"><div class="section-top"><p class="eyebrow">INCIDENT PREVENTION &amp; REPORTING</p></div><div class="ohs-report-grid"><div><h2>Report early.<br>Learn completely.</h2><p>Hazards, near misses, injuries, illnesses, spills, equipment damage and community concerns should be reported promptly. Immediate care and scene safety come first; investigations then focus on system causes and control improvement.</p><p>A fair, learning-focused culture protects good-faith reporting. Deliberate reckless conduct is handled separately from human error and system weakness.</p></div><ol><li><span>01</span><div><strong>Make safe</strong><small>Stop, assist and prevent further harm.</small></div></li><li><span>02</span><div><strong>Notify</strong><small>Use the site escalation route without delay.</small></div></li><li><span>03</span><div><strong>Preserve &amp; understand</strong><small>Secure evidence and involve the people who know the work.</small></div></li><li><span>04</span><div><strong>Correct &amp; share</strong><small>Assign actions, verify effectiveness and communicate learning.</small></div></li></ol></div></section>'''
ohs+='''<section class="section ohs-environment"><div class="section-top"><p class="eyebrow">ENVIRONMENTAL &amp; SITE SAFETY</p></div><div class="ohs-split-heading"><h2>Safe sites respect<br>their wider setting.</h2><p>OHS and environmental controls meet wherever work can affect air, water, land, access or people beyond the immediate task.</p></div><div class="environment-bands"><article><strong>Dust &amp; air</strong><span>Suppress, enclose, monitor and maintain separation from receptors.</span></article><article><strong>Water &amp; chemicals</strong><span>Protect storage, manage spills and keep contaminated flows controlled.</span></article><article><strong>Waste &amp; housekeeping</strong><span>Segregate, contain and remove materials while keeping access and emergency routes clear.</span></article><article><strong>Site security</strong><span>Control entry, sign hazards and protect visitors and communities from operational areas.</span></article><article><strong>Noise, vibration &amp; blasting</strong><span>Plan, communicate, exclude and monitor in relation to workers and nearby communities.</span></article></div></section>'''
ohs+='''<section class="section ohs-compliance" id="compliance"><div class="section-top"><p class="eyebrow">OHS STANDARDS &amp; COMPLIANCE</p></div><div class="ohs-compliance-grid"><div><h2>Requirements made<br>visible at the workface.</h2><p>Before work begins, the applicable legal, regulatory, permit, contractual and site requirements are identified for the country and activity. Responsibilities, records and verification methods are then built into work plans and contractor controls.</p><p>Audits and inspections are used to test implementation and close gaps. Requirements are reviewed when legislation, scope, equipment or site conditions change.</p><aside><strong>Clear statement</strong><span>This page does not claim that Global Mino holds a particular OHS certification or has achieved a specific safety performance result. Any future certification or numerical performance claim should be published only after independent verification and company approval.</span></aside></div><div class="compliance-layers"><article><span>01</span><strong>Applicable law &amp; regulation</strong></article><article><span>02</span><strong>Permits &amp; licence conditions</strong></article><article><span>03</span><strong>Client, partner &amp; site rules</strong></article><article><span>04</span><strong>Recognised industry good practice</strong></article><article><span>05</span><strong>Global Mino procedures &amp; records</strong></article></div></div></section>'''
ohs+='''<section class="section ohs-kpi"><div class="section-top"><p class="eyebrow">MEASUREMENT &amp; CONTINUOUS IMPROVEMENT</p></div><div class="ohs-split-heading"><h2>Measure what prevents harm.</h2><p>Performance review should combine leading indicators with verified event data. Trends are used to prioritise resources, update risk controls and share lessons across projects.</p></div><div class="kpi-grid"><article><span>LEADING</span><h3>Critical controls verified</h3><p>Field checks confirming the barriers for high-consequence hazards are present and effective.</p></article><article><span>LEADING</span><h3>Actions closed effectively</h3><p>Corrective actions completed on time and checked for sustained effectiveness.</p></article><article><span>LEADING</span><h3>Training &amp; competency current</h3><p>Role requirements completed, assessed and refreshed when conditions change.</p></article><article><span>HEALTH</span><h3>Surveillance completed</h3><p>Risk-based monitoring participation and anonymised trends, handled confidentially.</p></article><article><span>LEARNING</span><h3>Hazards &amp; near misses reported</h3><p>Reporting quality and learning themes—not numerical targets that discourage speaking up.</p></article><article><span>OUTCOME</span><h3>Verified incident trends</h3><p>Severity, exposure and recurrence reviewed only from validated operational data.</p></article></div><p class="kpi-disclaimer">No company accident rate, certification status or achievement figure is displayed because verified source data has not been provided.</p><ol class="improvement-loop" aria-label="Continuous improvement cycle"><li>Plan</li><li>Do</li><li>Check</li><li>Learn</li><li>Improve</li></ol></section>'''
ohs+='<section class="contact ohs-cta"><div class="contact-intro"><p class="eyebrow">PARTNER WITH GLOBAL MINO</p><h2>Build risk control<br>into every operation.</h2><p>Discuss occupational health, field safety, emergency preparedness and practical OHS systems for mining and exploration work.</p><div class="actions">'+link('DISCUSS HEALTH & SAFETY','/contact','button gold')+'</div></div></section>'
pages['/services/occupational-health-safety']=('Occupational Health & Safety | Global Mino',ohs)

filters='<div class="filters" role="group" aria-label="Filter projects by country">'+''.join(f'<button type="button" data-filter="{key}" aria-pressed="{str(key=="all").lower()}">{name}</button>' for name,key in [('All','all')]+[(c[0],c[1]) for c in countries])+'</div><p id="filter-status" class="filter-status" aria-live="polite">3 project placeholders shown.</p>'
pages['/projects']=('Projects | Global Mino',hero('Projects & Opportunities','From mineral potential<br>to progress.','Explore our country focus. Project information is awaiting verification.','sudan')+section('PROJECT DIRECTORY','Opportunities in focus.',filters+projects(),'projects')+cta())
for i,c in enumerate(countries,1):
 d=PROFILES[c[1]]
 kind='Gold Mining' if i==1 else 'Exploration'
 body=hero('Project placeholder',f'Project 0{i}',c[0]+' · '+kind+' · Project information coming soon.',c[2])
 # Project specifics are still unverified. Everything shown below is sourced
 # country background, and the notice keeps that distinction explicit.
 notice=f'<article class="detail-block project-notice"><p class="eyebrow">STATUS</p><h2>Project details pending</h2><p>Verified information for this project has not yet been provided. The background below describes the mineral context of {c[0]} from the published sources listed at the foot of this page. It does not describe a Global Mino concession, licence, ownership interest or active project.</p></article>'
 regional=[('Country Overview',d['intro']),('Gold in '+c[0],d['gold']),('The Wider Mining Sector',d['mining']),('Before Moving Forward',d['consideration'])]
 blocks_=''.join(f'<article class="detail-block"><p class="eyebrow">{label.upper()}</p><h2>{html.escape(label)}</h2><p>{text}</p></article>' for label,text in regional)
 facts=[('Country',c[0]),('Key minerals (country)',d['minerals']),('Geographic focus (country)',d['regions']),('Project type',kind),('Commodity','Not confirmed'),('Stage','Not confirmed'),('Status','Information coming soon')]
 body+='<section class="section project-detail"><div>'+notice+blocks_+'</div><aside><p class="eyebrow">PROJECT INFORMATION</p><dl>'+''.join(f'<dt>{a}</dt><dd>{b}</dd>' for a,b in facts)+'</dl></aside></section>'
 sources=''.join(f'<li><a href="{url}">{html.escape(label)} ↗</a></li>' for label,url in d['sources'])
 body+=f'<section class="section project-sources"><p class="eyebrow">SOURCES</p><h2>Where this background comes from.</h2><p class="project-sources-intro">Country background on this page is drawn from the publications below. It is general mineral-sector context for {c[0]}, not a description of a Global Mino project, concession or available licence.</p><ul>{sources}</ul></section>'
 body+=section('GALLERY','A perspective from the field.','<figure class="gallery">'+image(c[2])+'</figure>')+cta('Discuss this opportunity',f'/contact?project=project-0{i}')
 pages[f'/projects/project-0{i}']=(f'Project 0{i} | Global Mino',body)
# The enquiries table constrains `country`, and api/contact.js and server.cjs
# validate the same values. Ethiopia is left out of this list until
# supabase/migrations/202609180001_add_ethiopia_country.sql has been applied to
# the database; offering it sooner would let a visitor submit an enquiry the
# database then refuses. Add it to all four places together.
enquiry_countries=[c for c in countries if c[1]!='ethiopia']
def field(label,name,typ='text',required=False): return f'<label>{label}{" *" if required else ""}<input name="{name}" type="{typ}" {"required" if required else ""} maxlength="200" autocomplete="{dict(name="name",company="organization",email="email",phone="tel").get(name,"off")}"></label>'
form='<form id="contact-form"><div class="form-heading"><p class="eyebrow">YOUR NEXT OPPORTUNITY</p><h3>Send an enquiry.</h3><p>Tell us where you are working and how we can help.</p></div><div class="form-grid">'+field('Full Name','name',required=True)+field('Company','company')+field('Email','email','email',True)+field('Phone','phone','tel')+'<label>Country *<select name="country" required><option value="">Select a country</option>'+''.join(f'<option value="{c[1]}">{c[0]}</option>' for c in enquiry_countries)+'<option value="other">Other</option></select></label><label>Area of Interest *<select name="interest" required><option value="">Select an interest</option>'+''.join(f'<option value="{x.lower().replace(" ","-")}">{x}</option>' for x in ['Gold Mining','Mineral Exploration','Mining Consultancy','Investment Opportunity','Partnership','Other'])+'</select></label><label class="full">Message *<textarea aria-describedby="message-hint" name="message" required minlength="10" maxlength="5000" rows="6" placeholder="Tell us about your opportunity, location and the support you need."></textarea><span id="message-hint" class="field-hint">At least 10 characters.</span></label></div><p class="form-note">* Required fields. Your details are used to respond to this enquiry.</p><button class="button gold" type="submit">SEND ENQUIRY <span>↗</span></button><p id="form-status" role="status" aria-live="polite" tabindex="-1"></p><p class="form-note">You can also email <a href="mailto:info@globalmino.com">info@globalmino.com</a> directly.</p></form>'
pages['/contact']=('Contact | Global Mino',hero('Let’s Talk','Let’s uncover<br>the next opportunity.','Connect with Global Mino to discuss mining opportunities, mineral exploration and technical consultancy across Africa.','sudan')+'<section class="section contact-layout"><div><p class="eyebrow">GET IN TOUCH</p><h2>A conversation<br>starts here.</h2><address><a href="mailto:info@globalmino.com">info@globalmino.com</a><br><br>Khartoum, Sudan<br><br><a href="https://globalmino.com">globalmino.com</a></address></div>'+form+'</section>')
pages['/404']=('Page not found | Global Mino',hero('404 / Page not found','A different path<br>to opportunity.','The page you requested could not be found.','sudan')+section('CONTINUE EXPLORING','Find your way forward.',link('RETURN HOME','/','button gold')))
head=source.split('<body>')[0].replace('<html lang="en">','<html lang="en" dir="ltr">')
head=re.sub(r'<link[^>]+(?:fonts.googleapis.com|fonts.gstatic.com)[^>]*>', '', head)
head=head.replace('</head>', '<link rel="stylesheet" href="/fonts.css"><link rel="preload" href="/assets/fonts/dm-sans-0.woff2" as="font" type="font/woff2" crossorigin></head>')
translators={lang:i18n.Translator(lang) for lang in i18n.TRANSLATED}
for path,(title,body) in pages.items():
 desc=('Global Mino’s occupational health and safety approach for gold mining, mineral exploration and remote field operations.' if path=='/services/occupational-health-safety' else 'Global Mino — '+('mining, mineral exploration and technical consultancy across Sudan, Ethiopia, Cameroon and the Central African Republic.' if path=='/' else title.split(' | ')[0]+'. Explore mining, geological knowledge and responsible resource development across Africa.'))
 h=re.sub(r'<title>.*?</title>',lambda m:f'<title>{html.escape(title)}</title>',head)
 h=re.sub(r'<meta name="description"[^>]+>',lambda m:f'<meta name="description" content="{html.escape(desc,quote=True)}">',h)
 h=h.replace('href="style.css"','href="/style.css"').replace('</head>',f'<link rel="stylesheet" href="/pages.css"><link rel="canonical" href="https://globalmino.com{path}"><meta property="og:title" content="{html.escape(title,quote=True)}"><meta property="og:description" content="{html.escape(desc,quote=True)}"><meta property="og:url" content="https://globalmino.com{path}"><meta property="og:type" content="website"><meta property="og:image" content="https://globalmino.com/assets/hero.jpg"></head>')
 if path=='/': h=h.replace('https://globalmino.com/assets/hero.jpg','https://globalmino.com/assets/hero-gold-mining-v2.jpg')
 if path=='/services/occupational-health-safety': h=h.replace('https://globalmino.com/assets/hero.jpg','https://globalmino.com/assets/ohs-mining-safety.jpg')
 if path.startswith('/countries/'): h=h.replace('</head>', '<link rel="stylesheet" href="/countries.css"></head>')
 if path=='/gallery': h=h.replace('</head>', '<link rel="stylesheet" href="/gallery.css"></head>')
 if path=='/ceo-message': h=h.replace('</head>', '<link rel="stylesheet" href="/ceo-message.css"></head>')
 # Keep the brand palette last so it consistently governs every page-specific
 # stylesheet while src/home.html remains directly previewable.
 h=h.replace('<link rel="stylesheet" href="/brand.css">','').replace('</head>', '<link rel="stylesheet" href="/brand.css"><link rel="stylesheet" href="/site.css">'+('<link rel="stylesheet" href="/home.css">' if path=='/' else '')+'<link rel="stylesheet" href="/i18n.css">'+i18n.alternates(path)+'</head>')
 active=header.replace(f'href="{path}"',f'href="{path}" aria-current="page"')
 if path.startswith('/team/'): active=active.replace('href="/team"','href="/team" aria-current="page"')
 for group in ['countries','services']:
  if path.startswith('/'+group): active=active.replace(f'data-navigation-group="{group}"',f'data-navigation-group="{group}" class="current-group"')
 doc=h+'<body id="top"'+(' class="page-home"' if path=='/' else '')+'><a class="skip-link" href="#main">Skip to content</a>'+active+'<button class="menu-backdrop" tabindex="-1" aria-label="Close navigation" hidden></button><main id="main">'+body+'</main>'+('' if path=='/' else '<div class="contact">'+footer+'</div>')+credits+'<script src="/script.js" defer></script></body></html>'
 for lang in i18n.LANGS:
  # The French and Arabic editions are translated from the finished English
  # page, so every layout change above reaches all three languages.
  edition=doc if lang=='en' else i18n.localize(doc,path,translators[lang])
  if lang=='ar': edition=re.sub(r'href="/((?:style|pages|countries|gallery|ceo-message|brand|site|home)\.css)"',r'href="/rtl/\1"',edition)
  folder=out if lang=='en' else out/lang
  dest=folder/('404.html' if path=='/404' else path.strip('/')+'/index.html' if path!='/' else 'index.html')
  dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(i18n.finish(edition,path,lang),encoding='utf-8')
(out/'sitemap.xml').write_text(i18n.sitemap([p for p in pages if p!='/404']),encoding='utf-8')
(out/'robots.txt').write_text('User-agent: *\nAllow: /\nDisallow: /admin\nDisallow: /api/\nSitemap: https://globalmino.com/sitemap.xml\n')
print(f'Built {len(pages)-1} pages and 404 fallback in {len(i18n.LANGS)} languages.')
i18n.report(translators.values())
