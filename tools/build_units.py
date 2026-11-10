"""Собирает AA_юниты.xlsx из данных вики Anime Adventures (data/data.json + data/aoe.json).

Запуск:  python -I tools/build_units.py [путь.xlsx]
Данные обновляются:  python -I tools/update_wiki.py  (качает модули с вики и парсит их)

Соглашение как в бюджете: жёлтая заливка FFF2CC = ячейка для ручного ввода,
всё остальное — формулы. xlsx руками не пересобирать, править этот скрипт.
При пересборке жёлтые ячейки переносятся из прошлой версии книги.
"""
import json, re, os, sys
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.hyperlink import Hyperlink
from openpyxl.formatting.rule import ColorScaleRule, CellIsRule, FormulaRule
from openpyxl.chart.series import SeriesLabel
from openpyxl.chart import BarChart, Reference

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_ARGS = [a for a in sys.argv[1:] if not a.startswith('--')]
OUT = _ARGS[0] if _ARGS else os.path.join(ROOT, 'AA_юниты.xlsx')
PROTECT = '--protect' in sys.argv     # копия для раздачи: защита листов и структуры паролем

# ── стили ──────────────────────────────────────────────────────────────
YELLOW = PatternFill('solid', fgColor='FFF2CC')   # ручной ввод
YELLOW_RGB = ('00FFF2CC', 'FFFFF2CC')             # так её читает openpyxl (своя / после LibreOffice)
GREY = PatternFill('solid', fgColor='EDEDED')     # данные вики (не формулы)
BAND = PatternFill('solid', fgColor='F2F6FC')     # полосы через строку
GREEN = PatternFill('solid', fgColor='C6EFCE')
HEAD = PatternFill('solid', fgColor='1F3864')
HEAD_DPS = PatternFill('solid', fgColor='375623')
HEAD_INPUT = PatternFill('solid', fgColor='BF8F00')
SUB = PatternFill('solid', fgColor='D9E1F2')
WHITE_B = Font(bold=True, color='FFFFFF')
BOLD = Font(bold=True)
LINK = Font(color='1F3864', bold=True)
TITLE = Font(bold=True, size=16, color='1F3864')
HINT = Font(italic=True, color='595959')
THIN = Side(style='thin', color='BFBFBF')
BOX = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
CENTER = Alignment(horizontal='center', vertical='center', wrap_text=True)
TOPWRAP = Alignment(wrap_text=True, vertical='top')

MONEY = '#,##0'          # игровые деньги, без валютного символа
DPS = '#,##0.0'
NUM2 = '0.00'
PCT = '0%'
PLUSPCT = '+0%;-0%;0%'

RARITY_RU = {'Exclusive': 'Эксклюзив', 'Secret': 'Секретный', 'Mythic': 'Мифический',
             'Legendary': 'Легендарный', 'Epic': 'Эпический', 'Rare': 'Редкий'}
RARITY_ORDER = list(RARITY_RU)
RARITY_FILL = {'Эксклюзив': 'F4B6E0', 'Секретный': 'F4B6B6', 'Мифический': 'FFD8A8',
               'Легендарный': 'FFF2A8', 'Эпический': 'D9C8F0', 'Редкий': 'BDD7EE'}
DMG_RU = {'physical': 'Физ', 'magic': 'Маг', 'true_damage': 'Чистый'}

# Бафферы — цифры со страниц вики (раздел описания способности).
# (имя, что даёт, %, на кого, пояснение). Порядок не менять: прошлые правки переносятся по адресу ячейки.
BUFFS = [
    ('Commander (1 шт.)', 'Урон', 25, 'Физ', 'Commander: +25% физ. урона юнитам в радиусе, 30 с, КД 60 с'),
    ('Commander ×4 (бесконечный баф)', 'Урон', 100, 'Физ', 'Commander: цепочка из 4 шт. с проклятием +SPA держит 100%'),
    ('Wind Dragon (1 шт.)', 'Урон', 30, 'Маг', 'Wind Dragon: +30% маг. урона в радиусе, 30 с, КД 60 с'),
    ('Wind Dragon ×4 (бесконечный баф)', 'Урон', 100, 'Маг', 'Wind Dragon: цепочка из 4 шт. держит 100%'),
    ('Elfy (Sylph)', 'Урон', 50, 'Маг', 'Elfy (Sylph): +50% маг. урона в радиусе, 30 с, КД 60 с'),
    ('Blossom', 'Урон', 10, 'Все', 'Blossom: аура +10% урона юнитам в радиусе'),
    ('Griffin (Reincarnation)', 'Урон', 100, 'Все', 'Griffin (Reincarnation) / Гриффит: +100% урона всем юнитам, глобально'),
    ('Skeleton (Soul King)', 'Урон', 15, 'Все', 'Skeleton (Soul King): каждая атака случайно даёт +15% урона ИЛИ +10% радиуса на 10 с'),
    ('Idol (макс. апгрейд)', 'Урон', 10, 'Все', 'Idol: +5/7/10% урона всем юнитам на карте'),
    ('Idol (Star) — урон', 'Урон', 15, 'Все', 'Idol (Star): до +15% урона всем юнитам'),
    ('Idol (Star) — скидка', 'Скидка', 20, 'Все', 'Idol (Star): до −20% цены апгрейдов'),
    ('Trickster (Release) — SPA', 'SPA', 10, 'Все', 'Trickster (Release): −10% SPA союзникам'),
    ('Trickster (Release) — радиус', 'Радиус', 20, 'Все', 'Trickster (Release): +20% радиуса союзникам'),
    ('Gambler (Jackpot)', 'Крит', 50, 'Все', 'Gambler (Jackpot): Frenzy +50% крит-шанса юнитам в радиусе'),
    ('Дебафф: Cursed King / Switchblade', 'Урон', 20, 'Физ', 'Враги навсегда получают +20% физ. урона (вики Effects)'),
    ('Дебафф: Blackhair', 'Урон', 15, 'Маг', 'Враги получают +15% маг. урона (вики Effects)'),
    ('Дебафф: Hexed / Shadow Sorcerer', 'Урон', 30, 'Маг', 'Враги получают +30% маг. урона (Hexed — навсегда)'),
    # усилители DoT: вид «DoT», в «На кого» — какой DoT (Кровотечение / Горение / Яд / Иссушение / Все)
    ('Bloodcry (Fallen) — Bleed Amp ×5', 'DoT', 400, 'Кровотечение', 'Bleed Amplification: враги получают ×3,5–×5 урона от ВСЕХ кровотечений (×5 = +400%)'),
    ('Blood (Unleashed) — Bleed Amp ×5', 'DoT', 400, 'Кровотечение', 'Bleed Amplification: ×3,5–×5 урона от всех кровотечений (×5 = +400%)'),
    ('Bleed Amp ×3,5 (низкий апгрейд)', 'DoT', 250, 'Кровотечение', 'Bloodcry / Blood на ранних апгрейдах: ×3,5 = +250%'),
    # найдено проверкой вики 09.11.2026
    ('Priest (Heaven) — Time Acceleration', 'SPA', 50, 'Все', 'Priest (Heaven): −50% SPA всем на карте на 30 с, КД 300 с. Не складывается с SPA Trickster'),
    ('Priest (Heaven) — в среднем', 'SPA', 5, 'Все', 'Time Acceleration в среднем: 30 с из 300 = −5% SPA'),
    ('Devil Boss — Time Erase', 'Урон', 50, 'Все', 'Devil Boss: +50% урона всем на 8–9 с, КД 90 с (ручная способность)'),
    ('Дебафф: Chuuni (Delusion) ×1', 'Урон', 50, 'Маг', 'Pact of Frailty: цель получает +50% маг. урона (1 цель на каждую Chuuni)'),
    ('Дебафф: Chuuni (Delusion) ×3', 'Урон', 150, 'Маг', 'Pact of Frailty на 3 стаках: +150% маг. урона по цели'),
    # вид «Призыв» — только урон призывов; умножается на остальные бафы (вики, Zombie (Risen))
    ('Zombie (Risen) ×1', 'Призыв', 25, 'Все', 'Undead Blessing: +25% урона и +10% радиуса всем призывам за каждую Zombie (Risen)'),
    ('Zombie (Risen) ×4 (соло, макс.)', 'Призыв', 100, 'Все', '4 копии (лимит на игрока) = +100% урона призывам'),
    ('Zombie (Risen) ×8 (кооп, макс.)', 'Призыв', 200, 'Все', '8 копий в коопе — потолок +200% урона призывам'),
]
# Не складываются — берётся больший: (вид бафа, группа A, группа B).
# Blossom ↔ Idol / Idol (Star) — страницы Blossom, Idol, Idol (Star); SPA Trickster ↔ Priest — страница Trickster (Release)
NO_STACK = (('Урон', ('Blossom',), ('Idol (макс. апгрейд)', 'Idol (Star) — урон')),
            ('SPA', ('Trickster (Release) — SPA',), ('Priest (Heaven) — Time Acceleration', 'Priest (Heaven) — в среднем')))
DOT_KINDS = ('Кровотечение', 'Горение', 'Яд', 'Иссушение')
DOT_RU = {'Bleed': 'Кровотечение', 'Burn': 'Горение', 'Poison': 'Яд', 'Wither': 'Иссушение'}
# Чёрное пламя = горение на 100% урона (вики, страница Effects)
BLACK_BURN = {'Izo (Black Fire)', 'Izo (Samurai)', 'Izo', 'Shinobi (Eternal)', 'Shinobi (Awakened)'}
BUFFERS = {'Commander', 'Wind Dragon', 'Elfy (Sylph)', 'Blossom', 'Griffin (Reincarnation)',
           'Skeleton (Soul King)', 'Idol', 'Idol (Star)', 'Trickster (Release)', 'Gambler (Jackpot)'}
# Пометки, которых нет в данных вики, но без них таблица вводит в заблуждение
SPECIAL = {
    'Griffin (Darkness)': '⚠ Форма Griffin (Ascension): включается жертвой юнитов-бафферов — цена в таблице не настоящая',
    'Griffin (Reincarnation)': '⚠ Форма Griffin (Ascension): включается жертвой юнитов-бафферов — цена в таблице не настоящая',
}
# ── Призывы (исследование вики + data.json, 10.11.2026) ─────────────────
# Урон тарана ≈ HP призыва; HP растёт с уровнем как урон (×9,204 на 100 ур.).
# Правило: f(i, hp) → dict формул-фрагментов ДО множителя урона юнита (уровень, статы, бафы применяются в формулах):
#   t — урон призывов за цикл, c — цикл: число секунд / 'spa' (SPA юнита) / 'jelly' (медузы Elyssia),
#   k — урон призывов за 1 убийство, cap — потолок «урона за убийства» в секунду, hit — урон ОДНОГО удара призыва.
# Плейсхолдеры: {E} — урон юнита по вики, {S} — SPA юнита итог, {hp} — HP призыва по вики (число).
JELLY = 'jelly'
SUMMON_RULES = {
    'Commander': (lambda i, hp: dict(t='{hp}', c='spa', hit='{hp}', ram=1),
                  'Survey Corps Member: таран по пути, урон ≈ HP призыва; 1 призыв за SPA (до 3 живых на Commander)'),
    'Usurper': (lambda i, hp: dict(t='{hp}', c='spa', hit='{hp}', ram=1), 'маленький титан: таран, урон ≈ HP; 1 призыв за SPA (до 3)'),
    'Usurper (Founder)': (lambda i, hp: dict(t='11*{hp}', c=480, hit='{hp}', ram=1),
                          'The Extinction (ульта, КД 480 с): 10 Wall Titan + 1 Founding Titan, таран, урон ≈ HP каждого (= HP юнита по данным)'),
    'Dracula (Unholy King)': (lambda i, hp: dict(t='25*{hp}', c=120, hit='{hp}', ram=1) if i >= 10 else {},
                              'Soul Restraint (ульта с апгрейда 10, КД 120 с): 15 Ghoul + 5 Ghoul Rider (2 полоски) = 25 × HP (= урону)'),
    'Supreme Being (Sovereign)': (lambda i, hp: dict(k='{hp}/10', hit='{hp}', ram=1, own=1) if hp else {},
                                  'Shade Birth за каждые 10 СВОИХ убийств (до 3): таран, HP = 5× урона. Убийств в секунду — не больше '
                                  '«целей / SPA» самого юнита. Бафы: только физ. урона (Commander, Griffin), Elfy / Wind Dragon / Idol не действуют'),
    'Jackal (Alpha)': (lambda i, hp: dict(t='{E}/3', c='spa', hit='{E}/3') if i >= 8 else {},
                       'Spirit Wolf (с апгрейда 8): взрыв при смерти на ⅓ урона Jackal, ~1 за атаку (предположение)'),
    # дрон: ОДИН удар (3 «хита» делят урон) 25% урона, SPA 5,5, живёт 30 с; с апгрейда 6 — 50%, SPA 4, 60 с; за 20 убийств
    'Iron Knight (Arsenal)': (lambda i, hp: (dict(k='0.5*{E}*60/4/20', hit='0.5*{E}') if i >= 6 else
                                             dict(k='0.25*{E}*30/5.5/20', hit='0.25*{E}')),
                              'дрон за каждые 20 убийств: 1 удар на 25% урона Iron Knight, SPA 5,5, живёт 30 с; с апгрейда 6 — 50%, SPA 4, 60 с'),
    # медуза: раз в SPA без врага, ≤3 на Elyssia, урон = урону Elyssia, после смерти откат 1,5×SPA (+ путь до врага)
    'Elyssia': (lambda i, hp: dict(t='{E}', c=JELLY, hit='{E}'),
                'Abyssal Jelly: раз в SPA (без врага), до 3 на Elyssia; взрыв = урон Elyssia; после смерти откат 1,5×SPA. '
                'Сама не атакует'),
    # + угорь за 5 убийств: урон ¼, SPA ×2, живёт 60 с, ≤3 одновременно → потолок 3 угря постоянно
    'Elyssia (Abyssal)': (lambda i, hp: dict(t='{E}', c=JELLY, hit='{E}', k='{E}/4*60/(2*{S})/5', cap='3*{E}/4/(2*{S})'),
                          'Abyssal Jelly: раз в SPA (без врага), до 3; взрыв = урон Elyssia; откат 1,5×SPA. Abyssal Eel за 5 убийств: '
                          'урон ¼, SPA ×2, радиус ×2,5, живёт 60 с, до 3. Сама не атакует'),
}
NO_OWN_HITS = {'Elyssia', 'Elyssia (Abyssal)'}   # урон только призывами
# Призывы-тараны (ram=1) наносят ФИЗИЧЕСКИЙ урон: их усиливают только бафы физ. урона + «Все», кроме Idol
# (вики, Supreme Being (Sovereign): «Elfy, Wind Dragon, Idol не влияют; Griffin и Commander — да»). own=1 — убийства только свои.
RAM_EXCLUDE = ('Idol (макс. апгрейд)', 'Idol (Star) — урон')
# статов нет в базе вики — со страницы (шаблон Stats Box): (цена шага, урон, SPA, радиус)
STATS_OVERRIDE = {
    'Elyssia': [(2000, 2000, 4, 9), (5000, 5000, 4, 12), (10000, 10000, 4, 12)],
    'Elyssia (Abyssal)': [(2000, 2800, 4, 9), (5000, 7000, 4, 12), (10000, 14000, 4, 12), (35000, 21000, 4, 15),
                          (70000, 42000, 4, 15)],
}
SUMMON_NOTES = {   # призыватели, у которых урон призыва на вики не описан — только текст
    'Lulu': 'призывает 3 Britannia Soldier + Shinjira; урон призывов на вики не описан — DPS юнита считается по его урону',
    'Lulu (Emperor)': 'призывает 3 Britannia Soldier + Shinjira (лазер); урон призывов на вики не описан',
    'Lyla': 'призывает духов зодиака (Taurus/Aquarius/Leo); урон духов на вики не описан — считается по урону юнита',
    'Lyla (Celestial)': 'призывает духов зодиака (Taurus/Aquarius/Leo); урон духов на вики не описан — считается по урону юнита',
    'Ghosty (Sacrifice)': 'Final Sacrifice (апгрейд 8, один раз): юнит исчезает, Ghost Devil бьёт 2 раза по ½ урона',
    'Violentine (Brutal Angel)': 'каждые 5 атак воскрешает врага с 25% его HP (до 10) — зависит от врагов, не считается',
    'Shadow Sorcerer (Ritual)': 'Ritual: удаляет себя и призывает Divine General (урон ≈ 0,5–1,25× урона Shadow Sorcerer)',
    'Zombie (Risen)': 'Undead Blessing: всем призывам на карте +25% урона и +10% радиуса за каждую копию (выбери как баф «Призыв»)',
}
LVL100 = 9.20406501834430488   # множитель урона 100 ур. из шаблона вики Stats Box
LVL110 = LVL100 * 1.19         # Limit Break до 110 ур.: «примерно +19% урона» (вики, Powerups)

ELEM_RU = {'fire_damage': 'Огонь', 'water_damage': 'Вода', 'rose_damage': 'Роза', 'air_damage': 'Воздух',
           'lightning_damage': 'Шторм', 'light_damage': 'Свет', 'dark_damage': 'Тьма', 'ice_damage': 'Лёд'}
# Пассивки из данных атак, которые дают урон: (+% урона на максимуме)
PASSIVE_PCT = {'Battlelust': 25, 'Sunshine': 125}
# Пассивки со страниц юнитов (проверка всех страниц вики 09.11.2026).
# (описание, +% урона, +% крит-шанса, +% крит-урона, +% к DoT) — числа предзаполняются в жёлтые столбцы юнита.
# Постоянные эффекты считаются сразу; зависящие от волны/времени/ульты — 0, подсказка в описании.
PASSIVE_NOTES = {
    'Vengeful Swordsman (Sky Reaver)': ('Spellforged Blades: каждый удар ещё раз бьёт магическим уроном = урон ×2 (бафы физ. урона действуют и на него)', 100, 0, 0, 0),
    'Switchblade': ('крит наносит +100% урона (×2), как у Lex', 0, 0, 50, 0),
    'Switchblade (Deception)': ('крит наносит +100% урона (×2); Dismember: враги получают +25% физ. урона (баф-строка)', 0, 0, 50, 0),
    'Spirit Archer (Reversal)': ('Holy Arrow: каждая 5-я атака — двойной урон ≈ +20% в среднем', 20, 0, 0, 0),
    'Waterfist': ('Piercing Fangs: с апгрейда 4 три удара по 50% ≈ +50% DPS', 50, 0, 0, 0),
    'Waterfist (White Tooth)': ('Piercing Fangs: +50% на апгрейдах 4–7, на апгрейде 8 пропадает — впиши 50, если стоишь на 4–7', 0, 0, 0, 0),
    'Black Blade (Captain)': ('+10% урона чистым уроном за атаку, бьёт сквозь щиты', 10, 0, 0, 0),
    'Curse (Contract)': ('Curse Stack: каждые 4 крита — +200% чистого урона; при 30% крита ≈ +15% в среднем. Форма Kon: +50% урона и +50% SPA', 15, 0, 0, 0),
    'Chuuni (Delusion)': ('Pact of Revelation: цель получает 7% урона Chuuni каждые 0,5 с ≈ +126% к DPS по одной цели (SPA 9). '
                          'Pact of Frailty: +50% маг. урона по цели, до +150% — выбери как баф', 126, 0, 0, 0),
    'Sepsis (Moon)': ('OverCrit: 100% крит по кровоточащим врагам. Поставь 0 в «крит-шанс», если рядом нет кровотечения', 0, 100, 0, 0),
    'Divine General': ('Adapted Slash: +100% крит-шанса в режиме Boss. Статы зависят от Shadow Sorcerer (Ritual) — в базе вики нули', 0, 100, 0, 0),
    'Martial Demon (Destruction)': ('Compass Needle: +50% урона на ~5 с каждые 12 с ≈ +21% в среднем', 21, 0, 0, 0),
    'Cowardly (Scared)': ('каждый 2-й удар ×2 урона ≈ +50% в среднем (тир-лист вики)', 50, 0, 0, 0),
    'Ratio (Overtime)': ('Overtime: +1% урона за волну, сложный процент. Стоит значение к 30-й волне (+35%); к 50-й ≈ +64%, к 100-й ≈ +170%', 35, 0, 0, 0),
    'Kansai (Daydream)': ('Daydream: после 10 с без атаки +10% урона в секунду (до +200%), сброс после удара. SPA на макс. апгрейде 14 с → '
                          'перед каждым ударом 4 с «мечты» = +40%. С бафами SPA меньше — уменьши', 40, 0, 0, 0),
    'Legendary Assassin (Prime)': ('Slim Down: +0,8% (спавн) … +2% (апгрейд 8) урона за атаку; на 100% получает ещё +100% → максимум +200% '
                                   '(≈50 атак). Бафы усиливают только базовую ⅓ урона — так и считается. Стоит максимум', 200, 0, 0, 0),
    'Paradox (Divine Sight)': ('Unlimited Void: +100% урона себе на 8 с, КД 60 с ≈ +13% в среднем; Limitless: +10% урона за уровень', 13, 0, 0, 0),
    'Hubris (The One)': ('Sunshine: до +125% урона и +67,5% радиуса к 15-й волне; с апгрейда 17 Griffin усиливает Sunshine', 0, 0, 0, 0),
    'Honey (Hive)': ('с апгрейда 3 иногда поле пчёл 3× урона за 3 тика, с апгрейда 6 — Nectar Cannon 5× урона; частота на вики не указана', 0, 0, 0, 0),
    'Iron Knight (Arsenal)': ('дроны за каждые 20 убийств: 25% урона (с апгрейда 6 — 50%), SPA 5,5 / 4', 0, 0, 0, 0),
    'Jackal (Alpha)': ('Spirit Wolf взрывается на ⅓ урона Jackal', 0, 0, 0, 0),
    'Supreme Being (Sovereign)': ('Shade Birth каждые 10 убийств (до 3), урон 5× показанного; Nihilism: 5× урона по всем в радиусе', 0, 0, 0, 0),
    'Fiery Commander (Hellfire)': ('Zanka no Tachi (ульта): +2% урона за каждую душу, до +1000% на 500 душах', 0, 0, 0, 0),
    'Zombie (Risen)': ('Undead Blessing: призывы +25% урона и +10% радиуса за каждую копию (до 8)', 0, 0, 0, 0),
    'Izo (Samurai)': ('Black Flames: горение на 100% урона; с Infernal Gaze горение ×2', 0, 0, 0, 0),
}

