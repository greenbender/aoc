import sys
import numpy
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
    grid = numpy.zeros((1000,1000), dtype=numpy.int)
    for i in instructions:
        if i.action == Instruction.ACTION_TOGGLE:
            grid[i.left:i.right+1,i.top:i.bottom+1] ^= 1
        elif i.action == Instruction.ACTION_ON:
            grid[i.left:i.right+1,i.top:i.bottom+1] = 1
        else:
            grid[i.left:i.right+1,i.top:i.bottom+1] = 0
    print sum(sum(grid))
                

def part2():
    grid = numpy.zeros((1000,1000), dtype=numpy.int)
    for i in instructions:
        if i.action == Instruction.ACTION_TOGGLE:
            grid[i.left:i.right+1,i.top:i.bottom+1] += 2
        elif i.action == Instruction.ACTION_ON:
            grid[i.left:i.right+1,i.top:i.bottom+1] += 1
        else:
            grid[i.left:i.right+1,i.top:i.bottom+1] -= 1
            grid[grid < 0] = 0
    print sum(sum(grid))


part1()
part2()
