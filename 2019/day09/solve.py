import sys
from intcode import IntCodeRunner


if len(sys.argv) != 2:
    print "Usage: %s input"
    sys.exit(1)


prog = map(int, open(sys.argv[1], 'rb').read().split(','))


class Boost(IntCodeRunner):

    def __init__(self, prog, value):
        super(Boost, self).__init__(prog, self, self)
        self.value = value

    def read(self):
        return self.value

    def write(self, v):
        print v
        

def part1():
    boost = Boost(prog, 1)
    boost.run()


def part2():
    boost = Boost(prog, 2)
    boost.run()


part1()
part2()
