# Country geological and mineral-sector content.
# Rule: no figures. No tonnages, grades, reserves, production or export numbers.
# Everything here is qualitative, documented geology and sector context.
# Edit this file to change country page copy; build.py renders it.

INFO = {
 'sudan': {
  'country': 'Sudan',
  'setting_title': 'An ancient shield,<br>worked since antiquity.',
  'setting': [
   'Sudan’s mineral geology is dominated by the Arabian–Nubian Shield, a Neoproterozoic terrane of accreted island-arc volcanic rocks, volcaniclastic and metasedimentary sequences, ophiolite belts and later granitoid intrusions, assembled during the Pan-African orogeny. The shield is exposed most extensively across the Red Sea Hills in the east and continues north and west beneath the Nubian Desert.',
   'Gold mineralisation is largely orogenic in character — structurally controlled quartz veins and shear-hosted systems developed within the arc sequences, typically accompanied by hydrothermal alteration. Volcanogenic massive sulphide occurrences in the same belts carry base metals alongside precious metals.',
   'Prolonged weathering and wadi drainage have redistributed gold into eluvial and alluvial concentrations, which is where much artisanal activity concentrates. Ancient workings scattered across the Red Sea Hills and Nubian Desert remain a practical guide to mineralised structures.',
  ],
  'commodities_title': 'Gold first,<br>but not gold alone.',
  'commodities': [
   ('Gold', 'The country’s principal mineral export. Present as orogenic vein and shear-hosted systems within the basement, and as eluvial and alluvial concentrations through the wadi systems.'),
   ('Chromite', 'Hosted in ophiolite complexes, most notably the Ingessana Hills in Blue Nile State and parts of the Red Sea Hills.'),
   ('Copper and Zinc', 'Associated with volcanogenic massive sulphide settings in the Red Sea Hills. Copper is also long documented at Hofrat en Nahas in the south-west.'),
   ('Iron Ore', 'Occurrences documented across northern Sudan, including the Wadi Halfa and Baljrawiya areas.'),
   ('Manganese', 'Recorded through the Red Sea Hills, generally in association with the volcanic-sedimentary sequences.'),
   ('Industrial Minerals', 'Gypsum, limestone, salt, marble, mica and feldspar, with evaporite and coastal deposits along the Red Sea.'),
  ],
  'context_title': 'A long history,<br>an active present.',
  'context': [
   'Gold has been worked in this region for millennia — the name Nubia is widely linked to <em>nub</em>, the ancient Egyptian word for gold. Modern activity spans a full spectrum, from artisanal and small-scale working through to organised concession-based operations, and the artisanal sector forms a substantial part of the national picture.',
   'Mineral rights and concessions are administered through the Ministry of Minerals and the Sudanese Mineral Resources Company. Licence standing, concession boundaries and the status of existing workings should be independently verified before any commitment is made — that verification is a core part of the technical due diligence Global Mino provides.',
  ],
  'facts': [
   ('Principal Geology', 'Arabian–Nubian Shield, Neoproterozoic'),
   ('Lead Commodity', 'Gold'),
   ('Mineralisation Styles', 'Orogenic vein, shear-hosted, alluvial, VMS'),
   ('Key Regions', 'Red Sea Hills, Nubian Desert, River Nile, Northern State, Blue Nile'),
   ('Also Documented', 'Chromite, copper, zinc, manganese, iron ore, industrial minerals'),
   ('Artisanal Sector', 'Extensive'),
   ('Administration', 'Ministry of Minerals; Sudanese Mineral Resources Company'),
  ],
 },
 'cameroon': {
  'country': 'Cameroon',
  'setting_title': 'Craton, fold belt<br>and volcanic line.',
  'setting': [
   'Cameroon spans three broad geological domains. In the south, the Archaean to Palaeoproterozoic Ntem Complex forms the northern margin of the Congo Craton and hosts extensive banded iron formation. Across the centre and east lies the Pan-African Central African Fold Belt, a Neoproterozoic mobile belt of metavolcanic and metasedimentary rocks cut by granitoids and major shear zones.',
   'Overprinting both is the Cameroon Volcanic Line, a Cenozoic alkaline volcanic chain running north-east from the Gulf of Guinea through Mount Cameroon and onto the Adamawa Plateau. Its deep lateritic weathering profiles are the setting for the country’s bauxite.',
   'Gold is concentrated in the Pan-African belt of the East and Adamawa regions, as orogenic quartz-vein systems within metavolcanic and metasedimentary sequences and, far more visibly, as alluvial and eluvial workings along the drainage. Alluvial diamonds occur in the far east around Mobilong.',
  ],
  'commodities_title': 'A genuinely<br>diversified endowment.',
  'commodities': [
   ('Gold', 'Concentrated in the East Region around Bétaré-Oya, Batouri, Colomines and Ngoura, and through Adamawa. Both primary vein systems and widespread alluvial workings.'),
   ('Diamonds', 'Alluvial diamonds in the Mobilong area near Yokadouma, in the East Region.'),
   ('Iron Ore', 'Banded iron formation within the Ntem Complex, including the Mbalam, Nkout and Bipindi–Grand Zambi areas of the south.'),
   ('Bauxite', 'Lateritic bauxite on the Adamawa Plateau, principally the Minim-Martap and Ngaoundal plateaux.'),
   ('Cobalt, Nickel and Manganese', 'Lateritic deposits in the Lomié area of the East Region, including Nkamouna.'),
   ('Rutile', 'Documented through the Akonolinga area of the Centre Region.'),
   ('Tin and Sapphire', 'Tin at Mayo-Darlé in Adamawa, with sapphire occurrences recorded in the Mayo-Kewol area.'),
   ('Industrial Minerals', 'Limestone, marble and pozzolan, supporting domestic construction materials.'),
  ],
  'context_title': 'Geology reachable<br>by infrastructure.',
  'context': [
   'Cameroon combines an established mining code with comparatively developed export infrastructure — the deep-water port at Kribi and the port of Douala, linked inland by road and rail. That infrastructure materially shapes which deposits are economically reachable, and it is why bulk commodities such as iron ore and bauxite feature in the country’s development plans alongside precious metals.',
   'The sector is administered by the Ministry of Mines, Industry and Technological Development, with the national mining corporation SONAMINES holding a role in state participation and artisanal production channels. Artisanal and small-scale mining is significant in the East Region and frequently overlaps with formal concession ground — one reason concession status and ground occupancy need verifying on site rather than on paper.',
  ],
  'facts': [
   ('Principal Geology', 'Congo Craton (Ntem Complex), Pan-African Fold Belt, Cameroon Volcanic Line'),
   ('Lead Commodities', 'Gold, iron ore, bauxite'),
   ('Gold Styles', 'Orogenic vein, alluvial, eluvial'),
   ('Key Regions', 'East, Adamawa, South, Centre'),
   ('Also Documented', 'Diamonds, cobalt, nickel, manganese, rutile, tin, sapphire'),
   ('Export Infrastructure', 'Kribi deep-water port; Douala'),
   ('Administration', 'Ministry of Mines, Industry and Technological Development; SONAMINES'),
  ],
 },
 'central-african-republic': {
  'country': 'the Central African Republic',
  'setting_title': 'Alluvial diamonds,<br>an unanswered source.',
  'setting': [
   'The Central African Republic sits on Precambrian basement of the Congo Craton, overlain and flanked by Pan-African mobile belts. Greenstone-belt sequences within this basement host the country’s primary gold occurrences, while younger continental sandstone formations are central to its diamond story.',
   'Diamonds are recovered from two broad zones: a western zone around Carnot and Berbérati, associated with the Carnot Sandstone, and an eastern zone on the Mouka–Ouadda sandstone plateau. Production is overwhelmingly alluvial — stones are won from river gravels and reworked sandstone-derived placers.',
   'The primary kimberlitic sources feeding those placers remain largely unidentified. That open question is among the more significant exploration propositions in the region, and it is precisely why systematic geological work carries particular weight here rather than opportunistic ground-taking.',
  ],
  'commodities_title': 'Diamonds and gold,<br>across dispersed ground.',
  'commodities': [
   ('Diamonds', 'Alluvial stones from the western Carnot–Berbérati zone and the eastern Mouka–Ouadda plateau, historically noted for a high proportion of gem-quality material.'),
   ('Gold', 'Primary occurrences in greenstone-belt sequences together with alluvial workings. Documented areas include Ndassima, Bambari, Bogoin, Yaloké and Roandji.'),
   ('Iron Ore', 'Occurrences documented in the Bogoin area and more widely around the Bangui region.'),
   ('Uranium', 'Documented in the Bakouma area of the south-east.'),
   ('Limestone', 'Deposits in the Bobassa and Fatima areas near Bangui, relevant to construction materials.'),
   ('Other Occurrences', 'Copper, manganese, rutile, ilmenite, tin and lignite are recorded across the basement and its sedimentary cover.'),
  ],
  'context_title': 'Artisanal ground,<br>certified exports.',
  'context': [
   'Mining in the Central African Republic is dominated by artisanal and small-scale working, particularly for diamonds, where recovery from alluvial ground requires little capital but produces a highly dispersed and hard-to-trace supply chain. Understanding who is working which ground is a field question before it is a legal one.',
   'Rough diamond exports operate under the Kimberley Process Certification Scheme, and compliance arrangements have applied differently to different parts of the country. Certification standing for any specific zone must be confirmed at the time of transaction rather than assumed. The sector is administered by the Ministry of Mines and Geology.',
  ],
  'facts': [
   ('Principal Geology', 'Congo Craton basement, greenstone belts, continental sandstone cover'),
   ('Lead Commodities', 'Diamonds, gold'),
   ('Diamond Occurrence', 'Alluvial; primary kimberlite sources largely unidentified'),
   ('Diamond Zones', 'Carnot–Berbérati (west); Mouka–Ouadda (east)'),
   ('Also Documented', 'Iron ore, uranium, limestone, copper, manganese, rutile, tin'),
   ('Artisanal Sector', 'Dominant, especially diamonds'),
   ('Export Regime', 'Kimberley Process Certification Scheme'),
   ('Administration', 'Ministry of Mines and Geology'),
  ],
 },
}

