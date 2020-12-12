import sys


actions = []
for line in sys.stdin:
    actions.append((line[0], int(line[1:])))


L90 = {
    (0, -1):  (-1, 0),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (-1, 0): (0, 1),
}


R90 = {
    (0, -1):  (1, 0),
    (0, 1): (-1, 0),
    (1, 0): (0, 1),
    (-1, 0): (0, -1),
}


def part1():
    x = y = 0
    dx, dy = 1, 0
    for a, d in actions:
        if a == 'N':
            y -= d
        elif a == 'S':
            y += d
        elif a == 'E':
            x += d
        elif a == 'W':
            x -= d
        elif a == 'L':
            if d == 90:
                dx, dy = L90[(dx, dy)]
            elif d == 180:
                dx, dy = -dx, -dy
            elif d == 270:
                dx, dy = R90[(dx, dy)]
        elif a == 'R':
            if d == 90:
                dx, dy = R90[(dx, dy)]
            elif d == 180:
                dx, dy = -dx, -dy
            elif d == 270:
                dx, dy = L90[(dx, dy)]
        elif a == 'F':
            x += d * dx
            y += d * dy
    print(abs(x) + abs(y))


def part2():
    x, y = 0, 0
    wx, wy = 10, -1
    for a, d in actions:
        if a == 'N':
            wy -= d
        elif a == 'S':
            wy += d
        elif a == 'E':
            wx += d
        elif a == 'W':
            wx -= d
        elif a == 'L':
            if d == 90:
                wx, wy = wy, -wx
            elif d == 180:
                wx, wy = -wx, -wy
            elif d == 270:
                wx, wy = -wy, wx
        elif a == 'R':
            if d == 90:
                wx, wy = -wy, wx
            elif d == 180:
                wx, wy = -wx, -wy
            elif d == 270:
                wx, wy = wy, -wx
        elif a == 'F':
            x += d * wx
            y += d * wy
    print(abs(x) + abs(y))


part1()
part2()
