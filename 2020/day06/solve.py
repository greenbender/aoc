import sys
import collections


Group = collections.namedtuple('Group', ['size', 'answers'])


groups = []
s, a = 0, {}
for line in sys.stdin:
    line = line.strip()
    if not line:
        if s:
            groups.append(Group(s, a))
            s, a = 0, {}
        continue
    s += 1
    for c in line:
        a.setdefault(c, 0)
        a[c] += 1
if s:
    groups.append(Group(s, a))


def part1():
    print(sum(len(g.answers) for g in groups))


def part2():
    count = 0
    for group in groups:
        count += sum(1 for a, c in group.answers.items() if c == group.size)
    print(count)


part1()
part2()
