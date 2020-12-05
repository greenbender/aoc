import sys


tickets = []
for line in sys.stdin:
    line = line.strip()
    seatid = 0
    for c in line:
        seatid <<= 1
        seatid |= 0 if c in ('F', 'L') else 1
    tickets.append(seatid)

 
def part1():
    print(max(tickets))


def part2():
    tickets.sort()
    for i in range(len(tickets)):
        if tickets[i + 1] == tickets[i] + 2:
            print(tickets[i] + 1)
            break


part1()
part2()
