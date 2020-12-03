import sys
import operator
import functools


slope = []
for line in sys.stdin:
    slope.append([1 if v == '#' else 0 for v in line.strip()])


w = len(slope[0])
h = len(slope)


def toboggan(dx, dy):
    x = y = trees = 0
    while y < h:
        trees += slope[y][x]
        x += dx
        x %= w
        y += dy
    return trees


def part1():
    print(toboggan(3, 1))


def part2():
    gradients = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    print(functools.reduce(operator.mul, [toboggan(*g) for g in gradients]))


part1()
part2()