# Deep-dive gold and mining detail. Same rule: no figures — no tonnages, grades,
# reserves, production, permit durations or state-interest percentages.
GOLD = {
 'cameroon': {
  'eyebrow': 'GOLD IN CAMEROON',
  'title': 'Where the gold is,<br>and why it is there.',
  'intro': 'Gold is the most widely worked precious metal in Cameroon, and the great majority of it comes from the eastern third of the country. The geology responsible is the Pan-African Central African Fold Belt — Neoproterozoic metavolcanic and metasedimentary sequences intruded by granitoids and cut by major crustal shear zones, including the Central Cameroon Shear Zone. Those shears acted as the plumbing for gold-bearing hydrothermal fluids, and deep tropical weathering has since redistributed the metal into the weathered profile and the drainage.',
  'districts_title': 'The goldfields,<br>district by district.',
  'districts': [
   ('Bétaré-Oya', 'The best-known goldfield in the country, on the Lom River in the East Region. Gold occurs both as quartz-vein systems within Lom Group metasediments and in the alluvial and terrace gravels of the Lom and its tributaries, which carry the bulk of artisanal activity.'),
   ('Batouri', 'A long-worked district of the East Region, with vein-hosted gold in sheared metavolcanic rocks and granitoids alongside extensive eluvial workings developed on the weathered profile.'),
   ('Colomines', 'Among the older organised workings in the East, historically dredged and now dominated by artisanal and semi-mechanised alluvial recovery.'),
   ('Ngoura and Garoua-Boulaï', 'Ground along the eastern corridor toward the Central African Republic border, combining alluvial workings on the drainage with vein occurrences in the underlying basement.'),
   ('Kette and the Kadey Basin', 'Alluvial and eluvial gold distributed across the Kadey drainage in the south-east of the East Region.'),
   ('Adamawa', 'Occurrences through the Meiganga, Tibati and Banyo areas, associated with Pan-African basement and the shear systems crossing the plateau.'),
   ('Northern Occurrences', 'Gold is also recorded in the North Region, including the Rey Bouba area, in a broadly comparable basement setting.'),
  ],
  'styles_title': 'Four styles,<br>four different problems.',
  'styles': [
   ('Orogenic Quartz-Vein Gold', 'Structurally controlled mesothermal veins within metavolcanic and metasedimentary sequences, typically along or adjacent to shear zones and commonly carrying sulphides with hydrothermal alteration halos.'),
   ('Shear-Hosted Disseminated Gold', 'Gold distributed through sheared and altered rock rather than in discrete veins. This changes both the sampling approach and the processing route, and it is routinely underestimated by vein-focused reconnaissance.'),
   ('Eluvial Gold', 'Metal released by deep tropical weathering and concentrated in the saprolite and laterite profile above its source. Usually the first ground artisanal miners take, and a useful vector back to the primary system.'),
   ('Alluvial and Terrace Placers', 'River gravels and older elevated terraces along the Lom, Kadey and Boumbé drainages. Low capital to work, which is precisely why they dominate artisanal production and why they are rarely unoccupied.'),
  ],
  'asm_title': 'The ground is rarely<br>as empty as the map.',
  'asm': [
   'Artisanal and small-scale mining accounts for the great majority of gold actually produced in Cameroon. The work ranges from hand-dug pits and sluicing on river gravels through to semi-mechanised operations running excavators and washing plants, the latter frequently operated under arrangements with outside partners.',
   'Because that activity is mobile and follows the gravels, ground that reads as unencumbered on a concession map is often occupied in practice. Establishing who is working where, and under what authorisation, is a field exercise rather than a documentary one — and it is where most disputes over Cameroonian gold ground begin.',
   'Abandoned pits and disturbed drainage are a recognised legacy issue across the East Region. Rehabilitation obligations attach to title holders, so the condition in which ground is inherited is a commercial question as well as an environmental one.',
  ],
  'titles_title': 'The title ladder<br>under the mining code.',
  'titles': [
   ('Reconnaissance Permit', 'A non-exclusive right to carry out preliminary surface work, used to establish whether a target justifies committing exploration capital.'),
   ('Exploration Permit', 'An exclusive right over a defined perimeter, renewable, and carrying work programme and reporting commitments that must be met to retain the ground.'),
   ('Mining Permit', 'The exclusive right to extract and sell, granted on the basis of a feasibility study, an environmental and social impact assessment, and an agreed mining convention with the state.'),
   ('Artisanal Authorisation', 'Covers manual working, with a distinct semi-mechanised category for operations deploying limited plant.'),
   ('Quarry Titles', 'A separate regime governs quarry substances used in construction, and should not be assumed to travel with a mineral title.'),
  ],
  'opportunity_title': 'What is actually<br>on the table.',
  'opportunity': [
   ('Primary Sources Behind the Placers', 'Most of what has been worked in eastern Cameroon is secondary — alluvial, terrace and eluvial gold. The bedrock systems that shed that metal remain only partly delineated in most districts. Tracing productive placers back up-slope to their hard-rock source is the clearest single exploration proposition in the region.'),
   ('Thin Modern Data', 'Much of the available mapping predates current geochemical and geophysical practice. A disciplined programme — stream sediment and soil geochemistry, structural mapping along the shear corridors, targeted geophysics — can materially change the picture on ground already known to carry gold, without taking frontier risk.'),
   ('Formalisation of Existing Workings', 'Semi-mechanised artisanal operations exist in number and are frequently under-capitalised and technically unsupported. Structured partnership, brought in with proper title, environmental compliance and rehabilitation planning, can convert informal working into a compliant operation rather than displacing it.'),
   ('Infrastructure Reach', 'The Bertoua corridor and the road links toward Douala and Kribi determine what can practically be moved. Access is what decides the scale at which a given deposit becomes worth developing, and it varies sharply between districts.'),
  ],
  'opportunity_note': 'None of this substitutes for verification. Title standing, ground occupancy and inherited rehabilitation liability must each be established before value is ascribed to any position. That verification is the work Global Mino does first.',
  'titles_note': 'Titles are granted by the Ministry of Mines, Industry and Technological Development. The state retains a participation interest, and SONAMINES, the national mining corporation, holds a role in state participation and in channelling artisanal production. Title standing, perimeter coordinates and the status of any overlapping artisanal authorisation should be verified directly against the cadastre before value is ascribed to ground.',
 },
}

