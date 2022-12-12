import sys


grid = [list(line.strip()) for line in sys.stdin]
w = len(grid[0])
h = len(grid)


start = (0, 0)
goal = (0, 0)
for y in range(h):
    for x in range(w):
        if grid[y][x] == "S":
            start = (x, y)
            grid[y][x] = "a"
        if grid[y][x] == "E":
            goal = (x, y)
            grid[y][x] = "z"


def walk(start, goal):
    distance = 0
    visited = set([start])
    nodes = [start]
    while nodes:
        n = []
        for pos0 in nodes:
            if pos0 == goal:
                return distance
            x0, y0 = pos0
            h0 = ord(grid[y0][x0])
            for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                x1, y1 = x0 + dx, y0 + dy
                pos1 = (x1, y1)
                if 0 <= x1 < w and 0 <= y1 < h and pos1 not in visited:
                    h1 = ord(grid[y1][x1])
                    if h1 <= h0 + 1:
                        visited.add(pos1)
                        n.append(pos1)
        distance += 1
        nodes = n


# part 1
print(walk(start, goal))


# part 2
distances = []
for y in range(h):
    for x in range(w):
        if grid[y][x] == "a":
            d = walk((x, y), goal)
            if d is not None:
                distances.append(d)
print(min(distances))