# Трейты — страница вики Traits. (имя, урон %, снижение SPA %, радиус %, пояснение)
# Урон трейта — отдельный множитель (не складывается с бафами саппортов).
TRAITS = [
    ('Нет', 0, 0, 0, 'без трейта (Adept тоже не влияет на DPS)'),
    ('Superior I', 10, 0, 0, '+10% урона'),
    ('Superior II', 12.5, 0, 0, '+12,5% урона'),
    ('Superior III', 15, 0, 0, '+15% урона'),
    ('Nimble I', 0, 5, 0, '−5% SPA (DPS +5,2%)'),
    ('Nimble II', 0, 7.5, 0, '−7,5% SPA (DPS +8,1%)'),
    ('Nimble III', 0, 12, 0, '−12% SPA (DPS +13,6%)'),
    ('Range I', 0, 0, 10, '+10% радиуса'),
    ('Range II', 0, 0, 12.5, '+12,5% радиуса'),
    ('Range III', 0, 0, 15, '+15% радиуса'),
    ('Culling', 6, 0, 0, '+20% урона по врагам с ≤30% HP — в среднем +6%'),
    ('Sniper', 0, 0, 25, '+25% радиуса'),
    ('Godspeed', 0, 20, 0, '−20% SPA (DPS +25%)'),
    ('Reaper', 15, 0, 0, '+15% урона, по боссам ещё +25%'),
    ('Reaper (по боссу)', 43.75, 0, 0, 'Reaper против босса: 1,15 × 1,25 = +43,75%'),
    ('Celestial', 32, 0, 10, '+10% урона и +20% урона как чистый → в среднем +32%, +10% радиуса'),
    ('Divine', 20, 10, 20, '+20% урона, −10% SPA, +20% радиуса'),
    ('Golden', 30, 0, 0, '+30% урона, +20% денег у ферм'),
    ('Unique', 300, 10, 10, '×4 урона, −10% SPA, +10% радиуса; можно поставить только 1 такого юнита'),
]
TRAIT_FIRST, TRAIT_LAST = 5, 34

# Реликвии — страница вики Relics. По умолчанию МАКСИМАЛЬНЫЙ ролл, диапазон — в пояснении.
# (имя, урон %, для типа, урон2 %, для типа2, крит %, крит для, +крит-урон %, ситуативный %, пояснение)
RELICS = [
    ('Нет', 0, '', 0, '', 0, '', 0, 0, 'без реликвии'),
    ('Steel Shiv', 4, 'Физ', 0, '', 0, '', 0, 0, '1 ролл из: +1–4% физ. урона / +0,5–2 PWR / +20–40 PEN'),
    ('Kunai', 0, '', 0, '', 8, 'Физ', 0, 0, '+2–8% физ. крит-шанса'),
    ('Amplifying Codex', 4, 'Маг', 0, '', 0, '', 0, 0, '1 ролл из: +1–4% маг. урона / +0,5–2 PWR / +20–40 PEN'),
    ('5-Leaf Clover', 5, 'Физ', 8, 'Тьма', 0, '', 0, 0, '+2–5% физ.; ролл: +2–8% Тьма / PWR / PEN. Anti Magic: +10–15% по врагам с маг. сопротивлением (ситуативно)'),
    ('Clover Of The Wind', 5, 'Маг', 8, 'Воздух', 0, '', 0, 0, '+2–5% маг.; ролл: +2–8% Воздух / PWR / PEN. +10–15% по летающим (ситуативно)'),
    ('Mermaid Crown', 5, 'Маг', 8, 'Вода', 0, '', 0, 0, '+2–5% маг.; ролл: +2–8% Вода / PWR / PEN. Удары водой снижают маг. сопротивление'),
    ('Miracle Timepiece', 5, 'Маг', 8, '', 0, '', 0, 0, '+2–5% маг.; ролл +2–8% ОДНОЙ стихии — выбери её в «Для типа 2», иначе бонус не считается. Каждые 30–50 с маг. удар +70–130% чистого'),
    ('Infernal Gaze', 5, 'Огонь', 0, '', 0, '', 0, 0, '1 ролл: +2–5% урона одной стихии (впиши свою). Горение длится вдвое дольше'),
    ('Mirrorblade', 5, 'Физ', 0, '', 20, 'Физ', 0, 0, '+2–5% физ., +10–20% физ. крита; каждый 4–6-й удар — гарантированный крит'),
    ('Endless Blades', 6, 'Физ', 0, '', 50, 'Физ', 0, 0, '+2–6% физ., +30–50 PEN, +20–50% физ. крита; по боссам с Dismember — % от HP'),
    ('Nail', 5.5, 'Физ', 0, '', 20, 'Физ', 30, 0, '+2–5,5% физ., +10–20% физ. крита, +15–30% крит-урона'),
    ('Hellfire Blade', 5, 'Огонь', 0, '', 0, '', 0, 0, '+2–5% урона огнём; ролл: PWR / +2–5% физ. / +2–5% маг.; +5–10% по горящим'),
    ('Black Blade: Autumn Water', 0, '', 0, '', 0, '', 0, 0, '+30–50 физ. PEN (только против сопротивления)'),
    ('Awakened Tear', 0, '', 0, '', 0, '', 0, 25, '+25% урона только в рейдах Storm Hideout — впиши в «ситуативный», если там'),
    ('Awakened Double Tear', 0, '', 0, '', 0, '', 0, 50, '+50% урона только в рейдах Storm Hideout'),
    ('Awakened Triple Tear', 0, '', 0, '', 0, '', 0, 100, '+100% урона только в рейдах Storm Hideout'),
    ('Aranca Crown', 0, '', 0, '', 0, '', 0, 270, '+90–270% урона только в Karakora Town'),
    ('Mangekyō Eye', 0, '', 0, '', 0, '', 0, 0, 'Удваивает горение (100% за 10 т. → 200% за 20 т.); с обновления 18 — на любой тип урона'),
]
RELIC_FIRST = 5
RELIC_LAST = RELIC_FIRST + 1 + (len(RELICS) - 1) * 3 + 10 - 1   # + 10 пустых строк под свои реликвии
# Усиление DoT от реликвий: (+% урона DoT, какой DoT). Eternal Flame — горение длится вдвое дольше = ×2 урона горения
RELIC_DOT = {'Infernal Gaze': (100, 'Горение'), 'Mangekyō Eye': (100, 'Горение')}
# PEN реликвий (снижает сопротивление врага): (значение, для типа). Где PEN — один из случайных роллов, по умолчанию 0
RELIC_PEN = {'Endless Blades': (50, 'Физ'), 'Black Blade: Autumn Water': (50, 'Физ')}
# Периодический бонус-удар: (раз в N с, +% урона). Miracle Timepiece «Final Hour»: каждые 30–50 с следующая
# МАГИЧЕСКАЯ атака +70–130% чистым уроном → среднее 40 с и 100%
RELIC_CLOCK = {'Miracle Timepiece': (40, 100)}
# PWR реликвий по умолчанию 0: у всех реликвий PWR — один из случайных роллов (вместо урона/PEN), вписывается свой
RELIC_PWR = {}
RELIC_COPIES = 3      # каждая реликвия в 3 экземплярах: «X», «X #2», «X #3» — разные роллы/стихии на разных юнитах


def relic_rows():
    """Строки листа «Реликвии»: «Нет», затем каждая реликвия в RELIC_COPIES экземплярах."""
    rows = [RELICS[0]]
    for t in RELICS[1:]:
        for i in range(1, RELIC_COPIES + 1):
            rows.append((t[0] if i == 1 else f'{t[0]} #{i}',) + t[1:])
    return rows


def relic_base(name):
    return re.sub(r' #\d+$', '', name or '')


def clean(s):
    if not isinstance(s, str):
        return ''
    s = re.sub(r'<br\s*/?>', '; ', s)
    s = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]*)\]\]', r'\1', s)
    s = re.sub(r'\{\{[^}]*\}\}', '', s)
    s = re.sub(r'<[^>]+>', '', s)
    return re.sub(r'\s+', ' ', s).strip(' ;')


def num(v):
    if isinstance(v, str):          # на вики встречаются числа строкой: Ticks = '3'
        try:
            v = float(v)
        except ValueError:
            return None
    return round(float(v), 4) if isinstance(v, (int, float)) and not isinstance(v, bool) else None


def load():
    data = json.load(open(os.path.join(ROOT, 'data', 'data.json'), encoding='utf-8'))
    aoe = json.load(open(os.path.join(ROOT, 'data', 'aoe.json'), encoding='utf-8'))
    units = []
    for u in data.values():
        if not isinstance(u, dict) or u.get('rarity') not in RARITY_RU or not num(u.get('cost')):
            continue  # призываемые помощники без цены и редкости
        rows = []
        dmg, spa, rng = num(u.get('damage')) or 0, num(u.get('attack_cooldown')) or 0, num(u.get('range')) or 0
        atk_id = u.get('primary_attack_no_upgrades')
        total = num(u['cost'])
        farm = num(u.get('farm_amount'))
        steps = [{'cost': u['cost'], 'note': u.get('note')}] + [x for x in (u.get('upgrade') or []) if isinstance(x, dict)]
        if u['name'] in STATS_OVERRIDE:
            ov = STATS_OVERRIDE[u['name']]
            dmg, spa, rng, total = ov[0][1], ov[0][2], ov[0][3], ov[0][0]
            steps = [{'cost': ov[0][0]}] + [{'cost': c, 'damage': d, 'attack_cooldown': s, 'range': g} for c, d, s, g in ov[1:]]
        for i, st in enumerate(steps):
            if i > 0:
                dmg = num(st.get('damage')) if num(st.get('damage')) is not None else dmg
                spa = num(st.get('attack_cooldown')) if num(st.get('attack_cooldown')) is not None else spa
                rng = num(st.get('range')) if num(st.get('range')) is not None else rng
                atk_id = st.get('primary_attack') or atk_id
                total += num(st.get('cost')) or 0
                farm = num(st.get('farm_amount')) or farm
            atk = aoe.get(atk_id) if isinstance(aoe.get(atk_id), dict) else {}
            atype = (atk.get('AOE_TYPE') or '').replace('Aoe (', 'AoE (') or '(нет данных)'
            # DoT переносится с прошлой атаки, если у новой он не указан — так его показывает модуль вики
            # (Berserker (Rage): «Beast of Darkness» с апгрейда 8 без Effect, а на странице кровотечение есть)
            if isinstance(atk.get('Effect'), dict):
                eff = atk['Effect']
            elif i == 0:
                eff = {}
            hits = num(st.get('hits')) or num(atk.get('Hits')) or 1
            note = '; '.join(x for x in (clean(st.get('note')), clean(st.get('note2'))) if x)
            ticks, mult = num(eff.get('Ticks')) or 0, num(eff.get('Multiplier')) or 0
            kind = DOT_RU.get(eff.get('Name'), eff.get('Name') or '')
            label = ''
            if kind:
                shown = 'Чёрное пламя' if kind == 'Горение' and u['name'] in BLACK_BURN else kind
                label = f'{shown} {ticks * mult:.0%} / {ticks:g} т.'
            rows.append(dict(upg=i, step=num(st.get('cost')) or 0, total=total, dmg=dmg, spa=spa, rng=rng,
                             atype=atype, hits=hits, eff=label, dotkind=kind, ticks=ticks, mult=mult, note=note))
        # пассивки = особые эффекты атак на всех апгрейдах
        passives, pas_pct = [], 0
        for aid in [u.get('primary_attack_no_upgrades')] + [x.get('primary_attack') for x in steps[1:]]:
            se = (aoe.get(aid) or {}).get('Special_Effect') if isinstance(aoe.get(aid), dict) else None
            if isinstance(se, dict) and se.get('Name') and se['Name'] not in [p[0] for p in passives]:
                note = clean(((aoe.get('Special_Effect_List') or {}).get(se['Name']) or {}).get('note', ''))
                passives.append((se['Name'], note.split(':', 1)[-1].strip() if ':' in note else note))
                pas_pct = max(pas_pct, PASSIVE_PCT.get(se['Name'], 0))
        pas_crit = pas_cd = pas_dot = 0
        if u['name'] in PASSIVE_NOTES:
            text, pct, pas_crit, pas_cd, pas_dot = PASSIVE_NOTES[u['name']]
            passives.append(('Вики', text))
            pas_pct = max(pas_pct, pct)
        # призывы: HP призыва по апгрейдам (переносится с прошлого шага, как статы)
        hp = num(u.get('health')) if u['name'] in SUMMON_RULES else None
        for i, (st, row) in enumerate(zip(steps, rows)):
            if i > 0 and num(st.get('health')) is not None:
                hp = num(st.get('health'))
            rule = SUMMON_RULES.get(u['name'])
            row['summon'] = {k: (v.replace('{hp}', repr(hp or 0)) if isinstance(v, str) else v)
                             for k, v in (rule[0](i, hp or 0) if rule else {}).items()}
            row['own_hits'] = u['name'] not in NO_OWN_HITS
        summ = SUMMON_RULES[u['name']][1] if u['name'] in SUMMON_RULES else SUMMON_NOTES.get(u['name'], '')
        maxdmg = max(r['dmg'] for r in rows)
        role = ('Баффер' if u['name'] in BUFFERS or u.get('aura_buff') else
                'Ферма' if farm else 'Призыв' if u.get('spawn_unit') else
                'Саппорт' if maxdmg == 0 else 'Урон')
        place = 'Холм' if u.get('hill_unit') else 'Гибрид' if u.get('hybrid_placement') else 'Земля'
        feats = [SPECIAL[u['name']]] if u['name'] in SPECIAL else []
        if u.get('evolve'): feats.append('Эволюция: ' + clean((u['evolve'] or {}).get('evolve_text', '')))
        if u.get('active_attack') and isinstance(u['active_attack'], str) and ':' not in u['active_attack']:
            feats.append('Способность: ' + clean(u['active_attack']))
        evo_from = ''
        if isinstance(u.get('evolved'), dict):
            src = data.get(u['evolved'].get('from'))
            evo_from = src['name'] if isinstance(src, dict) else ''
        units.append(dict(name=u['name'], rarity=u['rarity'], dtype=DMG_RU.get(u.get('_base_damage_type'), 'Физ'),
                          role=role, place=place, cap=num(u.get('spawn_cap')) or '', farm=farm or '',
                          crit=num(u.get('crit_chance')) or 0, critdmg=num(u.get('crit_damage')) or '',
                          limited='Да' if isinstance(u.get('limited'), dict) else 'Нет',
                          elem=', '.join(ELEM_RU[k] for k in (u.get('_secondary_damage_types') or {}) if k in ELEM_RU),
                          passives='; '.join(f'{n}: {d}' for n, d in passives), pas_pct=pas_pct,
                          pas_crit=pas_crit, pas_cd=pas_cd, pas_dot=pas_dot, summ=summ,
                          evo_from=evo_from, feats='; '.join(f for f in feats if f.strip(': ')), rows=rows))
    units.sort(key=lambda x: (RARITY_ORDER.index(x['rarity']), x['name'].lower()))
    return units


# ── общие помощники ────────────────────────────────────────────────────
def header(ws, row, titles, fills=None):
    for c, t in enumerate(titles, 1):
        cell = ws.cell(row, c, t)
        cell.fill, cell.font, cell.alignment, cell.border = (fills or {}).get(c, HEAD), WHITE_B, CENTER, BOX
    ws.row_dimensions[row].height = 46


def title(ws, text, hint):
    ws['A1'] = text; ws['A1'].font = TITLE
    ws['A2'] = hint; ws['A2'].font = HINT


def dv_list(ws, formula, rng):
    dv = DataValidation(type='list', formula1=formula, allow_blank=True)
    dv.showDropDown = False   # в openpyxl False = ПОКАЗЫВАТЬ стрелку
    ws.add_data_validation(dv); dv.add(rng)


def dv_number(ws, *ranges):
    """Только число (текст «5.5» с точкой отклоняется с подсказкой) — для таблиц, где формулы берут SUMIFS/N()."""
    dv = DataValidation(type='decimal', operator='between', formula1='-1000000', formula2='1000000', allow_blank=True)
    dv.error = 'Введи число без знака %, дробь — через запятую: 15 или 5,5'
    dv.errorTitle = 'Нужно число'
    dv.showErrorMessage = True
    ws.add_data_validation(dv)
    for rng in ranges:
        dv.add(rng)


def inp(cell, value=None, fmt=None):
    if value is not None: cell.value = value
    cell.fill, cell.border = YELLOW, BOX
    if fmt: cell.number_format = fmt


def autofit(ws, header_row, widths, wrap_cols=(), cap=60):
    """Ширина = самый длинный текст в столбце (заголовок построчно, данные-константы).
    widths — минимальные ширины для столбцов с формулами; wrap_cols — длинный текст переносится."""
    best = {}
    for row in ws.iter_rows(min_row=header_row):
        for c in row:
            v = c.value
            if v is None or (isinstance(v, str) and v.startswith('=')):
                continue
            if isinstance(v, float):
                s = f'{v:,.1f}'
            else:
                s = str(v)
            n = max(len(x) for x in s.split('\n'))
            if c.row == header_row:
                n = max(len(w) for x in s.split('\n') for w in x.split(' ')) + 2
            best[c.column] = max(best.get(c.column, 0), n)
    for col in range(1, ws.max_column + 1):
        letter = get_column_letter(col)
        w = max(best.get(col, 0) * 1.1 + 2, widths.get(letter, 6))
        ws.column_dimensions[letter].width = min(w, cap if letter not in wrap_cols else wrap_cols[letter])


def rarity_cf(ws, rng):
    for name, color in RARITY_FILL.items():
        ws.conditional_formatting.add(rng, CellIsRule(operator='equal', formula=[f'"{name}"'],
                                                      fill=PatternFill('solid', fgColor=color)))


def scale(ws, rng, kind='percentile'):
    if kind == 'percentile':
        rule = ColorScaleRule(start_type='percentile', start_value=5, start_color='F8696B',
                              mid_type='percentile', mid_value=50, mid_color='FFEB84',
                              end_type='percentile', end_value=95, end_color='63BE7B')
    else:
        rule = ColorScaleRule(start_type='min', start_color='F8696B', mid_type='percentile', mid_value=50,
                              mid_color='FFEB84', end_type='max', end_color='63BE7B')
    ws.conditional_formatting.add(rng, rule)


def link(cell, sheet, addr='A1'):
    cell.hyperlink = Hyperlink(ref=cell.coordinate, location=f"'{sheet}'!{addr}")
    cell.font = LINK


# ── Настройки ──────────────────────────────────────────────────────────
S = "'Настройки'!"
LVL, CRIT, DOT = S + '$B$6', S + '$B$7', S + '$B$8'
GD, GS, GC, GR = S + '$I$7', S + '$B$10', S + '$B$11', S + '$B$12'   # GD = общий бонус + Limit Break отряда
RES_P, RES_M = S + '$I$5', S + '$I$6'
TICK = f'MAX(0.01,N({S}$I$8))'   # интервал тика DoT, с (вики его не указывает — по умолчанию 1); 0 не даёт #DIV/0!
KPS = f'MAX(0,N({S}$I$9))'        # врагов убивается в секунду — для призывов «за убийства»; минус → 0
WALK = f'MAX(0,N({S}$I$10))'      # время пути призыва до врага, с
PWRP = f'N({S}$I$11)'             # +% урона за 1 PWR реликвии
SUMB = S + '$I$38'         # бафы призывов (вид «Призыв», Zombie (Risen)) из «Настроек»
BRAM = S + '$I$39'         # урон призывов-таранов: физ. + «Все» бафы, кроме Idol
AOE = S + '$A$16:$B$21'
BF, BM, BT, BS, BR, BC, DISC = (S + f'$I${r}' for r in range(25, 32))
BUFF_FIRST, BUFF_LAST = 25, 54
BUFF_NAMES = f'{S}$A${BUFF_FIRST}:$A${BUFF_LAST}'
BUFF_KIND = f'{S}$B${BUFF_FIRST}:$B${BUFF_LAST}'
BUFF_VAL = f'{S}$C${BUFF_FIRST}:$C${BUFF_LAST}'
BUFF_WHO = f'{S}$D${BUFF_FIRST}:$D${BUFF_LAST}'
SIT = S + '$B$13'
BUFF_ROW = {b[0]: BUFF_FIRST + i for i, b in enumerate(BUFFS)}
NSG = {'Урон': S + '$I$36', 'SPA': S + '$I$37'}     # «не складываются» среди активных бафов «Настроек»


