import sys
from collections import defaultdict


lines = []
for l in sys.stdin:
    p0, p1 = l.split(' -> ')
    p0 = tuple(map(int, p0.split(',')))
    p1 = tuple(map(int, p1.split(',')))
    lines.append((p0, p1))


def plot(grid, x0, x1, y0, y1):
    dx = 1 if x1 > x0 else -1
    dy = 1 if y1 > y0 else -1
    x, y = x0, y0
    while True:
        grid[(x, y)] += 1
        if x == x1 and y == y1:
            break
        if x != x1:
            x += dx
        if y != y1:
            y += dy


# part1
grid = defaultdict(int)
for p0, p1 in lines:
    x0, y0 = p0
    x1, y1 = p1
    if x0 == x1 or y0 == y1:
        plot(grid, x0, x1, y0, y1)
print(sum(1 if v > 1 else 0 for v in grid.values()))


# part2
grid = defaultdict(int)
for p0, p1 in lines:
    x0, y0 = p0
    x1, y1 = p1
    plot(grid, x0, x1, y0, y1)
print(sum(1 if v > 1 else 0 for v in grid.values()))
