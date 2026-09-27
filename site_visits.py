"""Mining site visits gallery content.

Photographs from employee field visits have not been supplied yet, so every
photo entry below is a reserved slot: `src` stays None and `caption` stays
None until a real image is available. To publish a photograph, copy the file
into `dist/assets/` and set `src` to its file name plus a factual `caption`;
the grid, the counters and the lightbox pick it up on the next build.

The same applies to `site`, `date` and `party`. Leave the pending values in
place until the team confirms the real location name, the date of the visit
and who attended. Nothing on this page should state a visit detail that has
not been provided.
"""

PENDING_DATE = 'Date to be confirmed'
PENDING_SITE = 'Specific site to be confirmed'
PENDING_PARTY = 'Visiting team to be confirmed'


def slots(count):
    """Reserve `count` empty photo frames for a visit."""
    return [{'src': None, 'caption': None} for _ in range(count)]


# Photo counts are multiples that tile cleanly: the first frame of each visit
# is the feature tile and covers a 2x2 area, so 5 frames fill the grid exactly
# at every breakpoint.
VISITS = [
    {
        'slug': 'sudan',
        'country': 'Sudan',
        'site': PENDING_SITE,
        'date': PENDING_DATE,
        'party': PENDING_PARTY,
        'focus': 'Gold mining and mineral opportunity assessment',
        'description': 'Global Mino’s work in Sudan centres on gold mining and mineral opportunity assessment. The photographs below were taken during a team visit to a Sudanese mining and processing site. The specific location, the date of the visit and the names of those present are still to be confirmed.',
        'photos': [
            {'src': 'visits/sudan-01.jpg', 'caption': 'The visiting group beside a lined pond at the site.'},
            # Two faces in sudan-02 are masked at the company's request; the unedited
            # original is in the supplied photo folder, not in the repository.
            {'src': 'visits/sudan-02.jpg', 'caption': 'Standing on the pond liner, with the excavated ground behind.'},
            {'src': 'visits/sudan-03.jpg', 'caption': 'Beside the tanks on the processing line.'},
            {'src': 'visits/sudan-04.jpg', 'caption': 'On the haul road, with tipper trucks behind.'},
            {'src': 'visits/sudan-05.jpg', 'caption': 'In conversation under the equipment shelter.'},
        ],
    },
    {
        'slug': 'cameroon',
        'country': 'Cameroon',
        'site': PENDING_SITE,
        'date': PENDING_DATE,
        'party': PENDING_PARTY,
        'focus': 'Geological mapping and field exploration',
        'description': 'Work in Cameroon centres on geological mapping, field exploration and mineral resource intelligence. The photographs below were taken as the team arrived in the country; photographs from the sites themselves have not been supplied yet. The location, the date of the visit and the names of those present are still to be confirmed.',
        'photos': [
            {'src': 'visits/cameroon-01.jpg', 'caption': 'Arriving on the apron.'},
            {'src': 'visits/cameroon-02.jpg', 'caption': 'Leaving the aircraft at the head of the airstairs.'},
            {'src': 'visits/cameroon-03.jpg', 'caption': 'On the apron after landing.'},
        ],
    },
    {
        'slug': 'central-african-republic',
        'country': 'Central African Republic',
        'site': PENDING_SITE,
        'date': PENDING_DATE,
        'party': PENDING_PARTY,
        'focus': 'Mineral exploration and geological assessment',
        'description': 'Work in the Central African Republic centres on mineral exploration and geological assessment. The photographs below were taken during a team visit to a mining camp in the country. The specific location, the date of the visit and the names of those present are still to be confirmed.',
        'photos': [
            {'src': 'visits/car-01.jpg', 'caption': 'On the track to the site, at the edge of cultivated ground.'},
            {'src': 'visits/car-02.jpg', 'caption': 'In discussion with a worker on the camp ground.'},
            {'src': 'visits/car-03.jpg', 'caption': 'Talking with workers beside the shelters after rain.'},
            {'src': 'visits/car-04.jpg', 'caption': 'Tarpaulin shelters and covered loads across the camp.'},
        ],
    },
]
