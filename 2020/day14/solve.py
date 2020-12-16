import sys
import collections


Mask = collections.namedtuple('Mask', [
    'zeros', 'ones', 'floats'
])


instructions = []
for line in sys.stdin:
    op, value = line.strip().split(' = ')
    if op == 'mask':
        zeros = ones = floats = 0
        for c in value:
            zeros <<= 1
            ones <<= 1
            floats <<= 1
            if c == '0':
                zeros |= 1
            elif c == '1':
                ones |= 1
            else:
                floats |= 1
        instructions.append((op, Mask(zeros, ones, floats)))
    elif op.startswith('mem'):
        addr = int(op[4:-1])
        instructions.append(('mem', addr, int(value)))


def itermask(mask):
    yield 0
    def _itermask(mask, v, bit):
        if mask & bit:
            vs = v | bit
            yield vs
            yield from _itermask(mask, v, bit << 1)
            yield from _itermask(mask, vs, bit << 1)
        elif bit < mask:
            yield from _itermask(mask, v, bit << 1)
    yield from _itermask(mask, 0, 1)


def part1():
    mask, mem = Mask(0, 0, 0), {}
    for i in instructions:
        op = i[0]
        if op == 'mask':
            mask = i[1]
        elif op == 'mem':
            addr, value = i[1:]
            value &= ~mask.zeros
            value |= mask.ones
            mem[addr] = value
    print(sum(mem.values()))


def part2():
    mask, mem = Mask(0, 0, 0), {}
    for i in instructions:
        op = i[0]
        if op == 'mask':
            mask = i[1]
        elif op == 'mem':
            addr, value = i[1:]
            addr |= mask.ones
            addr &= ~mask.floats
            for a in itermask(mask.floats):
                mem[addr | a] = value
    print(sum(mem.values()))


part1()
part2()
