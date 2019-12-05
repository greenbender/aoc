import sys


prog = map(int, sys.stdin.read().split(','))


def add(p, o):
    p[p[o + 3]] = p[p[o + 1]] + p[p[o + 2]]
    return o + 4


def mult(p, o):
    p[p[o + 3]] = p[p[o + 1]] * p[p[o + 2]]
    return o + 4


def run(p):
    o = 0
    while True:
        if p[o] == 99:
            return p[0]
        elif p[o] == 1:
            o = add(p, o)
        elif p[o] == 2:
            o = mult(p, o)
        else:
            raise Exception('Program error at %d: %d' % (o, p[o]))


def part1():
    p = list(prog)
    p[1] = 12
    p[2] = 2
    print run(p)


def part2():
    for noun in range(100):
        for verb in range(100):
            p = list(prog)
            p[1] = noun
            p[2] = verb
            if run(p) == 19690720:
                print '%02d%02d' % (noun, verb)
                return


part1()
part2()
