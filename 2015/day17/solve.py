import sys
import itertools


containers = [int(line.strip()) for line in sys.stdin]


def combos(l, tgt):
    def _combos(l, tgt):
        if l:
            v = l[0]
            if v == tgt:
                yield [v]
            elif v < tgt:
                for c in combos(l[1:], tgt - v):
                    c.insert(0, v)
                    yield c
            yield from _combos(l[1:], tgt)
    l = list(sorted(l, reverse=True))
    yield from _combos(l, tgt)


def part1():
    print(len(list(combos(containers, 150))))


def part2():
    count, min_length = 0, len(containers)
    for combo in combos(containers, 150):
        length = len(combo)
        if length < min_length:
            min_length = length
            count = 1
        elif length == min_length:
            count += 1
    print(count)


part1()
part2()
