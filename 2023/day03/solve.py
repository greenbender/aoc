import sys
from collections import defaultdict

grid = [list(line) for line in sys.stdin]


adjacent = (
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
)


def numbers():
    w = len(grid[0])
    h = len(grid)
    for y in range(h):
        number, symbols = 0, {}
        for x in range(w):
            value = grid[y][x]
            if value not in "01234567890":
                if number:
                    yield number, symbols
                number, symbols = 0, {}
                continue
            number *= 10
            number += int(value)
            for dx, dy in adjacent:
                sx, sy = x + dx, y + dy
                if 0 <= sx < w and 0 <= y + dy < h:
                    symbol = grid[sy][sx]
                    if symbol not in ".0123456789":
                        symbols[(sx, sy)] = symbol
        if number:
            yield number, symbols


def part1():
    print(sum(number for number, symbols in numbers() if symbols))


def part2():
    gears = defaultdict(list)
    for number, symbols in numbers():
        for pos, symbol in symbols.items():
            if symbol == "*":
                gears[pos].append(number)
    print(sum(gear[0] * gear[1] for gear in gears.values() if len(gear) == 2))


part1()
part2()