def nostack_expr(kind, on, val):
    """Величина, которую надо вычесть, если обе группы NO_STACK вида kind включены (on(name) — условие, val(name) — %)."""
    for k, ga, gb in NO_STACK:
        if k == kind:
            any_a, any_b = ('OR(' + ','.join(on(n) for n in g) + ')' for g in (ga, gb))
            max_a, max_b = ('MAX(' + ','.join(f'IF({on(n)},{val(n)},0)' for n in g) + ')' for g in (ga, gb))
            return f'IF(AND({any_a},{any_b}),MIN({max_a},{max_b}),0)'
    return '0'
DOTG = {k: S + f'$I${32 + i}' for i, k in enumerate(DOT_KINDS)}   # итоги активных усилителей DoT


def dot_global(kind_cell):
    """Активные (из «Настроек») усилители DoT для вида DoT в ячейке kind_cell."""
    expr = '0'
    for k in reversed(DOT_KINDS):
        expr = f'IF({kind_cell}="{k}",{DOTG[k]},{expr})'
    return expr

TR = "'Трейты'!"
TRAIT_COL = {k: f'{TR}${c}${TRAIT_FIRST}:${c}${TRAIT_LAST}' for k, c in zip(('name', 'd', 's', 'r'), 'ABCD')}
RL = "'Реликвии'!"
RELIC_COL = {k: f'{RL}${c}${RELIC_FIRST}:${c}${RELIC_LAST}'
             for k, c in zip(('name', 'd1', 't1', 'd2', 't2', 'c', 'ct', 'cd', 'sit', 'dot', 'dotk', 'pen', 'penk',
                              'clkn', 'clkp', 'pwr', 'pwrk'), 'ABCDEFGHIJKLMNOPQ')}
ELEM_LIST = '"Все,Физ,Маг,' + ','.join(ELEM_RU.values()) + '"'


def mods_formulas(trait, relic, dtype, elem):
    """Формулы бонусов трейта и реликвии для юнита.
    trait/relic — ячейки с названиями, dtype/elem — ячейки с типом урона и стихиями юнита."""
    def tr(k):
        return f'IFERROR(INDEX({TRAIT_COL[k]},MATCH({trait},{TRAIT_COL["name"]},0)),0)'

    m = f'MATCH({relic},{RELIC_COL["name"]},0)'

    def rl(k):
        return f'INDEX({RELIC_COL[k]},{m})'

    def fits(t):  # реликвия подходит: тип пустой → нет; «Все», тип урона или стихия юнита → да
        return f'AND({t}<>"",OR({t}="Все",{t}={dtype},ISNUMBER(SEARCH({t},{elem}))))'
    return {
        'tD': tr('d'), 'tS': tr('s'), 'tR': tr('r'),
        'rD': f'IFERROR(IF({fits(rl("t1"))},N({rl("d1")}),0)+IF({fits(rl("t2"))},N({rl("d2")}),0)'
              f'+IF({SIT}="Да",N({rl("sit")}),0),0)',
        'rC': f'IFERROR(IF(OR({rl("ct")}="",{fits(rl("ct"))}),N({rl("c")}),0),0)',
        'rCD': f'IFERROR(N({rl("cd")}),0)',
        # PWR: + «уровни» → урон × (1 + PWR × %), если тип/стихия подходят
        'rPwr': f'IFERROR(IF({fits(rl("pwrk"))},N({rl("pwr")}),0),0)',
        # часы: % урона в секунду = бонус% / период (только магическим юнитам)
        'rClk': f'IFERROR(IF(AND({dtype}="Маг",N({rl("clkn")})>0),N({rl("clkp")})/N({rl("clkn")}),0),0)',
        'rDot': f'IFERROR(N({rl("dot")}),0)',
        'rDotK': f'IFERROR({rl("dotk")}&"","")',
        # сопротивление врага: урон × 100 / (100 + сопр. − PEN), чистый урон игнорирует
        'resm': f'IF({dtype}="Чистый",1,100/(100+MAX(0,IF({dtype}="Физ",{RES_P},IF({dtype}="Маг",{RES_M},0))'
                f'-IFERROR(IF(OR({rl("penk")}="Все",{rl("penk")}={dtype}),N({rl("pen")}),0),0))))',
    }


def relic_dot(val, kind, dot_kind):
    """Усиление DoT от реликвии, если её «Какой DoT» = Все или совпадает с DoT атаки."""
    return f'IF(AND({dot_kind}<>"",OR({kind}="Все",{kind}={dot_kind})),{val},0)'


def sheet_traits(wb):
    ws = wb.create_sheet('Трейты')
    ws.sheet_properties.tabColor = 'BF8F00'
    title(ws, 'Трейты', 'Цифры с вики (страница Traits). Всё жёлтое можно менять; пустые строки — для своих (например, двойной трейт: значения складываются)')
    header(ws, 4, ['Трейт', 'Урон, %', 'Снижение\nSPA, %', 'Радиус, %', 'Пояснение'])
    for r in range(TRAIT_FIRST, TRAIT_LAST + 1):
        t = TRAITS[r - TRAIT_FIRST] if r - TRAIT_FIRST < len(TRAITS) else (None, None, None, None, 'свой трейт — впиши')
        for c, v in enumerate(t[:4], 1):
            inp(ws.cell(r, c), v)
        ws.cell(r, 5, t[4]).font = HINT
    for col, w in zip('ABCDE', (24, 10, 11, 10, 80)):
        ws.column_dimensions[col].width = w
    dv_number(ws, f'B{TRAIT_FIRST}:D{TRAIT_LAST}')
    ws['A36'] = 'Урон трейта — отдельный множитель: урон × (1 + бафы) × (1 + трейт). Unique (×4) с Commander 100% даёт ×8.'
    ws['A36'].font = HINT
    ws.freeze_panes = 'B5'
    return ws


def sheet_relics(wb):
    ws = wb.create_sheet('Реликвии')
    ws.sheet_properties.tabColor = 'BF8F00'
    title(ws, 'Реликвии', 'Каждая реликвия — в 3 экземплярах (#2, #3): настрой их по-разному (свои роллы, стихия) и выдай разным юнитам. '
          'По умолчанию максимальный ролл. Свои реликвии — в пустые строки внизу. Ставятся только на Легендарных и выше')
    header(ws, 4, ['Реликвия', 'Урон, %', 'Для типа', 'Урон 2, %', 'Для типа 2', 'Крит-шанс, %', 'Крит для',
                   '+Крит-урон, %', 'Ситуативный, %', 'Усиление\nDoT, %', 'Какой\nDoT', 'PEN', 'PEN для',
                   'Бонус-удар\nраз в N с', 'Бонус-удар,\n+% урона', 'PWR', 'PWR для', 'Пояснение (диапазон роллов)'])
    rows = relic_rows()
    for r in range(RELIC_FIRST, RELIC_LAST + 1):
        t = rows[r - RELIC_FIRST] if r - RELIC_FIRST < len(rows) else (None,) + (None,) * 8 + ('своя реликвия — впиши',)
        base = relic_base(t[0])
        empty = (0, None) if t[0] else (None, None)
        dot = RELIC_DOT.get(base, empty)
        pen = RELIC_PEN.get(base, empty)
        clk = RELIC_CLOCK.get(base, (0, 0) if t[0] else (None, None))
        pwr = RELIC_PWR.get(base, empty)
        for c, v in enumerate(t[:9] + dot + pen + clk + pwr, 1):
            # формат «General»: «0.##» в LibreOffice показывал целые как «4,»
            inp(ws.cell(r, c), v if v != '' else None)
        ws.cell(r, 18, t[9]).font = HINT
        if t[0] and base != t[0]:
            ws.cell(r, 1).font = Font(color='595959')      # копии #2/#3 — серым, чтобы видеть группы
    dv_list(ws, ELEM_LIST, f'C{RELIC_FIRST}:C{RELIC_LAST}')
    dv_list(ws, ELEM_LIST, f'E{RELIC_FIRST}:E{RELIC_LAST}')
    dv_list(ws, ELEM_LIST, f'G{RELIC_FIRST}:G{RELIC_LAST}')
    dv_list(ws, '"Все,' + ','.join(DOT_KINDS) + '"', f'K{RELIC_FIRST}:K{RELIC_LAST}')
    dv_list(ws, '"Физ,Маг,Все"', f'M{RELIC_FIRST}:M{RELIC_LAST}')
    dv_list(ws, ELEM_LIST, f'Q{RELIC_FIRST}:Q{RELIC_LAST}')
    dv_number(ws, *(f'{c}{RELIC_FIRST}:{c}{RELIC_LAST}' for c in 'BDFHIJLNOP'))
    for col, w in zip('ABCDEFGHIJKLMNOPQR', (28, 9, 10, 9, 10, 11, 9, 11, 12, 10, 13, 7, 9, 11, 11, 7, 10, 95)):
        ws.column_dimensions[col].width = w
    notes = ['«Для типа»: Физ / Маг — по типу урона юнита; Огонь, Вода, Шторм и т.д. — если у юнита есть эта стихия (столбец «Стихии» на «Юнитах»); Все — всем.',
             'PEN снижает сопротивление врага: урон × 100 / (100 + сопротивление − PEN). Сопротивление врага задаётся в «Настройках» (по умолчанию 0 — PEN ни на что не влияет).',
             'PWR (вики: «повышает уровень», растёт от уровня отряда): считается как + уровни → урон × (1 + PWR × «1 PWR = %» из «Настроек», по умолчанию 1,75%). '
             'У Steel Shiv / Amplifying Codex и рандомных роллов PWR — вместо урона или PEN: впиши свой ролл.',
             '«Ситуативный» учитывается, только если в «Настройках» включены ситуативные бонусы (рейды, особые локации, типы врагов).',
             'Часы (Miracle Timepiece, «Final Hour»): каждые 30–50 с следующая МАГИЧЕСКАЯ атака наносит +70–130% урона чистым. '
             'По умолчанию среднее: раз в 40 с, +100%. Это добавляет урон × 100% / 40 с в секунду — только магическим юнитам. '
             'Впиши свой ролл в «Бонус-удар». Стихию из ролла «+2–8% одной стихии» выбери в «Для типа 2».']
    for i, t in enumerate(notes, RELIC_LAST + 2):
        ws.cell(i, 1, t).font = HINT
    ws.freeze_panes = 'B5'
    return ws


def sheet_settings(wb):
    ws = wb.create_sheet('Настройки')
    ws.sheet_properties.tabColor = 'BF8F00'
    title(ws, 'Настройки расчёта', 'Жёлтые ячейки меняешь ты — все листы пересчитываются сами')
    for col, w in zip('ABCDEFGHIJ', (40, 16, 14, 10, 11, 62, 3, 36, 12, 50)):
        ws.column_dimensions[col].width = w

    ws['A3'] = 'ОБЩИЕ'; ws['A3'].font = BOLD
    rows = [
        ('Уровень юнитов (1 / 100 / 110 / Свой)', '1', None, '100 ур. = урон ×9,204; 110 (Limit Break) = ещё +19%'),
        ('Свой множитель урона от уровня', 1, NUM2, 'работает, если выше выбрано «Свой»'),
        ('→ Множитель урона от уровня', f'=IF(OR(B4=110,B4="110"),{LVL110},IF(OR(B4=100,B4="100"),{LVL100},'
                                        f'IF(B4="Свой",B5,1)))', '0.000', 'считается сам'),
        ('Множитель крита по умолчанию', 1.5, NUM2, 'вики: крит = ×1,5 (у кого-то свой — он в данных)'),
        ('Учитывать DoT (кровотечение, горение, яд)', 'Да', None,
         'DoT за атаку = урон × множитель × тики; бафы саппортов усиливают только КРОВОТЕЧЕНИЕ (горение — от урона без бафов)'),
        ('Общий бонус урона, %', 0, '0', 'всем юнитам сразу (трейты, реликвии, проклятия — у юнита, не сюда)'),
        ('Общее снижение SPA, %', 0, '0', '10 = атака на 10% чаще'),
        ('Общий бонус крит-шанса, %', 0, '0', 'прибавляется к шансу из вики'),
        ('Общий бонус радиуса, %', 0, '0', ''),
        ('Ситуативные бонусы реликвий (рейды, локации)', 'Нет', None, '«Да» — учитывать столбец «Ситуативный %» на листе «Реликвии»'),
    ]
    for i, (label, val, fmt, note) in enumerate(rows, 4):
        ws.cell(i, 1, label).border = BOX
        c = ws.cell(i, 2, val)
        if i == 6:
            c.font, c.border, c.number_format = BOLD, BOX, fmt
        else:
            inp(c, fmt=fmt)
        ws.cell(i, 3, note).font = HINT
    dv_list(ws, '"1,100,110,Свой"', 'B4')
    dv_number(ws, 'B5', 'B7', 'B9:B12', 'B16:B21', f'C{BUFF_FIRST}:C{BUFF_LAST}', 'I4:I6', 'I8:I11')

    ws['H3'] = 'ДОПОЛНИТЕЛЬНО'; ws['H3'].font = BOLD
    extra = [('Юнитов с Limit Break в отряде (0–6)', 0, 'вики: +5% урона всем твоим юнитам за каждого, до +30%'),
             ('Сопротивление врага к физ. урону', 0, 'урон × 100 / (100 + сопр. − PEN); 0 = не учитывать'),
             ('Сопротивление врага к маг. урону', 0, 'чистый урон сопротивление игнорирует')]
    for i, (label, val, note) in enumerate(extra, 4):
        ws.cell(i, 8, label).border = BOX
        inp(ws.cell(i, 9), val, '0')
        ws.cell(i, 10, note).font = HINT
    ws['H7'] = '→ Общий бонус урона итог, %'; ws['H7'].border = BOX
    # множители, а не сумма: в игре 256K = база × ранг × проклятие × (1 + 5% × LB) — сверено с игрой (Shinobi (Eternal))
    ws['I7'] = '=((1+N(B9)/100)*(1+0.05*MIN(6,MAX(0,N(I4))))-1)*100'
    ws['I7'].font, ws['I7'].border, ws['I7'].number_format = BOLD, BOX, '0.#'
    ws['J7'] = 'общий бонус × Limit Break отряда (множители)'; ws['J7'].font = HINT
    ws['H8'] = 'Интервал тика DoT, с'; ws['H8'].border = BOX
    inp(ws['I8'], 1)
    ws['J8'] = 'для «Урона за время боя»; вики его не указывает — по умолчанию 1 с'; ws['J8'].font = HINT
    ws['H9'] = 'Врагов убивается в секунду'; ws['H9'].border = BOX
    inp(ws['I9'], 1)
    ws['J9'] = 'для призывов «за убийства»: Supreme Being, дроны Iron Knight, угри Elyssia'; ws['J9'].font = HINT
    ws['H10'] = 'Время пути призыва до врага, с'; ws['H10'].border = BOX
    inp(ws['I10'], 5)
    ws['J10'] = 'медузы Elyssia ждут, пока дойдут до врага; урон призывов за бой начинается через это время'; ws['J10'].font = HINT
    ws['H11'] = '1 PWR реликвии = +% урона'; ws['H11'].border = BOX
    inp(ws['I11'], 1.75)
    ws['J11'] = 'вики: PWR «повышает уровень»; +1 уровень между 100 и 110 ≈ +1,75% урона'; ws['J11'].font = HINT
    dv_list(ws, '"Да,Нет"', 'B8')
    dv_list(ws, '"Да,Нет"', 'B13')

    ws['A14'] = 'ЦЕЛЕЙ ПОД АТАКОЙ (AoE)'; ws['A14'].font = BOLD
    ws['C14'] = 'Сколько врагов в среднем попадает под удар. 1 = честный DPS по одной цели'; ws['C14'].font = HINT
    for c, t in enumerate(('Тип атаки', 'Целей'), 1):
        x = ws.cell(15, c, t); x.fill, x.font, x.border = SUB, BOLD, BOX
    for r, t in enumerate(('Single', 'AoE (Circle)', 'AoE (Cone)', 'AoE (Line)', 'AoE (Full)', '(нет данных)'), 16):
        ws.cell(r, 1, t).border = BOX
        inp(ws.cell(r, 2), 1, '0.0')

    ws['A23'] = 'БАФЫ ОТ САППОРТОВ'; ws['A23'].font = BOLD
    ws['C23'] = ('«Активен = Да» — баф действует на «Юнитах», «Апгрейдах» и «Команде». '
                 'В «Сравнении» бафы выбираются отдельно в каждой строке. Урон-бафы складываются (Commander + Blossom = ×2,1). '
                 'Вид «DoT» усиливает урон от DoT: в «На кого» — какой DoT, значение ×5 = +400%')
    ws['C23'].font = HINT
    for c, t in enumerate(('Баффер', 'Что даёт', 'Значение, %', 'На кого', 'Активен', 'Откуда цифра'), 1):
        x = ws.cell(24, c, t); x.fill, x.font, x.border, x.alignment = SUB, BOLD, BOX, CENTER
    for r in range(BUFF_FIRST, BUFF_LAST + 1):
        b = BUFFS[r - BUFF_FIRST] if r - BUFF_FIRST < len(BUFFS) else ('', '', None, '', '')
        inp(ws.cell(r, 1), b[0] or None); inp(ws.cell(r, 2), b[1] or None)
        inp(ws.cell(r, 3), b[2], '0'); inp(ws.cell(r, 4), b[3] or None)
        inp(ws.cell(r, 5), 'Нет'); ws.cell(r, 6, b[4] or ('свой баф — впиши' if not b[0] else '')).font = HINT
    rng = lambda col: f'${col}${BUFF_FIRST}:${col}${BUFF_LAST}'
    dv_list(ws, '"Урон,SPA,Радиус,Крит,Скидка,DoT,Призыв"', f'B{BUFF_FIRST}:B{BUFF_LAST}')
    dv_list(ws, '"Физ,Маг,Все,' + ','.join(DOT_KINDS) + '"', f'D{BUFF_FIRST}:D{BUFF_LAST}')
    dv_list(ws, '"Да,Нет"', f'E{BUFF_FIRST}:E{BUFF_LAST}')
    ws.conditional_formatting.add(f'A{BUFF_FIRST}:E{BUFF_LAST}', FormulaRule(formula=[f'$E{BUFF_FIRST}="Да"'], fill=GREEN))

    def sumifs(kind, who=None):
        f = f'SUMIFS({rng("C")},{rng("B")},"{kind}",{rng("E")},"Да"'
        return f + (f',{rng("D")},"{who}")' if who else ')')
    ws['H24'] = 'ИТОГО АКТИВНЫХ БАФОВ'; ws['H24'].font = BOLD
    # «не складываются» (NO_STACK): если включены обе группы — меньшая вычитается; величины в I36 (урон), I37 (SPA)
    active = lambda name: f'$E${BUFF_ROW[name]}="Да"'
    totals = [('Урон физ. юнитам, %', f'={sumifs("Урон","Физ")}+{sumifs("Урон","Все")}-$I$36'),
              ('Урон маг. юнитам, %', f'={sumifs("Урон","Маг")}+{sumifs("Урон","Все")}-$I$36'),
              ('Урон юнитам с чистым уроном, %', f'={sumifs("Урон","Все")}-$I$36'),
              ('Снижение SPA, %', f'={sumifs("SPA")}-$I$37'),
              ('Радиус, %', f'={sumifs("Радиус")}'),
              ('Крит-шанс, %', f'={sumifs("Крит")}'),
              ('Скидка на апгрейды, %', f'=MIN(90,{sumifs("Скидка")})')]
    totals += [(f'Усиление DoT: {k.lower()}, %', f'={sumifs("DoT", k)}+{sumifs("DoT", "Все")}') for k in DOT_KINDS]
    for kind, label in (('Урон', 'Не складываются: Blossom ↔ Idol'), ('SPA', 'Не складываются: Trickster ↔ Priest')):
        totals.append((label, '=' + nostack_expr(kind, active, lambda n: f'$C${BUFF_ROW[n]}')))
    totals.append(('Урон призывам (Zombie (Risen)), %', f'={sumifs("Призыв")}'))       # I38
    totals.append(('Урон призывов-таранов (физ., без Idol), %', f'={sumifs("Урон","Физ")}+{sumifs("Урон","Все")}'
                   + ''.join(f'-IF($E${BUFF_ROW[n]}="Да",$C${BUFF_ROW[n]},0)' for n in RAM_EXCLUDE)))   # I39
    for r, (label, f) in enumerate(totals, 25):
        ws.cell(r, 8, label).border = BOX
        c = ws.cell(r, 9, f); c.font, c.border, c.number_format = BOLD, BOX, '0'
    ws.freeze_panes = 'A4'
    return ws


