import sys


class Cave:
    ROCK = b"#"
    SAND = b"o"

    def __init__(self, grid):
        self.grid = grid
        self.top = 0
        self.bottom = max(y for x, y in self.grid.keys())
        self.floor = self.bottom + 2

    @classmethod
    def load(cls, fd):
        grid = {}
        for line in fd:
            parts = line.strip().split(" -> ")
            for i in range(1, len(parts)):
                x0, y0 = [int(v) for v in parts[i - 1].split(",")]
                x1, y1 = [int(v) for v in parts[i].split(",")]
                if x0 == x1:
                    for y in range(min(y0, y1), max(y0, y1) + 1):
                        grid[(x0, y)] = cls.ROCK
                else:
                    for x in range(min(x0, x1), max(x0, x1) + 1):
                        grid[(x, y0)] = cls.ROCK
        return cls(grid)

    @property
    def left(self):
        return min(x for x, y in self.grid.keys())

    @property
    def right(self):
        return max(x for x, y in self.grid.keys())

    def draw(self):
        rows = []
        for y in range(self.top, self.floor):
            row = []
            for x in range(self.left, self.right + 1):
                row.append(self.grid.get((x, y), b" "))
            rows.append(b"".join(row))
        return b"\n".join(rows).decode()

    def pour(self, has_floor=False):
        x, y = 500, 0
        while True:
            if not has_floor and y >= self.bottom:
                return False
            if self.grid.get((500, 0)) is not None:
                return False
            d = self.ROCK if y + 1 >= self.floor else None
            if self.grid.get((x, y + 1), d) is None:
                y += 1
            elif self.grid.get((x - 1, y + 1), d) is None:
                x -= 1
                y += 1
            elif self.grid.get((x + 1, y + 1), d) is None:
                x += 1
                y += 1
            else:
                self.grid[(x, y)] = self.SAND
                return True


c = Cave.load(sys.stdin)


# part 1
count = 0
while c.pour():
    count += 1
print(count)


# part 2
while c.pour(has_floor=True):
    count += 1
print(count)
