import sys


policies = []
for line in sys.stdin:
    lu, l, pwd = line.split()
    lower, upper = map(int, lu.split('-'))
    l = l[0]
    policies.append((lower, upper, l, pwd))


def validate1(lower, upper, letter, pwd):
    if lower <= pwd.count(letter) <= upper:
        return True
    return False


def validate2(lower, upper, letter, pwd):
    if pwd[lower-1] == letter:
        if pwd[upper-1] == letter:
            return False
        return True
    elif pwd[upper-1] == letter:
        return True
    return False


def part1():
    print(len([policy for policy in policies if validate1(*policy)]))


def part2():
    print(len([policy for policy in policies if validate2(*policy)]))


part1()
part2()
