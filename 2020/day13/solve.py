import sys
import operator
from functools import reduce


ts = int(sys.stdin.readline())
buses = []
for i, v in enumerate(sys.stdin.readline().strip().split(',')):
    if v != 'x':
        buses.append((i, int(v)))


def chinese_remainder(n, a):
    def mul_inv(a, b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1:
            return 1
        while a > 1:
            q = a // b
            a, b = b, a % b
            x0, x1 = x1 - q * x0, x0
        if x1 < 0:
            x1 += b0
        return x1
    s = 0
    prod = reduce(operator.mul, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        s += a_i * mul_inv(p, n_i) * p
    return s % prod


def part1():
    wait, bus = min(((ts // b + 1) * b - ts, b) for _, b in buses)
    print(wait * bus)


def part2():
    n = [b[1] for b in buses]
    a = [b[1] - b[0] % b[1] for b in buses]
    print(chinese_remainder(n, a))


part1()
part2()
