"""French and Arabic editions of the site.

build.py renders every page in English first. localize() then produces the
French or Arabic document from that English HTML: text nodes and the readable
attributes (alt, aria-label, placeholder, captions, meta descriptions) are
looked up in i18n/<lang>/*.json, internal links move under /<lang>, and the
<html> element gets the right lang and dir.

Lookup order for a piece of text:
 1. an exact entry in the dictionary;
 2. the same entry in another letter case (an all-caps English label reuses
    the sentence-case translation, upper-cased for French);
 3. a template in i18n/<lang>/templates.json, for text that repeats with a
    changing part such as "Explore Sudan ↗" or "Project 03 | Global Mino".
    Each captured part is translated in turn.
Anything still unmatched stays in English and is listed in
i18n/_missing-<lang>.json so the gap is visible rather than silent.
"""
from pathlib import Path
import html, json, re

LANGS = {'en': ('English', 'EN', 'ltr'), 'fr': ('Français', 'FR', 'ltr'), 'ar': ('العربية', 'AR', 'rtl')}
# Open Graph locales for link previews; the English copy uses British spelling.
OG_LOCALES = {'en': 'en_GB', 'fr': 'fr_FR', 'ar': 'ar_AR'}
TRANSLATED = [lang for lang in LANGS if lang != 'en']
SITE = 'https://globalmino.com'
root = Path(__file__).parent / 'i18n'

ATTRS = ('alt', 'aria-label', 'placeholder', 'title', 'data-caption', 'data-collection')
# Text that is the same in every language: brand, addresses, codes and numbers.
LETTERS = re.compile(r'[A-Za-z]')
VERBATIM = re.compile(r'^(?:Global Mino|GLOBAL MINO|globalmino\.com|[\w.+-]+@[\w.-]+|https?://\S+)$')


def load(lang):
    entries, templates = {}, []
    for file in sorted((root / lang).glob('*.json')):
        data = json.loads(file.read_text(encoding='utf-8'))
        if file.stem == 'templates':
            templates += [(re.compile('^' + pattern + '$'), result) for pattern, result in data.items()]
            continue
        for key, value in data.items():
            if key in entries and entries[key] != value:
                raise ValueError(f'{file.name}: conflicting translation for {key!r}')
            entries[key] = value
    return entries, templates


class Translator:
    def __init__(self, lang):
        self.lang = lang
        self.entries, self.templates = load(lang)
        self.folded = {}
        for key in self.entries:
            self.folded.setdefault(key.casefold(), key)
        self.missing = {}
        self.used = set()

    def text(self, value, where=''):
        key = ' '.join(value.split())
        if not key:
            return value
        # Exact entries come first so symbols such as arrows can be mirrored for Arabic.
        found = self.entries.get(key)
        if found is not None:
            self.used.add(key)
        else:
            if not LETTERS.search(key) or VERBATIM.match(key):
                return value
            found = self.lookup(key)
        if found is None:
            self.missing.setdefault(key, where)
            return value
        lead = value[:len(value) - len(value.lstrip())]
        trail = value[len(value.rstrip()):]
        return lead + found + trail

    def lookup(self, key, depth=0):
        if key in self.entries:
            self.used.add(key)
            return self.entries[key]
        if not LETTERS.search(key) or VERBATIM.match(key):
            return key
        folded = self.folded.get(key.casefold())
        if folded is not None:
            self.used.add(folded)
            folded = self.entries[folded]
            return folded.upper() if key.isupper() and self.lang == 'fr' else folded
        if depth < 4:
            for pattern, result in self.templates:
                match = pattern.match(key)
                if match:
                    parts = [self.lookup(part, depth + 1) for part in match.groups()]
                    if None not in parts:
                        translated = result.format(*parts)
                        return translated.upper() if key.isupper() and self.lang == 'fr' else translated
        return None


def lang_path(path, lang):
    if lang == 'en':
        return path
    return '/' + lang + ('' if path == '/' else path)


def is_page_link(href):
    target = href.split('?')[0].split('#')[0]
    if not target.startswith('/') or target.startswith(('/assets/', '/api/', '//')):
        return False
    return '.' not in target.rsplit('/', 1)[-1]


def page_link(href, lang):
    target, sep, rest = re.match(r'([^?#]*)([?#]?)(.*)', href).groups()
    return lang_path(target, lang) + sep + rest


def switcher(path):
    """Language links for the header, shown identically on every edition."""
    # Order and labels follow the live site: EN, then Arabic shown in its own script, then FR.
    labels = {'en': 'EN', 'ar': 'ع', 'fr': 'FR'}
    links = ''.join(
        f'<a href="{lang_path(path, lang)}" hreflang="{lang}" lang="{lang}" title="{LANGS[lang][0]}" data-lang="{lang}">{labels[lang]}</a>'
        for lang in ('en', 'ar', 'fr'))
    return f'<div class="lang-switch" role="group" aria-label="Language / Langue / اللغة">{links}</div>'


