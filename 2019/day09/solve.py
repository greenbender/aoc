import sys
import itertools


if len(sys.argv) != 2:
    print "Usage: %s input"
    sys.exit(1)


prog = map(int, open(sys.argv[1], 'rb').read().split(','))


class IntIO(object):

    def __init__(self):
        self.buf = []

    def read(self):
        if self.buf:
            return self.buf.pop()
        return None

    def write(self, v):
        self.buf.insert(0, v)


class IntStdIO(object):

    def read(self):
        return int(input('Input: '))

    def write(self, v):
        print 'Output:', v
        

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
    r = IntRunner(prog, IntIO(), IntStdIO())
    r.stdin.write(1)
    r.run()


def part2():
    r = IntRunner(prog, IntIO(), IntStdIO())
    r.stdin.write(2)
    r.run()


part1()
part2()
