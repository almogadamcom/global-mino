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

Browser tests use installed Google Chrome (`channel: 'chrome'`) and cover all 15 concrete pages at 1440, 1280, 1024, 768 and 390 pixels, local links, image loading, accessibility, menus, project filters, contact states and 404 behavior. These implement 13 primary templates, with three placeholder project detail instances. There is no TypeScript or existing lint toolchain.

## Enquiry storage with Supabase

The Node server accepts `POST /api/contact`, validates the enquiry and inserts it into Supabase using server-only credentials. Success means the database accepted the enquiry; it does not send an email notification.

1. Populate `.env` with `SUPABASE_URL` and `SUPABASE_SERVICE_ROLE_KEY`.
2. Run `supabase/migrations/202609110001_create_enquiries.sql` in the Supabase SQL Editor. This creates the `enquiries` table with RLS enabled and no public access. If using a custom table name, adjust the migration and `SUPABASE_ENQUIRIES_TABLE` together.
3. Restart with `npm start`.

The local credentials were checked without logging their values. The API was reachable, but reported the table missing; the migration still needs to be applied. Supabase service credentials cannot execute database schema migrations through the Data REST API.

Static-only hosting needs an equivalent `/api/contact` server endpoint and a configured 404 page. Keep `.env` and the service key outside the public `dist/` directory. No production enquiry is submitted by automated tests; persistence tests use mocked API responses.

## Content and photography

Project entries are explicitly marked placeholders. No reserves, production, ownership, licensing or financial figures are invented. The GM wordmark remains the supplied provisional treatment. Images are illustrative, not evidence of Global Mino assets. Credits and licenses remain available on every page. Alaska and Hawaii field images must not be represented as African company operations. Replace with approved company photography when supplied.

Page metadata, canonical URLs, sitemap and robots file use `https://globalmino.com`. `dist/style.css` preserves the approved styling; `dist/pages.css` extends it for internal pages and accessible shared navigation.

## Supabase environment

The server loads `.env` on startup. It is excluded from Git; `.env.example` contains only empty placeholders. The service role key is never included in static pages. Storage uses Supabase’s [Data REST API](https://supabase.com/docs/guides/api), with [row level security](https://supabase.com/docs/guides/database/postgres/row-level-security) enabled on the enquiry table.
