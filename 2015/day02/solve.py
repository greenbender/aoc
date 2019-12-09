import sys


presents = [map(int, l.split('x')) for l in sys.stdin]


def paper(l, w, h):
    areas = (l * w, w * h, h * l)
    return 2 * sum(areas) + min(areas)


def ribbon(l, w, h):
    perims = map(lambda v: v * 2, (l + w, w + h, h + l))
    volume = l * w * h
    return min(perims) + volume


def part1():
    print sum([paper(*p) for p in presents])


def part2():
    print sum([ribbon(*p) for p in presents])


part1()
part2()
