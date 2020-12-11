import sys


seats = []
for line in sys.stdin:
    line = line.strip()
    row = [None if c == '.' else 0 for c in line]
    seats.append(row)


w = len(seats[0])
h = len(seats)


box = (
    (-1, -1), (-1, +0), (-1,  +1),
    (+0, -1),           (+0,  +1),
    (+1, -1), (+1, +0), (+1,  +1),
)


def occupied1(seats, x, y):
    o = 0
    for dx, dy in box:
        ax = x + dx
        if ax < 0 or ax >= w:
            continue
        ay = y + dy
        if ay < 0 or ay >= h:
            continue
        if seats[ay][ax] == 1:
            o += 1
    return o


def occupied2(seats, x, y):
    o = 0
    for dx, dy in box:
        r = 1
        while True:
            ax = x + r * dx
            if ax < 0 or ax >= w:
                break
            ay = y + r * dy
            if ay < 0 or ay >= h:
                break
            v = seats[ay][ax]
            if v == 1:
                o += 1
                break
            if v == 0:
                break
            r += 1
    return o

    
def step(seats, is_occupied, threshold):
    new = []
    changed = occupied = 0
    for y in range(h):
        row = list(seats[y])
        for x in range(w):
            v = seats[y][x]
            if v is None:
                continue
            o = is_occupied(seats, x, y)
            if v == 0:
                if o == 0:
                    changed += 1
                    v = 1
            elif o >= threshold:
                changed += 1
                v = 0
            occupied += v
            row[x] = v
        new.append(row)
    return new, changed, occupied


def part1():
    s = seats
    while True:
        s, changed, occupied = step(s, occupied1, 4)
        if changed == 0:
            print(occupied)
            break
    

def part2():
    s = seats
    while True:
        s, changed, occupied = step(s, occupied2, 5)
        if changed == 0:
            print(occupied)
            break


part1()
part2()