# ── Юниты: столбцы задаются ключами, буквы считаются ───────────────────
UNIT_SPEC = [
    ('name', 'Юнит'), ('mine', 'Есть\nу меня'), ('idx', '№\n(исходный\nпорядок)'), ('rnum', '№\nредк.'), ('rarity', 'Редкость'),
    ('tier', 'Тир\nпо DPS'), ('tierv', 'Тир по\nвыгоде'), ('dtype', 'Тип\nурона'), ('elem', 'Стихии'), ('role', 'Роль'),
    ('place', 'Размещение'), ('atype', 'Тип атаки\n(макс.)'), ('dot', 'DoT\n(макс. апгрейд)'), ('summ', 'Призыв'),
    ('cap', 'Лимит\nна поле'), ('ups', 'Апгрейдов'),
    ('cost0', 'Цена\nпостановки'), ('costmax', 'Цена до макс.\n(со скидкой)'), ('dmg', 'Урон макс.'),
    ('spa', 'SPA макс.'), ('rng', 'Радиус\nмакс.'), ('sdps', 'DPS призывов\n(макс.)'), ('dps', 'DPS макс.\n(с призывами)'),
    ('dpsk', 'DPS на 1000\n(макс.)'),
    ('best', 'Лучший DPS на\n1000 (любой\nапгрейд)'), ('bestup', 'Выгоднее\nвсего на\nапгрейде №'),
    ('rankv', 'Место по\nвыгоде'),
    ('rankd', 'Место\nпо DPS'), ('dpsall', 'DPS всех копий\n(× лимит)'), ('costall', 'Цена всех\nкопий'),
    ('farm', 'Ферма\n(за волну)'), ('lim', 'Лимитка'), ('evo', 'Эволюция из'), ('feats', 'Особенности'),
    ('passdesc', 'Пассивки (из вики)'),
    ('trait', 'Трейт'), ('relic', 'Реликвия'), ('pas', 'Пассивка,\n+% урона'),
    ('pasc', 'Пассивка,\n+% крит-шанса'), ('pascd', 'Пассивка,\n+% крит-урона'), ('pasdot', 'Пассивка,\n+% к DoT'),
    ('k1s', 'Проклятие 1:\nстат'), ('k1v', 'Проклятие 1:\n%'), ('k2s', 'Проклятие 2:\nстат'), ('k2v', 'Проклятие 2:\n%'),
    ('k3s', 'Проклятие 3:\nстат'), ('k3v', 'Проклятие 3:\n%'), ('k4s', 'Проклятие 4:\nстат'), ('k4v', 'Проклятие 4:\n%'),
    ('cd', 'Свой\n+% урона'), ('cs', 'Свой\n−% SPA'), ('cc', 'Свой\nкрит-шанс, %'), ('note', 'Заметка'),
    ('first', 'стр.1'), ('last', 'стр.N'), ('hd', 'топ DPS'), ('hv', 'топ выгода'), ('hm', 'топ мои'),
    ('tD', 'трейт урон'), ('tS', 'трейт SPA'), ('tR', 'трейт радиус'), ('rD', 'рел. урон'), ('rC', 'рел. крит'),
    ('rCD', 'рел. крит-урон'), ('rDot', 'рел. DoT'), ('rDotK', 'рел. какой DoT'), ('resm', 'множ. сопротивления'),
    ('rClk', 'рел. часы %/с'), ('rPwr', 'рел. PWR'),
    # жёлтые %-поля, переведённые в число (понимают 12.3 / 12,3 / 12.3% / текст), и итоги проклятий
    ('vcd', 'свой урон %'), ('vcs', 'своё SPA %'), ('vcc', 'свой крит %'), ('vpas', 'пасс. урон %'),
    ('vpasc', 'пасс. крит %'), ('vpascd', 'пасс. крит-урон %'), ('vpasdot', 'пасс. DoT %'),
    ('curD', 'прокл. урон %'), ('curS', 'прокл. SPA %'), ('curR', 'прокл. радиус %'),
]
UC = {k: get_column_letter(i) for i, (k, _) in enumerate(UNIT_SPEC, 1)}
CURSE_SLOTS = (('k1s', 'k1v'), ('k2s', 'k2v'), ('k3s', 'k3v'), ('k4s', 'k4v'))
UNIT_INPUT = ('mine', 'trait', 'relic', 'pas', 'pasc', 'pascd', 'pasdot') + sum(CURSE_SLOTS, ()) + ('cd', 'cs', 'cc', 'note')
PCT_INPUT = ('pas', 'pasc', 'pascd', 'pasdot', 'cd', 'cs', 'cc') + tuple(v for _, v in CURSE_SLOTS)
PAS_PREFILL = {'pas': 'pas_pct', 'pasc': 'pas_crit', 'pascd': 'pas_cd', 'pasdot': 'pas_dot'}
UNIT_HIDDEN = ('first', 'last', 'hd', 'hv', 'hm', 'tD', 'tS', 'tR', 'rD', 'rC', 'rCD', 'rDot', 'rDotK', 'resm', 'rClk', 'rPwr',
               'vcd', 'vcs', 'vcc', 'vpas', 'vpasc', 'vpascd', 'vpasdot', 'curD', 'curS', 'curR')


def _clean_text(ref):
    """Текст ячейки без %, пробелов (в т.ч. неразрывных), с обычным минусом и точкой вместо запятой."""
    t = f'TRIM({ref}&"")'
    for a, b in (('"%"', '""'), ('_xlfn.UNICHAR(160)', '""'), ('" "', '""'), ('"−"', '"-"'), ('","', '"."')):
        t = f'SUBSTITUTE({t},{a},{b})'
    return t


def pct(ref):
    """Жёлтое %-поле → число процентов. 12.3 → 12.3; ячейка в формате % (набрали «126%», хранится 1,26) → 126;
    текст «9.3» / «9,3%» / «−8» → 9.3 / 9.3 / −8; пусто → 0. Формат ячейки проверяется через CELL("format")."""
    return (f'IFERROR(IF(ISNUMBER({ref}),IF(LEFT(CELL("format",{ref}),1)="P",{ref}*100,{ref}),'
            f'_xlfn.NUMBERVALUE({_clean_text(ref)},".")),0)')


def numf(ref, blank='""'):
    """Формула: число из ячейки, даже если введено текстом («2», «5,5»); пусто/мусор → blank."""
    return (f'IF(ISNUMBER({ref}),{ref},IF(TRIM({ref}&"")="",{blank},'
            f'IFERROR(_xlfn.NUMBERVALUE({_clean_text(ref)},"."),{blank})))')
def upg_at(c, r, col):
    """Значение «Апгрейдов» на максимальном апгрейде юнита (номер строки — в скрытом «стр.N» этой строки)."""
    return f"=INDEX({A_}${col}:${col},${c['last']}{r})"


def upg_range(c, r, col):
    """Диапазон всех апгрейдов юнита на «Апгрейдах» по столбцу col (INDEX:INDEX — не ломается при сортировке)."""
    return f"INDEX({A_}${col}:${col},${c['first']}{r}):INDEX({A_}${col}:${col},${c['last']}{r})"


def tier_formula(col, r, end):
    rng = f'${col}$5:${col}${end}'
    p = f'(COUNTIF({rng},">0")-RANK({col}{r},{rng}))/MAX(1,COUNTIF({rng},">0")-1)'
    return f'=IF(N({col}{r})<=0,"—",LOOKUP({p},{{0,0.15,0.4,0.7,0.9}},{{"D","C","B","A","S"}}))'


U = "'Юниты'!"
A_ = "'Апгрейды'!"


def ucol(key, end):
    """Абсолютный диапазон столбца на «Юнитах» по строкам данных."""
    return f"{U}${UC[key]}$5:${UC[key]}${end}"


def sheet_units(wb, units):
    ws = wb.create_sheet('Юниты')
    ws.sheet_properties.tabColor = '1F3864'
    title(ws, f'Все юниты Anime Adventures — {len(units)} шт.',
          'Стрелки в заголовках — сортировка и фильтр (вернуть порядок — сортировка по «№»). Имя юнита — ссылка на его апгрейды. '
          'Жёлтые столбцы — твои правки (влияют на все листы)')
    fills = {i: HEAD_DPS for i, (k, _) in enumerate(UNIT_SPEC, 1) if k in ('dps', 'dpsk', 'best')}
    fills.update({i: HEAD_INPUT for i, (k, _) in enumerate(UNIT_SPEC, 1) if k in UNIT_INPUT})
    header(ws, 4, [t for _, t in UNIT_SPEC], fills)
    n = len(units)
    end = 4 + n
    c = UC
    for i, u in enumerate(units):
        r = 5 + i
        f, l = u['first'], u['last']
        last = u['rows'][-1]
        vals = {
            'name': u['name'], 'idx': i + 1, 'rnum': RARITY_ORDER.index(u['rarity']) + 1, 'rarity': RARITY_RU[u['rarity']],
            # тир = доля юнитов С УРОНОМ, которых этот юнит обходит (саппорты с DPS 0 не размывают шкалу)
            'tier': '—' if u['name'] in SPECIAL else tier_formula(c['dps'], r, end),
            'tierv': '—' if u['name'] in SPECIAL else tier_formula(c['dpsk'], r, end),
            'dtype': u['dtype'], 'role': u['role'], 'place': u['place'], 'atype': last['atype'],
            'cap': u['cap'], 'ups': len(u['rows']) - 1, 'cost0': u['rows'][0]['total'],
            # строки «Апгрейдов» берутся из стр.1 / стр.N ЭТОЙ ЖЕ строки — они переезжают вместе с юнитом при сортировке
            'costmax': upg_at(c, r, 'Q'), 'dmg': upg_at(c, r, 'R'), 'spa': upg_at(c, r, 'S'), 'rng': upg_at(c, r, 'T'),
            'dps': upg_at(c, r, 'Z'), 'dpsk': upg_at(c, r, 'AA'), 'sdps': upg_at(c, r, 'AJ'), 'summ': u['summ'] or None,
            'best': f'=MAX({upg_range(c, r, "AA")})',
            'bestup': f'=IF({c["best"]}{r}>0,INDEX({upg_range(c, r, "B")},MATCH({c["best"]}{r},{upg_range(c, r, "AA")},0)),"")',
            'rankv': '—' if u['name'] in SPECIAL else
                     f'=IF({c["dpsk"]}{r}>0,RANK({c["dpsk"]}{r},${c["dpsk"]}$5:${c["dpsk"]}${end}),"")',
            'rankd': '—' if u['name'] in SPECIAL else
                     f'=IF({c["dps"]}{r}>0,RANK({c["dps"]}{r},${c["dps"]}$5:${c["dps"]}${end}),"")',
            # у 20 юнитов лимит на поле в данных не указан — тогда «—», а не 0
            'dpsall': f'=IF(N({c["cap"]}{r})=0,"—",{c["dps"]}{r}*{c["cap"]}{r})',
            'costall': f'=IF(N({c["cap"]}{r})=0,"—",{c["costmax"]}{r}*{c["cap"]}{r})',
            'farm': u['farm'] or None, 'lim': u['limited'], 'evo': u['evo_from'] or None, 'feats': u['feats'] or None,
            'first': f, 'last': l,
            'hd': -1 if u['name'] in SPECIAL else f'=IF({c["dps"]}{r}>0,{c["dps"]}{r}-{c["idx"]}{r}/1E9,-1)',
            'hv': -1 if u['name'] in SPECIAL else f'=IF({c["dpsk"]}{r}>0,{c["dpsk"]}{r}-{c["idx"]}{r}/1E9,-1)',
            'hm': f'=IF(AND({c["mine"]}{r}="Да",{c["dps"]}{r}>0),{c["dps"]}{r}-{c["idx"]}{r}/1E9,-1)',
            'elem': u['elem'] or None, 'passdesc': u['passives'] or None, 'dot': last['eff'] or None,
        }
        vals.update({k: '=' + f for k, f in mods_formulas(f'{c["trait"]}{r}', f'{c["relic"]}{r}',
                                                          f'{c["dtype"]}{r}', f'{c["elem"]}{r}').items()})
        for v, src in (('vcd', 'cd'), ('vcs', 'cs'), ('vpas', 'pas'), ('vpasc', 'pasc'), ('vpascd', 'pascd'),
                       ('vpasdot', 'pasdot')):
            vals[v] = '=' + pct(f'{c[src]}{r}')
        cc_ref = f'{c["cc"]}{r}'
        # свой крит: пусто ИЛИ не число → крит из вики (не 0)
        vals['vcc'] = (f'=IF(TRIM({cc_ref}&"")="","",IF(ISNUMBER({cc_ref}),{pct(cc_ref)},'
                       f'IFERROR(_xlfn.NUMBERVALUE({_clean_text(cc_ref)},"."),"")))')
        for key, stat in (('curD', 'Урон'), ('curS', 'SPA'), ('curR', 'Радиус')):
            vals[key] = '=' + '+'.join(f'IF({c[s]}{r}="{stat}",{pct(f"{c[v]}{r}")},0)' for s, v in CURSE_SLOTS)
        for col, (key, _) in enumerate(UNIT_SPEC, 1):
            cell = ws.cell(r, col)
            if key in UNIT_INPUT:
                inp(cell, u[PAS_PREFILL[key]] or None if key in PAS_PREFILL else None,
                    fmt=None)
                if key == 'note': cell.alignment = TOPWRAP
                continue
            cell.value = vals.get(key)
        link(ws[f'{c["name"]}{r}'], 'Апгрейды', f'A{f}')
        ws[f'{c["feats"]}{r}'].alignment = TOPWRAP
        ws[f'{c["passdesc"]}{r}'].alignment = TOPWRAP
        ws[f'{c["summ"]}{r}'].alignment = TOPWRAP
        for key, fmt in (('cost0', MONEY), ('costmax', MONEY), ('dmg', DPS), ('spa', NUM2), ('rng', '0.0'),
                         ('dps', DPS), ('dpsk', DPS), ('best', DPS), ('dpsall', DPS), ('costall', MONEY), ('farm', MONEY),
                         ('sdps', DPS)):
            ws[f'{c[key]}{r}'].number_format = fmt
        for key in ('idx', 'rnum', 'tier', 'tierv', 'dtype', 'cap', 'ups', 'bestup', 'rankv', 'rankd', 'lim', 'mine'):
            ws[f'{c[key]}{r}'].alignment = Alignment(horizontal='center', vertical='top')
    from openpyxl.comments import Comment
    for key, text in (
            ('best', 'Наибольший DPS на 1000 денег среди всех апгрейдов юнита (0 = только поставить, без апгрейдов).'),
            ('bestup', 'Номер апгрейда, на котором у юнита лучший DPS на каждые 1000 потраченных денег. '
                       '0 почти у всех: поставить юнита дёшево, а апгрейды дорожают быстрее, чем растёт DPS. '
                       'Это не значит «не качай» — для решения смотри «Прирост DPS на 1000 за шаг» на листе «Апгрейды».'),
            ('pas', 'Пишешь число: 12 или 12,5 (можно со знаком %). Отрицательное — уменьшение.'),
            ('cs', 'На сколько % снизить SPA (атака чаще). Число: 9 или 9,3 (можно 9,3%).'),
            ('k1s', 'Проклятия (вики, Powerups): +2,5…13% к одному стату и −2,5…13% к другому. Статы: Урон, SPA, Радиус. '
                    'В «стат» выбери из списка Урон / SPA / Радиус, в соседний «%» — число, как показывает игра: '
                    'Урон | 12 (+12% урона), SPA | 5 (атака на 5% медленнее), SPA | -8 (на 8% быстрее), Радиус | -6. '
                    'До 4 проклятий: 2 бафа и 2 дебафа.')):
        note = Comment(text, AUTHOR)
        note.width, note.height = 320, 110
        ws[f'{c[key]}4'].comment = note
    dv_list(ws, '"Да,Нет"', f'{c["mine"]}5:{c["mine"]}{end}')
    dv_list(ws, TRAIT_COL['name'], f'{c["trait"]}5:{c["trait"]}{end}')
    dv_list(ws, RELIC_COL['name'], f'{c["relic"]}5:{c["relic"]}{end}')
    for s, _ in CURSE_SLOTS:
        dv_list(ws, '"Урон,SPA,Радиус"', f'{c[s]}5:{c[s]}{end}')

    # оформление: полосы, цвета редкости, тиры, шкалы
    last_vis = get_column_letter(len(UNIT_SPEC) - len(UNIT_HIDDEN))
    ws.conditional_formatting.add(f'{c["name"]}5:{c["name"]}{end}',
                                  FormulaRule(formula=[f'${c["mine"]}5="Да"'], fill=GREEN))
    rarity_cf(ws, f'{c["rarity"]}5:{c["rarity"]}{end}')
    for t, color in (('S', '63BE7B'), ('A', 'B5DB8F'), ('B', 'FFEB84'), ('C', 'FBC08D'), ('D', 'F8A5A5')):
        ws.conditional_formatting.add(f'{c["tier"]}5:{c["tierv"]}{end}', CellIsRule(
            operator='equal', formula=[f'"{t}"'], fill=PatternFill('solid', fgColor=color), font=BOLD))
    for key in ('dpsk', 'best'):
        scale(ws, f'{c[key]}5:{c[key]}{end}')
    banded = [k for k, _ in UNIT_SPEC if k not in UNIT_INPUT + UNIT_HIDDEN + ('name', 'rarity', 'tier', 'tierv', 'dpsk', 'best')]
    for k in banded:
        ws.conditional_formatting.add(f'{c[k]}5:{c[k]}{end}', FormulaRule(formula=['MOD(ROW(),2)=0'], fill=BAND))
    for k in UNIT_HIDDEN:
        ws.column_dimensions[c[k]].hidden = True
    autofit(ws, 4, {c['costmax']: 13, c['dmg']: 11, c['spa']: 8, c['rng']: 8, c['dps']: 11, c['dpsk']: 12,
                    c['best']: 12, c['bestup']: 9, c['rankv']: 9, c['rankd']: 8, c['dpsall']: 14, c['costall']: 11,
                    c['tier']: 7, c['tierv']: 7, c['mine']: 8, c['cd']: 9, c['cs']: 9, c['cc']: 12, c['note']: 30,
                    c['trait']: 16, c['relic']: 20, c['pas']: 10, c['pasc']: 12, c['pascd']: 12, c['pasdot']: 10},
            wrap_cols={c['feats']: 60, c['passdesc']: 60, c['note']: 40, c['summ']: 45})
    ws.freeze_panes = f'{get_column_letter(3)}5'     # имя и «Есть у меня» всегда видны
    # автофильтр — на ВСЕ столбцы, включая скрытые: сортировка через него переставляет строку целиком.
    # Если бы скрытые служебные столбцы остались вне фильтра, при сортировке они не переехали бы вместе с юнитом
    ws.auto_filter.ref = f'A4:{get_column_letter(len(UNIT_SPEC))}{end}'
    return ws, end


# ── Апгрейды ───────────────────────────────────────────────────────────
UPG_COLS = ['Юнит', 'Апгрейд\n(0 = постановка)', 'Цена шага', 'Цена всего\n(вики)', 'Урон\n(вики)', 'SPA\n(вики)',
            'Радиус\n(вики)', 'Тип атаки', 'Ударов', 'DoT', 'DoT\nтиков', 'DoT\nмнож.', 'Крит-шанс\n(вики)',
            'Крит-урон\n(вики)', 'Что даёт апгрейд', 'Тип\nурона',
            'Цена всего\n(со скидкой)', 'Урон\nитог', 'SPA\nитог', 'Радиус\nитог', 'Крит-шанс\nитог', 'Крит\nмнож.',
            'DPS\nудара', 'DPS\nDoT', 'Целей', 'DPS\nИТОГ', 'DPS на 1000\nденег', 'Прирост DPS\nна 1000 за шаг',
            'Вид DoT', 'Усиление\nDoT, %', 'стр. юнита', 'Призыв: урон\nза цикл (вики)', 'Призыв:\nцикл, с',
            'Призыв: урон\nза убийство', 'Множитель\nурона юнита', 'DPS\nпризывов',
            'Призыв: потолок\nурона за убийства, /с', 'Атакует\nсам', 'Множитель\nбез бафов\nсаппортов',
            'Урон одного\nпризыва (вики)', 'Тип цикла\nпризыва', 'Призыв-\nтаран', 'Убийства\nпризыва']


