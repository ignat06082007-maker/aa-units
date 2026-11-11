"""Проверка пересчитанной книги: ошибки формул, форматы и сверка DPS с независимым расчётом на Python.
Запуск: python -I tools/check_book.py <пересчитанный.xlsx>   (пересчёт: soffice --headless --convert-to xlsx)
Сверка корректна при настройках по умолчанию (уровень 1, бафы выключены, 1 цель, DoT = Да, крит ×1,5,
трейтов/реликвий у юнитов нет, пассивки — как из вики)."""
import sys, os
from collections import Counter
from openpyxl import load_workbook
from openpyxl.utils import column_index_from_string as ci

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_units as B

wb = load_workbook(sys.argv[1], data_only=True)
errors = []
for ws in wb.worksheets:
    for row in ws.iter_rows():
        for c in row:
            if isinstance(c.value, str) and (c.value.startswith('#') or c.value.startswith('Err:')):
                errors.append(f'{ws.title}!{c.coordinate}={c.value}')
print('листы:', wb.sheetnames)
print('ошибок формул:', len(errors), errors[:10])
print('форматы:', Counter(c.number_format for w in wb.worksheets for row in w.iter_rows()
                          for c in row if c.number_format != 'General'))

TRAIT = {t[0]: t for t in B.TRAITS}
RELIC = {t[0]: t for t in B.RELICS}
# правки пользователя на листе «Реликвии» (A..Q): урон/крит/PWR берём из книги
RELIC_PWR = {}
for _r in wb['Реликвии'].iter_rows(min_row=1, values_only=True):
    if _r and _r[0] and isinstance(_r[1], (int, float)) and len(_r) >= 17:
        RELIC[_r[0]] = (_r[0], _r[1] or 0, _r[2] or '', _r[3] or 0, _r[4] or '', _r[5] or 0, _r[6] or '', _r[7] or 0, _r[8] or 0)
        RELIC_PWR[_r[0]] = (_r[15] or 0, _r[16] or '')


def fits(t, u):
    return bool(t) and (t == 'Все' or t == u['dtype'] or t in u['elem'])


def py_pct(v):
    """Независимый разбор жёлтого %-поля, как задумано: 12.3 → 12.3; 0.123 (введено «12.3%») → 12.3; «9,3» → 9.3."""
    if v is None or v == '':
        return 0.0
    if isinstance(v, (int, float)):
        return v * 100 if 0 < abs(v) < 1 else float(v)
    try:
        return float(str(v).strip().replace('%', '').replace(',', '.'))
    except ValueError:
        return 0.0


def unit_inputs(Uws, col, r):
    """Жёлтые поля юнита на «Юнитах» (сырые значения) → числа."""
    g = lambda k: Uws.cell(r, col[k]).value
    inp = {k: py_pct(g(k)) for k in ('pas', 'pasc', 'pascd', 'pasdot', 'cd', 'cs')}
    inp['cc'] = None if g('cc') in (None, '') or str(g('cc')).strip() == '' else py_pct(g('cc'))
    for key, stat in (('curD', 'Урон'), ('curS', 'SPA'), ('curR', 'Радиус')):
        inp[key] = sum(py_pct(g(v)) for s, v in B.CURSE_SLOTS if g(s) == stat)
    inp['trait'], inp['relic'] = g('trait'), g('relic')
    return inp


