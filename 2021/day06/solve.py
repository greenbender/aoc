import sys


fish = [int(v) for v in sys.stdin.read().split(',')]
count = [0] * 9
for f in fish:
    count[f] += 1


def day(counts):
    born = counts.pop(0)
    counts[6] += born
    counts.append(born)


# part1
for _ in range(80):
    day(count)
print(sum(count))


# part2
for _ in range(256 - 80):
    day(count)
print(sum(count))
