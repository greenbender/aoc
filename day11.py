#!/usr/bin/python


import sys


serial = int(sys.stdin.read())


def level(x, y):
    rack_id = x + 10
    value = rack_id * y + serial
    value *= rack_id
    value = (value / 100) % 10
    return value - 5


# build summed area table
table = []
for y in range(301):
    table.append([0] * 301)
    if not y:
        continue
    for x in range(301):
        if not x:
            continue
        table[y][x] = \
            level(x, y) + \
            table[y - 1][x] + \
            table[y][x - 1] - \
            table[y - 1][x - 1]


def most_power(size):
    mp = None
    mx = my = 0
    for y in range(0, 301 - size):
        for x in range(0, 301 - size):
            power = \
                table[y + size][x + size] + \
                table[y][x] - \
                table[y][x + size] - \
                table[y + size][x]
            if mp is None or power > mp:
                mp = power
                mx = x + 1
                my = y + 1
    return mp, mx, my


# part 1
_, x, y = most_power(3)
print '%d,%d' % (x, y)


# part 2
mp = None
mx = my = ms = 0
for size in range(1, 301):
    p, x, y = most_power(size)
    if p < 0:
        break
    if mp is None or p > mp:
        mp = p
        mx = x
        my = y
        ms = size
print '%d,%d,%d' % (mx, my, ms)
