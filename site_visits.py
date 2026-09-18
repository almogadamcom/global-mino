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
        'description': 'Global Mino’s work in Sudan centres on gold mining and mineral opportunity assessment. Photographs from the team’s visits to Sudanese mining locations will be published in this section once they are supplied, together with the site name, the date of the visit and a short account of the work carried out.',
        'photos': slots(5),
    },
    {
        'slug': 'cameroon',
        'country': 'Cameroon',
        'site': PENDING_SITE,
        'date': PENDING_DATE,
        'party': PENDING_PARTY,
        'focus': 'Geological mapping and field exploration',
        'description': 'Work in Cameroon centres on geological mapping, field exploration and mineral resource intelligence. This section is reserved for photographs taken during the team’s visits to Cameroonian mining locations, with the site name, visit date and description added when the record is confirmed.',
        'photos': slots(5),
    },
    {
        'slug': 'central-african-republic',
        'country': 'Central African Republic',
        'site': PENDING_SITE,
        'date': PENDING_DATE,
        'party': PENDING_PARTY,
        'focus': 'Mineral exploration and geological assessment',
        'description': 'Work in the Central African Republic centres on mineral exploration and geological assessment. Photographs from field visits to mining locations in the country will appear here, each with the location, the date of the visit and a caption describing what is shown.',
        'photos': slots(5),
    },
]
