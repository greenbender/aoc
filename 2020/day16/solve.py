import sys


fields = {}
for line in sys.stdin:
    line = line.strip()
    if not line:
        break
    name, ranges = line.split(': ', 1)
    r0, _, r1 = ranges.split()
    l0, u0 = map(int, r0.split('-'))
    l1, u1 = map(int, r1.split('-'))
    fields[name] = [(l0, u0), (l1, u1)]


sys.stdin.readline()
mine = list(map(int, sys.stdin.readline().strip().split(',')))


sys.stdin.readline()
sys.stdin.readline()
nearby = []
for line in sys.stdin:
    line = line.strip()
    nearby.append(list(map(int, line.split(','))))


tickets = [mine] + nearby


def valid(field, value):
    r0, r1  = fields[field]
    l0, u0 = r0
    l1, u1 = r1
    return l0 <= value <= u0 or l1 <= value <= u1


def invalid_values(ticket):
    for v in ticket:
        if not any([valid(f, v) for f in fields]):
            yield v


def part1():
    print(sum(sum(invalid_values(t)) for t in tickets))


def part2():
    tkts = [t for t in tickets if sum(invalid_values(t)) == 0]
    options = [set() for _ in range(len(fields))]
    for field in fields:
        for i, values in enumerate(zip(*tkts)):
            if all([valid(field, v) for v in values]):
                options[i].add(field)
    ordered = list(sorted(options, key=len))
    while ordered:
        s0 = ordered.pop(0)
        if len(s0) == 1:
            for s in ordered:
                s -= s0
    v = 1
    for i, s in enumerate(options):
        if len(s) == 1:
            field = s.pop()
            if field.startswith('departure '):
                v *= mine[i]
    print(v)
    

part1()
part2()