def sheet_upgrades(wb, units, end):
    ws = wb.create_sheet('Апгрейды')
    ws.sheet_properties.tabColor = '808080'
    title(ws, 'Все апгрейды всех юнитов', 'Серые столбцы — данные вики, белые — формулы с учётом «Настроек» и твоих правок на «Юнитах». '
          '«Прирост DPS на 1000 за шаг» — выгоден ли апгрейд. Этот лист НЕ сортируй (только фильтр) — сортировать можно «Юниты»')
    header(ws, 4, UPG_COLS, {26: HEAD_DPS, 27: HEAD_DPS, 28: HEAD_DPS})
    r = 5
    for ui, u in enumerate(units):
        first = r
        for row in u['rows']:
            # юнит на «Юнитах» ищется ПО ИМЕНИ (AE) — после сортировки «Юнитов» ничего не съезжает.
            # Все жёлтые %-поля берутся через числовые скрытые столбцы v… (понимают 12.3 / 12,3% / текст)
            ws.cell(r, 31, f'=MATCH($A{r},{U}$A$5:$A${end},0)+4')
            cd, cs, cc, pas, tD, tS, tR, rD, rC, rCD, rDot, rDotK, resm, pasc, pascd, pasdot, curD, curS, curR, cost0, rClk, rPwr = (
                f"INDEX({U}${UC[k]}:${UC[k]},$AE{r})" for k in (
                    'vcd', 'vcs', 'vcc', 'vpas', 'tD', 'tS', 'tR', 'rD', 'rC', 'rCD', 'rDot', 'rDotK',
                    'resm', 'vpasc', 'vpascd', 'vpasdot', 'curD', 'curS', 'curR', 'cost0', 'rClk', 'rPwr'))
            vals = [u['name'], row['upg'], row['step'], row['total'], row['dmg'], row['spa'], row['rng'], row['atype'],
                    row['hits'], row['eff'] or None, row['ticks'] or None, row['mult'] or None, u['crit'],
                    u['critdmg'] or None, row['note'] or None, u['dtype']]
            for c, v in enumerate(vals, 1):
                ws.cell(r, c, v).fill = GREY
            ws.cell(r, 15).alignment = TOPWRAP
            ws.cell(r, 17, f'={cost0}+(D{r}-{cost0})*(1-{DISC}/100)')
            # AM — множитель урона БЕЗ бафов саппортов. Всё — ОТДЕЛЬНЫЕ множители (сверено с игрой: 256K у Shinobi (Eternal)):
            # уровень × общий/LB × свой ранг × проклятие × (пассивка + реликвия) × трейт × сопротивление × PWR
            ws.cell(r, 39, f'={LVL}*(1+{GD}/100)*(1+{cd}/100)*(1+{curD}/100)*(1+({pas}+{rD})/100)*(1+{tD}/100)*{resm}'
                           f'*(1+{rPwr}*{PWRP}/100)')
            # AI — с бафами саппортов: бафы складываются между собой и умножают урон (Wind Dragon ×4 / Griffin = ×2)
            ws.cell(r, 35, f'=AM{r}*(1+IF(P{r}="Физ",{BF},IF(P{r}="Маг",{BM},{BT}))/100)')
            ws.cell(r, 18, f'=E{r}*AI{r}')
            ws.cell(r, 38, 'Да' if row['own_hits'] else 'Нет').fill = GREY
            sm = row['summon']
            frag = lambda s: s.replace('{E}', f'E{r}').replace('{S}', f'S{r}')
            cyc = sm.get('c')
            ws.cell(r, 32, f'={frag(sm["t"])}' if sm.get('t') else None)
            ws.cell(r, 33, f'=S{r}' if cyc == 'spa' else
                    f'=IF(S{r}>0,MAX(S{r},({WALK}+1.5*S{r})/3),0)' if cyc == JELLY else cyc)
            ws.cell(r, 34, f'={frag(sm["k"])}' if sm.get('k') else None)
            ws.cell(r, 37, f'={frag(sm["cap"])}' if sm.get('cap') else None)
            ws.cell(r, 40, f'={frag(sm["hit"])}' if sm.get('hit') else None)
            ws.cell(r, 41, cyc if cyc in ('spa', JELLY) else None)
            ws.cell(r, 42, 'таран' if sm.get('ram') else None)
            ws.cell(r, 43, 'свои' if sm.get('own') else None)
            for col in (32, 33, 34, 37, 40, 41, 42, 43):
                ws.cell(r, col).fill = GREY
            # DPS призывов = множитель урона × (за цикл / цикл + MIN(за убийство × убийств/с, потолок)) × бафы «Призыв»
            # таран: множитель без бафов × (1 + физ. бафы без Idol); «свои» убийства: не больше целей / SPA юнита
            ws.cell(r, 36, f'=IF(AP{r}="таран",AM{r}*(1+{BRAM}/100),AI{r})*(IF(N(AG{r})>0,N(AF{r})/AG{r},0)'
                           f'+MIN(N(AH{r})*IF(AQ{r}="свои",IF(S{r}>0,MIN({KPS},Y{r}/S{r}),0),{KPS}),IF(N(AK{r})>0,AK{r},1E+300)))'
                           f'*(1+{SUMB}/100)')
            # проклятие SPA: «+5%» в игре = атака медленнее → SPA × 1,05
            ws.cell(r, 19, f'=F{r}*MAX(0.1,1-({GS}+{cs}+{BS})/100)*(1-{tS}/100)*MAX(0.1,1+{curS}/100)')
            ws.cell(r, 20, f'=G{r}*(1+({GR}+{BR})/100)*(1+{tR}/100)*MAX(0.1,1+{curR}/100)')
            ws.cell(r, 21, f'=MIN(1,IF({cc}="",M{r},{cc}/100)+({GC}+{BC}+{rC}+{pasc})/100)')
            ws.cell(r, 22, f'=IF(N{r}>0,N{r},{CRIT})+({rCD}+{pascd})/100')
            ws.cell(r, 23, f'=IF(AL{r}="Нет",0,IF(S{r}>0,R{r}/S{r},0))')
            ws.cell(r, 29, row['dotkind'] or None).fill = GREY
            ws.cell(r, 30, f'=IF(AC{r}="",0,{dot_global(f"AC{r}")}+{relic_dot(rDot, rDotK, f"AC{r}")}+{pasdot})')
            # DoT: бафы саппортов усиливают только кровотечение; остальные DoT — от урона без бафов (E × AM)
            ws.cell(r, 24, f'=IF(AND({DOT}="Да",S{r}>0,AL{r}<>"Нет"),IF(AC{r}="Кровотечение",R{r},E{r}*AM{r})'
                           f'*N(L{r})*N(K{r})/S{r}*(1+AD{r}/100),0)')
            ws.cell(r, 25, f'=IFERROR(VLOOKUP(H{r},{AOE},2,0),1)')
            # итог = (удар с критом + DoT + часы реликвии) × цели + призывы
            ws.cell(r, 26, f'=(W{r}*(1+U{r}*(V{r}-1))+X{r}+IF(AL{r}="Нет",0,R{r}*{rClk}/100))*Y{r}+AJ{r}')
            ws.cell(r, 27, f'=IF(Q{r}>0,Z{r}/Q{r}*1000,0)')
            ws.cell(r, 28, f'=AA{r}' if r == first else
                    f'=IF(OR(A{r-1}<>A{r},B{r-1}<>B{r}-1),AA{r},IF(Q{r}-Q{r-1}>0,(Z{r}-Z{r-1})/(Q{r}-Q{r-1})*1000,0))')
            for c, fmt in ((3, MONEY), (4, MONEY), (5, DPS), (6, NUM2), (7, '0.0'), (12, '0.000'), (13, PCT),
                           (14, NUM2), (17, MONEY), (18, DPS), (19, NUM2), (20, '0.0'), (21, PCT), (22, NUM2),
                           (23, DPS), (24, DPS), (25, '0.0'), (26, DPS), (27, DPS), (28, DPS), (30, '0'),
                           (32, MONEY), (33, '0.##'), (34, DPS), (35, '0.000'), (36, DPS), (37, DPS), (39, '0.000'),
                           (40, MONEY)):
                ws.cell(r, c).number_format = fmt
            r += 1
        assert (first, r - 1) == (u['first'], u['last'])
        for c in range(1, len(UPG_COLS) + 1):
            ws.cell(first, c).border = Border(top=Side(style='medium', color='1F3864'))
    last = r - 1
    for col in ('Z', 'AA', 'AB'):
        scale(ws, f'{col}5:{col}{last}')
    autofit(ws, 4, {'Q': 12, 'R': 11, 'S': 8, 'T': 8, 'U': 9, 'V': 7, 'W': 10, 'X': 9, 'Y': 7, 'Z': 11,
                    'AA': 12, 'AB': 13, 'AD': 10, 'AF': 12, 'AG': 9, 'AH': 11, 'AI': 10, 'AJ': 11, 'AK': 14, 'AL': 8,
                    'AM': 11, 'AN': 12}, wrap_cols={'O': 45})
    ws.column_dimensions['AE'].hidden = True
    ws.freeze_panes = 'C5'
    ws.auto_filter.ref = f'A4:{get_column_letter(len(UPG_COLS))}{last}'
    return ws


# ── Сравнение: свой уровень, бафы, трейт, реликвия и пассивка в каждой строке ──
CMP_SPEC = [  # (ключ, заголовок, ширина)
    ('name', 'Юнит', 34), ('upg', 'Апгрейд\n(пусто = макс.)', 11), ('lvl_in', 'Уровень\n(1 / 100 / 110)', 10),
    ('b1', 'Баф 1', 31), ('b2', 'Баф 2', 31), ('b3', 'Баф 3', 31), ('b4', 'Баф 4', 31),
    ('trait', 'Трейт\n(пусто = как\nу юнита)', 17), ('relic', 'Реликвия\n(пусто = как\nу юнита)', 24),
    ('pas_in', 'Пассивка\n(Да / Нет)', 10),
    ('used', 'Апгрейд\nв расчёте', 11), ('cost', 'Цена всего', 12), ('dmg', 'Урон\nза удар', 12),
    ('maxhit', 'Макс. удар\n(крит)', 12), ('spa', 'SPA', 7), ('rng', 'Радиус', 8), ('atype', 'Тип атаки', 13),
    ('tg', 'Целей', 7), ('dotname', 'DoT-эффект', 24), ('dottick', 'DoT: урон\nза тик', 12),
    ('dotatk', 'DoT: урон\nза атаку\n(все тики)', 13),
    ('dotpct', 'DoT за атаку,\n% базового урона\n(с бафами)', 13), ('dotamp', 'Усиление\nDoT', 9),
    ('dotpct2', 'DoT за атаку\nс усилением,\n% базового', 13), ('hitdps', 'DPS\nударами', 11),
    ('dotdps', 'DPS\nот DoT', 11), ('sumhit', 'Призыв:\nурон одного\nудара', 12), ('sumdps', 'DPS\nпризывов', 11),
    ('dps', 'DPS ИТОГ\n(удары + DoT\n+ призывы)', 13), ('dpsk', 'DPS на 1000\nденег', 12),
    ('tot_hit', 'Урон ударами\nза время боя', 14), ('tot_dot', 'Урон DoT\nза время боя', 14),
    ('tot_sum', 'Урон призывов\nза время боя', 14),
    ('tot', 'ВСЕГО урона\nза время боя', 15), ('avgdps', 'Средний DPS\nза время боя', 13),
    ('dps0', 'DPS без\nбафов\nсаппортов', 12), ('gain', 'Бафы\nдали', 8), ('cap', 'Лимит\nна поле', 8),
    ('rank', 'Место по\nвыгоде', 9), ('dtv', 'Тип\nурона', 7),
]
CMP_HELP = ['urow', 'arow', 'lvl', 'dt', 'el', 'trn', 'rln', 'tD', 'tS', 'tR', 'rD', 'rC', 'rCD', 'pasv', 'cd', 'cs',
            'bd', 'bs', 'br', 'bc', 'disc', 'own', 'crit0', 'crit', 'cm', 'd0', 's0',
            'dk', 'rDot', 'rDotK', 'rdot', 'bdot', 'resm', 'pc', 'pcd', 'pdot', 'kD', 'kS', 'kR',
            'tsec', 'nat', 'nfull', 'dfull', 'rClk', 'mul0', 'mulx', 'sumb', 'sbase', 'rPwr', 'own_hit', 'cyc', 'dmgdot',
            'bram', 'mram']
CC = {k: get_column_letter(i) for i, (k, _, _) in enumerate(CMP_SPEC, 1)}
CC.update({k: get_column_letter(len(CMP_SPEC) + 2 + i) for i, k in enumerate(CMP_HELP)})
CMP_INPUT = ('name', 'upg', 'lvl_in', 'b1', 'b2', 'b3', 'b4', 'trait', 'relic', 'pas_in')
CMP_SLOTS = range(5, 35)   # 30 строк; 15–34 — сворачиваемая группа
CMP_LAST = CMP_SLOTS[-1]
CMP_HINT = CMP_LAST + 1


BUFF_ACTIVE = f'{S}$E${BUFF_FIRST}:$E${BUFF_LAST}'


def buff_sum(r, kind, who_cell, only_global=False, exclude=()):
    """Сумма выбранных в строке бафов вида kind. «На кого» проверяется только для Урон и DoT
    (SPA/Радиус/Крит/Скидка действуют на всех — так же, как в «Настройках»).
    only_global=True — только те из выбранных, что ещё и включены в «Настройках» (для вычета двойного учёта при B3=Да)."""
    terms = []
    slots = ('b1', 'b2', 'b3', 'b4')
    for j, k in enumerate(slots):
        m = f'MATCH({CC[k]}{r},{BUFF_NAMES},0)'
        cond = [f'INDEX({BUFF_KIND},{m})="{kind}"']
        # один и тот же баф в двух слотах считается один раз
        cond += [f'{CC[k]}{r}<>{CC[p]}{r}' for p in slots[:j]]
        if kind in ('Урон', 'DoT'):
            cond.append(f'OR(INDEX({BUFF_WHO},{m})="Все",INDEX({BUFF_WHO},{m})={who_cell})')
        if only_global:
            cond.append(f'INDEX({BUFF_ACTIVE},{m})="Да"')
        cond += [f'{CC[k]}{r}<>"{n}"' for n in exclude]
        terms.append(f'IFERROR(IF(AND({",".join(cond)}),N(INDEX({BUFF_VAL},{m})),0),0)')
    return '+'.join(terms)


def row_buffs(r, kind, who_cell, glob_total, nostack=False, exclude=()):
    """Бафы строки + (при B3=Да) активные из «Настроек» без двойного учёта; «не складываются» — по общему набору."""
    own = buff_sum(r, kind, who_cell, exclude=exclude)
    dup = buff_sum(r, kind, who_cell, only_global=True, exclude=exclude)
    add_back = f'+{NSG[kind]}' if nostack else ''     # в итогах «Настроек» уже вычтено — вернуть и посчитать заново
    expr = f'{own}+IF($B$3="Да",{glob_total}{add_back}-({dup}),0)'
    if nostack:
        slots = f'${CC["b1"]}{r}:${CC["b4"]}{r}'
        on = lambda n: f'OR(COUNTIF({slots},{S}$A${BUFF_ROW[n]})>0,AND($B$3="Да",{S}$E${BUFF_ROW[n]}="Да"))'
        expr += '-' + nostack_expr(kind, on, lambda n: f'{S}$C${BUFF_ROW[n]}')
    return expr


def engine(x, end, buf):
    """Формулы расчёта одной строки (общие для «Сравнения» и «Команды»).
    x — ключ → адрес ячейки (входы name, upg, lvl_in, trait, relic, pas_in и все помощники);
    buf — выражения бафов строки: bd, bs, br, bc, disc, bdot, sumb."""
    uc = lambda key: f'{U}${UC[key]}:${UC[key]}'
    ok = f'{x["arow"]}=""'
    A = lambda col: f'INDEX({A_}${col}:${col},{x["arow"]})'
    f = {
            'urow': f'=IF({x["name"]}="","",IFERROR(MATCH({x["name"]},{U}$A$5:$A${end},0)+4,""))',
            'used': f'=IF({x["urow"]}="","",IF({numf(x["upg"])}="",INDEX({uc("ups")},{x["urow"]}),'
                    f'MAX(0,MIN(INT({numf(x["upg"])}),INDEX({uc("ups")},{x["urow"]})))))',
            'arow': f'=IF({x["urow"]}="","",INDEX({uc("first")},{x["urow"]})+{x["used"]})',
            'lvl': f'=IF({x["lvl_in"]}="",{LVL},IF(OR({x["lvl_in"]}=110,{x["lvl_in"]}="110"),{LVL110},'
                   f'IF(OR({x["lvl_in"]}=100,{x["lvl_in"]}="100"),{LVL100},1)))',
            'dt': f'=IF({ok},"",{A("P")})',
            'el': f'=IF({x["urow"]}="","",INDEX({uc("elem")},{x["urow"]})&"")',
            'trn': f'=IF({x["trait"]}<>"",{x["trait"]},IF({x["urow"]}="","",INDEX({uc("trait")},{x["urow"]})&""))',
            'rln': f'=IF({x["relic"]}<>"",{x["relic"]},IF({x["urow"]}="","",INDEX({uc("relic")},{x["urow"]})&""))',
            # свои значения, пассивки и проклятия юнита — из числовых скрытых столбцов «Юнитов»
            'pasv': f'=IF(OR({x["urow"]}="",{x["pas_in"]}="Нет"),0,N(INDEX({uc("vpas")},{x["urow"]})))',
            'pc': f'=IF(OR({x["urow"]}="",{x["pas_in"]}="Нет"),0,N(INDEX({uc("vpasc")},{x["urow"]})))',
            'pcd': f'=IF(OR({x["urow"]}="",{x["pas_in"]}="Нет"),0,N(INDEX({uc("vpascd")},{x["urow"]})))',
            'pdot': f'=IF(OR({x["urow"]}="",{x["pas_in"]}="Нет"),0,N(INDEX({uc("vpasdot")},{x["urow"]})))',
            'cd': f'=IF({x["urow"]}="",0,N(INDEX({uc("vcd")},{x["urow"]})))',
            'cs': f'=IF({x["urow"]}="",0,N(INDEX({uc("vcs")},{x["urow"]})))',
            'kD': f'=IF({x["urow"]}="",0,N(INDEX({uc("curD")},{x["urow"]})))',
            'kS': f'=IF({x["urow"]}="",0,MAX(0.1,1+N(INDEX({uc("curS")},{x["urow"]}))/100))',
            'kR': f'=IF({x["urow"]}="",1,MAX(0.1,1+N(INDEX({uc("curR")},{x["urow"]}))/100))',
            'bd': '=' + buf['bd'],
            'bs': '=' + buf['bs'],
            'br': '=' + buf['br'],
            'bc': '=' + buf['bc'],
            'disc': f'=MIN(90,{buf["disc"]})',
            'own': f'={x["pasv"]}+{x["rD"]}',
            'crit0': f'=IF({ok},0,MIN(1,IF(INDEX({uc("vcc")},{x["urow"]})&""="",{A("M")},'
                     f'INDEX({uc("vcc")},{x["urow"]})/100)+({GC}+{x["rC"]}+{x["pc"]})/100))',
            'crit': f'=MIN(1,{x["crit0"]}+{x["bc"]}/100)',
            'cm': f'=IF({ok},{CRIT},IF({A("N")}>0,{A("N")},{CRIT}))+({x["rCD"]}+{x["pcd"]})/100',
            # множители урона юнита: mul0 — только своё (без бафов саппортов), mulx — со всеми бафами
            'mul0': f'={x["lvl"]}*(1+{GD}/100)*(1+{x["cd"]}/100)*(1+{x["kD"]}/100)*(1+{x["own"]}/100)'
                    f'*(1+{x["tD"]}/100)*{x["resm"]}*(1+{x["rPwr"]}*{PWRP}/100)',
            # бафы саппортов — отдельный множитель (внутри группы складываются): Wind Dragon ×4 / Griffin = ×2
            'mulx': f'={x["mul0"]}*(1+{x["bd"]}/100)',
            'own_hit': f'=IF({ok},"Нет",{A("AL")}&"")',
            # цикл призыва по SPA ЭТОЙ строки (её бафы SPA): spa — 1 призыв за SPA; jelly — медузы Elyssia
            'cyc': f'=IF({ok},0,IF({A("AO")}&""="spa",{x["spa"]},IF({A("AO")}&""="{JELLY}",'
                   f'IF(N({x["spa"]})>0,MAX({x["spa"]},({WALK}+1.5*{x["spa"]})/3),0),N({A("AG")}))))',
            'sumb': '=' + buf['sumb'],
            'bram': '=' + buf['bram'],
            # множитель урона призыва: таран — без бафов + физ. бафы без Idol; остальные — как юнит
            'mram': f'=IF({ok},0,IF({A("AP")}&""="таран",{x["mul0"]}*(1+{x["bram"]}/100),{x["mulx"]}))',
            # призывы: (урон за цикл / цикл + урон за убийство × убийств/с) × множитель урона × бафы призывов
            'sbase': f'=IF({ok},0,IF(N({x["cyc"]})>0,N({A("AF")})/{x["cyc"]},0)'
                     f'+MIN(N({A("AH")})*IF({A("AQ")}&""="свои",IF(N({x["spa"]})>0,MIN({KPS},{x["tg"]}/{x["spa"]}),0),{KPS}),'
                     f'IF(N({A("AK")})>0,N({A("AK")}),1E+300)))',
            # урон ОДНОГО удара/взрыва призыва (с уровнем, статами и бафами)
            'sumhit': f'=IF({ok},"",IF(N({A("AN")})=0,"—",N({A("AN")})*{x["mram"]}*(1+{x["sumb"]}/100)))',
            'sumdps': f'=IF({ok},"",{x["sbase"]}*{x["mram"]}*(1+{x["sumb"]}/100))',
            'd0': f'=IF({ok},0,{A("E")}*{x["mul0"]})',
            's0': f'=IF({ok},0,{A("F")}*MAX(0.1,1-({GS}+{x["cs"]})/100)*(1-{x["tS"]}/100)*{x["kS"]})',
            'cost': f'=IF({ok},"",INDEX({uc("cost0")},{x["urow"]})+({A("D")}-INDEX({uc("cost0")},{x["urow"]}))'
                    f'*(1-{x["disc"]}/100))',
            'dmg': f'=IF({ok},"",{A("E")}*{x["mulx"]})',
            # урон, от которого считается DoT: кровотечение — с бафами саппортов, горение/яд/иссушение — без них (вики)
            'dmgdot': f'=IF({ok},0,IF({x["dk"]}="Кровотечение",{x["dmg"]},{x["d0"]}))',
            'dottick': f'=IF({ok},"",IF(OR({x["dk"]}="",{x["own_hit"]}="Нет"),"—",{x["dmgdot"]}*N({A("L")})'
                       f'*(1+({x["rdot"]}+{x["bdot"]})/100)))',
            'dotatk': f'=IF({ok},"",IF(N({x["dottick"]})=0,"—",{x["dottick"]}*N({A("K")})))',
            'maxhit': f'=IF({ok},"",{x["dmg"]}*IF({x["crit"]}>0,{x["cm"]},1))',
            'spa': f'=IF({ok},"",{A("F")}*MAX(0.1,1-({GS}+{x["cs"]}+{x["bs"]})/100)*(1-{x["tS"]}/100)*{x["kS"]})',
            'rng': f'=IF({ok},"",{A("G")}*(1+({GR}+{x["br"]})/100)*(1+{x["tR"]}/100)*{x["kR"]})',
            'atype': f'=IF({ok},"",{A("H")})',
            'tg': f'=IF({ok},"",IFERROR(VLOOKUP({x["atype"]},{AOE},2,0),1))',
            'dk': f'=IF({ok},"",{A("AC")}&"")',
            'dotname': f'=IF({ok},"",IF({A("J")}&""="","нет",{A("J")}))',
            'rdot': f'=IF({x["dk"]}="",0,{relic_dot(x["rDot"], x["rDotK"], x["dk"])}+{x["pdot"]})',
            'bdot': f'=IF({x["dk"]}="",0,{buf["bdot"]})',
            'dotamp': f'=IF(OR({ok},{x["dk"]}="",{DOT}<>"Да"),"",({x["rdot"]}+{x["bdot"]})/100)',
            'dotdps': f'=IF({ok},"",IF(AND({DOT}="Да",{x["spa"]}>0,{x["own_hit"]}<>"Нет"),{x["dmgdot"]}*N({A("L")})*N({A("K")})/{x["spa"]}'
                      f'*(1+({x["rdot"]}+{x["bdot"]})/100)*{x["tg"]},0))',
            # DPS = удары с критом + DoT + часы реликвии (урон × %/с) + призывы
            # DPS ударами = удары с критом × цели + часы реликвии; ИТОГ = удары + DoT + призывы
            'hitdps': f'=IF({ok},"",IF({x["own_hit"]}="Нет",0,IF({x["spa"]}>0,{x["dmg"]}/{x["spa"]}*(1+{x["crit"]}*({x["cm"]}-1))'
                      f'*{x["tg"]},0)+{x["dmg"]}*{x["rClk"]}/100*{x["tg"]}))',
            'dps': f'=IF({ok},"",{x["hitdps"]}+{x["dotdps"]}+{x["sumdps"]})',
            'dpsk': f'=IF(OR({ok},N({x["cost"]})=0),"",{x["dps"]}/{x["cost"]}*1000)',
            'dps0': f'=IF({ok},"",IF(AND({x["s0"]}>0,{x["own_hit"]}<>"Нет"),({x["d0"]}/{x["s0"]}*(1+{x["crit0"]}*({x["cm"]}-1))'
                    f'+IF({DOT}="Да",{x["d0"]}*N({A("L")})*N({A("K")})/{x["s0"]}*(1+{x["rdot"]}/100),0)'
                    f'+{x["d0"]}*{x["rClk"]}/100)*{x["tg"]},0)+{x["sbase"]}*{x["mul0"]})',
            'gain': f'=IF(OR({ok},N({x["dps0"]})=0),"",{x["dps"]}/{x["dps0"]}-1)',
            # «разгон» DoT: % базового урона юнита (вики × уровень), который DoT наносит за одну атаку
            # вложенные IF: OR вычисляет все условия, и INDEX(…;"") в пустой строке дал бы #VALUE!
            'dotpct': f'=IF({ok},"",IF(OR({x["dk"]}="",{DOT}<>"Да",N({A("E")})=0),"",N({A("L")})*N({A("K")})*{x["dmgdot"]}/({A("E")}*{x["lvl"]})))',
            'dotpct2': f'=IF({x["dotpct"]}="","",{x["dotpct"]}*(1+({x["rdot"]}+{x["bdot"]})/100))',
            # урон за время боя T: атаки в 0, SPA, 2·SPA…; DoT каждой атаки тикает раз в TICK с, недотикавшее к концу не считается
            'tsec': f'=MAX(0,{numf("$H$3", "30")})',
            'nat': f'=IF(OR({ok},N({x["spa"]})<=0),0,INT({x["tsec"]}/{x["spa"]})+1)',
            'dfull': f'=IF(OR({ok},{DOT}<>"Да",{x["own_hit"]}="Нет"),0,{x["dmgdot"]}*N({A("L")})*N({A("K")})*(1+({x["rdot"]}+{x["bdot"]})/100)*{x["tg"]})',
            'nfull': f'=IF({x["nat"]}=0,0,IF(N({A("K")})=0,0,MIN({x["nat"]},MAX(0,INT(({x["tsec"]}-N({A("K")})*{TICK})'
                     f'/{x["spa"]})+1))))',
            'tot_hit': f'=IF({ok},"",IF({x["own_hit"]}="Нет",0,{x["nat"]}*{x["dmg"]}*(1+{x["crit"]}*({x["cm"]}-1))*{x["tg"]}'
                       f'+{x["dmg"]}*{x["rClk"]}/100*{x["tg"]}*{x["tsec"]}))',
            # призывы начинают бить после пути до врага
            'tot_sum': f'=IF({ok},"",{x["sumdps"]}*MAX(0,{x["tsec"]}-{WALK}))',
            'tot_dot': f'=IF({ok},"",IF(OR(N({A("K")})=0,{x["nat"]}=0),0,{x["dfull"]}/N({A("K")})*({x["nfull"]}*N({A("K")})'
                       f'+MAX(0,({x["tsec"]}*({x["nat"]}-{x["nfull"]})-{x["spa"]}*({x["nfull"]}+{x["nat"]}-1)'
                       f'*({x["nat"]}-{x["nfull"]})/2)/{TICK}))))',
            # всего = удары + DoT + (часы + призывы) × время боя
            'tot': f'=IF({ok},"",{x["tot_hit"]}+{x["tot_dot"]}+{x["tot_sum"]})',
            'avgdps': f'=IF(OR({ok},{x["tsec"]}=0),"",{x["tot"]}/{x["tsec"]})',
            'cap': f'=IF({x["urow"]}="","",IF(N(INDEX({uc("cap")},{x["urow"]}))=0,"—",INDEX({uc("cap")},{x["urow"]})))',
            'rank': f'=IF({x["urow"]}="","",INDEX({uc("rankv")},{x["urow"]}))',
            'dtv': f'={x["dt"]}',
        }
    f.update({k: '=' + v for k, v in mods_formulas(x['trn'], x['rln'], x['dt'], x['el']).items()})
    return f


