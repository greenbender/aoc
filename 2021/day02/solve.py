import sys


def vector(line):
    d, a = line.split()
    a = int(a)
    if d == 'up':
        return 0, -a
    elif d == 'down':
        return 0, a
    elif d == 'forward':
        return a, 0


vectors = [vector(l) for l in sys.stdin]


# part1
print(sum(v[0] for v in vectors) * sum(v[1] for v in vectors))


# part2
x = y = aim = 0
for dx, dy in vectors:
    aim += dy
    x += dx
    y += dx * aim
print(x * y)
