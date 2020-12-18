import sys
import operator


exprs = [l.strip() for l in sys.stdin]


ops = {
    '+': operator.add,
    '*': operator.mul,
}


def tokens(expr):
    for c in expr:
        if c == ' ':
            continue
        if c in '0123456789':
            yield int(c)
        else:
            yield c


def parse(expr, prec=''):
    op = []
    for t in tokens(expr):
        if isinstance(t, int):
            yield t
        elif t in ops:
            while op:
                if op[-1] == '(':
                    break
                if prec.find(op[-1]) < prec.find(t):
                    break
                yield op.pop()
            op.append(t)
        elif t == '(':
            op.append(t)
        elif t == ')':
            while op:
                if op[-1] == '(':
                    break
                yield op.pop()
            op.pop()
    while op:
        yield op.pop()


def calc(expr, prec=''):
    stack = []
    for t in parse(expr, prec=prec):
        if isinstance(t, int):
            stack.append(t)
        elif t in ops:
            a = stack.pop()
            b = stack.pop()
            op = ops[t]
            stack.append(op(b, a))
    return stack[0]
        

def part1():
    print(sum(calc(e) for e in exprs))


def part2():
    print(sum(calc(e, '*+') for e in exprs))


part1()
part2()
