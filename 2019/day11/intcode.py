class IntCodeRunner(object):

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
    def _immediate(mod, n):
        return ((mod >> (8 * n)) & 0xff) == 1

    @staticmethod
    def _realative(mod, n):
        return ((mod >> (8 * n)) & 0xff) == 2

    def _pagefault(self, addr):
        if addr < 0:
            raise Exception('_pagefault: bad address %d' % addr)
        extra = addr - len(self.prog) + 1
        self.prog.extend([0] * extra)
        
    def _read(self, addr):
        try:
            return self.prog[addr]
        except IndexError:
            self._pagefault(addr)
            return self.prog[addr]

    def _write(self, addr, v):
        try:
            self.prog[addr] = v
        except IndexError:
            self._pagefault(addr)
            self.prog[addr] = v

    def _operand(self, mod, n):
        v = self.pc + n
        if self._immediate(mod, n):
            return v
        if self._realative(mod, n):
            return self.relbase + self._read(v)
        return self._read(v)

    def add(self, mod):
        if self._immediate(mod, 2):
            raise Exception('add: parameter 2 cannot use _immediate mode')
        o = [self._operand(mod, n) for n in range(3)]
        self._write(o[2], self._read(o[0]) + self._read(o[1]))
        self.pc += 3

    def mul(self, mod):
        if self._immediate(mod, 2):
            raise Exception('mul: parameter 2 cannot use _immediate mode')
        o = [self._operand(mod, n) for n in range(3)]
        self._write(o[2], self._read(o[0]) * self._read(o[1]))
        self.pc += 3

    def get(self, mod):
        v = self.stdin.read()
        if v is None:
            self.pc -= 1 # wait for input (move pc back to get opcode)
        else:
            self._write(self._operand(mod, 0), v)
            self.pc += 1

    def put(self, mod):
        v = self._read(self._operand(mod, 0))
        self.last_output = v
        self.stdout.write(v)
        self.pc += 1

    def jnz(self, mod):
        o = [self._operand(mod, n) for n in range(2)]
        if self._read(o[0]):
            self.pc = self._read(o[1])
        else:
            self.pc += 2

    def jz(self, mod):
        o = [self._operand(mod, n) for n in range(2)]
        if not self._read(o[0]):
            self.pc = self._read(o[1])
        else:
            self.pc += 2

    def lt(self, mod):
        if self._immediate(mod, 2):
            raise Exception('lt: parameter 2 cannot use _immediate mode')
        o = [self._operand(mod, n) for n in range(3)]
        self._write(o[2], 1 if self._read(o[0]) < self._read(o[1]) else 0)
        self.pc += 3

    def eq(self, mod):
        if self._immediate(mod, 2):
            raise Exception('eq: parameter 2 cannot use _immediate mode')
        o = [self._operand(mod, n) for n in range(3)]
        self._write(o[2], 1 if self._read(o[0]) == self._read(o[1]) else 0)
        self.pc += 3

    def rbase(self, mod):
        self.relbase += self._read(self._operand(mod, 0))
        self.pc += 1

    def end(self):
        self.done = True
        self.exit_code = self._read(0)

    @staticmethod
    def _parse(v):
        mod, opcode = divmod(v, 100)
        mod, m0 = divmod(mod, 10)
        mod, m1 = divmod(mod, 10)
        mod, m2 = divmod(mod, 10)
        if m0 > 2 or m1 > 2 or m2 > 2:
            raise Exception('getop: Invalid mode')
        mod = m2 << 16 | m1 << 8 | m0
        return opcode, mod

    def step(self):
        opcode, mod = self._parse(self._read(self.pc))
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
