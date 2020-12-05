import sys


lights = [0] * 10000
for y, line in enumerate(sys.stdin):
    for x, c in enumerate(line.strip()):
        if c == '#':
            lights[y * 100 + x] = 1


def step(l):
    n = [0] * 10000
    for y0 in range(100):
        for x0 in range(100):
            on = 0
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    y = y0 + dy
                    if y < 0 or y > 99:
                        continue
                    x = x0 + dx
                    if x < 0 or x > 99:
                        continue
                    on += l[y * 100 + x]
            i0 = y0 * 100 + x0
            state = l[i0]
            if state:
                if on not in (2, 3):
                    state = 0
            elif on == 3:
                state = 1
            n[i0] = state
    return n


def broken(l):
    for y in (0, 99):
        for x in (0, 99):
            l[y * 100 + x] = 1
    return l


def part1():
    l = list(lights)
    for _ in range(100):
        l = step(l)
    print(sum(l))


def part2():
    l = broken(list(lights))
    for _ in range(100):
        l = broken(step(l))
    print(sum(l))


part1()
part2()
