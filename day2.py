#!/usr/bin/python


import sys


box_ids = map(str.strip, sys.stdin)


# part 1
doubles = 0
triples = 0

for box_id in box_ids:
    counts = {}
    for letter in box_id:
        value = counts.setdefault(letter, 0)
        counts[letter] = value + 1
    values = counts.values()
    if 2 in values:
        doubles += 1
    if 3 in values:
        triples += 1

checksum = doubles * triples
print checksum


# part 2
while box_ids:
    test_id = box_ids.pop(0)
    for box_id in box_ids:
        index = -1
        for i, letter in enumerate(test_id):
            if box_id[i] != letter:
                if index >= 0:
                    index = -1
                    break
                index = i
        if index >= 0:
            print test_id[:index] + test_id[index + 1:]
            break 
