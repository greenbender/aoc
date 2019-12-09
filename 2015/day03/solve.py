import sys


directions = sys.stdin.read().strip()


class Map(object):
    dir_map = {
        '^': ( 0,  1),
        'v': ( 0, -1),
        '<': (-1,  0),
        '>': ( 1,  0),
    }

    def __init__(self):
        self.location = (0, 0)
        self.houses = set()
        self.houses.add(self.location)
    
    def move(self, direction):
        dx, dy = self.dir_map[direction]
        x, y = self.location
        self.location = (x + dx, y + dy)
        self.houses.add(self.location)

    @property
    def houses_with_presents(self):
        return self.houses


def part1():
    m = Map()
    for d in directions:
        m.move(d)
    print len(m.houses_with_presents)


def part2():
    santa, robot = Map(), Map()
    for i, d in enumerate(directions):
        if i & 1:
            robot.move(d)
        else:
            santa.move(d)
    print len(santa.houses_with_presents | robot.houses_with_presents)

    
part1()
part2()
