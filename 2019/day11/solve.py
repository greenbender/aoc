import sys
import itertools


if len(sys.argv) != 2:
    print "Usage: %s input"
    sys.exit(1)


prog = map(int, open(sys.argv[1], 'rb').read().split(','))


class RobotIO(object):
    transforms = [
        [0,  1,  1,  0],
        [0, -1, -1,  0],
    ]

    def __init__(self, start=0):
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
        

class IntRunner(object):

    def __init__(self, prog, stdin, stdout):
        self.prog = list(prog)
        self.stdin = stdin
        self.stdout = stdout
        self.last_output = None
        self.exit_code = None
        self.done = False
        self.pc = 0
        self.relbase = 0

    @staticmethod
    def immediate(mod, n):
        return ((mod >> (8 * n)) & 0xff) == 1

    @staticmethod
    def relative(mod, n):
        return ((mod >> (8 * n)) & 0xff) == 2

    def pagefault(self, addr):
        if addr < 0:
            raise Exception('pagefault: bad address %d' % addr)
        extra = addr - len(self.prog) + 1
        self.prog.extend([0] * extra)
        
    def read(self, addr):
        try:
            return self.prog[addr]
        except IndexError:
            self.pagefault(addr)
            return self.prog[addr]

    def write(self, addr, v):
        try:
            self.prog[addr] = v
        except IndexError:
            self.pagefault(addr)
            self.prog[addr] = v

    def operand(self, mod, n):
        v = self.pc + n
        if self.immediate(mod, n):
            return v
        if self.relative(mod, n):
            return self.relbase + self.read(v)
        return self.read(v)

    def add(self, mod):
        if self.immediate(mod, 2):
            raise Exception('add: parameter 2 cannot use immediate mode')
        o = [self.operand(mod, n) for n in range(3)]
        self.write(o[2], self.read(o[0]) + self.read(o[1]))
        self.pc += 3

    def mul(self, mod):
        if self.immediate(mod, 2):
            raise Exception('mul: parameter 2 cannot use immediate mode')
        o = [self.operand(mod, n) for n in range(3)]
        self.write(o[2], self.read(o[0]) * self.read(o[1]))
        self.pc += 3

    def get(self, mod):
        v = self.stdin.read()
        if v is None:
            self.pc -= 1 # wait for input (move pc back to get opcode)
        else:
            self.write(self.operand(mod, 0), v)
            self.pc += 1

    def put(self, mod):
        v = self.read(self.operand(mod, 0))
        self.last_output = v
        self.stdout.write(v)
        self.pc += 1

    def jnz(self, mod):
        o = [self.operand(mod, n) for n in range(2)]
        if self.read(o[0]):
            self.pc = self.read(o[1])
        else:
            self.pc += 2

    def jz(self, mod):
        o = [self.operand(mod, n) for n in range(2)]
        if not self.read(o[0]):
            self.pc = self.read(o[1])
        else:
            self.pc += 2

    def lt(self, mod):
        if self.immediate(mod, 2):
            raise Exception('lt: parameter 2 cannot use immediate mode')
        o = [self.operand(mod, n) for n in range(3)]
        self.write(o[2], 1 if self.read(o[0]) < self.read(o[1]) else 0)
        self.pc += 3

    def eq(self, mod):
        if self.immediate(mod, 2):
            raise Exception('eq: parameter 2 cannot use immediate mode')
        o = [self.operand(mod, n) for n in range(3)]
        self.write(o[2], 1 if self.read(o[0]) == self.read(o[1]) else 0)
        self.pc += 3

    def rbase(self, mod):
        self.relbase += self.read(self.operand(mod, 0))
        self.pc += 1

    def end(self):
        self.done = True
        self.exit_code = self.read(0)

    @staticmethod
    def parse(v):
        mod, opcode = divmod(v, 100)
        mod, m0 = divmod(mod, 10)
        mod, m1 = divmod(mod, 10)
        mod, m2 = divmod(mod, 10)
        if m0 > 2 or m1 > 2 or m2 > 2:
            raise Exception('getop: Invalid mode')
        mod = m2 << 16 | m1 << 8 | m0
        return opcode, mod

    def step(self):
        opcode, mod = self.parse(self.read(self.pc))
        self.pc += 1
        if opcode == 99:
            self.end()
            return False
        elif opcode == 1:
            self.add(mod)
        elif opcode == 2:
            self.mul(mod)
        elif opcode == 3:
            self.get(mod)
        elif opcode == 4:
            self.put(mod)
        elif opcode == 5:
            self.jnz(mod)
        elif opcode == 6:
            self.jz(mod)
        elif opcode == 7:
            self.lt(mod)
        elif opcode == 8:
            self.eq(mod)
        elif opcode == 9:
            self.rbase(mod)
        else:
            raise Exception('step: Program error at %d: %d' % (self.pc, opcode))
        return True

    def run(self):
        while self.step():
            pass
        return self.exit_code


def part1():
    io = RobotIO()
    r = IntRunner(prog, io, io)
    r.run()
    print len(io.tiles)


def part2():
    io = RobotIO(1)
    r = IntRunner(prog, io, io)
    r.run()
    io.draw()


part1()
part2()
