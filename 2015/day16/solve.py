import sys


sues = []
for line in sys.stdin:
    _, _, i = line.strip().split(None, 2) 
    sues.append({n: int(v) for n, v in [p.split(':') for p in i.split(', ')]})


def match1(sue):
    return \
        int(sue.get('children', 3) == 3) + \
        int(sue.get('cats', 7) == 7) + \
        int(sue.get('samoyeds', 2) == 2) + \
        int(sue.get('pomeranians', 3) == 3) + \
        int(sue.get('akitas', 0) == 0) + \
        int(sue.get('vizslas', 0) == 0) + \
        int(sue.get('goldfish', 5) == 5) + \
        int(sue.get('trees', 3) == 3) + \
        int(sue.get('cars', 2) == 2) + \
        int(sue.get('perfumes', 1) == 1)


def match2(sue):
    return \
        int(sue.get('children', 3) == 3) + \
        int(sue.get('cats', 8) > 7) + \
        int(sue.get('samoyeds', 2) == 2) + \
        int(sue.get('pomeranians', 2) < 3) + \
        int(sue.get('akitas', 0) == 0) + \
        int(sue.get('vizslas', 0) == 0) + \
        int(sue.get('goldfish', 4) < 5) + \
        int(sue.get('trees', 4) > 3) + \
        int(sue.get('cars', 2) == 2) + \
        int(sue.get('perfumes', 1) == 1)


def part1():
    print(max(enumerate([match1(s) for s in sues]), key=lambda v: v[1])[0] + 1)


def part2():
    print(max(enumerate([match2(s) for s in sues]), key=lambda v: v[1])[0] + 1)


part1()
part2()
