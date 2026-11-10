/* Расчётная модель AA Units — перенос формул из Excel-генератора (tools/build_units.py, engine()).
   Работает и в браузере (window.AAModel), и в Node (require) — для сверки с Excel. */
(function (root) {
  'use strict';

  const DEFAULT_SETTINGS = {
    lvl: '1',          // 1 / 100 / 110 / custom
    lvlCustom: 1,
    lb: 0,             // юнитов с Limit Break в отряде (0–6): +5% урона за каждого
    gDmg: 0, gSpa: 0, gCrit: 0, gRng: 0,
    critDef: 1.5,      // множитель крита по умолчанию
    dot: true,         // учитывать DoT
    sit: false,        // ситуативные бонусы реликвий
    resP: 0, resM: 0,  // сопротивление врага
    tick: 1,           // интервал тика DoT, с
    kps: 1,            // врагов убивается в секунду (призывы «за убийства»)
    walk: 5,           // время пути призыва до врага, с
    pwrp: 1.75,        // 1 PWR = +% урона
    time: 30,          // время боя для «урона за бой», с
    targets: {},       // тип атаки → целей под ударом (по умолчанию 1)
  };

  function lvlMul(v, D, custom) {
    const s = String(v == null ? '' : v);
    if (s === '110') return D.lvl110;
    if (s === '100') return D.lvl100;
    if (s === 'custom') return Number(custom) || 1;
    return 1;
  }

  // фрагменты правил призыва из генератора: только числа, {E}, {S}, + - * / ( ) — проверяем и считаем
  const SAFE = /^[0-9eE.+\-*/() ]*$/;
  function evalFrag(expr, E, S) {
    if (expr == null || expr === '') return 0;
    if (typeof expr === 'number') return expr;
    const s = String(expr).split('{E}').join('(' + E + ')').split('{S}').join('(' + S + ')');
    if (!SAFE.test(s)) return 0;
    try { const v = Function('"use strict";return (' + s + ')')(); return isFinite(v) ? v : 0; } catch (e) { return 0; }
  }

  // сумма бафов вида kind, подходящих юниту (who: «Все» или совпадает с match); дубли — один раз; NO_STACK — меньшая группа вычитается
  function buffSum(D, names, kind, match) {
    const uniq = [...new Set(names || [])];
    const by = D._buffBy || (D._buffBy = Object.fromEntries(D.buffs.map(b => [b.n, b])));
    let total = 0;
    const on = [];
    for (const n of uniq) {
      const b = by[n];
      if (!b || b.kind !== kind) continue;
      if (match !== undefined && b.who !== 'Все' && b.who !== match) continue;
      total += Number(b.v) || 0;
      on.push(n);
    }
    for (const g of D.noStack) {
      if (g.kind !== kind) continue;
      const a = on.filter(n => g.a.includes(n)).map(n => by[n].v);
      const b = on.filter(n => g.b.includes(n)).map(n => by[n].v);
      if (a.length && b.length) total -= Math.min(Math.max(...a), Math.max(...b));
    }
    return total;
  }

  function rowObj(D, u, i) {
    const r = u.rows[Math.max(0, Math.min(i, u.rows.length - 1))];
    const o = {};
    D.rowKeys.forEach((k, j) => { o[k] = r[j]; });
    return o;
  }

  /* Расчёт одного юнита.
     opt: { upg (номер апгрейда, null = максимум), lvl ('1'/'100'/'110', null = из настроек), buffs: [имена],
            trait, relic (имена, null = из профиля юнита), passive (true/false), inp: профиль юнита } */
  function calc(D, u, opt, S) {
    S = Object.assign({}, DEFAULT_SETTINGS, S || {});
    opt = opt || {};
    const inp = Object.assign({ pas: u.pp, pasc: u.pc, pascd: u.pcd, pasdot: u.pdot, cd: 0, cs: 0, cc: null,
      curD: 0, curS: 0, curR: 0, trait: '', relic: '' }, opt.inp || {});
    const upg = opt.upg == null || opt.upg === '' ? u.rows.length - 1 : Math.max(0, Math.min(parseInt(opt.upg, 10) || 0, u.rows.length - 1));
    const row = rowObj(D, u, upg);
    const lvl = lvlMul(opt.lvl == null || opt.lvl === '' ? S.lvl : opt.lvl, D, S.lvlCustom);
    const dt = u.dt, el = u.el || '';
    const fits = t => !!t && (t === 'Все' || t === dt || el.indexOf(t) >= 0);

    const tr = (D.traits.find(t => t.n === (opt.trait || inp.trait)) || { d: 0, s: 0, r: 0 });
    const rl = (D.relics.find(t => t.n === (opt.relic || inp.relic)) ||
      { d1: 0, t1: '', d2: 0, t2: '', c: 0, ct: '', cd: 0, sit: 0, dot: 0, dotk: '', pen: 0, penk: '', clkn: 0, clkp: 0, pwr: 0, pwrk: '' });
    const rD = (fits(rl.t1) ? +rl.d1 || 0 : 0) + (fits(rl.t2) ? +rl.d2 || 0 : 0) + (S.sit ? +rl.sit || 0 : 0);
    const rC = (!rl.ct || fits(rl.ct)) ? +rl.c || 0 : 0;
    const rCD = +rl.cd || 0;
    const rPwr = fits(rl.pwrk) ? +rl.pwr || 0 : 0;
    const rClk = dt === 'Маг' && rl.clkn > 0 ? rl.clkp / rl.clkn : 0;
    const pen = (rl.penk === 'Все' || rl.penk === dt) ? +rl.pen || 0 : 0;
    const res = dt === 'Физ' ? S.resP : dt === 'Маг' ? S.resM : 0;
    const resm = dt === 'Чистый' ? 1 : 100 / (100 + Math.max(0, (+res || 0) - pen));

    const pass = opt.passive !== false;
    const pasv = pass ? +inp.pas || 0 : 0, pc = pass ? +inp.pasc || 0 : 0;
    const pcd = pass ? +inp.pascd || 0 : 0, pdot = pass ? +inp.pasdot || 0 : 0;
    const cd = +inp.cd || 0, cs = +inp.cs || 0, kD = +inp.curD || 0;
    const kS = Math.max(0.1, 1 + (+inp.curS || 0) / 100), kR = Math.max(0.1, 1 + (+inp.curR || 0) / 100);
    const GD = ((1 + (+S.gDmg || 0) / 100) * (1 + 0.05 * Math.min(6, Math.max(0, +S.lb || 0))) - 1) * 100;

    const B = opt.buffs || [];
    const dk = row.dotkind || '';
    const bd = buffSum(D, B, 'Урон', dt), bs = buffSum(D, B, 'SPA'), br = buffSum(D, B, 'Радиус');
    const bc = buffSum(D, B, 'Крит'), disc = Math.min(90, buffSum(D, B, 'Скидка'));
    const bdot = dk ? buffSum(D, B, 'DoT', dk) : 0, sumb = buffSum(D, B, 'Призыв');

    const cc = inp.cc === null || inp.cc === '' || inp.cc === undefined ? null : +inp.cc;
    const crit0 = Math.min(1, (cc === null ? u.crit : cc / 100) + ((+S.gCrit || 0) + rC + pc) / 100);
    const crit = Math.min(1, crit0 + bc / 100);
    const cm = (u.cdm > 0 ? u.cdm : S.critDef) + (rCD + pcd) / 100;
    const own = pasv + rD;
    const mul0 = lvl * (1 + GD / 100) * (1 + cd / 100) * (1 + kD / 100) * (1 + own / 100) * (1 + tr.d / 100) * resm
      * (1 + rPwr * S.pwrp / 100);
    const mulx = mul0 * (1 + bd / 100);
    const spa = row.spa * Math.max(0.1, 1 - ((+S.gSpa || 0) + cs + bs) / 100) * (1 - tr.s / 100) * kS;
    const s0 = row.spa * Math.max(0.1, 1 - ((+S.gSpa || 0) + cs) / 100) * (1 - tr.s / 100) * kS;
    const rng = row.rng * (1 + ((+S.gRng || 0) + br) / 100) * (1 + tr.r / 100) * kR;
    const tg = S.targets && S.targets[row.atype] != null ? +S.targets[row.atype] : 1;
    const ownHit = !!row.own;

    const E = row.dmg;
    const dmg = E * mulx, d0 = E * mul0;
    const dmgdot = dk === 'Кровотечение' ? dmg : d0;    // горение/яд/иссушение — от урона без бафов
    const rdot = dk ? ((rl.dotk === 'Все' || rl.dotk === dk) ? +rl.dot || 0 : 0) + pdot : 0;
    const amp = rdot + bdot;
    const dottick = dk && ownHit ? dmgdot * row.mult * (1 + amp / 100) : 0;
    const dotatk = dottick * row.ticks;
    const dotdps = S.dot && spa > 0 && ownHit ? dmgdot * row.mult * row.ticks / spa * (1 + amp / 100) * tg : 0;
    const hitdps = ownHit ? (spa > 0 ? dmg / spa * (1 + crit * (cm - 1)) * tg : 0) + dmg * rClk / 100 * tg : 0;

    const sm = row.summon || {};
    const cyc = sm.c === 'spa' ? spa : sm.c === 'jelly' ? (spa > 0 ? Math.max(spa, (S.walk + 1.5 * spa) / 3) : 0) : (+sm.c || 0);
    const fT = evalFrag(sm.t, E, spa), fK = evalFrag(sm.k, E, spa), fCap = evalFrag(sm.cap, E, spa), fHit = evalFrag(sm.hit, E, spa);
    const sbase = (cyc > 0 ? fT / cyc : 0) + Math.min(fK * Math.max(0, S.kps), fCap > 0 ? fCap : Infinity);
    const sumdps = sbase * mulx * (1 + sumb / 100);
    const sumhit = fHit ? fHit * mulx * (1 + sumb / 100) : 0;

    const dps = hitdps + dotdps + sumdps;
    const cost0 = u.rows[0][2];
    const cost = cost0 + (row.total - cost0) * (1 - disc / 100);
    const dps0 = (ownHit && s0 > 0 ? (d0 / s0 * (1 + crit0 * (cm - 1))
      + (S.dot ? d0 * row.mult * row.ticks / s0 * (1 + rdot / 100) : 0) + d0 * rClk / 100) * tg : 0) + sbase * mul0;

    // урон за время боя T: атаки в 0, SPA, 2·SPA…; DoT каждой атаки тикает раз в tick с, недотикавшее к концу не считается
    const T = Math.max(0, +S.time || 0), tick = Math.max(0.01, +S.tick || 1);
    const nat = spa > 0 ? Math.floor(T / spa) + 1 : 0;
    const dfull = S.dot && ownHit ? dmgdot * row.mult * row.ticks * (1 + amp / 100) * tg : 0;
    const nfull = nat === 0 || !row.ticks ? 0 : Math.min(nat, Math.max(0, Math.floor((T - row.ticks * tick) / spa) + 1));
    const totHit = ownHit ? nat * dmg * (1 + crit * (cm - 1)) * tg + dmg * rClk / 100 * tg * T : 0;
    const totDot = !row.ticks || nat === 0 ? 0 : dfull / row.ticks * (nfull * row.ticks
      + Math.max(0, (T * (nat - nfull) - spa * (nfull + nat - 1) * (nat - nfull) / 2) / tick));
    const totSum = sumdps * Math.max(0, T - S.walk);
    const tot = totHit + totDot + totSum;

    return {
      upg, maxUpg: u.rows.length - 1, row, cost, dmg, maxhit: dmg * (crit > 0 ? cm : 1), spa, rng, tg, crit, cm,
      dotkind: dk, eff: row.eff, dottick, dotatk, amp, hitdps, dotdps, sumhit, sumdps, dps,
      dpsk: cost ? dps / cost * 1000 : 0, dps0, gain: dps0 ? dps / dps0 - 1 : 0,
      tot, totHit, totDot, totSum, avgdps: T ? tot / T : 0, ownHit, disc,
    };
  }

  // тир по месту в рейтинге DPS среди юнитов с DPS > 0: S ≥ 90%, A ≥ 70%, B ≥ 40%, C ≥ 15%, иначе D
  function tiers(values) {
    const pos = values.filter(v => v > 0).sort((a, b) => b - a);
    const n = pos.length;
    return values.map(v => {
      if (!(v > 0)) return '—';
      const rank = pos.indexOf(v) + 1;
      const p = (n - rank) / Math.max(1, n - 1);
      return p >= 0.9 ? 'S' : p >= 0.7 ? 'A' : p >= 0.4 ? 'B' : p >= 0.15 ? 'C' : 'D';
    });
  }

  const api = { calc, buffSum, tiers, lvlMul, evalFrag, DEFAULT_SETTINGS };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.AAModel = api;
})(typeof window !== 'undefined' ? window : globalThis);
