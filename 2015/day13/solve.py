import sys
import itertools


people = set()
happiness = {}
for line in sys.stdin:
    p0, _, gl, n, _, _, _, _, _, _, p1 = line.split()
    p1 = p1.rstrip('.')
    n = int(n)
    if gl == 'lose':
        n = -n
    happiness[(p0, p1)] = n
    people.add(p0)
    people.add(p1)


def max_happiness(happiness, people):
    happinesses = []
    for arrangement in itertools.permutations(people):
        h = 0
        for i in range(len(arrangement)):
            p, n = i - 1, (i + 1) % len(arrangement)
            h += happiness[(arrangement[i], arrangement[p])]
            h += happiness[(arrangement[i], arrangement[n])]
        happinesses.append(h)
    return max(happinesses)


def part1():
    print(max_happiness(happiness, people))


def part2():
    for person in people:
        happiness[('Me', person)] = 0
        happiness[(person, 'Me')] = 0
    people.add('Me')
    print(max_happiness(happiness, people))


part1()
part2()
