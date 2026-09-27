-- Adds Ethiopia to the countries an enquiry may name.
-- The website, api/contact.js and server.cjs validate the same list.
begin;
alter table public.enquiries drop constraint if exists enquiries_country_check;
alter table public.enquiries add constraint enquiries_country_check
  check (country in ('ethiopia','sudan','cameroon','central-african-republic','other'));
notify pgrst, 'reload schema';
commit;
