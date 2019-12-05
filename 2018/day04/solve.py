#!/usr/bin/python


import sys


def sleeping(iterable):
    gid = None
    start = None
    for value in sorted(iterable):
        value = value.strip()
        minute = int(value[15:17])
        if value.endswith('begins shift'):
            gid = int(value.rsplit(None, 3)[1][1:])
        elif value.endswith('falls asleep'):
            start = minute
        else:
            end = minute
            yield gid, start, end


guards = {}
for gid, start, end in sleeping(sys.stdin):
    guard = guards.setdefault(gid, {})
    for minute in range(start, end):
        value = guard.setdefault(minute, 0)
        guard[minute] = value + 1


# part 1
sleepy = max(guards, key=lambda g: sum(guards[g].values()))
when = max(guards[sleepy], key=lambda m: guards[sleepy][m])
print sleepy * when


# part 2
sleepy = max(guards, key=lambda g: max(guards[g].values()))
when = max(guards[sleepy], key=lambda m: guards[sleepy][m])
print sleepy * when
