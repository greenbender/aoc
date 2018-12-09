#!/usr/bin/python


import sys


class Marble(object):
    def __init__(self, value):
        self.value = value
        self.next = self
        self.prev = self
    def anticlockwise(self, count):
        if not count:
            return self
        return self.prev.anticlockwise(count - 1)
    def clockwise(self, count):
        if not count:
            return self
        return self.next.clockwise(count - 1)
    def place(self, other):
        other.prev = self
        other.next = self.next
        self.next.prev = other
        self.next = other
        return other
    def pick(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        return self.next


def highest_score(players, last):
    player = 0
    score = [0] * players
    marbles = [Marble(i) for i in range(last + 1)]
    current = marbles[0]
    for marble in marbles:
        if marble.value % 23 == 0:
            score[player] += marble.value
            current = current.anticlockwise(7)
            score[player] += current.value
            current = current.pick()
        else:
            current = current.clockwise(1)
            current = current.place(marble)
        player = (player + 1) % players
    return max(score)


parts = sys.stdin.read().split()
players = int(parts[0])
last = int(parts[-2])


# part 1
print highest_score(players, last)


# part 2 (required refactor to circluar linked list for speed)
print highest_score(players, last * 100)
