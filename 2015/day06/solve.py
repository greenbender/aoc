import sys
import collections


class Instruction(object):

    ACTION_OFF = 0
    ACTION_ON = 1
    ACTION_TOGGLE = 2

    action_map = {
        'turn on': ACTION_ON,
        'turn off': ACTION_OFF,
        'toggle': ACTION_TOGGLE,
    }

    def __init__(self, action, left, top, right, bottom):
        self.action = action
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    @classmethod
    def parse(cls, text):
        action, start, _, end = text.rsplit(None, 3)
        action = cls.action_map[action]
        left, top = map(int, start.split(','))
        right, bottom = map(int, end.split(','))
        return cls(action, left, top, right, bottom)


instructions = [Instruction.parse(l) for l in sys.stdin]


def part1():
    grid = [0] * 1000000
    for i in instructions:
        for y in range(i.top, i.bottom + 1):
            for x in range(i.left, i.right + 1):
                if i.action == Instruction.ACTION_TOGGLE:
                    grid[1000 * y + x] ^= 1
                elif i.action == Instruction.ACTION_ON:
                    grid[1000 * y + x] = 1
                else:
                    grid[1000 * y + x] = 0
    print sum(grid)
                

def part2():
    grid = [0] * 1000000
    for i in instructions:
        for y in range(i.top, i.bottom + 1):
            for x in range(i.left, i.right + 1):
                if i.action == Instruction.ACTION_TOGGLE:
                    grid[1000 * y + x] += 2
                elif i.action == Instruction.ACTION_ON:
                    grid[1000 * y + x] += 1
                elif grid[1000 * y + x] > 0:
                    grid[1000 * y + x] -= 1
    print sum(grid)


part1()
part2()