def sheet_compare(wb, end, demo):
    ws = wb.create_sheet('Сравнение', 0)
    ws.sheet_properties.tabColor = '375623'
    title(ws, 'Сравнение юнитов', 'Жёлтое выбираешь сам: юнит, апгрейд, уровень, до 4 бафов, трейт, реликвия, пассивка. '
          'Один юнит можно поставить в несколько строк с разными наборами и сравнить')
    from openpyxl.comments import Comment
    ws['A3'] = 'Добавить бафы из «Настроек»:'; ws['A3'].font = BOLD
    inp(ws['B3'], 'Нет'); dv_list(ws, '"Да,Нет"', 'B3')
    ws['B3'].comment = Comment('«Нет» — в строке действуют только её бафы. «Да» — плюс включённые в «Настройках» '
                               '(без двойного учёта).', AUTHOR)
    ws['D3'] = '🔍 Поиск юнита:'; ws['D3'].font = BOLD; ws['D3'].alignment = Alignment(horizontal='right')
    inp(ws['E3'])
    ws['E3'].comment = Comment('Впиши часть имени (например «sorc») — в списке юнитов останутся только подходящие. '
                               'Сотри, чтобы снова видеть всех.', AUTHOR)
    ws['G3'] = '⏱ Время боя, с:'; ws['G3'].font = BOLD; ws['G3'].alignment = Alignment(horizontal='right')
    inp(ws['H3'], 30, '0')
    dv = DataValidation(type='list', formula1='"5,15,30,45,60"', allow_blank=True)
    dv.showErrorMessage = False          # можно вписать и своё число
    ws.add_data_validation(dv); dv.add('H3')
    ws['H3'].comment = Comment('Время, за которое считается «Урон за время боя»: 5, 15, 30, 45, 60 с или своё число.', AUTHOR)
    fills = {i: HEAD_INPUT for i, (k, _, _) in enumerate(CMP_SPEC, 1) if k in CMP_INPUT}
    fills.update({i: HEAD_DPS for i, (k, _, _) in enumerate(CMP_SPEC, 1) if k in ('dps', 'dpsk')})
    header(ws, 4, [t for _, t, _ in CMP_SPEC], fills)
    ws.row_dimensions[4].height = 58
    c = CC
    uc = lambda key: f'{U}${UC[key]}:${UC[key]}'
    for r in CMP_SLOTS:
        d = demo[r - 5] if r - 5 < len(demo) else {}
        inp(ws[f'{c["name"]}{r}'], d.get('name'))
        inp(ws[f'{c["upg"]}{r}'], fmt='0')
        inp(ws[f'{c["lvl_in"]}{r}'], d.get('lvl'))
        for i, k in enumerate(('b1', 'b2', 'b3', 'b4')):
            b = d.get('buffs', ())
            inp(ws[f'{c[k]}{r}'], b[i] if i < len(b) else None)
        inp(ws[f'{c["trait"]}{r}'], d.get('trait'))
        inp(ws[f'{c["relic"]}{r}'], d.get('relic'))
        inp(ws[f'{c["pas_in"]}{r}'])
        x = {k: f'${c[k]}{r}' for k in c}
        buf = {'bd': row_buffs(r, 'Урон', x['dt'], f'IF({x["dt"]}="Физ",{BF},IF({x["dt"]}="Маг",{BM},{BT}))',
                               nostack=True),
               'bs': row_buffs(r, 'SPA', x['dt'], BS, nostack=True),
               'br': row_buffs(r, 'Радиус', x['dt'], BR),
               'bc': row_buffs(r, 'Крит', x['dt'], BC),
               'disc': row_buffs(r, 'Скидка', x['dt'], DISC),
               'bdot': row_buffs(r, 'DoT', x['dk'], dot_global(x['dk'])),
               'sumb': row_buffs(r, 'Призыв', x['dt'], SUMB),
               'bram': row_buffs(r, 'Урон', '"Физ"', BRAM, exclude=RAM_EXCLUDE)}
        f = engine(x, end, buf)
        for key, formula in f.items():
            ws[f'{c[key]}{r}'] = formula
        for key, fmt in (('cost', MONEY), ('dmg', DPS), ('maxhit', DPS), ('spa', NUM2), ('rng', '0.0'), ('tg', '0.0'),
                         ('dps', DPS), ('dpsk', DPS), ('dps0', DPS), ('gain', PLUSPCT), ('dotamp', PLUSPCT),
                         ('dotdps', DPS), ('sumdps', DPS), ('sumhit', MONEY), ('dottick', DPS), ('dotatk', MONEY), ('dotpct', PCT), ('dotpct2', PCT), ('tot_hit', MONEY), ('tot_dot', MONEY), ('tot_sum', MONEY), ('hitdps', DPS),
                         ('tot', MONEY), ('avgdps', DPS)):
            ws[f'{c[key]}{r}'].number_format = fmt
        for i in range(1, len(CMP_SPEC) + 1):
            ws.cell(r, i).border = BOX
        ws[f'{c["dps"]}{r}'].font = BOLD
    ws[f'A{CMP_HINT}'] = ('Строки 15–34 — группа «+/−» слева: свернул — видно 10 юнитов и графики только по ним; развернул — до 30. '
                 'Убрать юнита или баф: выбери в списке «— убрать» или выдели ячейки и нажми Delete (не Backspace). '
                 'Бафы, трейты и реликвии берутся из листов «Настройки», «Трейты», «Реликвии» — там же можно дописать свои')
    ws[f'A{CMP_HINT}'].font = HINT
    ws.row_dimensions.group(15, CMP_LAST, outline_level=1, hidden=False)
    ws.sheet_properties.outlinePr.summaryBelow = True
    col_rng = lambda k: f'{c[k]}5:{c[k]}{CMP_LAST}'
    dv_list(ws, UNIT_PICK['Сравнение'], col_rng('name'))
    dv_list(ws, '"1,100,110"', col_rng('lvl_in'))
    dv_list(ws, UPG_LIST, col_rng('upg'))
    dv_list(ws, BUFF_PICK, f'{c["b1"]}5:{c["b4"]}{CMP_LAST}')
    dv_list(ws, TRAIT_COL['name'], col_rng('trait'))
    dv_list(ws, RELIC_COL['name'], col_rng('relic'))
    dv_list(ws, '"Да,Нет"', col_rng('pas_in'))
    scale(ws, col_rng('dpsk'), 'minmax'); scale(ws, col_rng('dps'), 'minmax')
    ws.conditional_formatting.add(col_rng('gain'), CellIsRule(operator='greaterThan', formula=['0'], fill=GREEN))
    for k in CMP_HELP:
        ws.column_dimensions[c[k]].hidden = True
    for k, _, w in CMP_SPEC:
        ws.column_dimensions[c[k]].width = w

    # 7 графиков сеткой 2 в ряд под таблицей; скрытые (свёрнутые) строки в графики не попадают
    top, step = CMP_HINT + 2, 30
    charts = (
        (('dpsk',), 'DPS на 1000 денег — кто выгоднее', '#,##0'),
        (('dps',), 'DPS — кто сильнее', '#,##0'),
        (('hitdps', 'dotdps', 'sumdps'), 'Из чего состоит DPS: удары / DoT / призывы', '#,##0'),
        (('tot',), 'Урон за время боя (время — ячейка H3)', '#,##0'),
        (('dmg',), 'Урон за один удар (с бафами)', '#,##0'),
        (('cost',), 'Стоимость до выбранного апгрейда', '#,##0'),
        (('spa',), 'SPA — секунд между атаками (меньше = быстрее)', '0.00'),
    )
    for i, (keys, name, nf) in enumerate(charts):
        ch = BarChart(); ch.type = 'bar'; ch.style = 10
        ch.title = name
        for key in keys:
            col = ws[f'{c[key]}4'].column
            ch.add_data(Reference(ws, min_col=col, min_row=5, max_row=CMP_LAST), titles_from_data=False)
        if len(keys) > 1:
            ch.grouping = 'stacked'; ch.overlap = 100
            for sr, t in zip(ch.series, ('Удары', 'DoT', 'Призывы')):
                sr.tx = SeriesLabel(v=t)
            ch.legend.position = 'b'
        else:
            ch.legend = None
        ch.set_categories(Reference(ws, min_col=1, min_row=5, max_row=CMP_LAST))
        ch.y_axis.numFmt = nf
        ch.x_axis.scaling.orientation = 'maxMin'
        ch.height, ch.width = 14, 18 if i % 2 == 0 else 22
        ws.add_chart(ch, f'{"AE"[i % 2]}{top + (i // 2) * step}')
    ws.freeze_panes = 'B5'
    return ws


def picker_formulas(r, name_col, upg_col, urow, used, arow, end):
    """Выбор юнита: строка на «Юнитах», использованный апгрейд, строка на «Апгрейдах»."""
    ups, first = f'{U}${UC["ups"]}:${UC["ups"]}', f'{U}${UC["first"]}:${UC["first"]}'
    return {
        urow: f'=IF({name_col}{r}="","",IFERROR(MATCH({name_col}{r},{U}$A$5:$A${end},0)+4,""))',
        used: f'=IF({urow}{r}="","",IF({numf(f"{upg_col}{r}")}="",INDEX({ups},{urow}{r}),'
              f'MAX(0,MIN(INT({numf(f"{upg_col}{r}")}),INDEX({ups},{urow}{r})))))',
        arow: f'=IF({urow}{r}="","",INDEX({first},{urow}{r})+{used}{r})',
    }


# ── Команда: бафферы в команде сами дают бафы остальным ────────────────
# юнит → (баф, баф при ≥4 копиях или None, «за каждую копию» до N (0 — нет), второй баф, его «за копию»).
# Названия — строки таблицы бафов «Настроек», значения берутся оттуда (их можно поправить).
TEAM_BUFFS = {
    'Commander': ('Commander (1 шт.)', 'Commander ×4 (бесконечный баф)', 0, None, 0),
    'Wind Dragon': ('Wind Dragon (1 шт.)', 'Wind Dragon ×4 (бесконечный баф)', 0, None, 0),
    'Elfy (Sylph)': ('Elfy (Sylph)', None, 0, None, 0),
    'Blossom': ('Blossom', None, 0, None, 0),
    'Griffin (Reincarnation)': ('Griffin (Reincarnation)', None, 0, None, 0),
    'Skeleton (Soul King)': ('Skeleton (Soul King)', None, 0, None, 0),
    'Idol': ('Idol (макс. апгрейд)', None, 0, None, 0),
    'Idol (Star)': ('Idol (Star) — урон', None, 0, 'Idol (Star) — скидка', 0),
    'Trickster (Release)': ('Trickster (Release) — SPA', None, 0, 'Trickster (Release) — радиус', 0),
    'Gambler (Jackpot)': ('Gambler (Jackpot)', None, 0, None, 0),
    'Priest (Heaven)': ('Priest (Heaven) — в среднем', None, 0, None, 0),
    'Devil Boss': ('Devil Boss — Time Erase', None, 0, None, 0),
    'Cursed King': ('Дебафф: Cursed King / Switchblade', None, 0, None, 0),
    'Switchblade (Deception)': ('Дебафф: Cursed King / Switchblade', None, 0, None, 0),
    'Blackhair': ('Дебафф: Blackhair', None, 0, None, 0),
    'Infinity Mage (Endless)': ('Дебафф: Hexed / Shadow Sorcerer', None, 0, None, 0),
    'Shadow Sorcerer (Hybrid Shadow)': ('Дебафф: Hexed / Shadow Sorcerer', None, 0, None, 0),
    'Chuuni (Delusion)': ('Дебафф: Chuuni (Delusion) ×1', None, 3, None, 0),
    'Bloodcry (Fallen)': ('Bloodcry (Fallen) — Bleed Amp ×5', None, 0, None, 0),
    'Blood (Unleashed)': ('Blood (Unleashed) — Bleed Amp ×5', None, 0, None, 0),
    'Zombie (Risen)': ('Zombie (Risen) ×1', None, 8, None, 0),
}
TEAM_KINDS = [('Урон', 'Физ'), ('Урон', 'Маг'), ('Урон', 'Все'), ('SPA', None), ('Радиус', None), ('Крит', None),
              ('Скидка', None)] + [('DoT', k) for k in DOT_KINDS] + [('DoT', 'Все'), ('Призыв', None)]
TEAM_ROWS = range(5, 13)
TEAM_VIS = [  # (ключ, заголовок, ширина)
    ('name', 'Юнит', 32), ('upg', 'Апгрейд\n(пусто = макс.)', 11), ('cnt_in', 'Сколько\nштук', 8),
    ('used', 'Апгрейд\nв расчёте', 9), ('cost', 'Цена 1 шт.', 11), ('dps', 'DPS 1 шт.\n(с бафами\nкоманды)', 12),
    ('costall', 'Цена всего', 12), ('dpsall', 'DPS всего', 13), ('dpsk', 'DPS на 1000', 11),
    ('cap', 'Лимит\nна поле', 7), ('check', 'Проверка', 17), ('role', 'Роль', 9),
    ('gives', 'Даёт команде\n(баф)', 34), ('dps0', 'DPS 1 шт.\nбез бафов\nкоманды', 12), ('gain', 'Бафы\nкоманды\nдали', 9),
    ('trtxt', 'Трейт', 28), ('rltxt', 'Реликвия', 22), ('rleff', 'Что даёт реликвия', 30),
    ('pastxt', 'Пассивка (числа)', 28), ('curtxt', 'Проклятия', 24), ('dtv', 'Тип\nурона', 7),
]
TEAM_EXTRA = ['cnt', 'pb1', 'pb2', 'm1', 'm2', 'd0all'] + [f'tk{i}' for i in range(len(TEAM_KINDS))]
_ENGINE_KEYS = [k for k, _, _ in CMP_SPEC if k not in CMP_INPUT] + CMP_HELP
TK = {k: get_column_letter(i) for i, (k, _, _) in enumerate(TEAM_VIS, 1)}
for i, k in enumerate([k for k in _ENGINE_KEYS if k not in TK] + TEAM_EXTRA):
    TK.setdefault(k, get_column_letter(len(TEAM_VIS) + 3 + i))
TEAM_MAP = "'Списки'!$H$1:$M$60"     # таблица TEAM_BUFFS на скрытом листе


def team_kind_total(i):
    """Сумма бафа вида TEAM_KINDS[i] от всех бафферов команды (строка 13 — итоги)."""
    return f'${TK[f"tk{i}"]}$13'


