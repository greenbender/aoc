import sys


sequence = list(map(int, sys.stdin.readline().strip()))


def look_and_say(sm):
    sn, c, l = [], 1, None
    for v in sm:
        if l == v:
            c += 1
        elif l is not None:
            sn.extend([c, l])
            c = 1
        l = v
    sn.extend([c, l])
    return sn


def look_and_say_game(seq):
    while True:
        seq = look_and_say(seq)
        yield seq


play = look_and_say_game(sequence)


def part1():
    for _ in range(39):
        next(play)
    print(len(next(play)))


def part2():
    for _ in range(9):
        next(play)
    print(len(next(play)))
        

part1()
part2()
