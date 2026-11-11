"""Способности юнитов со страниц вики → data/abilities.json.
Скачивает wikitext страниц всех юнитов (по 50 за запрос, как данные, код вики не исполняется) и вытаскивает разделы
«Passive Ability: …» / «Active Ability: …» (и похожие). Запуск: python -I tools/fetch_abilities.py"""
import json, os, re, sys, time, urllib.parse, urllib.request

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_units as B

API = 'https://animeadventures.fandom.com/api.php'
OUT = os.path.join(B.ROOT, 'data', 'abilities.json')
HEAD = re.compile(r'^(={2,4})\s*(.+?)\s*\1\s*$', re.M)


def fetch(titles):
    q = urllib.parse.urlencode({'action': 'query', 'prop': 'revisions', 'rvprop': 'content', 'rvslots': 'main',
                                'titles': '|'.join(titles), 'format': 'json', 'formatversion': 2, 'redirects': 1})
    req = urllib.request.Request(API + '?' + q, headers={'User-Agent': 'aa-units-data/1.0'})
    js = json.load(urllib.request.urlopen(req, timeout=90))['query']
    back = {r['to']: r['from'] for r in js.get('redirects', [])}
    out = {}
    for p in js['pages']:
        if 'revisions' in p:
            out[back.get(p['title'], p['title'])] = p['revisions'][0]['slots']['main']['content']
    return out


def clean(s):
    s = re.sub(r'\[\[File:[^\]]*\]\]', '', s)
    s = re.sub(r'<gallery>.*?</gallery>', '', s, flags=re.S)
    s = re.sub(r'\{\{PAGENAME\}\}', '§', s)
    s = re.sub(r'\{\{(?:Damage Type|Rarity|Yen)\|([^}|]*)[^}]*\}\}', r'\1', s)
    s = re.sub(r"'''?", '', s)
    s = B.clean(s)
    return re.sub(r'\s+', ' ', s).strip()


def abilities(name, text):
    """Разделы со способностями: заголовок содержит Ability / Passive / Active / Skill (не Selling / Trivia / Gallery)."""
    res = []
    heads = list(HEAD.finditer(text))
    for i, h in enumerate(heads):
        title = re.sub(r"'''?", '', h.group(2)).strip()
        if not re.search(r'abilit|passive|active|skill|ultimate', title, re.I):
            continue
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        body = clean(text[h.end():end]).replace('§', name)
        kind = 'active' if re.search(r'active|ultimate', title, re.I) else 'passive'
        nm = re.sub(r'^(?:passive|active)\s*(?:ability|skill)?\s*[:\-–]?\s*', '', title, flags=re.I).strip() or title
        if body:
            res.append({'type': kind, 'name': nm, 'text': body[:1200]})
    return res


def main():
    units = [u['name'] for u in B.load()]
    pages = {}
    for i in range(0, len(units), 50):
        pages.update(fetch(units[i:i + 50]))
        print(f'страниц {len(pages)}/{len(units)}', flush=True)
        time.sleep(1)
    data = {n: abilities(n, pages.get(n, '')) for n in units}
    json.dump(data, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    n_ab = sum(len(v) for v in data.values())
    print('OK', OUT, 'юнитов со способностями:', sum(1 for v in data.values() if v), 'способностей:', n_ab,
          'без страницы:', [n for n in units if n not in pages][:10])


if __name__ == '__main__':
    main()
