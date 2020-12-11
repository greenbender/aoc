'''Alternate version of solve1.py'''
import sys
from functools import lru_cache


adapters = list(sorted(map(int, sys.stdin)))
adapters.insert(0, 0)
adapters.append(adapters[-1] + 3)


@lru_cache(maxsize=None)
def combos(v):
    if v not in adapters:
        return 0
    if v == adapters[-1]:
        return 1
    return combos(v + 1) + combos(v + 2) + combos(v + 3)


def part1():
    diffs = [b - a for a, b in zip(adapters, adapters[1:])]
    print(diffs.count(1) * diffs.count(3))

    
def part2():
    print(combos(0))


part1()
part2()
