import sys
import itertools


n = list(map(int, sys.stdin))


def part1(pl):
    for i in range(pl, len(n)):
        p, c, found = n[i-pl:i], n[i], False
        for a, b in itertools.combinations(p, 2):
            if c == a + b:
                found = True
                break
        if not found:
            print(c)
            return c


def part2(tgt):
    i = j = 0
    while True:
        r = n[i:j+1]
        v = sum(r)
        if v == tgt:
            print(min(r) + max(r))
            break
        if v > tgt:
            i += 1
        else:
            j += 1


part2(part1(25))
