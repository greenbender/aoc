import sys
import itertools
import fractions
import math


class Asteroid(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.others = {}

    @staticmethod
    def normalise(a, b):
        gcd = fractions.gcd(abs(a), abs(b))
        return a / gcd, b / gcd

    def gradient(self, other):
        dy = self.y - other.y
        dx = other.x - self.x
        return self.normalise(dx, dy)

    def relate(self, other):
        gs = self.gradient(other)
        os = self.others.setdefault(gs, [])
        os.append(other)
        go = other.gradient(self)
        oo = other.others.setdefault(go, [])
        oo.append(self)

    def _key_distance(self, other):
        dy = other.y - self.y
        dx = other.x - self.x
        return dx * dx + dy * dy

    @staticmethod
    def _key_angle(k):
        x, y = k
        a = (math.degrees(math.atan2(y, x)) + 270) % 360
        return a or 360.0

    def clockwise(self):
        for v in self.others.values():
            v.sort(key=self._key_distance)
        while True:
            none = True
            for k in sorted(self.others.keys(), key=self._key_angle, reverse=True):
                if self.others[k]:
                    none = False
                    yield self.others[k]
            if none:
                break


asteroids = []
for y, line in enumerate(sys.stdin):
    for x, char in enumerate(line.strip()):
        if char == '#':
            asteroids.append(Asteroid(x, y))
for a0, a1 in itertools.combinations(asteroids, 2):
    a0.relate(a1)


def part1():
    most = max(asteroids, key=lambda a: len(a.others))
    print len(most.others)
    return most


def part2(most):
    count = 0
    for asteroids in most.clockwise():
        asteroid = asteroids.pop(0)
        count += 1
        if count == 200:
            print asteroid.x * 100 + asteroid.y
            break


part2(part1())
