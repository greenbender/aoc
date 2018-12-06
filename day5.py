#!/usr/bin/python


import sys


polymer = map(ord, sys.stdin.read().strip())


def collapse(polymer):
    collapsed = []
    for unit in polymer:
        collapsed.append(unit)
        if len(collapsed) > 1 and collapsed[-2] ^ collapsed[-1] == 0x20:
            collapsed[-2:] = []
    return collapsed


# part 1
print len(collapse(polymer))


# part 2
types = set([v | 0x20 for v in polymer])
print min([len(collapse([u for u in polymer if u | 0x20 != t])) for t in types])
