import sys
import itertools


if len(sys.argv) != 2:
    print "Usage: %s input"
    sys.exit(1)


prog = map(int, open(sys.argv[1], 'rb').read().split(','))


class IntCoder(object):

    def __init__(self, prog, phase):
        self.prog = prog
        self.pc = 0
        self.inputs = [phase]
        self.attached = None
        self.signal = None
        self.done = False

    def attach(self, coder):
        self.attached = coder

    def add_input(self, value):
        self.inputs.append(value)

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
        return self.pc + 3

    def mul(self, mod):
        if self.immediate(mod, 2):
            raise Exception('mul: parameter 2 must use position mode')
        o = [self.operand(mod, n) for n in range(3)]
        self.prog[o[2]] = self.prog[o[0]] * self.prog[o[1]]
        return self.pc + 3

    def get(self, mod):
        if not self.inputs:
            return self.pc - 1
        else:
            v = self.inputs.pop(0)
            self.prog[self.operand(mod, 0)] = v
            return self.pc + 1

    def put(self, mod):
        v = self.prog[self.operand(mod, 0)]
        self.signal = v
        if self.attached:
            self.attached.add_input(v)
        else:
            print "Output:", v
        return self.pc + 1

    def jnz(self, mod):
        o = [self.operand(mod, n) for n in range(2)]
        if self.prog[o[0]]:
            return self.prog[o[1]]
        return self.pc + 2

    def jz(self, mod):
        o = [self.operand(mod, n) for n in range(2)]
        if not self.prog[o[0]]:
            return self.prog[o[1]]
        return self.pc + 2

    def lt(self, mod):
        if self.immediate(mod, 2):
            raise Exception('lt: parameter 2 must use position mode')
        o = [self.operand(mod, n) for n in range(3)]
        self.prog[o[2]] = 1 if self.prog[o[0]] < self.prog[o[1]] else 0
        return self.pc + 3

    def eq(self, mod):
        if self.immediate(mod, 2):
            raise Exception('eq: parameter 2 must use position mode')
        o = [self.operand(mod, n) for n in range(3)]
        self.prog[o[2]] = 1 if self.prog[o[0]] == self.prog[o[1]] else 0
        return self.pc + 3


    @staticmethod
    def getop(v):
        mod, opcode = divmod(v, 100)
        mod, b0 = divmod(mod, 10)
        mod, b1 = divmod(mod, 10)
        mod, b2 = divmod(mod, 10)
        if b0 > 1 or b1 > 1 or b2 > 1:
            raise Exception('Invalid mode')
        mod = b2 << 2 | b1 << 1 | b0
        return opcode, mod


    def step(self):
        opcode, mod = self.getop(self.prog[self.pc])
        self.pc += 1
        if opcode == 99:
            self.done = True
            return True
        elif opcode == 1:
            self.pc = self.add(mod)
        elif opcode == 2:
            self.pc = self.mul(mod)
        elif opcode == 3:
            self.pc = self.get(mod)
        elif opcode == 4:
            self.pc = self.put(mod)
        elif opcode == 5:
            self.pc = self.jnz(mod)
        elif opcode == 6:
            self.pc = self.jz(mod)
        elif opcode == 7:
            self.pc = self.lt(mod)
        elif opcode == 8:
            self.pc = self.eq(mod)
        else:
            raise Exception('Program error at %d: %d' % (pc, p[pc]))
        return False

    def run(self):
        while True:
            if self.step():
                break


outputs = []
for c in itertools.permutations(range(5, 10)):

    print c

    amps = []
    for i in range(5):
        amps.append(IntCoder(list(prog), c[i]))

    amps[0].attach(amps[1])
    amps[1].attach(amps[2])
    amps[2].attach(amps[3])
    amps[3].attach(amps[4])
    amps[4].attach(amps[0])

    amps[0].add_input(0)

    while True:
        if amps[4].done:
            outputs.append(amps[4].signal)
            print amps[4].signal
            break
        for amp in amps:
            if not amp.done:
                amp.step()

print max(outputs)
