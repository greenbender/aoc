import sys


if len(sys.argv) != 2:
    print "Usage: %s input"
    sys.exit(1)


prog = map(int, open(sys.argv[1], 'rb').read().split(','))


def immediate(mod, n):
    return mod & (1 << n)

    
def operand(p, pc, mod, n):
    v = pc + n
    if immediate(mod, n):
        return v
    return p[v]

    
def add(p, pc, mod):
    if immediate(mod, 2):
        raise Exception('add: parameter 2 must use position mode')
    o = [operand(p, pc, mod, n) for n in range(3)]
    p[o[2]] = p[o[0]] + p[o[1]]
    return pc + 3


def mul(p, pc, mod):
    if immediate(mod, 2):
        raise Exception('mul: parameter 2 must use position mode')
    o = [operand(p, pc, mod, n) for n in range(3)]
    p[o[2]] = p[o[0]] * p[o[1]]
    return pc + 3


def get(p, pc, mod):
    if immediate(mod, 0):
        raise Exception('get: parameter 0 must use position mode')
    v = int(input('Input: '))
    p[operand(p, pc, mod, 0)] = v
    return pc + 1


def put(p, pc, mod):
    print 'Output:', p[operand(p, pc, mod, 0)]
    return pc + 1


def jnz(p, pc, mod):
    o = [operand(p, pc, mod, n) for n in range(2)]
    if p[o[0]]:
        return p[o[1]]
    return pc + 2


def jz(p, pc, mod):
    o = [operand(p, pc, mod, n) for n in range(2)]
    if not p[o[0]]:
        return p[o[1]]
    return pc + 2


def lt(p, pc, mod):
    if immediate(mod, 2):
        raise Exception('lt: parameter 2 must use position mode')
    o = [operand(p, pc, mod, n) for n in range(3)]
    p[o[2]] = 1 if p[o[0]] < p[o[1]] else 0
    return pc + 3


def eq(p, pc, mod):
    if immediate(mod, 2):
        raise Exception('eq: parameter 2 must use position mode')
    o = [operand(p, pc, mod, n) for n in range(3)]
    p[o[2]] = 1 if p[o[0]] == p[o[1]] else 0
    return pc + 3


def getop(v):
    mod, opcode = divmod(v, 100)
    mod, b0 = divmod(mod, 10)
    mod, b1 = divmod(mod, 10)
    mod, b2 = divmod(mod, 10)
    if b0 > 1 or b1 > 1 or b2 > 1:
        raise Exception('Invalid mode')
    mod = b2 << 2 | b1 << 1 | b0
    return opcode, mod


def run(p):
    pc = 0
    while True:
        opcode, mod = getop(p[pc])
        pc += 1
        if opcode == 99:
            return p[0]
        elif opcode == 1:
            pc = add(p, pc, mod)
        elif opcode == 2:
            pc = mul(p, pc, mod)
        elif opcode == 3:
            pc = get(p, pc, mod)
        elif opcode == 4:
            pc = put(p, pc, mod)
        elif opcode == 5:
            pc = jnz(p, pc, mod)
        elif opcode == 6:
            pc = jz(p, pc, mod)
        elif opcode == 7:
            pc = lt(p, pc, mod)
        elif opcode == 8:
            pc = eq(p, pc, mod)
        else:
            raise Exception('Program error at %d: %d' % (pc, p[pc]))


# part1 & part2
run(prog)
