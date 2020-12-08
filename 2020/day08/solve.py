import sys


instructions = []
for line in sys.stdin:
    op, value = line.split()
    instructions.append((op, int(value)))


def run(inst):
    accum = pc = 0
    count = [0] * len(inst)
    while True:
        if pc == len(inst):
            return True, accum
        if count[pc] > 0:
            return False, accum
        count[pc] += 1
        op, value = inst[pc]
        if op == 'acc':
            accum += value
            pc += 1
        elif op == 'jmp':
            pc += value
        else:
            pc += 1


def part1():
    print(run(instructions)[1])


def part2():
    for i in range(len(instructions)):
        op, value = instructions[i]
        if op == 'nop':
            instructions[i] = ('jmp', value)
        elif op == 'jmp':
            instructions[i] = ('nop', value)
        done, accum = run(instructions)
        if done:
            print(accum)
            break
        instructions[i] = (op, value)


part1()
part2()
