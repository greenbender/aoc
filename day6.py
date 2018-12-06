#!/usr/bin/python


import sys


points = [(int(x), int(y)) for x, y in [line.split(',') for line in sys.stdin]]


left = min(p[0] for p in points)
top = min(p[1] for p in points)
right = max(p[0] for p in points)
bottom = max(p[1] for p in points)


count = {}
region_size = 0
for y in range(top, bottom + 1):
    for x in range(left, right + 1):
        distances = [abs(x0 - x) + abs(y0 - y) for x0, y0 in points]
        if sum(distances) < 10000:
            region_size += 1
        near = [i for i, d in enumerate(distances) if d == min(distances)]
        nearest = points[near[0]] if len(near) == 1 else None
        if nearest:
            value = count.setdefault(nearest, 0)
            if x in (left, right) or y in (top, bottom):
                count[nearest] = None
            elif value is not None:
                count[nearest] = value + 1
        

# part 1
print max([v for v in count.values() if v is not None])


# part 2
print region_size
