import sys


between = map(int, sys.stdin.read().split('-'))


def valid1(attempt):
    if attempt <= 99999 or attempt > 999999:
        return False
    consecutive = False
    attempt, last_d = divmod(attempt, 10)
    while attempt:
        attempt, d = divmod(attempt, 10)
        if d > last_d:
            return False
        if d == last_d:
            consecutive = True
        last_d = d
    return consecutive


def valid2(attempt):
    if attempt <= 99999 or attempt > 999999:
        return False
    groups = []
    attempt, last_d = divmod(attempt, 10)
    groups.append(1)
    while attempt:
        attempt, d = divmod(attempt, 10)
        if d > last_d:
            return False
        if d == last_d:
            groups[-1] += 1
        else:
            groups.append(1)
        last_d = d
    return 2 in groups


def part1():
    print len(filter(valid1, range(between[0], between[1] + 1)))


def part2():
    print len(filter(valid2, range(between[0], between[1] + 1)))


part1()
part2()
