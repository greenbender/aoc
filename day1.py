#!/usr/bin/python


import sys
import itertools


changes = map(int, sys.stdin)


# part 1
print sum(changes)


# generate frequencies
def freqs():
    freq = 0
    yield freq
    for change in itertools.cycle(changes):
        freq += change
        yield freq


# part 2
seen = set()
for freq in freqs():
    if freq in seen:
        print freq
        break
    seen.add(freq)
