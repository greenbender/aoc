import sys


directions = sys.stdin.read().strip()


def part1():
    print directions.count('(') - directions.count(')')


def part2():
    floor = 0
    for i, d in enumerate(directions):
        floor += 1 if d == '(' else -1
        if floor == -1:
            print i + 1
            break


part1()
part2()
