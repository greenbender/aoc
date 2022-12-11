import sys


instructions = [line.strip() for line in sys.stdin]


def cycles(instructions, X=1):
    for instruction in instructions:
        if instruction == "noop":
            yield X
        else:
            yield X
            yield X
            X += int(instruction.split()[-1])


# part 1
signal = 0
for c0, X in enumerate(cycles(instructions)):
    c = c0 + 1
    if c in set([20, 60, 100, 140, 180, 220]):
        signal += X * c
    if c == 220:
        break
print(signal)


# part 2
crt = []
for c0, X in enumerate(cycles(instructions)):
    x = c0 % 40
    if x in (X - 1, X, X + 1):
        crt.append("#")
    else:
        crt.append(".")
    if x == 39:
        crt.append("\n")
print("".join(crt))