def sheet_team(wb, end, demo):
    ws = wb.create_sheet('Команда', 1)
    ws.sheet_properties.tabColor = '375623'
    title(ws, 'Моя команда', 'Выставь до 8 юнитов и сколько штук. Бафферы в команде (Commander, Wind Dragon, Griffin, Blossom, Idol, '
          'Trickster, Zombie (Risen), Bloodcry…) сами дают бафы остальным. Трейт, реликвия, пассивка, проклятия — с листа «Юниты»')
    fills = {i: HEAD_INPUT for i, (k, _, _) in enumerate(TEAM_VIS, 1) if k in ('name', 'upg', 'cnt_in')}
    fills.update({i: HEAD_DPS for i, (k, _, _) in enumerate(TEAM_VIS, 1) if k in ('dps', 'dpsall', 'dpsk')})
    header(ws, 4, [t for _, t, _ in TEAM_VIS], fills)
    ws.row_dimensions[4].height = 58
    t = TK
    tot = lambda i: team_kind_total(i)
    pb_rng = lambda k: f'${t[k]}$5:${t[k]}$12'
    kind_idx = {kw: i for i, kw in enumerate(TEAM_KINDS)}
    for r in TEAM_ROWS:
        d = demo[r - 5] if r - 5 < len(demo) else (None, None)
        inp(ws[f'{t["name"]}{r}'], d[0]); inp(ws[f'{t["upg"]}{r}'], fmt='0'); inp(ws[f'{t["cnt_in"]}{r}'], d[1], '0')
        x = {k: f'${t[k]}{r}' for k in t}
        x.update({'lvl_in': '""', 'trait': '""', 'relic': '""', 'pas_in': '""', 'name': f'${t["name"]}{r}',
                  'upg': f'${t["upg"]}{r}'})
        # бафы цели = сумма бафов бафферов команды подходящего вида и типа; «не складываются» — по всей команде
        ns_on = lambda n: f'(COUNTIF({pb_rng("pb1")},{S}$A${BUFF_ROW[n]})+COUNTIF({pb_rng("pb2")},{S}$A${BUFF_ROW[n]}))>0'
        ns_val = lambda n: f'{S}$C${BUFF_ROW[n]}'
        dot_by_kind = '0'
        for k in reversed(DOT_KINDS):
            dot_by_kind = f'IF({x["dk"]}="{k}",{tot(kind_idx[("DoT", k)])},{dot_by_kind})'
        buf = {'bd': f'IF({x["dt"]}="Физ",{tot(0)},IF({x["dt"]}="Маг",{tot(1)},0))+{tot(2)}'
                     f'-{nostack_expr("Урон", ns_on, ns_val)}',
               'bs': f'{tot(3)}-{nostack_expr("SPA", ns_on, ns_val)}', 'br': tot(4), 'bc': tot(5), 'disc': tot(6),
               'bdot': f'{dot_by_kind}+{tot(kind_idx[("DoT", "Все")])}', 'sumb': tot(len(TEAM_KINDS) - 1),
               'bram': f'{tot(0)}+{tot(2)}' + ''.join(
                   f'-{S}$C${BUFF_ROW[n]}*(COUNTIF({pb_rng("pb1")},"{n}")+COUNTIF({pb_rng("pb2")},"{n}"))' for n in RAM_EXCLUDE)}
        for key, formula in engine(x, end, buf).items():
            if key in t:
                ws[f'{t[key]}{r}'] = formula
        ok = f'{x["arow"]}=""'
        # что даёт этот юнит: баф(ы) из TEAM_BUFFS (на «Списках»), с учётом числа копий
        tm = lambda col: f'INDEX({TEAM_MAP},MATCH({x["name"]},INDEX({TEAM_MAP},0,1),0),{col})'
        ws[f'{t["cnt"]}{r}'] = f'=IF({ok},0,MAX(0,INT({numf(x["cnt_in"], "0")})))'
        ws[f'{t["pb1"]}{r}'] = f'=IF({x["cnt"]}=0,"",IFERROR(IF(AND({x["cnt"]}>=4,{tm(3)}&""<>""),{tm(3)},{tm(2)})&"",""))'
        ws[f'{t["pb2"]}{r}'] = f'=IF({x["cnt"]}=0,"",IFERROR({tm(5)}&"",""))'
        ws[f'{t["m1"]}{r}'] = f'=IFERROR(IF(N({tm(4)})>0,MIN({x["cnt"]},{tm(4)}),1),1)'
        ws[f'{t["m2"]}{r}'] = f'=IFERROR(IF(N({tm(6)})>0,MIN({x["cnt"]},{tm(6)}),1),1)'
        for i, (kind, who) in enumerate(TEAM_KINDS):
            terms = []
            for pb, m in (('pb1', 'm1'), ('pb2', 'm2')):
                mm = f'MATCH({x[pb]},{BUFF_NAMES},0)'
                cond = [f'{x[pb]}<>""', f'INDEX({BUFF_KIND},{mm})="{kind}"']
                if who:
                    cond.append(f'INDEX({BUFF_WHO},{mm})="{who}"')
                terms.append(f'IFERROR(IF(AND({",".join(cond)}),N(INDEX({BUFF_VAL},{mm}))*{x[m]},0),0)')
            ws[f'{t[f"tk{i}"]}{r}'] = '=' + '+'.join(terms)
        # видимые итоги строки
        give = lambda pb, m: (f'IF({x[pb]}="","",{x[pb]}&": +"&ROUND(N(INDEX({BUFF_VAL},MATCH({x[pb]},{BUFF_NAMES},0)))*{x[m]},0)'
                              f'&"% "&LOWER(INDEX({BUFF_KIND},MATCH({x[pb]},{BUFF_NAMES},0)))&" → "'
                              f'&INDEX({BUFF_WHO},MATCH({x[pb]},{BUFF_NAMES},0)))')
        part = lambda cond, text: f'IF({cond},{text}&"; ","")'
        ws[f'{t["d0all"]}{r}'] = f'=IF({ok},0,N({x["dps0"]})*{x["cnt"]})'
        ws[f'{t["costall"]}{r}'] = f'=IF({ok},"",{x["cost"]}*{x["cnt"]})'
        ws[f'{t["dpsall"]}{r}'] = f'=IF({ok},"",{x["dps"]}*{x["cnt"]})'
        ws[f'{t["dpsk"]}{r}'] = f'=IF(OR({ok},N({x["costall"]})=0),"",{x["dpsall"]}/{x["costall"]}*1000)'
        ws[f'{t["check"]}{r}'] = (f'=IF({x["urow"]}="",IF(OR({x["name"]}="",{x["name"]}="{CLEAR}"),"","нет такого юнита"),'
                                  f'IF(N({x["cap"]})=0,"ОК (лимит не указан)",IF({x["cnt"]}>{x["cap"]},"больше лимита!","ОК")))')
        ws[f'{t["role"]}{r}'] = f'=IF({x["urow"]}="","",INDEX({U}${UC["role"]}:${UC["role"]},{x["urow"]}))'
        ws[f'{t["gives"]}{r}'] = (f'=IF({ok},"",IF({x["pb1"]}="","—",IFERROR({give("pb1", "m1")},{x["pb1"]})'
                                  f'&IF({x["pb2"]}="","","; "&IFERROR({give("pb2", "m2")},{x["pb2"]}))))')
        ws[f'{t["trtxt"]}{r}'] = (f'=IF({ok},"",IF({x["trn"]}="","нет",{x["trn"]}&IF({x["tD"]}+{x["tS"]}+{x["tR"]}=0,"",'
                                  f'" (урон +"&{x["tD"]}&"%, SPA −"&{x["tS"]}&"%, радиус +"&{x["tR"]}&"%)")))')
        ws[f'{t["rltxt"]}{r}'] = f'=IF({ok},"",IF({x["rln"]}="","нет",{x["rln"]}))'
        rl = (part(f'{x["rD"]}<>0', f'"урон +"&ROUND({x["rD"]},1)&"%"') + '&' +
              part(f'{x["rC"]}<>0', f'"крит +"&ROUND({x["rC"]},1)&"%"') + '&' +
              part(f'{x["rCD"]}<>0', f'"крит-урон +"&ROUND({x["rCD"]},1)&"%"') + '&' +
              part(f'{x["rDot"]}<>0', f'"DoT +"&ROUND({x["rDot"]},0)&"% ("&{x["rDotK"]}&")"') + '&' +
              part(f'{x["rClk"]}>0', f'"часы +"&ROUND({x["rClk"]},2)&"% урона/с"') + '&' +
              part(f'{x["resm"]}<>1', f'"сопротивление ×"&ROUND({x["resm"]},2)'))
        trim = lambda s: f'LEFT({s},LEN({s})-2)'          # убрать «; » в конце
        ws[f'{t["rleff"]}{r}'] = f'=IF(OR({ok},{x["rln"]}=""),"",IF(({rl})="","ничего для этого юнита",{trim(f"({rl})")}))'
        ps = (part(f'{x["pasv"]}<>0', f'"урон +"&ROUND({x["pasv"]},1)&"%"') + '&' +
              part(f'{x["pc"]}<>0', f'"крит +"&ROUND({x["pc"]},1)&"%"') + '&' +
              part(f'{x["pcd"]}<>0', f'"крит-урон +"&ROUND({x["pcd"]},1)&"%"') + '&' +
              part(f'{x["pdot"]}<>0', f'"DoT +"&ROUND({x["pdot"]},1)&"%"'))
        ws[f'{t["pastxt"]}{r}'] = f'=IF({ok},"",IF(({ps})="","—",{trim(f"({ps})")}))'
        cs = (part(f'{x["kD"]}<>0', f'"урон "&ROUND({x["kD"]},1)&"%"') + '&' +
              part(f'{x["kS"]}<>1', f'"SPA "&ROUND(({x["kS"]}-1)*100,1)&"%"') + '&' +
              part(f'{x["kR"]}<>1', f'"радиус "&ROUND(({x["kR"]}-1)*100,1)&"%"'))
        ws[f'{t["curtxt"]}{r}'] = f'=IF({ok},"",IF(({cs})="","—",{trim(f"({cs})")}))'
        for key, fmt in (('cost', MONEY), ('dps', DPS), ('costall', MONEY), ('dpsall', DPS), ('dpsk', DPS),
                         ('dps0', DPS), ('gain', PLUSPCT)):
            ws[f'{t[key]}{r}'].number_format = fmt
        for i in range(1, len(TEAM_VIS) + 1):
            ws.cell(r, i).border = BOX
        for key in ('gives', 'trtxt', 'rleff', 'pastxt', 'curtxt'):
            ws[f'{t[key]}{r}'].alignment = TOPWRAP
    # строка 13 (скрыта по столбцам): итоги бафов команды по видам
    for i in range(len(TEAM_KINDS)):
        col = t[f'tk{i}']
        ws[f'{col}13'] = f'=SUM({col}5:{col}12)'
    ck = t['check']
    ws.conditional_formatting.add(f'{ck}5:{ck}12', FormulaRule(formula=[f'LEFT(${ck}5,2)="ОК"'], fill=GREEN))
    ws.conditional_formatting.add(f'{ck}5:{ck}12', FormulaRule(formula=[f'OR(${ck}5="больше лимита!",${ck}5="нет такого юнита")'],
                                                                fill=PatternFill('solid', fgColor='FFC7CE')))
    ws.conditional_formatting.add(f'{t["gain"]}5:{t["gain"]}12', CellIsRule(operator='greaterThan', formula=['0'], fill=GREEN))
    # итоги команды
    ws['A15'] = 'ИТОГО КОМАНДА'; ws['A15'].font = BOLD
    sm = lambda key: f'SUM({t[key]}5:{t[key]}12)'
    dps0_all = sm('d0all')
    totals = [('Юнитов на поле', f'={sm("cnt")}', '0'), ('Цена всего', f'={sm("costall")}', MONEY),
              ('DPS всего (с бафами команды)', f'={sm("dpsall")}', DPS),
              ('DPS всего без бафов команды', f'={dps0_all}', DPS),
              ('Бафы команды дали', f'=IF({dps0_all}>0,{sm("dpsall")}/{dps0_all}-1,"")', PLUSPCT),
              ('DPS на 1000 денег', f'=IF({sm("costall")}>0,{sm("dpsall")}/{sm("costall")}*1000,"")', DPS)]
    for i, (label, f, fmt) in enumerate(totals, 15):
        ws[f'E{i}'] = label; ws[f'E{i}'].border = BOX
        c = ws[f'G{i}']; c.value, c.number_format, c.font, c.border = f, fmt, Font(bold=True, size=12), BOX
    ws['I15'] = 'БАФЫ ОТ КОМАНДЫ (всем юнитам)'; ws['I15'].font = BOLD
    labels = {('Урон', 'Физ'): 'Урон физ. юнитам', ('Урон', 'Маг'): 'Урон маг. юнитам', ('Урон', 'Все'): 'Урон всем',
              ('SPA', None): 'Снижение SPA', ('Радиус', None): 'Радиус', ('Крит', None): 'Крит-шанс',
              ('Скидка', None): 'Скидка на апгрейды', ('DoT', 'Все'): 'Усиление всех DoT', ('Призыв', None): 'Урон призывам'}
    labels.update({('DoT', k): f'Усиление DoT: {k.lower()}' for k in DOT_KINDS})
    # показываем то, что реально действует: «не складываются» уже вычтены
    ns_on_all = lambda n: f'(COUNTIF({pb_rng("pb1")},{S}$A${BUFF_ROW[n]})+COUNTIF({pb_rng("pb2")},{S}$A${BUFF_ROW[n]}))>0'
    ns_val_all = lambda n: f'{S}$C${BUFF_ROW[n]}'
    shown = {('Урон', 'Все'): f'-{nostack_expr("Урон", ns_on_all, ns_val_all)}',
             ('SPA', None): f'-{nostack_expr("SPA", ns_on_all, ns_val_all)}'}
    for j, kw in enumerate(TEAM_KINDS):
        ws.cell(16 + j, 9, labels[kw]).border = BOX
        c = ws.cell(16 + j, 11, f'={tot(j)}{shown.get(kw, "")}'); c.number_format = '0"%"'; c.border = BOX; c.font = BOLD
    ws['A22'] = ('Бафы команды: бафферы, которых ты ставишь в команду, дают бафы всем юнитам команды (силу бафа можно поправить '
                 'в таблице бафов «Настроек»). Commander / Wind Dragon ×4 = бесконечный баф 100%. Zombie (Risen) и Chuuni — за каждую копию. '
                 'Blossom не складывается с Idol, Trickster (SPA) — с Priest. Бафы, включённые в «Настройках», здесь НЕ добавляются.')
    ws['A22'].font = HINT
    ws['A22'].alignment = Alignment(wrap_text=True, vertical='top')
    ws.merge_cells('A22:H25')
    dv_list(ws, UNIT_PICK['Команда'], f'{t["name"]}5:{t["name"]}12')
    dv_list(ws, UPG_LIST, f'{t["upg"]}5:{t["upg"]}12')
    from openpyxl.comments import Comment
    ws['D3'] = '🔍 Поиск юнита:'; ws['D3'].font = BOLD; ws['D3'].alignment = Alignment(horizontal='right')
    inp(ws['E3'])
    ws['E3'].comment = Comment('Впиши часть имени — в списке юнитов останутся только подходящие. Твои юниты («Есть у меня») — первыми.', AUTHOR)
    for k, _, w in TEAM_VIS:
        ws.column_dimensions[t[k]].width = w
    for k in t:
        if k not in dict((kk, 1) for kk, _, _ in TEAM_VIS):
            ws.column_dimensions[t[k]].hidden = True
    ws.freeze_panes = 'B5'
    return ws


# ── Главная ────────────────────────────────────────────────────────────
def sheet_home(wb, end, n_units):
    ws = wb.create_sheet('Главная', 0)
    ws.sheet_properties.tabColor = 'C00000'
    title(ws, 'Anime Adventures — юниты', f'{n_units} юнитов с вики. Нажми на название листа, чтобы перейти')
    nav = [('Сравнение', 'сравнить юнитов: свой апгрейд, уровень и бафы в каждой строке + графики'),
           ('Команда', 'собрать свою команду: общая цена, DPS, проверка лимита'),
           ('Настройки', 'уровень юнитов, цели под AoE, какие бафы стоят на карте'),
           ('Трейты', 'все трейты и их бонусы — можно менять и добавлять свои'),
           ('Реликвии', 'все реликвии с вики — впиши свои роллы или свою реликвию'),
           ('Юниты', 'все юниты: сортировка, фильтры, тиры, отметка «Есть у меня»'),
           ('Апгрейды', 'каждый шаг каждого юнита и выгодность апгрейда'),
           ('Справка', 'как всё считается')]
    for i, (sheet, desc) in enumerate(nav, 4):
        c = ws.cell(i, 2, '→ ' + sheet); link(c, sheet)
        ws.cell(i, 3, desc).font = HINT
    tables = [('A', 'СИЛЬНЕЙШИЕ (DPS)', 'hd'), ('H', 'САМЫЕ ВЫГОДНЫЕ (DPS на 1000)', 'hv'),
              ('O', 'ЛУЧШИЕ ИЗ МОИХ («Есть у меня» = Да)', 'hm')]
    top = 14
    for start, name, helper in tables:
        c0 = ws[f'{start}1'].column
        ws.cell(top - 1, c0, name).font = Font(bold=True, size=12, color='1F3864')
        for j, t in enumerate(('№', 'Юнит', 'Редкость', 'DPS', 'DPS на 1000')):
            x = ws.cell(top, c0 + j, t); x.fill, x.font, x.alignment, x.border = HEAD, WHITE_B, CENTER, BOX
        hcol = get_column_letter(c0 + 5)     # скрытый: номер строки на «Юнитах»
        hr = ucol(helper, end)
        for k in range(1, 16):
            r = top + k
            ws.cell(r, c0, k).alignment = Alignment(horizontal='center')
            ws[f'{hcol}{r}'] = f'=IFERROR(IF(LARGE({hr},{k})<0,"",MATCH(LARGE({hr},{k}),{hr},0)),"")'
            for j, key in enumerate(('name', 'rarity', 'dps', 'dpsk'), 1):
                cell = ws.cell(r, c0 + j, f'=IF(${hcol}{r}="","",INDEX({ucol(key, end)},${hcol}{r}))')
                cell.border = BOX
                if key in ('dps', 'dpsk'): cell.number_format = DPS
            ws.cell(r, c0).border = BOX
        rarity_cf(ws, f'{get_column_letter(c0 + 2)}{top + 1}:{get_column_letter(c0 + 2)}{top + 15}')
        ws.column_dimensions[hcol].hidden = True
        for j, w in enumerate((4, 32, 12, 11, 11)):
            ws.column_dimensions[get_column_letter(c0 + j)].width = w
    ws.column_dimensions['G'].width = 3; ws.column_dimensions['N'].width = 3
    ws.column_dimensions['B'].width = 32
    ws['A30'] = 'Топы считаются с текущими «Настройками». Отметь своих юнитов на листе «Юниты» (столбец «Есть у меня»)'
    ws['A30'].font = HINT
    return ws


CLEAR = '— убрать'
UPG_LIST = '"' + ','.join(str(i) for i in range(0, 14)) + '"'   # апгрейд 0…13 (выше максимума юнита — его максимум)
LISTS = "'Списки'!"


SEARCH_CELLS = {'Сравнение': "'Сравнение'!$E$3", 'Команда': "'Команда'!$E$3"}


def sheet_lists(wb, units):
    """Скрытый лист для выпадающих списков: первым пунктом «— убрать», чтобы очищать ячейку выбором.
    C/D — список юнитов «Сравнения», отфильтрованный по полю поиска; E/F — то же для «Команды».
    Свои юниты («Есть у меня» = Да) идут в списке первыми. G — признак «мой». H:M — кто какой баф даёт (TEAM_BUFFS)."""
    ws = wb.create_sheet('Списки')
    n = len(units) + 1
    end = 4 + len(units)
    ws['A1'] = CLEAR
    for i, u in enumerate(units, 2):
        ws.cell(i, 1, u['name'])
        ws.cell(i, 7, f'=IFERROR(INDEX({U}${UC["mine"]}$5:${UC["mine"]}${end},MATCH($A{i},{U}$A$5:$A${end},0))="Да",FALSE)')
    ws['B1'] = CLEAR
    for i, r in enumerate(range(BUFF_FIRST, BUFF_LAST + 1), 2):
        ws.cell(i, 2, f'=IF({S}A{r}="","",{S}A{r})')
    picks = {}
    for (sheet, q), (key, lst) in zip(SEARCH_CELLS.items(), (('C', 'D'), ('E', 'F'))):
        ws[f'{lst}1'] = CLEAR
        query = f'TRIM({q}&"")'
        for i in range(2, n + 1):
            # ключ порядка: подходит под поиск → свои юниты (0…) раньше остальных (100000…), внутри — исходный порядок
            ws[f'{key}{i}'] = f'=IF(OR({query}="",ISNUMBER(SEARCH({query},$A{i}))),IF($G{i},0,100000)+{i},"")'
            ws[f'{lst}{i}'] = (f'=IFERROR(INDEX($A$1:$A${n},MATCH(SMALL(${key}$2:${key}${n},{i - 1}),'
                               f'${key}$1:${key}${n},0)),"")')
        picks[sheet] = f'{LISTS}${lst}$1:${lst}${n}'
    for i, (name, b) in enumerate(TEAM_BUFFS.items(), 1):
        for j, v in enumerate((name,) + b):
            ws.cell(i, 8 + j, v)
    ws.sheet_state = 'hidden'
    return picks, f'{LISTS}$B$1:$B${BUFF_LAST - BUFF_FIRST + 2}'