def alternates(path):
    # The not-found page has no translated counterparts at a real address.
    if path == '/404':
        return '<!--og-locale-->'
    tags = ''.join(f'<link rel="alternate" hreflang="{lang}" href="{SITE}{lang_path(path, lang)}">' for lang in LANGS)
    return tags + f'<link rel="alternate" hreflang="x-default" href="{SITE}{path}">' + '<!--og-locale-->'


def sitemap(paths):
    """Sitemap listing every edition, each entry naming its language alternates."""
    entries = ''
    for path in paths:
        links = ''.join(f'<xhtml:link rel="alternate" hreflang="{lang}" href="{SITE}{lang_path(path, lang)}"/>' for lang in LANGS)
        links += f'<xhtml:link rel="alternate" hreflang="x-default" href="{SITE}{path}"/>'
        entries += ''.join(f'<url><loc>{SITE}{lang_path(path, lang)}</loc>{links}</url>' for lang in LANGS)
    return ('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml">' + entries + '</urlset>')


def finish(doc, path, lang):
    """Mark the current language in the switcher. Used for every edition, English included."""
    current = f'data-lang="{lang}"'
    locale = f'<meta property="og:locale" content="{OG_LOCALES[lang]}">' + ''.join(
        f'<meta property="og:locale:alternate" content="{OG_LOCALES[other]}">' for other in LANGS if other != lang and path != '/404')
    return (doc.replace('<!--lang-switch-->', switcher(path)).replace('<!--og-locale-->', locale)
            .replace(current, current + ' aria-current="true"'))


TAG = re.compile(r'(<!--.*?-->|<[^>]+>)', re.S)
ATTR = re.compile(r'\s([\w:-]+)="([^"]*)"')


def localize(doc, path, translator):
    lang = translator.lang
    name, code, direction = LANGS[lang]
    out, raw = [], None
    for token in TAG.split(doc):
        if not token:
            continue
        if token.startswith('<'):
            tag = re.match(r'</?([\w-]+)', token)
            tag = tag.group(1).lower() if tag else ''
            if raw:
                if token.lower().startswith('</' + raw):
                    raw = None
                out.append(token)
                continue
            if tag in ('script', 'style') and not token.startswith('</'):
                raw = tag
            if tag and not token.startswith('</'):
                token = localize_tag(token, tag, path, translator)
            out.append(token)
        elif raw:
            out.append(token)
        else:
            out.append(html.escape(translator.text(html.unescape(token), path), quote=False))
    doc = ''.join(out)
    doc = re.sub(r'<html lang="en" dir="ltr"', f'<html lang="{lang}" dir="{direction}"', doc, count=1)
    return doc


def localize_tag(token, tag, path, translator):
    lang = translator.lang

    def attr(match):
        key, value = match.group(1), match.group(2)
        if key == 'href' and tag in ('a', 'link') and 'hreflang=' not in token:
            if tag == 'a' and is_page_link(value):
                value = page_link(value, lang)
            elif tag == 'link' and 'rel="canonical"' in token:
                value = SITE + lang_path(value[len(SITE):], lang)
        elif key in ATTRS:
            value = html.escape(translator.text(html.unescape(value), path), quote=True)
        elif key == 'content' and tag == 'meta' and re.search(r'(name="description"|property="og:(?:title|description)")', token):
            value = html.escape(translator.text(html.unescape(value), path), quote=True)
        elif key == 'content' and tag == 'meta' and 'property="og:url"' in token:
            value = SITE + lang_path(value[len(SITE):], lang)
        return f' {key}="{value}"'

    return ATTR.sub(attr, token)


def report(translators):
    for translator in translators:
        # Entries no page uses any more, usually left behind when English copy is
        # removed. Listed so they can be deleted from i18n/<lang>/*.json.
        unused = sorted(set(translator.entries) - translator.used)
        stale = root / f'_unused-{translator.lang}.json'
        if unused:
            stale.write_text(json.dumps(unused, ensure_ascii=False, indent=1), encoding='utf-8')
            print(f'{translator.lang}: {len(unused)} translations no longer used - see {stale.relative_to(root.parent)}')
        else:
            stale.unlink(missing_ok=True)
        target = root / f'_missing-{translator.lang}.json'
        if translator.missing:
            target.write_text(json.dumps(translator.missing, ensure_ascii=False, indent=1), encoding='utf-8')
            print(f'{translator.lang}: {len(translator.missing)} strings left in English - see {target.relative_to(root.parent)}')
        else:
            target.unlink(missing_ok=True)
            print(f'{translator.lang}: fully translated')
