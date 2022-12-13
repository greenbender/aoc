import sys
import functools


pairs = [
    tuple(map(eval, p.strip().split("\n"))) for p in sys.stdin.read().split("\n\n")
]


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        return 0
    if not isinstance(left, list):
        return compare([left], right)
    if not isinstance(right, list):
        return compare(left, [right])
    for l, r in zip(left, right):
        result = compare(l, r)
        if result:
            return result
    if len(left) < len(right):
        return -1
    elif len(right) < len(left):
        return 1
    return 0


# part 1
total = 0
for i, pair in enumerate(pairs):
    if compare(pair[0], pair[1]) < 0:
        total += i + 1
print(total)


# part2
packets = []
for pair in pairs:
    packets.extend(pair)
dividers = [[[2]], [[6]]]
packets.extend(dividers)
packets.sort(key=functools.cmp_to_key(compare))
key = 1
for i, packet in enumerate(packets):
    if packet in dividers:
        key *= i + 1
print(key)
