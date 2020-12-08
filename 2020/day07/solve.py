import sys


rules = {}
for line in sys.stdin:
    line = line.strip()
    d1, c1, _, _, rest = line.split(None, 4)
    r = rules.setdefault((d1, c1), []) 
    for b in rest.split(', '):
        if b != 'no other bags.':
            n, d2, c2, _ = b.split()
            r.append((int(n), d2, c2))


def holds(d, c):
    for bag, subbags in rules.items():
        d1, c1 = bag
        for n, d2, c2 in subbags:
            if d2 == d and c2 == c:
                yield d1, c1
                yield from holds(d1, c1)


def contains(d, c):
    count = 0
    for n, d2, c2 in rules[(d, c)]:
        count += (1 + contains(d2, c2)) * n
    return count


def part1():
    print(len(set(holds('shiny', 'gold'))))


def part2():
    print(contains('shiny', 'gold'))


part1()
part2()
