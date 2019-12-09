import sys


orbits = [l.strip().split(')') for l in sys.stdin]


class Body(object):

    def __init__(self):
        self.orbiting = None

    @property
    def orbits(self):
        if self.orbiting:
            yield self.orbiting
            for o in self.orbiting.orbits:
                yield o

    @property
    def count(self):
        if self.orbiting:
            return 1 + self.orbiting.count
        return 0

    def common(self, other):
        for s in self.orbits:
            for o in other.orbits:
                if o == s:
                    return o
        return None


bodies = {}
for orbiting, body in orbits:
    orbiting = bodies.setdefault(orbiting, Body())
    body = bodies.setdefault(body, Body())
    body.orbiting = orbiting


def part1():
    print sum([b.count for b in bodies.values()])


def part2():
    you_o = bodies['YOU'].orbiting
    santa_o = bodies['SAN'].orbiting
    common_o = you_o.common(santa_o)
    if common_o:
        print santa_o.count + you_o.count - 2 * common_o.count


part1()
part2()
