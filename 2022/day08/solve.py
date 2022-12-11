import sys


grid = [list(map(int, line.strip())) for line in sys.stdin]
w, h = len(grid[0]), len(grid)


# part 1
visible = set()
for x in range(w):
    m = -1
    for y in range(h):
        if grid[y][x] > m:
            m = grid[y][x]
            visible.add((x, y))
        if m == 9:
            break
    m = -1
    for y in reversed(range(h)):
        if grid[y][x] > m:
            m = grid[y][x]
            visible.add((x, y))
        if m == 9:
            break
for y in range(h):
    m = -1
    for x in range(w):
        if grid[y][x] > m:
            m = grid[y][x]
            visible.add((x, y))
        if m == 9:
            break
    m = -1
    for x in reversed(range(w)):
        if grid[y][x] > m:
            m = grid[y][x]
            visible.add((x, y))
        if m == 9:
            break
print(len(visible))


# part 2
best = 0
for y in range(h):
    for x in range(w):
        m = grid[y][x]
        l = r = u = d = 0
        for xl in reversed(range(0, x)):
            l += 1
            if grid[y][xl] >= m:
                break
        for xr in range(x + 1, w):
            r += 1
            if grid[y][xr] >= m:
                break
        for yu in reversed(range(0, y)):
            u += 1
            if grid[yu][x] >= m:
                break
        for yd in range(y + 1, h):
            d += 1
            if grid[yd][x] >= m:
                break
        score = l * r * u * d
        if score > best:
            best = score
print(best)
