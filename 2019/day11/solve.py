import sys
from intcode import IntCodeRunner


if len(sys.argv) != 2:
    print "Usage: %s input"
    sys.exit(1)


prog = map(int, open(sys.argv[1], 'rb').read().split(','))


class Robot(IntCodeRunner):

    transforms = [
        [0,  1,  1,  0],
        [0, -1, -1,  0],
    ]

    def __init__(self, prog, start=0):
        super(Robot, self).__init__(prog, self, self)
        self.x = self.y = 0
        self.dx, self.dy = 0, 1
        self.tiles = {(self.x, self.y): start}
        self.moving = False
        self.left = self.right = self.top = self.bottom = 0

    def move(self, d):
        t = self.transforms[d]
        self.dx, self.dy = (
            self.dx * t[0] - self.dy * t[1],
            self.dx * t[2] + self.dy * t[3]
        )
        self.x += self.dx
        self.y += self.dy
        self.left = min(self.left, self.x)
        self.right = max(self.right, self.x)
        self.top = min(self.top, self.y)
        self.bottom = max(self.bottom, self.y)

    def draw(self):
        for y in range(self.bottom, self.top - 1, -1):
            for x in range(self.left, self.right + 1):
                v = self.tiles.get((x, y), 0)
                sys.stdout.write('#' if v else ' ')
            sys.stdout.write('\n')
        
    def read(self):
        return self.tiles.setdefault((self.x, self.y), 0)

    def write(self, v):
        if self.moving:
            self.move(v)
        else:
            self.tiles[(self.x, self.y)] = v
        self.moving = not self.moving


def part1():
    robot = Robot(prog)
    robot.run()
    print len(robot.tiles)


def part2():
    robot = Robot(prog, 1)
    robot.run()
    robot.draw()


part1()
part2()
