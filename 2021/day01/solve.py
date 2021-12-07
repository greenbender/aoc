import sys
import itertools


depths = list(map(int, sys.stdin))


def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def window(iterable):
    a, b, c = itertools.tee(iterable, 3)
    next(b, None)
    next(c, None)
    next(c, None)
    return zip(a, b, c)


# part1
print(sum(int(b > a) for a, b, in pairwise(depths)))


# part2
print(sum(int(b > a) for a, b in pairwise(sum(w) for w in window(depths))))