def sheet_help(wb, n_units, n_rows):
    ws = wb.create_sheet('Справка')
    ws.sheet_properties.tabColor = '808080'
    ws.column_dimensions['A'].width = 125
    lines = [
        ('Как пользоваться', True),
        ('1. «Главная» — топы и ссылки на листы.', False),
        ('2. «Сравнение» — юнит, апгрейд, уровень (1/100/110), до 4 бафов, трейт, реликвия и пассивка прямо в строке.', False),
        ('   Сверху: 🔍 Поиск юнита (E3) — фильтрует список юнитов; ⏱ Время боя (H3) — для «урона за время боя».', False),
        ('   Пустой трейт/реликвия = как выставлено юниту на «Юнитах». «Макс. удар» = урон крита со всеми бонусами.', False),
        ('   «DPS без бафов саппортов» — с трейтом, реликвией и пассивкой, но без бафферов; «Бафы дали» — во сколько выросло.', False),
        ('3a. «Трейты» и «Реликвии» — все с вики, цифры можно менять, в пустые строки — свои (например, своя реликвия со своими роллами).', False),
        ('3b. На «Юнитах» у каждого юнита: Трейт, Реликвия, 4 поля пассивки, 4 проклятия, свои %. Действуют на ВСЕ листы, включая «Сравнение».', False),
        ('3. «Команда» — свой состав с количеством, внизу общая цена и DPS (бафы — из «Настроек»).', False),
        ('4. «Настройки» — уровень юнитов, сколько врагов попадает под AoE, бафы (Активен = Да) и свои бафы в пустых строках.', False),
        ('5. «Юниты» — все юниты на макс. апгрейде. Стрелка в заголовке → «Сортировка по возрастанию/убыванию» или фильтр.', False),
        ('   Удобные сортировки: «Место по выгоде» (1 = самый выгодный), «Место по DPS», «№ редк.» (1 = Эксклюзив … 6 = Редкий).', False),
        ('   Тиры S/A/B/C/D: S — верхние 10% юнитов, A — следующие 20%, B — 30%, C — 25%, D — нижние 15%.', False),
        ('   Фильтр «Есть у меня = Да» оставит только твоих. Имя юнита — ссылка на его строки на «Апгрейдах».', False),
        ('6. «Апгрейды» — каждый шаг. «Прирост DPS на 1000 за шаг» показывает, выгоднее прокачать или поставить ещё одного.', False),
        ('Жёлтое — меняешь сам. Серое — данные вики. Белое — формулы, их не трогать.', False),
        ('', False),
        ('Как считается', True),
        ('Урон итог = урон(вики) × уровень × (1 + общий) × (1 + 5% × Limit Break отряда) × (1 + свой %) × (1 + проклятие %)', False),
        ('   × (1 + пассивка + реликвия) × (1 + трейт) × (1 + PWR × 1,75%) × сопротивление × (1 + бафы саппортов) — всё ОТДЕЛЬНЫЕ множители', False),
        ('   Сверено с игрой: Shinobi (Eternal) 16 800 × 10,953 (ур.110) × 1,183 × 1,071 × 1,10 = 256 450 (в игре 256K).', False),
        ('SPA итог = SPA(вики) × (1 − (общее снижение + своё + баф SPA) / 100) × (1 − SPA трейта / 100) × (1 + проклятие SPA / 100)', False),
        ('Радиус = радиус(вики) × (1 + бафы / 100) × (1 + трейт / 100) × (1 + проклятие радиуса / 100)', False),
        ('Жёлтые % на «Юнитах» понимают 12, 12,5, «12,5%» и даже текст «12.5». В «Сравнении» номер апгрейда и количество тоже можно текстом.', False),
        ('DPS удара = урон итог / SPA итог.  Крит: × (1 + шанс × (множитель крита − 1)), реликвии добавляют шанс и крит-урон', False),
        ('Реликвия «Урон %» действует, если её тип совпадает с типом урона юнита (Физ/Маг) или его стихией (столбец «Стихии»).', False),
        ('Пассивки: 4 жёлтых столбца у юнита — +% урона, +% крит-шанса, +% крит-урона, +% к DoT. Предзаполнены по страницам вики', False),
        ('   (Battlelust, Sunshine, Spellforged Blades ×2, крит ×2 Switchblade, чистый урон Black Blade/Curse/Chuuni, OverCrit Sepsis и др.).', False),
        ('   Условные пассивки (волны, бездействие, ульты) — 0, подсказка с числами в столбце «Пассивки (из вики)». В «Сравнении» «Пассивка = Нет» выключает все 4.', False),
        ('Кровотечение считается от урона С бафами саппортов (30% при бафе +100% = 60%, вики Effects); горение, яд, иссушение — от урона БЕЗ бафов.', False),
        ('DPS DoT = урон итог × множитель DoT × тики / SPA (горение и кровотечение за каждую атаку)', False),
        ('DPS итог = (DPS удара с критом + DPS DoT + часы реликвии) × число целей + DPS призывов', False),
        ('DPS призывов = множитель урона юнита × (урон призывов за цикл / цикл + урон за убийство × убийств/с) × (1 + бафы «Призыв»)', False),
        ('Урон за время боя: атаки в 0, SPA, 2·SPA…; DoT каждой атаки тикает раз в «интервал тика»; к концу боя часть DoT не дотикала — '
         'это учитывается приблизительно (по времени, без округления тиков)', False),
        ('Цена всего = цена постановки + сумма апгрейдов; скидка (Idol (Star)) уменьшает только апгрейды', False),
        ('DPS на 1000 = DPS итог / цена всего × 1000 — главный показатель выгодности', False),
        ('Бафы саппортов складываются между собой (Commander 100% + Blossom 10% = ×2,1) и умножают урон отдельно от статов: Wind Dragon ×4 = ×2. '
         'Физ-бафы действуют только на физ. юнитов, маг — на маг.', False),
        ('Призывы: урон одного удара (столбец «Призыв: урон одного удара») = HP/урон призыва × множитель урона юнита × бафы «Призыв». '
         'Медузы Elyssia — раз в SPA, ≤3, откат 1,5×SPA и «время пути до врага» из «Настроек»; угри — за 5 убийств, ≤3, живут 60 с.', False),
        ('«Ударов» не умножает урон: по вики урон делится на число ударов (это про снятие щитов).', False),
        ('', False),
        ('Что НЕ учтено автоматически (поправь вручную на «Юнитах» → «Свой +% урона» / «Свой −% SPA»)', True),
        ('• Разброс статов ±10% у каждой копии юнита, трейты, шайни-бонус, реликвии', False),
        ('• Активные способности (ульты) и пассивки, которых нет в данных вики (впиши их в «Пассивка, %»)', False),
        ('• PWR у реликвий; ситуативные бонусы реликвий — только если включены в «Настройках»', False),
        ('', False),
        ('Учтено после проверки всей вики (09.11.2026)', True),
        ('• Limit Break: уровень 110 = урон ×9,204 × 1,19; «Юнитов с Limit Break в отряде» даёт +5% урона всем за каждого (до +30%).', False),
        ('• Blossom НЕ складывается с Idol / Idol (Star) — если включены оба, считается только больший (страницы Blossom, Idol).', False),
        ('• Сопротивление врага: урон × 100 / (100 + сопротивление − PEN реликвии); чистый урон его игнорирует.', False),
        ('• Новые бафы: Priest (Heaven) −50% SPA (30 с из 300), Devil Boss +50% урона, дебафф Chuuni (Delusion) +50…150% маг.', False),
        ('• Реликвия Mangekyō Eye — горение ×2. Пассивки 13 юнитов со страниц вики — в столбце «Пассивки (из вики)».', False),
        ('• Bleed Amplification (Bloodcry, Blood) — ×3,5…×5 урона от всех кровотечений; бафы урона усиливают и DoT.', False),
        ('', False),
        ('Ситуативное — не считается автоматически (впиши своим бафом или «свой %», если нужно)', True),
        ('• Слабости врагов складываются: урон × (1 + слабость к типу + слабость к стихии). Летающие получают 50% от наземных юнитов,', False),
        ('  бронированные — ½ от AoE (Full), ледяные враги получают ×3 от огня и горения.', False),
        ('• Бафы турнира и контрактов по стихиям (до +500%), скины ивентов (+50…+5000% только в своём ивенте).', False),
        ('• Челленджи: High Cost — цена ×1,5 (Idol (Star) отменяет), Triple Cost — ×3, Short/Mini Range — радиус меньше.', False),
        ('• Ранг статов (реролл): урон −10…+20%, SPA ±10%, радиус ±10% — вписывай в «Свой %» юнита. '
         'Проклятия (Curses, ±2,5–13%) — в столбцы «Проклятие 1–4».', False),
        ('• Шайни — только внешний вид, статов не дают (FAQ вики).', False),
        ('• Дебаффы врагов в таблице бафов складываются с бафами, в игре они множатся — это приближение', False),
        ('• Призывы Lulu, Lyla, Ghosty, Violentine, Shadow Sorcerer (Ritual) — на вики нет их урона, только описание; фермы', False),
        ('• Сортировать можно «Юниты» (вернуть порядок — по «№»). «Апгрейды» не сортируй — только фильтр.', False),
        ('', False),
        ('Источник', True),
        (f'Вики animeadventures.fandom.com — модуль Module:UnitData/Data (база всех юнитов), {n_units} юнитов, {n_rows} строк апгрейдов.', False),
        ('Бафы — страницы Commander, Wind Dragon, Elfy (Sylph), Blossom, Griffin (Reincarnation), Skeleton (Soul King), Idol, Trickster (Release), Gambler (Jackpot), Effects.', False),
        ('Множитель 100 уровня (×9,204) и крит ×1,5 — из шаблонов вики Stats Box и страницы Effects.', False),
        ('Обновить данные: закрыть книгу → python -I tools\\update_wiki.py → python -I tools\\build_units.py (папка AnimeAdventures)', False),
    ]
    for i, (t, b) in enumerate(lines, 1):
        c = ws.cell(i, 1, t)
        c.font = Font(bold=True, size=13, color='1F3864') if b else Font()
        c.alignment = Alignment(wrap_text=True)
    return ws


# ── перенос ручных правок из прошлой версии ────────────────────────────
DEFAULTS_SHEET = '_defaults'
SKIP_SHEETS = ('Апгрейды', 'Списки', 'Автор', DEFAULTS_SHEET)
# значения по умолчанию прошлой версии, которые поменялись (для старых книг без листа _defaults)
LEGACY_DEFAULTS = {('Реликвии', f'E{RELIC_FIRST + [r[0] for r in RELICS].index("Miracle Timepiece")}'): 'Все'}


def yellow_cells(wb):
    """Все жёлтые ячейки книги: ключ → (лист, ячейка). «Юниты» — по имени юнита и заголовку столбца."""
    out = {}
    for ws in wb.worksheets:
        if ws.title in SKIP_SHEETS:
            continue
        if ws.title == 'Юниты':
            heads = {c: ws.cell(4, c).value for c in range(1, ws.max_column + 1)
                     if ws.cell(5, c).fill.fgColor.rgb in YELLOW_RGB}
            for r in range(5, ws.max_row + 1):
                name = ws.cell(r, 1).value
                if name:
                    for c, h in heads.items():
                        out[('Юниты', name, h)] = ws.cell(r, c)
        else:
            for row in ws.iter_rows():
                for c in row:
                    if c.fill.fgColor.rgb in YELLOW_RGB:
                        out[(ws.title, c.coordinate)] = c
    return out


def _norm(v):
    if v is None or (isinstance(v, str) and v.strip() == ''):
        return None
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        return round(float(v), 9)
    return str(v)


def read_inputs(path):
    """Жёлтые ячейки старой книги (вместе с пустыми) и её значения по умолчанию (лист _defaults)."""
    if not os.path.exists(path):
        return None
    from openpyxl import load_workbook
    old = load_workbook(path)
    values = {k: c.value for k, c in yellow_cells(old).items() if not str(c.value).startswith('=')}
    # формат «%» важен: «20%» хранится как 0,2 и читается формулой как 20 только в ячейке с форматом процентов
    formats = {k: c.number_format for k, c in yellow_cells(old).items()
               if isinstance(c.value, (int, float)) and '%' in (c.number_format or '')}
    defaults = None
    if DEFAULTS_SHEET in old.sheetnames:
        defaults = {}
        for k, v in old[DEFAULTS_SHEET].iter_rows(min_row=1, values_only=True):
            if k:
                defaults[tuple(json.loads(k))] = v
    return {'values': values, 'defaults': defaults, 'formats': formats}


def restore_inputs(wb, saved, new_defaults):
    """Правило: если старое значение = старому значению по умолчанию — пользователь ячейку не трогал,
    берём новое значение по умолчанию. Иначе (изменил ИЛИ стёр) — переносим старое, в том числе пустоту."""
    old_def = saved['defaults']
    if old_def is None:                                  # книга до появления _defaults
        old_def = dict(new_defaults)
        old_def.update(LEGACY_DEFAULTS)
    cells = yellow_cells(wb)
    for key, v in saved['values'].items():
        if key in cells and _norm(v) != _norm(old_def.get(key)):
            cells[key].value = v
            if key in saved.get('formats', {}):
                cells[key].number_format = saved['formats'][key]
    # строки «Сравнения»/«Команды» без юнита — убрать хвосты (бафы, трейт, уровень от прошлых примеров)
    for title_, last_row, cols in (('Сравнение', CMP_LAST, range(2, len(CMP_SPEC) + 1)), ('Команда', 12, range(2, 4))):
        ws = wb[title_]
        for r in range(5, last_row + 1):
            if ws.cell(r, 1).value in (None, '', CLEAR):
                for c in cols:
                    cell = ws.cell(r, c)
                    if cell.fill.fgColor.rgb in YELLOW_RGB:
                        cell.value = None


def write_defaults(wb, defaults):
    ws = wb.create_sheet(DEFAULTS_SHEET)
    i = 1
    for k, v in defaults.items():
        if v is not None:
            ws.cell(i, 1, json.dumps(list(k), ensure_ascii=False))
            ws.cell(i, 2, v)
            i += 1
    ws.sheet_state = 'veryHidden'


AUTHOR = 'Петров Игнат'
AUTHOR_CELL = "'Автор'!$B$2"
# листы, которые защищаются в режиме --protect. «Юниты» и «Апгрейды» — нет: на защищённом листе
# LibreOffice не даёт сортировать, а сортировка там нужна
PROTECTED_SHEETS = ('Главная', 'Сравнение', 'Команда', 'Настройки', 'Трейты', 'Реликвии', 'Справка')
PASSWORD_FILE = os.path.join(ROOT, 'ЗАЩИТА — пароль.txt')


def author_sheet(wb, n_units, n_rows):
    """Суперскрытый лист с отметкой автора — источник имени для всех надписей «©»."""
    from datetime import date
    ws = wb.create_sheet('Автор')
    rows = [('Отметка автора', ''), ('Автор', AUTHOR), ('Создано', date.today().strftime('%d.%m.%Y')),
            ('Таблица', 'Anime Adventures — юниты: сравнение, DPS, DPS на 1000, бафы, трейты, реликвии, пассивки'),
            ('Данные', f'вики animeadventures.fandom.com: {n_units} юнитов, {n_rows} строк апгрейдов'),
            ('Права', f'© {AUTHOR}. Все расчёты и оформление — авторская работа')]
    for i, (k, v) in enumerate(rows, 1):
        ws.cell(i, 1, k).font = BOLD
        ws.cell(i, 2, v)
    ws.column_dimensions['A'].width, ws.column_dimensions['B'].width = 14, 90
    ws.sheet_state = 'veryHidden'


def watermark(wb):
    """Водяной знак автора: формула-надпись в верхней строке каждого листа (имя — с листа «Автор»),
    примечание к заголовку, колонтитулы (печать/PDF), свойства файла и скрытое имя «Автор»."""
    from openpyxl.comments import Comment
    from openpyxl.workbook.defined_name import DefinedName
    for ws in wb.worksheets:
        if ws.sheet_state != 'visible':
            continue
        c = ws.cell(1, 10, f'="© "&{AUTHOR_CELL}')
        c.font = Font(italic=True, bold=True, size=12, color='A6A6A6')
        note = Comment(f'Автор таблицы: {AUTHOR}', AUTHOR)
        note.width, note.height = 220, 40
        ws['A1'].comment = note
        for hf in (ws.oddHeader, ws.evenHeader):
            hf.right.text = AUTHOR
        for hf in (ws.oddFooter, ws.evenFooter):
            hf.center.text = f'© {AUTHOR} · стр. &P из &N'
    p = wb.properties
    p.creator = p.lastModifiedBy = AUTHOR
    p.title = 'Anime Adventures — юниты'
    p.subject = f'Автор: {AUTHOR}'
    p.keywords = f'{AUTHOR}; Anime Adventures; DPS'
    p.description = f'© {AUTHOR}. Таблица юнитов Anime Adventures'
    dn = DefinedName('Автор', attr_text=AUTHOR_CELL, hidden=True)
    try:
        wb.defined_names['Автор'] = dn          # openpyxl 3.1
    except TypeError:
        wb.defined_names.append(dn)


def protect(wb):
    """Защита для копии, которую раздают: жёлтые ячейки открыты, остальное (знак, формулы) — под паролем."""
    from openpyxl.styles import Protection
    from openpyxl.workbook.protection import WorkbookProtection
    import secrets
    if os.path.exists(PASSWORD_FILE):
        pwd = open(PASSWORD_FILE, encoding='utf-8').read().split('Пароль:')[-1].strip().splitlines()[0].strip()
    else:
        pwd = 'AA-' + secrets.token_hex(4)
        open(PASSWORD_FILE, 'w', encoding='utf-8').write(
            'Пароль защиты таблицы AA_юниты.xlsx (копия для раздачи)\n'
            'Снимает защиту листов (Сервис → Защитить лист) и структуры книги (Сервис → Защитить книгу).\n'
            f'Пароль: {pwd}\n')
    for name in PROTECTED_SHEETS:
        ws = wb[name]
        for row in ws.iter_rows():
            for cell in row:
                if cell.fill.fgColor.rgb in YELLOW_RGB:
                    cell.protection = Protection(locked=False)
        sp = ws.protection
        sp.sheet = True
        sp.password = pwd
        # разрешено: выделять, менять ширину/высоту, фильтровать
        sp.formatColumns = sp.formatRows = sp.autoFilter = sp.sort = False
        sp.selectLockedCells = sp.selectUnlockedCells = False
    wb.security = WorkbookProtection(lockStructure=True)
    wb.security.workbookPassword = pwd
    return pwd


def main():
    lock = os.path.join(os.path.dirname(OUT), '.~lock.' + os.path.basename(OUT) + '#')
    if os.path.exists(lock):
        sys.exit('Книга открыта в LibreOffice — закрой её и запусти снова (иначе правки потеряются)')
    saved = read_inputs(OUT)
    units = load()
    wb = Workbook(); wb.remove(wb.active)
    r = 5                                # строки «Апгрейдов» известны заранее — листы ссылаются друг на друга
    for u in units:
        u['first'], u['last'] = r, r + len(u['rows']) - 1
        r = u['last'] + 1
    sheet_settings(wb)
    sheet_traits(wb)
    sheet_relics(wb)
    _, end = sheet_units(wb, units)
    sheet_upgrades(wb, units, end)
    names = {u['name'] for u in units}
    pick = [n for n in ('Vengeful Swordsman (Sky Reaver)', 'Kansai (Daydream)', 'Chuuni (Delusion)',
                        'Violentine (Brutal Angel)', 'Sorcerer Killer (Heavenly Body)') if n in names]
    demo = [{'name': n} for n in pick]
    if len(pick) >= 2:   # пример: те же юниты на 100 уровне с бафами, трейтом и реликвией
        demo += [{'name': pick[0], 'lvl': '100', 'trait': 'Superior III', 'relic': 'Nail',
                  'buffs': ('Griffin (Reincarnation)', 'Commander ×4 (бесконечный баф)', 'Blossom')},
                 {'name': pick[1], 'lvl': '100', 'trait': 'Godspeed', 'relic': 'Clover Of The Wind',
                  'buffs': ('Griffin (Reincarnation)', 'Wind Dragon ×4 (бесконечный баф)', 'Blossom')}]
    # примеры с DoT: кровотечение под Bleed Amplification, чёрное пламя с Infernal Gaze
    demo += [d for d in ({'name': 'Saka (Ribbon)', 'buffs': ('Bloodcry (Fallen) — Bleed Amp ×5',)},
                         {'name': 'Izo (Black Fire)', 'relic': 'Infernal Gaze'}) if d['name'] in names]
    global UNIT_PICK, BUFF_PICK
    UNIT_PICK, BUFF_PICK = sheet_lists(wb, units)
    sheet_compare(wb, end, demo)
    sheet_team(wb, end, [(n, 1) for n in pick[:3]])
    sheet_home(wb, end, len(units))
    sheet_help(wb, len(units), sum(len(u['rows']) for u in units))
    author_sheet(wb, len(units), sum(len(u['rows']) for u in units))
    order = ['Главная', 'Сравнение', 'Команда', 'Настройки', 'Трейты', 'Реликвии', 'Юниты', 'Апгрейды', 'Справка',
             'Списки', 'Автор']
    wb._sheets = [wb[n] for n in order]
    new_defaults = {k: c.value for k, c in yellow_cells(wb).items()}
    if saved:
        restore_inputs(wb, saved, new_defaults)
        print('жёлтые ячейки перенесены из прошлой версии')
    write_defaults(wb, new_defaults)
    watermark(wb)
    if PROTECT:
        protect(wb)
        print('защита включена, пароль в', PASSWORD_FILE)
    wb.active = 0
    wb.save(OUT)
    print('OK', OUT, len(units), 'юнитов', sum(len(u['rows']) for u in units), 'строк апгрейдов')


if __name__ == '__main__':
    main()
