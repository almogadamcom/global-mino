-- Run in the Supabase SQL Editor. Enquiries are private to the server.
begin;
create table public.enquiries (
  id uuid primary key default gen_random_uuid(),
  created_at timestamptz not null default now(),
  name text not null check (char_length(btrim(name)) between 1 and 200),
  company text not null default '' check (char_length(company) <= 200),
  email text not null check (char_length(email) between 3 and 200),
  phone text not null default '' check (char_length(phone) <= 200),
  country text not null check (country in ('sudan','cameroon','central-african-republic','other')),
  interest text not null check (interest in ('gold-mining','mineral-exploration','mining-consultancy','investment-opportunity','partnership','other')),
  message text not null check (char_length(btrim(message)) between 10 and 5000)
);
alter table public.enquiries enable row level security;
revoke all on public.enquiries from anon, authenticated;
grant select, insert on public.enquiries to service_role;
notify pgrst, 'reload schema';
commit;