def expected_dps(u, row, lvl=1.0, buff_pct=0.0, trait=None, relic=None, passive=True, dot_buff=0.0,
                 crit_buff=0.0, spa_buff=0.0, inp=None, summon_buff=0.0, ram_buff=0.0, targets=1.0):
    inp = inp or {'pas': u['pas_pct'], 'pasc': u['pas_crit'], 'pascd': u['pas_cd'], 'pasdot': u['pas_dot'],
                  'cd': 0, 'cs': 0, 'cc': None, 'curD': 0, 'curS': 0, 'curR': 0}
    tr = TRAIT.get(trait, (None, 0, 0, 0))
    base = B.relic_base(relic)                   # копии «X #2» / «X #3» по умолчанию такие же, как «X»
    rl = RELIC.get(relic, RELIC.get(base, (None, 0, '', 0, '', 0, '', 0, 0)))
    rd = (rl[1] if fits(rl[2], u) else 0) + (rl[3] if fits(rl[4], u) else 0)
    rc = rl[5] if (not rl[6] or fits(rl[6], u)) else 0
    spa = row['spa'] * max(0.1, 1 - (inp['cs'] + spa_buff) / 100) * (1 - tr[2] / 100) * max(0.1, 1 + inp['curS'] / 100)
    # отдельные множители (сверено с игрой): общий/LB × ранг × проклятие × (пассивка + реликвия) × трейт × PWR; бафы — свой множитель
    _pw = RELIC_PWR.get(relic, (0, ''))
    pwr = _pw[0] if (not _pw[1] or fits(_pw[1], u)) else 0
    mult0 = (lvl * (1 + GD / 100) * (1 + inp['cd'] / 100) * (1 + inp['curD'] / 100)
             * (1 + ((inp['pas'] if passive else 0) + rd) / 100) * (1 + tr[1] / 100) * (1 + pwr * (_st['I11'].value or 1.75) / 100))
    mult = mult0 * (1 + buff_pct / 100)
    dmg = row['dmg'] * mult
    dmg_dot = dmg                    # любой DoT — от финального удара со всеми бафами
    pc, pcd, pdot = (inp['pasc'], inp['pascd'], inp['pasdot']) if passive else (0, 0, 0)
    base_crit = u['crit'] if inp['cc'] is None else inp['cc'] / 100
    crit = min(1, base_crit + (rc + pc + crit_buff) / 100)
    cm = (u['critdmg'] or 1.5) + (rl[7] + pcd) / 100
    rdot, rdotk = B.RELIC_DOT.get(base, (0, ''))
    amp = dot_buff + pdot + (rdot if row['dotkind'] and rdotk in ('Все', row['dotkind']) else 0)
    clk_n, clk_p = B.RELIC_CLOCK.get(base, (0, 0))
    clock = dmg * clk_p / 100 / clk_n if clk_n and u['dtype'] == 'Маг' else 0
    # призывы: фрагменты правил с {E} = урон по вики, {S} = SPA итог
    sm = row['summon']
    ev = lambda key: eval(sm[key].replace('{E}', repr(row['dmg'])).replace('{S}', repr(spa)), {}) if sm.get(key) else 0
    c = sm.get('c')
    cyc = spa if c == 'spa' else (max(spa, (WALK + 1.5 * spa) / 3) if spa > 0 else 0) if c == B.JELLY else (c or 0)
    kps = (min(KPS, targets / spa) if spa > 0 else 0) if sm.get('own') else KPS
    k, cap = ev('k') * kps, ev('cap')
    smult = mult0 * (1 + ram_buff / 100) if sm.get('ram') else mult
    summ = smult * ((ev('t') / cyc if cyc else 0) + (min(k, cap) if cap else k)) * (1 + summon_buff / 100)
    if not row['own_hits']:
        return summ
    hits = dmg / spa * (1 + crit * (cm - 1)) + dmg_dot * row['mult'] * row['ticks'] / spa * (1 + amp / 100) if spa > 0 else 0
    return hits + clock + summ


_st = wb['Настройки']
_b4 = _st['B4'].value
lvl_set = (_st['B5'].value or 1) if _b4 == 'Свой' else B.lvl_mult(_b4)   # уровень из «Настроек» (для «Апгрейдов» и «Команды»)
GD = _st['I7'].value or 0                       # общий бонус × LB отряда, % (как в книге)
KPS = max(0, _st['I9'].value or 0)
WALK = max(0, _st['I10'].value if _st['I10'].value is not None else 5)
units = B.load()
ws = wb['Апгрейды']
Uws = wb['Юниты']
col = {k: ci(v) for k, v in B.UC.items()}
urow = {Uws.cell(i, 1).value: i for i in range(5, Uws.max_row + 1)}
r, bad, n = 5, 0, 0
for u in units:
    inp = unit_inputs(Uws, col, urow[u['name']])
    for row in u['rows']:
        exp = expected_dps(u, row, lvl_set, trait=inp['trait'], relic=inp['relic'], inp=inp)
        got = ws.cell(r, 26).value or 0
        if abs(got - exp) > 1e-6 * max(1, exp):
            bad += 1
            if bad <= 5: print('расхождение', u['name'], row['upg'], got, exp)
        if ws.cell(r, 1).value != u['name']:
            print('сдвиг строк', r, ws.cell(r, 1).value, u['name']); break
        n += 1; r += 1
print(f'DPS сверено: {n} строк, расхождений {bad}  (с пассивкой из вики: {sum(1 for u in units if u["pas_pct"])} юнитов)')

U = wb['Юниты']
print('Юниты, пример строки:', {k: U.cell(5, col[k]).value for k in ('name', 'rarity', 'tier', 'dtype', 'elem', 'dps', 'dpsk')})
print('тиры:', Counter(U.cell(i, col['tier']).value for i in range(5, 5 + len(units))))

