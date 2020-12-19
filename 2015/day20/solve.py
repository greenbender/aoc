import sys


presents = int(sys.stdin.readline())


def part1():
    houses = [1] * (presents // 20)
    for e in range(2, len(houses)):
        for h in range(e, len(houses), e):
            houses[h - 1] += e * 10
        if houses[e - 1] >= presents:
            print(e)
            break


def part2():
    houses = [0] * (presents // 22)
    for e in range(1, len(houses)):
        for i, h in enumerate(range(e, len(houses), e)):
            if i == 50:
                break
            houses[h - 1] += e * 11
        if houses[e - 1] >= presents:
            print(e)
            break


part1()
part2()
