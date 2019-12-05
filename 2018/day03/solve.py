#!/usr/bin/python


import sys


def to_claim(line):
    cid, _, location, dimensions = line.split()
    cid = int(cid[1:])
    x, y = map(int, location[:-1].split(','))
    w, h = map(int, dimensions.split('x'))
    return cid, x, y, w, h


claims = map(to_claim, sys.stdin)


# build bitmap
bitmap = [None] * (1000 * 1000)
for cid, x0, y0, w, h in claims:
    for x in range(x0, x0 + w):
        for y in range(y0, y0 + h):
            i = y * 1000 + x
            bitmap[i] = cid if bitmap[i] is None else 'X'


# counts
counts = {}
for v in bitmap:
    count = counts.setdefault(v, 0)
    counts[v] = count + 1


# part 1
print counts['X']


# part 2
for cid, _, _, w, h in claims:
    if counts.get(cid, 0) == w * h:
        print cid
        break
