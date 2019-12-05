import sys


wires = [l.split(',') for l in sys.stdin]


class Grid(object):

    dir_map = {
        'L': (-1,  0),
        'R': ( 1,  0),
        'U': ( 0,  1),
        'D': ( 0, -1),
    }

    def __init__(self, wires):
        self.wires = wires
        self.points = {}
        self.wirepos = [(0, 0)] * wires
        self.wirestep = [0] * wires

    def intersections(self):
        for p, w in self.points.iteritems():
            if all(w):
                yield p, w

    def trace(self, w, v):
        x, y = self.wirepos[w]
        dx, dy = self.dir_map[v[0]]
        for i in range(int(v[1:])):
            x += dx
            y += dy
            point = self.points.setdefault((x, y), [0] * self.wires)
            self.wirestep[w] += 1
            point[w] = self.wirestep[w]
        self.wirepos[w] = (x, y)


g = Grid(len(wires))
for i, w in enumerate(wires):
    for v in w:
        g.trace(i, v)


def part1():
    print min([abs(i[0][0]) + abs(i[0][1]) for i in g.intersections()])


def part2():
    print min([sum(i[1]) for i in g.intersections()])


part1()
part2()