by = {u['name']: u for u in units}
C = wb['Сравнение']
cc = {k: ci(v) for k, v in B.CC.items()}
buff = {b[0]: b for b in B.BUFFS}
cmp_bad = 0
for i in B.CMP_SLOTS:
    g = lambda k: C.cell(i, cc[k]).value
    if g('name') not in by:          # пусто или «— убрать»
        continue
    u = by[g('name')]
    upg = g('upg')
    row = u['rows'][-1] if upg in (None, '') else u['rows'][min(int(upg), len(u['rows']) - 1)]
    lvl = lvl_set if g('lvl_in') in (None, '') else B.lvl_mult(g('lvl_in'))
    chosen = list(dict.fromkeys(s for s in (g(k) for k in ('b1', 'b2', 'b3', 'b4')) if s in buff))   # дубли — один раз
    who_ok = lambda s, who: buff[s][3] in ('Все', who)

    def kind_sum(kind, who=None, exclude=()):
        total = sum(buff[s][2] for s in chosen if buff[s][1] == kind and (who is None or who_ok(s, who)) and s not in exclude)
        for k, ga, gb in B.NO_STACK:      # «не складываются» — вычесть меньшую группу
            if k == kind:
                a = [buff[s][2] for s in chosen if s in ga and s not in exclude]; b_ = [buff[s][2] for s in chosen if s in gb and s not in exclude]
                if a and b_:
                    total -= min(max(a), max(b_))
        return total
    if C['B3'].value == 'Да':
        print(f'Сравнение {i}: B3 = Да — проверка бафов из «Настроек» не поддерживается, пропуск'); continue
    pct = kind_sum('Урон', u['dtype'])
    dot_pct = kind_sum('DoT', row['dotkind'])
    uinp = unit_inputs(U, col, urow[u['name']])
    exp = expected_dps(u, row, lvl, pct, g('trait') or uinp['trait'], g('relic') or uinp['relic'],
                       g('pas_in') != 'Нет', dot_pct, kind_sum('Крит'), kind_sum('SPA'), inp=uinp,
                       summon_buff=kind_sum('Призыв'), ram_buff=kind_sum('Урон', 'Физ', B.RAM_EXCLUDE))
    got = g('dps')
    print(f'   DoT: {g("dotname")}  усиление={g("dotamp")}  DPS от DoT={g("dotdps")}')
    ok = abs((got or 0) - exp) <= 1e-6 * max(1, exp)
    cmp_bad += not ok
    print(f'Сравнение {i}: {u["name"]:32s} ур.{g("lvl_in") or 1:>3} бафы={pct:>4}% трейт={g("trait") or "-":13s} '
          f'реликвия={g("relic") or "-":18s} DPS={got:,.1f} удар={g("maxhit"):,.0f} без бафов={g("dps0"):,.1f} '
          f'{"OK" if ok else "РАСХОЖДЕНИЕ " + str(exp)}')
print('Сравнение расхождений:', cmp_bad)

H = wb['Главная']
print('Главная топ-3 DPS:', [H.cell(r, 2).value for r in range(15, 18)], ' выгода:', [H.cell(r, 9).value for r in range(15, 18)])
T = wb['Команда']
tk = {k: ci(v) for k, v in B.TK.items()}
team = []
for r in B.TEAM_ROWS:
    n = T.cell(r, tk['name']).value
    if n in by:
        c = T.cell(r, tk['cnt_in']).value
        team.append((r, by[n], int(float(c)) if str(c or '').strip() not in ('', 'None') else 0, T.cell(r, tk['upg']).value))
given = []                                   # (баф, множитель) от каждого баффера команды
for r, u, cnt, _ in team:
    tb = B.TEAM_BUFFS.get(u['name'])
    if tb and cnt > 0:
        a, a4, capa, bb, capb = tb
        given.append(((a4 if a4 and cnt >= 4 else a), min(cnt, capa) if capa else 1))
        if bb:
            given.append((bb, min(cnt, capb) if capb else 1))


def team_sum(kind, who=None, exclude=()):
    total = sum(buff[b][2] * m for b, m in given if buff[b][1] == kind and (who is None or buff[b][3] in ('Все', who)) and b not in exclude)
    names = [b for b, _ in given if b not in exclude]
    for k, ga, gb in B.NO_STACK:
        if k == kind:
            a = [buff[s][2] for s in names if s in ga]; b_ = [buff[s][2] for s in names if s in gb]
            if a and b_:
                total -= min(max(a), max(b_))
    return total


team_bad = 0
for r, u, cnt, upg in team:
    row = u['rows'][-1] if upg in (None, '') else u['rows'][min(int(upg), len(u['rows']) - 1)]
    uinp = unit_inputs(U, col, urow[u['name']])
    exp = expected_dps(u, row, lvl_set, team_sum('Урон', u['dtype']), uinp['trait'], uinp['relic'], True,
                       team_sum('DoT', row['dotkind']) if row['dotkind'] else 0, team_sum('Крит'), team_sum('SPA'),
                       inp=uinp, summon_buff=team_sum('Призыв'), ram_buff=team_sum('Урон', 'Физ', B.RAM_EXCLUDE))
    got = T.cell(r, tk['dps']).value or 0
    ok = abs(got - exp) <= 1e-6 * max(1, exp)
    team_bad += not ok
    print(f'Команда {r}: {u["name"]:30s} ×{cnt} DPS={got:,.1f} | даёт: {T.cell(r, tk["gives"]).value} '
          f'{"OK" if ok else "РАСХОЖДЕНИЕ " + str(exp)}')
print('Команда расхождений:', team_bad, '| бафы команды:', given)
raw = load_workbook(sys.argv[1])
print('графики:', {w.title: len(w._charts) for w in raw if w._charts},
      ' ссылки на Юнитах:', sum(1 for c in raw['Юниты']['A'] if c.hyperlink), ' на Главной:', sum(1 for c in raw['Главная']['B'] if c.hyperlink))
