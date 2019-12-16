import sys
from intcode import IntCodeRunner


if len(sys.argv) != 2:
    print "Usage: %s input"
    sys.exit(1)


prog = map(int, open(sys.argv[1], 'rb').read().split(','))


class Game(IntCodeRunner):

    TILEID_EMPTY = 0
    TILEID_WALL = 1
    TILEID_BLOCK = 2
    TILEID_PADDLE = 3
    TILEID_BALL = 4

    STATE_X = 0
    STATE_Y = 1
    STATE_TILEID = 2
    STATE_SCORE = 3

    JOYSTICK_LEFT = -1
    JOYSTICK_NEUTRAL = 0
    JOYSTICK_RIGHT = 1

    def __init__(self, prog):
        super(Game, self).__init__(prog, self, self)
        self.state = self.STATE_X
        self.tiles = {}
        self.tile_x = 0
        self.tile_y = 0
        self.score = 0
        self.ball_x = 0
        self.paddle_x = 0

    def pay(self):
        self._write(0, 2)

    def updateState(self):
        if self.state == self.STATE_X:
            self.state = self.STATE_Y
        elif self.state == self.STATE_Y:
            if self.tile_x == -1 and self.tile_y == 0:
                self.state = self.STATE_SCORE
            else:
                self.state = self.STATE_TILEID
        else:
            self.state = self.STATE_X

    def read(self):
        if self.paddle_x == self.ball_x:
            return self.JOYSTICK_NEUTRAL
        return self.JOYSTICK_LEFT if self.ball_x < self.paddle_x else self.JOYSTICK_RIGHT

    def write(self, v):
        if self.state == self.STATE_X:
            self.tile_x = v
        elif self.state == self.STATE_Y:
            self.tile_y = v
        elif self.state == self.STATE_TILEID:
            self.tiles[(self.tile_x, self.tile_y)] = v
            if v == self.TILEID_PADDLE:
                self.paddle_x = self.tile_x
            elif v == self.TILEID_BALL:
                self.ball_x = self.tile_x
        elif self.state == self.STATE_SCORE:
            self.score = v
        self.updateState()

    @property
    def blocks(self): 
        return len([t for t in self.tiles.values() if t == self.TILEID_BLOCK])


def part1():
    game = Game(prog)
    game.run()
    print game.blocks


def part2():
    game = Game(prog)
    game.pay()
    game.run()
    print game.score


part1()
part2()
