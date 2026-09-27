"""Message from the Founder & Chief Executive Officer (/ceo-message).

The text is the message as supplied by the company and is reproduced without
addition. One note on the closing paragraph: the supplied copy ends mid-word
("...through the hierarchy of controls, with priority given to e"), so the
final sentence stops at the last complete clause. Nothing has been written to
finish it. When the remainder of the message arrives, extend the last entry in
`SECTIONS` and add any closing paragraphs and sign-off wording.
"""

NAME = 'Dr. Hashim Sulieman'
ROLE = 'Founder & Chief Executive Officer'
COMPANY = 'Global Mining Consultancy Company'
PHOTO = 'ceo-portrait.jpg'
# Cropped to the subject at 4:5; update together with the file.
PHOTO_SIZE = (1100, 1375)
PROFILE = '/team/hashim-sulieman'

LEAD = 'It is my privilege to welcome you to GLOBAL MINING CONSULTANCY COMPANY, an African-focused consultancy established to support the responsible exploration, development, processing, and management of the continent’s exceptional mineral resources.'

# Pulled out of the health and safety section and set as a quotation.
QUOTE = 'We firmly believe that no mineral resource is more valuable than human life.'

SECTIONS = [
    {
        'heading': None,
        'paragraphs': [
            'Africa possesses some of the world’s most significant reserves of gold, diamonds, copper, lithium, bauxite, lead, and other strategic and precious minerals. These resources represent enormous opportunities for investment, industrial development, employment, infrastructure, and sustainable economic growth. Our vision is to help transform these natural resources into long-term value while protecting the health and safety of workers, safeguarding communities, and preserving the environment for future generations.',
            'At GLOBAL MINING CONSULTANCY COMPANY, we bring together mining consultancy, mineral exploration and processing expertise, occupational health and safety, environmental management, operational oversight, and strategic advisory services to provide integrated solutions throughout the mining lifecycle.',
        ],
    },
    {
        'heading': 'From Exploration to Sustainable Production',
        'paragraphs': [
            'Our approach begins with understanding the mineral resource and identifying exploration and processing methods appropriate to the geology, mineral characteristics, scale of operation, available infrastructure, environmental conditions, and commercial objectives of each project.',
            'With particular interest in gold and diamond projects, we support clients in evaluating suitable exploration, extraction, recovery, and mineral-processing approaches. Our role extends beyond technical advice. Where required, we provide professional oversight and operational support during mineral processing to promote safe practices, effective resource recovery, responsible management, quality assurance, and continuous operational improvement.',
            'We recognise that there is no single solution suitable for every mining operation. Our philosophy is therefore based on providing practical, evidence-based, site-specific and commercially sustainable solutions, adapted to local African operating conditions while informed by recognised international practices.',
        ],
    },
    {
        'heading': 'Health, Safety and Environment at the Centre of Mining',
        'quote': QUOTE,
        'paragraphs': [
            'Occupational health, safety, and environmental protection are therefore fundamental components of our business model and are integrated into our mining consultancy and operational services.',
            'Our company supports mining organisations in applying recognised international occupational health, safety and environmental standards and good practice, alongside applicable national legislation and regulatory requirements.',
            'We design and assist in implementing tailored Occupational Health, Safety and Environmental programmes based on the actual hazards, workforce characteristics, operational processes, regulatory requirements, and environmental conditions of each mining project.',
            'Our approach incorporates systematic hazard identification, occupational and environmental risk assessment, risk prioritisation, implementation of appropriate control measures, occupational health surveillance, worker education and training, emergency preparedness, incident prevention, environmental monitoring, performance evaluation, and continuous improvement.',
            'Mining operations can expose workers and surrounding communities to significant physical, mechanical, chemical, biological, ergonomic, psychosocial and environmental hazards. These may include respirable crystalline silica and other mineral dusts, mercury, cyanide and other hazardous chemicals, excessive noise and vibration, heat stress, heavy machinery and mobile equipment, working at height, confined spaces, ground instability, manual handling, fatigue, infectious and tropical diseases, and other risks specific to individual mining environments.',
            # The supplied text breaks off inside this sentence; it ends here at
            # the last complete clause rather than being completed by hand.
            'Our objective is to identify these risks early and manage them through the hierarchy of controls.',
        ],
    },
]
