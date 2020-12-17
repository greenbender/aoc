import sys


values = list(map(int, sys.stdin.readline().strip().split(',')))


def play():
    idxs = {}
    for i, v in enumerate(values[:-1]):
        idxs[v] = i
        yield i + 1, v
    i, v = i + 1, values[-1]
    while True:
        yield i + 1, v
        idx = idxs.get(v, i)
        idxs[v] = i
        v = i - idx
        i += 1
    

def part1():
    for i, v in play():
        if i == 2020:
            print(v)
            break


def part2():
    for i, v in play():
        if i == 30000000:
            print(v)
            break
    
        
part1()
part2()
