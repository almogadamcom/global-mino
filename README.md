# Global Mino

Complete static website extending the approved homepage. The original homepage design is retained in `src/home.html`; `build.py` composes the shared header, footer, page templates and company content into `dist/`. Runtime pages use plain HTML, CSS and JavaScript with no frontend framework or runtime dependencies.

## Run

Requires Node.js 22+; rebuilding also requires Python 3.

```sh
npm run build
npm start
```

Open http://127.0.0.1:4173. All routes support direct entry. The server returns the designed 404 page for unknown URLs.

## Checks

```sh
npm install
npm run check
npm test
```

Browser tests use installed Google Chrome (`channel: 'chrome'`) and cover all 26 concrete pages at 1440, 1280, 1024, 768 and 390 pixels, local links, image loading, accessibility, menus, project filters, the site visits lightbox, contact states and 404 behavior. Seven of those pages are team CV profiles and three are placeholder project details. There is no TypeScript or existing lint toolchain.

## Enquiry storage with Supabase

The Node server accepts `POST /api/contact`, validates the enquiry and inserts it into Supabase using server-only credentials. Success means the database accepted the enquiry; it does not send an email notification.

1. Populate `.env` with `SUPABASE_URL` and `SUPABASE_SERVICE_ROLE_KEY`.
2. Run `supabase/migrations/202609110001_create_enquiries.sql` in the Supabase SQL Editor. This creates the `enquiries` table with RLS enabled and no public access. If using a custom table name, adjust the migration and `SUPABASE_ENQUIRIES_TABLE` together.
3. Restart with `npm start`.

The migration has been applied to the configured Supabase project. A live browser submission was verified in the database, and its test record was removed. Row level security is enabled; anon and authenticated API roles have no table read access. Supabase service credentials cannot execute schema migrations through the Data REST API; the setup script uses the separate management token.

Static-only hosting needs an equivalent `/api/contact` server endpoint and a configured 404 page. Keep `.env` and the service key outside the public `dist/` directory. No production enquiry is submitted by automated tests; persistence tests use mocked API responses.

## Content and photography

Project entries and the `/gallery` site visit frames are explicitly marked placeholders. No reserves, production, ownership, licensing or financial figures are invented. The GM wordmark remains the supplied provisional treatment. Images are illustrative, not evidence of Global Mino assets. Credits and licenses remain available on every page. Alaska and Hawaii field images must not be represented as African company operations. Replace with approved company photography when supplied.

Page metadata, canonical URLs, sitemap and robots file use `https://globalmino.com`. `dist/style.css` preserves the approved styling; `dist/pages.css` extends it for internal pages and accessible shared navigation.

## Mining site visits gallery

`/gallery` groups field photography by visit, one section per location, each with its location name, visit date, short description and a lightbox that steps through that visit's collection only. `site_visits.py` holds the record.

No field photography has been supplied, so every frame renders as a labelled reserved slot instead of an image, and the page states this in full. To publish a photograph, copy the file into `dist/assets/`, set `src` and a factual `caption` on the matching entry in `site_visits.py`, replace the pending location, date and visiting team values with the confirmed ones, and rebuild. The grid, the frame counts and the lightbox all read that one record. Photo counts of five per visit tile the grid exactly at every breakpoint.

## CEO message

`/ceo-message`, linked from the footer's Company column, carries the message from the Founder & Chief Executive Officer. The text lives in `ceo_message.py` and is reproduced as supplied, with no sentences written to extend it. The supplied copy breaks off mid-word in the final paragraph of the health and safety section, so that paragraph stops at the last complete clause; the module records this. `dist/assets/ceo-portrait.jpg` is the supplied photograph, cropped to the subject at 4:5 — replace the file and `PHOTO_SIZE` together.

## Supabase environment

The server loads `.env` on startup. It is excluded from Git; `.env.example` contains only empty placeholders. The service role key is never included in static pages. Storage uses Supabase’s [Data REST API](https://supabase.com/docs/guides/api), with [row level security](https://supabase.com/docs/guides/database/postgres/row-level-security) enabled on the enquiry table.

## UI refinements and database setup

Libre Caslon Display and DM Sans are self-hosted as WOFF2 files with their open font licenses in `dist/assets/fonts/`. Typography and spacing follow the approved editorial direction. Project filters support refresh and browser history; the mobile menu manages scrolling and keyboard focus; the enquiry form provides field-level validation and preserves messages after failures.

To let the setup script create the table, put a Supabase management token with database query access in the local `SUPABASE_ACCESS_TOKEN` setting, then run `npm run db:setup`. It checks for the table before applying the supplied migration and verifies row level security. This token is only used by the setup script, never the website.
