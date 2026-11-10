# Anime Adventures — калькулятор юнитов

Веб-справочник и калькулятор юнитов игры **Anime Adventures** (Roblox):
урон, DPS, DPS на 1000 ¥, апгрейды, тиры, бафы, трейты, реликвии и пассивки.

**Сайт:** откройте `web/index.html` (или страницу GitHub Pages этого репозитория).

## Как устроено

| Папка / файл | Что это |
|---|---|
| `web/` | Сайт: `index.html`, расчётная модель `model.js`, данные `units.js` |
| `tools/update_wiki.py` | Скачивает Lua-модули с вики и разбирает их в `data/*.json` |
| `tools/luaparse.py` | Парсер Lua-таблиц **как данных** — код вики не исполняется |
| `tools/export_web.py` | Собирает `web/units.js` из `data/*.json` |
| `tools/build_units.py` | Общие константы и расчёты (и генератор Excel-версии) |
| `data/` | Данные вики: исходные `.lua` и разобранные `.json` |

Обновить данные вручную:

```bash
pip install openpyxl
python -I tools/update_wiki.py
python -I tools/export_web.py
```

Данные на сайте обновляются автоматически раз в день (GitHub Actions).

## Источник данных и лицензия

Данные о юнитах взяты с **[Anime Adventures Wiki](https://animeadventures.fandom.com/)**
(модули `Module:UnitData/Data` и `Module:UnitData/Data/AoE_Type`)
и распространяются по лицензии **[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)**,
как и исходный контент вики. Файлы `data/*` и `web/units.js` — производные от этих данных
и тоже доступны по CC BY-SA.

Проект неофициальный и не связан с разработчиками игры или Fandom.
