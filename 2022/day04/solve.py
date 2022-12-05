import sys


pairs = []
for line in sys.stdin:
    l, r = line.strip().split(",")
    s0, e0 = l.split("-")
    ids0 = set(range(int(s0), int(e0) + 1))
    s1, e1 = r.split("-")
    ids1 = set(range(int(s1), int(e1) + 1))
    pairs.append((ids0, ids1))


count = 0
for ids0, ids1 in pairs:
    if ids0 <= ids1 or ids1 <= ids0:
        count += 1
print(count)


count = 0
for ids0, ids1 in pairs:
    if ids0 & ids1:
        count += 1
print(count)
