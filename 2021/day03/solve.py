import sys


bits = 12
report = [int(l, 2) for l in sys.stdin]


def common(report, bit):
    ones = sum((r >> bit) & 1 for r in report)
    return 1 if ones >= len(report) / 2 else 0


# part1
gamma = 0
for b in range(bits):
    gamma |= common(report, b) << b
print(gamma * ((~gamma) & ((1 << bits) - 1)))


# part2
remain = list(report)
for b in reversed(list(range(bits))):
    c = common(remain, b)
    remain = [r for r in remain if (r >> b) & 1 == c]
    if len(remain) == 1:
        break
o2 = remain[0]
remain = list(report)
for b in reversed(list(range(bits))):
    c = common(remain, b)
    remain = [r for r in remain if (r >> b) & 1 != c]
    if len(remain) == 1:
        break
co2 = remain[0]
print(o2 * co2)
