import sys


masses = map(int, sys.stdin)


def fuel(mass):
    return (mass / 3) - 2


def fuel_r(mass):
    f = fuel(mass)
    if f <= 0:
        return 0
    return f + fuel_r(f)


def part1():
    print sum(map(fuel, masses))


def part2():
    print sum(map(fuel_r, masses))


part1()
part2()
    
