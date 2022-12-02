import sys


calories = [
    [int(c) for c in e.split("\n")] for e in sys.stdin.read().strip().split("\n\n")
]


totals = [sum(d) for d in calories]
totals.sort(reverse=True)


# part1
print(totals[0])


# part2
print(sum(totals[:3]))