# Concise public profiles. Opportunities are assessment themes, not available assets.
PROFILES = {
 'ethiopia': {
  'intro': 'Gold across the Arabian\u2013Nubian Shield, pegmatite and evaporite minerals, and scope for exploration and practical mining support.',
  'minerals': 'Gold \u00b7 Tantalum \u00b7 Potash \u00b7 Opal',
  'regions': 'Oromia \u00b7 Benishangul-Gumuz \u00b7 Tigray \u00b7 Afar',
  'gold': 'Ethiopia\u2019s established primary gold mining sits in the Adola belt of the Guji Zone in southern Oromia, where the Lega Dembi and Sakaro deposits occur in Precambrian greenstone rocks of the Arabian\u2013Nubian Shield. Artisanal workings in both alluvial ground and weathered hard rock are widespread across Oromia, Benishangul-Gumuz, Tigray and Gambella, and artisanal and small-scale miners supply much of the gold sold through official channels.',
  'mining': 'Beyond gold, the documented mineral base includes tantalum and lithium-bearing pegmatites in the Kenticha field of southern Oromia, potash and salt in the Danakil Depression of Afar, soda ash at Lake Abijata, opal in the Wollo highlands of Amhara, and industrial minerals such as limestone, gypsum and marble supplying domestic cement and construction. Power supply, road access and the distance to port at Djibouti shape project economics.',
  'consideration': 'Confirm licence status and boundaries with the Ministry of Mines and the relevant regional authority before committing to a site. Security conditions, land use and community interests differ substantially between regions and need local assessment kept under review. Water supply, tailings handling and rehabilitation belong in the initial plan rather than a later stage.',
  'opportunities': [
   ('Trace gold to its bedrock source', 'Map and sample the greenstone belts of the Arabian\u2013Nubian Shield where artisanal alluvial workings point to a primary source that has not been defined.'),
   ('Support artisanal and small-scale operations', 'Assess recovery methods, mercury handling, site safety and rehabilitation alongside licensed cooperatives and regional mining offices.'),
   ('Assess strategic and industrial minerals', 'Review the tantalum and lithium-bearing pegmatite belts and the Danakil evaporite basin against current processing, logistics and market conditions.'),
  ],
  'sources': [
   ('USGS \u00b7 Ethiopia mineral industry (2019)', 'https://pubs.usgs.gov/myb/vol3/2019/myb3-2019-ethiopia.pdf'),
   ('EITI \u00b7 Ethiopia country page', 'https://eiti.org/countries/ethiopia'),
  ],
 },

 'sudan': {
  'intro': 'A long history of gold mining, with opportunities that begin with careful geological and operational assessment.',
  'minerals': 'Gold · Chromite · Industrial minerals',
  'regions': 'Red Sea Hills · Northern Sudan',
  'gold': 'Gold is Sudan’s leading mineral export by value. Artisanal mining accounts for much of its output, alongside organised mining operations. The Red Sea Hills and northern desert form part of the country’s established gold exploration landscape.',
  'mining': 'Sudan also produces chromite, gypsum, salt and other industrial minerals. Geological work, sampling and reliable site information are essential to understanding individual deposits.',
  'consideration': 'Conflict affects access, logistics and gold supply chains. Any proposed work needs a current security assessment, verified counterparties and responsible sourcing checks before field activity is considered.',
  'opportunities': [
   ('Gold exploration', 'Review historic workings and geological records to identify targets for mapping and sampling, where safe access is possible.'),
   ('Technical assessment', 'Assess sampling quality, mineral processing options and operating conditions before planning further development.'),
   ('Responsible sourcing', 'Evaluate traceability and working practices with verified local partners before considering a supply relationship.'),
  ],
  'sources': [('USGS · Sudan mineral industry', 'https://www.usgs.gov/centers/national-minerals-information-center/sudan'), ('US State Department · Sudan business advisory (2023)', 'https://2021-2025.state.gov/june-2023-update-risks-for-us-businesses-operating-in-sudan/')],
 },
 'cameroon': {
  'intro': 'Gold in the east, a diverse mineral base, and opportunities for exploration and practical mining support.',
  'minerals': 'Gold · Iron ore · Bauxite',
  'regions': 'East · Adamawa · South',
  'gold': 'Eastern Cameroon is an established gold mining area, including Bétaré-Oya, Batouri and Colomines. Gold occurs in river deposits and in the underlying rock. Both small-scale workings and industrial development shape the sector.',
  'mining': 'Beyond gold, Cameroon has iron ore, bauxite and other mineral resources. Government reporting in 2026 identifies new gold, iron ore, bauxite and marble projects. Roads, power and the distance to export ports remain project-specific considerations.',
  'consideration': 'Check mineral title boundaries, existing land use and community interests early. Water management, disturbed ground and rehabilitation should be included in the site assessment.',
  'opportunities': [
   ('Find the source of gold', 'Use mapping and geochemical sampling to investigate bedrock targets around known alluvial gold areas.'),
   ('Improve small-scale operations', 'Assess recovery methods, site safety and rehabilitation needs with authorised operators and local communities.'),
   ('Evaluate mineral projects', 'Combine geological evidence with access, infrastructure and title checks to assess gold and other mineral prospects.'),
  ],
  'sources': [('USGS · Cameroon mineral industry (2020–2021)', 'https://pubs.usgs.gov/myb/vol3/2020-21/myb3-2020-21-cameroon.pdf'), ('Cameroon Ministry of Communication · Mining sector update (2026)', 'https://www.mincom.gov.cm/2026/07/17/government-unveils-new-reforms-to-transform-cameroons-mining-sector/')],
 },
 'central-african-republic': {
  'intro': 'Gold and diamonds underpin the mining sector, with opportunities for better exploration data and responsible site development.',
  'minerals': 'Gold · Diamonds',
  'regions': 'Western and central mineral districts',
  'gold': 'Gold is one of the Central African Republic’s principal mined commodities. Small-scale mining plays a major role. Assessing a gold prospect requires site-specific sampling to understand the deposit and the reliability of existing information.',
  'mining': 'Gold and diamond mining are important to the country’s exports. Diamond workings are widely distributed, with documented alluvial fields in the west and east. Access, local working arrangements and the origin of material need close attention.',
  'consideration': 'Assess local security, site safety, mineral rights and community land use before work begins. Diamond opportunities also require verification of the applicable certification and export requirements.',
  'opportunities': [
   ('Build reliable gold data', 'Review historical information and plan geological mapping and sampling to evaluate prospective ground.'),
   ('Support safer mining', 'Assess excavation practices, water management and rehabilitation needs at authorised small-scale sites.'),
   ('Assess diamond ground', 'Review alluvial deposit information alongside access, traceability and certification requirements before considering a project.'),
  ],
  'sources': [('USGS · Central African Republic mineral industry', 'https://www.usgs.gov/centers/national-minerals-information-center/central-african-republic'), ('USGS · Diamond occurrence database', 'https://www.usgs.gov/publications/central-african-republic-diamond-database-a-geodatabase-archival-diamond-occurrences')],
 },
}
