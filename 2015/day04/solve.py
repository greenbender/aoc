import sys
import hashlib


key = sys.stdin.read().strip()


def findhash(key, start):
    i = 1
    while True:
        data = '%s%d' % (key, i)
        h = hashlib.md5(data)
        if h.hexdigest().startswith(start):
            return i
        i += 1


def part1():
    print findhash(key, '00000')


def part2():
    print findhash(key, '000000')


part1()
part2()
