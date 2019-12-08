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
        

class IntRunner(object):

    def __init__(self, prog, stdin, stdout):
        self.prog = list(prog)
        self.stdin = stdin
        self.stdout = stdout
        self.last_output = None
        self.exit_code = None
        self.done = False
        self.pc = 0

    @staticmethod
    def immediate(mod, n):
        return mod & (1 << n)

    def operand(self, mod, n):
        v = self.pc + n
        if self.immediate(mod, n):
            return v
        return self.prog[v]

    def add(self, mod):
        if self.immediate(mod, 2):
            raise Exception('add: parameter 2 must use position mode')
        o = [self.operand(mod, n) for n in range(3)]
        self.prog[o[2]] = self.prog[o[0]] + self.prog[o[1]]
        self.pc += 3

    def mul(self, mod):
        if self.immediate(mod, 2):
            raise Exception('mul: parameter 2 must use position mode')
        o = [self.operand(mod, n) for n in range(3)]
        self.prog[o[2]] = self.prog[o[0]] * self.prog[o[1]]
        self.pc += 3

    def get(self, mod):
        v = self.stdin.read()
        if v is None:
            self.pc -= 1 # wait for input (move pc back to get opcode)
        else:
            self.prog[self.operand(mod, 0)] = v
            self.pc += 1

    def put(self, mod):
        v = self.prog[self.operand(mod, 0)]
        self.last_output = v
        self.stdout.write(v)
        self.pc += 1

    def jnz(self, mod):
        o = [self.operand(mod, n) for n in range(2)]
        if self.prog[o[0]]:
            self.pc = self.prog[o[1]]
        else:
            self.pc += 2

    def jz(self, mod):
        o = [self.operand(mod, n) for n in range(2)]
        if not self.prog[o[0]]:
            self.pc = self.prog[o[1]]
        else:
            self.pc += 2

    def lt(self, mod):
        if self.immediate(mod, 2):
            raise Exception('lt: parameter 2 must use position mode')
        o = [self.operand(mod, n) for n in range(3)]
        self.prog[o[2]] = 1 if self.prog[o[0]] < self.prog[o[1]] else 0
        self.pc += 3

    def eq(self, mod):
        if self.immediate(mod, 2):
            raise Exception('eq: parameter 2 must use position mode')
        o = [self.operand(mod, n) for n in range(3)]
        self.prog[o[2]] = 1 if self.prog[o[0]] == self.prog[o[1]] else 0
        self.pc += 3

    def end(self):
        self.done = True
        self.exit_code = self.prog[0]

    @staticmethod
    def parse(v):
        mod, opcode = divmod(v, 100)
        mod, b0 = divmod(mod, 10)
        mod, b1 = divmod(mod, 10)
        mod, b2 = divmod(mod, 10)
        if b0 > 1 or b1 > 1 or b2 > 1:
            raise Exception('getop: Invalid mode')
        mod = b2 << 2 | b1 << 1 | b0
        return opcode, mod

    def step(self):
        opcode, mod = self.parse(self.prog[self.pc])
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
        else:
            raise Exception('step: Program error at %d: %d' % (self.pc, opcode))
        return True

    def run(self):
        while self.step():
            pass
        return self.exit_code


def part1():
    outputs = []
    for c in itertools.permutations(range(5)):

        # create 6 IntIO's
        ios = []
        for i in range(6):
            ios.append(IntIO())
     
        # create 5 amplifiers and connect their stdin/stdout
        amps = []
        for i in range(5):
            amp = IntRunner(prog, ios[i], ios[i + 1])
            amp.stdin.write(c[i])
            amps.append(amp)

        # initialise first amplifier
        amps[0].stdin.write(0)

        # run amplifier to get final output
        while True:
            if amps[4].done:
                outputs.append(amps[4].last_output)
                break
            for amp in amps:
                if not amp.done:
                    amp.step()

    print max(outputs)


def part2():
    outputs = []
    for c in itertools.permutations(range(5, 10)):

        # create 5 IntIO's
        ios = []
        for i in range(5):
            ios.append(IntIO())
     
        # create 5 amplifiers and connect their stdin/stdout
        amps = []
        for i in range(5):
            amp = IntRunner(prog, ios[i], ios[(i + 1) % 5])
            amp.stdin.write(c[i])
            amps.append(amp)

        # initialise first amplifier
        amps[0].stdin.write(0)

        # run amplifier to get final output
        while True:
            if amps[4].done:
                outputs.append(amps[4].last_output)
                break
            for amp in amps:
                if not amp.done:
                    amp.step()

    print max(outputs)


part1()
part2()
