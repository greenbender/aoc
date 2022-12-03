import sys


rucksacks = [l.strip() for l in sys.stdin]


# part 1
total = 0
for r in rucksacks:
    l = len(r) // 2
    c1, c2 = set(r[:l]), set(r[l:])
    common = c1 & c2
    c = common.pop()
    if "A" <= c <= "Z":
        value = ord(c) - ord("A") + 27
    else:
        value = ord(c) - ord("a") + 1
    total += value
print(total)


# part 2
total = 0
for i in range(0, len(rucksacks), 3):
    r0 = set(rucksacks[i])
    r1 = set(rucksacks[i + 1])
    r2 = set(rucksacks[i + 2])
    common = r0 & r1 & r2
    c = common.pop()
    if "A" <= c <= "Z":
        value = ord(c) - ord("A") + 27
    else:
        value = ord(c) - ord("a") + 1
    total += value
print(total)
