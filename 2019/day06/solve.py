import sys


class Node(object):
    def __init__(self, name):
        self.name = name
        self.orbit = None
    @property
    def orbits(self):
        if self.orbit:
            yield self.orbit
            for o in self.orbit.orbits:
                yield o
    @property
    def count(self):
        if self.orbit:
            return 1 + self.orbit.count
        return 0
    def common(self, other):
        for s in self.orbits:
            for o in other.orbits:
                if o == s:
                    return o
        return None


def get_nodes():
    nodes = {}
    for line in sys.stdin:
        orbit, name = line.strip().split(')')
        orbit = nodes.setdefault(orbit, Node(orbit))
        name = nodes.setdefault(name, Node(name))
        name.orbit = orbit
    return nodes


nodes = get_nodes()


def part1():
    print sum([n.count for n in nodes.values()])


def part2():
    you_o = nodes['YOU'].orbit
    santa_o = nodes['SAN'].orbit
    common_o = you_o.common(santa_o)
    if common_o:
        print santa_o.count + you_o.count - 2 * common_o.count


part1()
part2()
