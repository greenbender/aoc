#!/usr/bin/python


import sys


pairs = [(w[1], w[-3]) for w in map(str.split, sys.stdin)]


def instructions(pairs):
    inst = {}
    for p, i in pairs:
        inst.setdefault(p, set())
        pending = inst.setdefault(i, set())
        pending.add(p)
    return inst


# part 1        
path = []
inst = instructions(pairs)
while inst:
    step = sorted([i for i, pending in inst.items() if len(pending) == 0])[0]
    del inst[step]
    path.append(step)
    for pending in inst.values():
        pending.discard(step)

print ''.join(path)


# part 2
elapsed = 0
working = {}
inst = instructions(pairs)
while inst:
    steps = sorted([i for i, pending in inst.items() if len(pending) == 0])

    # waiting for next step
    if len(working) == 5 or not steps:
        elapsed = min(working.values())
        for done in [i for i, end in working.items() if end == elapsed]:
            del working[done]
        for pending in inst.values():
            pending -= set(done)
    
    # start working on pending steps
    for step in steps:
        if len(working) < 5:
            working[step] = elapsed + ord(step) - 4
            del inst[step]

print max(working.values())
