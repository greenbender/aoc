#!/usr/bin/python


import sys


polymer = map(ord, sys.stdin.read().strip())


def react(polymer):
    reactd = []
    for unit in polymer:
        reactd.append(unit)
        if len(reactd) > 1 and reactd[-2] ^ reactd[-1] == 0x20:
            reactd[-2:] = []
    return reactd


# part 1
print len(react(polymer))


# part 2
types = set([v | 0x20 for v in polymer])
print min([len(react([u for u in polymer if u | 0x20 != t])) for t in types])
