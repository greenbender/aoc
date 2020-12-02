import sys
import itertools


cities = set()
roads = {}
for line in sys.stdin:
    f, _, t, _, d = line.split()
    roads[(f, t)] = int(d)
    roads[(t, f)] = int(d)
    cities.add(f)
    cities.add(t)


distances = []
for route in itertools.permutations(cities):
    distances.append(sum(roads[v] for v in zip(route, route[1:])))


def part1():
    print(min(distances))


def part2():
    print(max(distances))


part1()
part2()
