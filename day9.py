#!/usr/bin/python


import sys


class Marble(object):
    def __init__(self, value):
        self.value = value
        self.n = self
        self.p = self
    def next(self):
        return self.n
    def push(self, other):
        other.p = self
        other.n = self.n
        self.n.p = other
        self.n = other
        return other
    def pop(self):
        self.p.n = self.n
        self.n.p = self.p
        return self
    def reverse(self, count):
        if not count:
            return self
        return self.p.reverse(count - 1)


def highest_score(players, last_marble):
    game = Marble(0)
    score = [0] * players
    player = 0
    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            score[player] += marble
            game = game.reverse(7)
            score[player] += game.value
            game = game.pop().next()
        else:
            game = game.next()
            game = game.push(Marble(marble))
        player = (player + 1) % players
    return max(score)


parts = sys.stdin.read().split()
players = int(parts[0])
last_marble = int(parts[-2])


# part 1
print highest_score(players, last_marble)


# part 2 (required refactor to circluar linked list for speed)
print highest_score(players, last_marble * 100)
