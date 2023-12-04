import sys
from functools import cache


def parse(line):
    _, numbers = line.split(": ")
    winners, mine = numbers.split(" | ")
    winners = {int(x) for x in winners.split()}
    mine = {int(x) for x in mine.split()}
    return winners, mine


cards = [parse(line.strip()) for line in sys.stdin]


def part1():
    total = 0
    for winners, mine in cards:
        count = len(winners & mine)
        if count:
            total += 2 ** (count - 1)
    print(total)


part1()


@cache
def cards_from(i):
    winners, mine = cards[i]
    count = len(winners & mine)
    start = i + 1
    end = min(i + 1 + count, len(cards))
    return count + sum(cards_from(j) for j in range(start, end))


def part2():
    print(sum(cards_from(i) + 1 for i in range(len(cards))))


part2()
