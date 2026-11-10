"""Парсер Lua-таблиц как ДАННЫХ (без исполнения кода).
Понимает: { }, key = v, ['key'] = v, [1] = v, строки '..' ".." [[..]],
числа, true/false/nil, арифметику над числами (+ - * / ^ и скобки), комментарии."""
import re, json, sys

TOK = re.compile(r'''
  (?P<ws>\s+)
 |(?P<lcomment>--\[(?P<eq>=*)\[.*?\](?P=eq)\])
 |(?P<comment>--[^\n]*)
 |(?P<lstr>\[(?P<eq2>=*)\[.*?\](?P=eq2)\])
 |(?P<str>"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*')
 |(?P<num>0[xX][0-9a-fA-F]+|(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?)
 |(?P<name>[A-Za-z_][A-Za-z_0-9]*)
 |(?P<op>[{}\[\]=,;()+\-*/^%])
''', re.S | re.X)

ESC = {'n': '\n', 't': '\t', 'r': '\r', '\\': '\\', '"': '"', "'": "'", '\n': '\n'}


def unescape(s):
    out, i = [], 0
    while i < len(s):
        c = s[i]
        if c == '\\' and i + 1 < len(s):
            n = s[i + 1]
            if n.isdigit():
                m = re.match(r'\d{1,3}', s[i + 1:]).group()
                out.append(chr(int(m))); i += 1 + len(m); continue
            out.append(ESC.get(n, n)); i += 2; continue
        out.append(c); i += 1
    return ''.join(out)


def tokenize(src):
    toks, pos = [], 0
    while pos < len(src):
        m = TOK.match(src, pos)
        if not m:
            raise SyntaxError(f'неизвестный символ на {pos}: {src[pos:pos+30]!r}')
        pos = m.end()
        k = m.lastgroup
        if k in ('ws', 'comment', 'lcomment', 'eq'):
            continue
        v = m.group(k)
        if k == 'lstr':
            body = re.match(r'\[=*\[(.*)\]=*\]$', v, re.S).group(1)
            toks.append(('str', body.lstrip('\n')))
        elif k == 'eq2':
            continue
        elif k == 'str':
            toks.append(('str', unescape(v[1:-1])))
        elif k == 'num':
            toks.append(('num', int(v, 16) if v[:2].lower() == '0x' else float(v)))
        else:
            toks.append((k, v))
    return toks


class P:
    def __init__(self, toks):
        self.t, self.i = toks, 0

    def peek(self, o=0):
        j = self.i + o
        return self.t[j] if j < len(self.t) else ('eof', None)

    def eat(self, v=None):
        tok = self.peek()
        if v is not None and tok[1] != v:
            raise SyntaxError(f'ожидалось {v!r}, получено {tok!r} (токен {self.i})')
        self.i += 1
        return tok

    # выражения: только числа/строки/таблицы/литералы + арифметика
    def expr(self):
        v = self.term()
        while self.peek()[1] in ('+', '-'):
            op = self.eat()[1]; r = self.term()
            v = v + r if op == '+' else v - r
        return v

    def term(self):
        v = self.power()
        while self.peek()[1] in ('*', '/', '%'):
            op = self.eat()[1]; r = self.power()
            v = v * r if op == '*' else (v / r if op == '/' else v % r)
        return v

    def power(self):
        v = self.unary()
        if self.peek()[1] == '^':
            self.eat(); v = v ** self.power()
        return v

    def unary(self):
        if self.peek()[1] == '-':
            self.eat(); return -self.unary()
        return self.atom()

    def atom(self):
        k, v = self.peek()
        if k == 'num': self.eat(); return v
        if k == 'str': self.eat(); return v
        if v == '{': return self.table()
        if v == '(':
            self.eat(); r = self.expr(); self.eat(')'); return r
        if k == 'name' and v in ('true', 'false', 'nil'):
            self.eat(); return {'true': True, 'false': False, 'nil': None}[v]
        raise SyntaxError(f'неподдерживаемое значение {self.peek()!r} (токен {self.i})')

    def table(self):
        self.eat('{')
        arr, d, n = [], {}, 0
        while self.peek()[1] != '}':
            if self.peek()[1] == '[':
                self.eat(); key = self.expr(); self.eat(']'); self.eat('=')
                d[key] = self.expr()
            elif self.peek()[0] == 'name' and self.peek(1)[1] == '=':
                key = self.eat()[1]; self.eat('=')
                d[key] = self.expr()
            else:
                arr.append(self.expr())
            if self.peek()[1] in (',', ';'):
                self.eat()
        self.eat('}')
        if arr and not d:
            return arr
        if not d:
            return {} if not arr else arr
        # смешанная таблица: числовые ключи тоже как позиции
        for idx, val in enumerate(arr, 1):
            d[idx] = val
        if all(isinstance(k, (int, float)) for k in d):
            ks = sorted(d)
            if ks == list(range(1, len(ks) + 1)):
                return [d[k] for k in ks]
        return {(str(int(k)) if isinstance(k, float) and k.is_integer() else str(k)): v for k, v in d.items()}


def parse_module(src):
    toks = tokenize(src)
    p = P(toks)
    p.eat('return')
    v = p.expr()
    return v


if __name__ == '__main__':
    for src, dst in zip(sys.argv[1::2], sys.argv[2::2]):
        data = parse_module(open(src, encoding='utf-8').read())
        json.dump(data, open(dst, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(src, '->', dst, len(data))
