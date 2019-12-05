import sys


def fuel(mass):
    return (mass / 3) - 2


def fuel_r(mass):
    f = fuel(mass)
    if f <= 0:
        return 0
    return f + fuel_r(f)


def part1():
    print sum([fuel(int(l)) for l in sys.stdin])


def part2():
    print sum([fuel_r(int(l)) for l in sys.stdin])


#part1()
part2()
    
