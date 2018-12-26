#!/usr/bin/python


import sys


def to_python(fd):
    data = fd.read().strip()
    return int(data), map(int, data)


stop, sequence = to_python(sys.stdin)


elf0 = 0
elf1 = 1
scores = [3, 7]
while True:
    receipe0 = scores[elf0]
    receipe1 = scores[elf1]
    combined = receipe0 + receipe1
    scores.extend(map(int, str(combined)))

    # part 1
    if stop + 10 <= len(scores) < stop + 12:
        print ''.join(map(str, scores[stop:stop+10]))

    # part 2
    if scores[-7:-1] == sequence:
        print len(scores) - 7
        break
    elif scores[-6:] == sequence:
        print len(scores) - 6
        break

    elf0 = (elf0 + receipe0 + 1) % len(scores)
    elf1 = (elf1 + receipe1 + 1) % len(scores)
