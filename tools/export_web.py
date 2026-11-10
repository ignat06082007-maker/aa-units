"""Экспорт данных для веб-версии: web/units.js (window.AA_DATA = {...}).
Берёт те же данные и константы, что и генератор Excel (build_units.load(), BUFFS, TRAITS, RELICS…),
поэтому сайт и таблица считают одинаково. Запуск: python -I tools/export_web.py
.js, а не .json — чтобы страница открывалась и двойным кликом (file://), где fetch() не работает."""
import json, os, sys, datetime

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_units as B

OUT = os.path.join(B.ROOT, 'web', 'units.js')



def compact_row(r):
    """Одна строка апгрейда — массивом, чтобы файл был меньше (порядок = ROW_KEYS)."""
    sm = r['summon'] or {}
    return [r['upg'], r['step'], r['total'], r['dmg'], r['spa'], r['rng'], r['atype'], r['eff'], r['dotkind'],
            r['ticks'], r['mult'], r['note'], {k: v for k, v in sm.items()} or 0, 1 if r['own_hits'] else 0]


ROW_KEYS = ['upg', 'step', 'total', 'dmg', 'spa', 'rng', 'atype', 'eff', 'dotkind', 'ticks', 'mult', 'note', 'summon', 'own']


def main():
    units = B.load()
    out_units = []
    for u in units:
        out_units.append(dict(
            n=u['name'], r=u['rarity'], dt=u['dtype'], role=u['role'], place=u['place'], cap=u['cap'] or 0,
            farm=u['farm'] or 0, crit=u['crit'], cdm=u['critdmg'] or 0, lim=u['limited'] == 'Да',
            el=u['elem'], pas=u['passives'], pp=u['pas_pct'], pc=u['pas_crit'], pcd=u['pas_cd'], pdot=u['pas_dot'],
            summ=u['summ'], evo=u['evo_from'], feats=u['feats'],
            rows=[compact_row(r) for r in u['rows']]))
    data = dict(
        version=datetime.date.today().isoformat(),
        source='Anime Adventures Wiki (animeadventures.fandom.com), CC BY-SA',
        rowKeys=ROW_KEYS,
        rarityOrder=B.RARITY_ORDER, rarityRu=B.RARITY_RU,
        lvl100=B.LVL100, lvl110=B.LVL110,
        buffs=[dict(n=b[0], kind=b[1], v=b[2], who=b[3], note=b[4]) for b in B.BUFFS],
        noStack=[dict(kind=k, a=list(a), b=list(b)) for k, a, b in B.NO_STACK],
        traits=[dict(n=t[0], d=t[1], s=t[2], r=t[3], note=t[4]) for t in B.TRAITS],
        relics=[dict(n=t[0], d1=t[1], t1=t[2], d2=t[3], t2=t[4], c=t[5], ct=t[6], cd=t[7], sit=t[8], note=t[9],
                     dot=B.RELIC_DOT.get(t[0], (0, ''))[0], dotk=B.RELIC_DOT.get(t[0], (0, ''))[1],
                     pen=B.RELIC_PEN.get(t[0], (0, ''))[0], penk=B.RELIC_PEN.get(t[0], (0, ''))[1],
                     clkn=B.RELIC_CLOCK.get(t[0], (0, 0))[0], clkp=B.RELIC_CLOCK.get(t[0], (0, 0))[1],
                     pwr=0, pwrk='') for t in B.RELICS],
        teamBuffs={k: dict(a=v[0], a4=v[1], capa=v[2], b=v[3], capb=v[4]) for k, v in B.TEAM_BUFFS.items()},
        dotKinds=list(B.DOT_KINDS),
        elems=list(B.ELEM_RU.values()),
        atypes=['Single', 'AoE (Circle)', 'AoE (Cone)', 'AoE (Line)', 'AoE (Full)', '(нет данных)'],
        units=out_units,
    )
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    s = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write('/* Данные юнитов Anime Adventures — генерируется tools/export_web.py, руками не править */\n')
        f.write('window.AA_DATA = ' + s + ';\n')
    print('OK', OUT, len(out_units), 'юнитов', sum(len(u['rows']) for u in out_units), 'апгрейдов',
          f'{len(s) / 1024:.0f} КБ')


if __name__ == '__main__':
    main()
