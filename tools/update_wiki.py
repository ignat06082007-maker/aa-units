"""Скачивает свежую базу юнитов с вики Anime Adventures и разбирает её в data/*.json.
Lua-код вики НЕ исполняется — таблицы читаются как данные парсером luaparse.py.
Запуск: python -I tools/update_wiki.py   затем   python -I tools/build_units.py"""
import json, os, sys, urllib.parse, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from luaparse import parse_module

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API = 'https://animeadventures.fandom.com/api.php'
MODULES = {'Module:UnitData/Data': ('UnitData.lua', 'data.json'),
           'Module:UnitData/Data/AoE_Type': ('AoE_Type.lua', 'aoe.json')}

for title, (lua_name, json_name) in MODULES.items():
    q = urllib.parse.urlencode({'action': 'query', 'prop': 'revisions', 'rvprop': 'content',
                                'rvslots': 'main', 'titles': title, 'format': 'json'})
    req = urllib.request.Request(f'{API}?{q}', headers={'User-Agent': 'Mozilla/5.0'})
    page = next(iter(json.load(urllib.request.urlopen(req, timeout=60))['query']['pages'].values()))
    src = page['revisions'][0]['slots']['main']['*']
    open(os.path.join(ROOT, 'data', lua_name), 'w', encoding='utf-8').write(src)
    data = parse_module(src)
    json.dump(data, open(os.path.join(ROOT, 'data', json_name), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(title, '->', json_name, len(data), 'записей')
