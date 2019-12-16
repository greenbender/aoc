import sys
import fractions
import itertools


class Moon(object):
    
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z
        self.reset()

    @staticmethod
    def _change(a, b):
        if a == b:
            return 0
        return 1 if a < b else -1

    def interact(self, other):
        self.dx += self._change(self.x, other.x)
        self.dy += self._change(self.y, other.y)
        self.dz += self._change(self.z, other.z)

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.z += self.dz

    @property
    def energy(self):
        potential = sum(map(abs, [self.x, self.y, self.z]))
        kinetic = sum(map(abs, [self.dx, self.dy, self.dz]))
        return potential * kinetic

    @classmethod
    def load(cls, line):
        x, y, z = [int(v[2:]) for v in line.strip()[1:-1].split(', ')]
        return cls(x, y, z)

    def reset(self):
        self.x = self._x
        self.y = self._y
        self.z = self._z
        self.dx = self.dy = self.dz = 0

    @property
    def isInitialX(self):
        return self._x == self.x and self.dx == 0

    @property
    def isInitialY(self):
        return self._y == self.y and self.dy == 0

    @property
    def isInitialZ(self):
        return self._z == self.z and self.dz == 0


def update(moons):
    for m1, m2 in itertools.combinations(moons, 2):
        m1.interact(m2)
        m2.interact(m1)
    for m in moons:
        m.update()


def reset(moons):
    for m in moons:
        m.reset()


def lcm(*v):
    if len(v) == 2:
        x, y = v
        return x * y // fractions.gcd(x, y)
    return reduce(lcm, v)


moons = [Moon.load(l) for l in sys.stdin]


def part1():
    for _ in range(1000):
        update(moons)
    print sum([m.energy for m in moons])


def part2():
    reset(moons)
    i = rx = ry = rz = 0
    while True:
        update(moons)
        i += 1
        if not rx and all([m.isInitialX for m in moons]):
            rx = i
        if not ry and all([m.isInitialY for m in moons]):
            ry = i
        if not rz and all([m.isInitialZ for m in moons]):
            rz = i
        if rx and ry and rz:
            print lcm(rx, ry,  rz)
            break


part1()
part2()
