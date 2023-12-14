import sys

grid = [list(line.strip()) for line in sys.stdin]
dim = len(grid)


def print_grid(grid):
    for line in grid:
        print("".join(line))
    print()


def load(grid):
    load = 0
    for y in range(dim):
        for x in range(dim):
            if grid[y][x] == "O":
                load += dim - y
    return load


def north(grid):
    for y in range(dim):
        for x in range(dim):
            if grid[y][x] == "O":
                grid[y][x] = "."
                up = y - 1
                while up >= 0 and grid[up][x] == ".":
                    up -= 1
                grid[up + 1][x] = "O"


def south(grid):
    for y in range(dim - 1, -1, -1):
        for x in range(dim):
            if grid[y][x] == "O":
                grid[y][x] = "."
                down = y + 1
                while down < dim and grid[down][x] == ".":
                    down += 1
                grid[down - 1][x] = "O"


def east(grid):
    for x in range(dim - 1, -1, -1):
        for y in range(dim):
            if grid[y][x] == "O":
                grid[y][x] = "."
                right = x + 1
                while right < dim and grid[y][right] == ".":
                    right += 1
                grid[y][right - 1] = "O"


def west(grid):
    for x in range(dim):
        for y in range(dim):
            if grid[y][x] == "O":
                grid[y][x] = "."
                left = x - 1
                while left >= 0 and grid[y][left] == ".":
                    left -= 1
                grid[y][left + 1] = "O"


def part1():
    g = [list(row) for row in grid]
    north(g)
    print(load(g))


part1()


def cycle(grid):
    north(grid)
    west(grid)
    south(grid)
    east(grid)


def freeze(grid):
    return tuple(tuple(row) for row in grid)


def part2():
    g = [list(row) for row in grid]
    frozen = freeze(g)
    states, grids = {frozen: 0}, [frozen]
    for i in range(1, 1000000001):
        cycle(g)
        frozen = freeze(g)
        if frozen in states:
            cycle_length = i - states[frozen]
            cycle_start = states[frozen]
            index = cycle_start + (1000000000 - cycle_start) % cycle_length
            print(load(grids[index]))
            break
        states[frozen] = i
        grids.append(frozen)


part2()
