#!/usr/bin/python


import sys


serial = int(sys.stdin.read())


def level(x, y):
    rack_id = x + 10
    value = rack_id * y + serial
    value *= rack_id
    value = (value / 100) % 10
    return value - 5


# build basic grid
grid = []
for y in range(300):
    grid.append([0] * 300)
    for x in range(300):
        grid[y][x] = level(x + 1, y + 1)


# iterate over larger block sizes updating grid
gp = None
gs = gx = gy = 0
for size in range(2, 301):
    bp = None
    bx = by = 0
    for y in range(300 - size):
        for x in range(300 - size):
            for dy in range(1, size + 1):
                grid[y][x] += level(x + size, y + dy)
            for dx in range(1, size):
                grid[y][x] += level(x + dx, y + size)

            # keep track of best block
            if bp is None or grid[y][x] > bp:
                bp = grid[y][x]
                bx = x + 1
                by = y + 1

    # keep track of best block across all sizes 
    if bp is None or bp > gp:
        gp = bp
        gs = size
        gx = bx
        gy = by

    # part 1
    if size == 3:
        print "%d,%d" % (bx, by)

    # since power levels tend to be negative on average since (0-5=-5 and
    # 9-5=4) when block sizes reach a certain size the total power for a block
    # will be negative. As such when we first find that all blocks of a given
    # size have power levels at or below zero we can stop searching
    if bp < 0:
        break


# part 2
print "%d,%d,%d" % (gx, gy, gs)
