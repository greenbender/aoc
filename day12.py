#!/usr/bin/python


import sys
import re


def debug(state):
    print ''.join(['#' if v else '.' for v in state])


def to_python(fd):
    initial = []
    transform = []
    for i, c in enumerate(re.findall(r'[\.#]', fd.readline())):
        initial.append(1 if c == '#' else 0)
    fd.readline()
    for line in sorted(fd, reverse=True):
        transform.append(1 if line.strip().endswith('#') else 0)
    return initial, transform


initial, transform = to_python(sys.stdin)


def population(pots, left=0):
    total = 0
    for i, p in enumerate(pots):
        total += p * (i + left)
    return total


def breed(generations):
    pots, left = initial[:], 0
    while generations:
        spawn = []
        left -= 2
        for i0 in range(-2, len(pots) + 2):
            value = 0
            for di in range(-2, 3):
                i = i0 + di
                value <<= 1
                if 0 <= i < len(pots):
                    value |= pots[i]
            value = transform[value]
            if spawn or value:
                spawn.append(value)
            else:
                left += 1
        while not spawn[-1]:
            spawn.pop()
        pots = spawn
        generations -= 1
        yield population(pots, left)


p_last = p_diff = p_stable = 0
for i, p in enumerate(breed(50000000000)):

    # part 1
    if i == 20:
        print p

    # part 2 (wait for population growth to become stable then calculate the
    # final popluation)
    pd = p - p_last
    if pd == p_diff:
        p_stable += 1
    else:
        p_stable = 0
    p_last = p
    p_diff = pd
    if p_stable > 20:
        print p + (50000000000 - i - 1) * p_diff
        break
