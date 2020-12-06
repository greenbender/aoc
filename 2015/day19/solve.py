import sys
import re


replacements = []
for line in sys.stdin:
    line = line.strip()
    if not line:
        break
    f, t = line.split(' => ')
    replacements.append((f, t))


molecule = sys.stdin.readline().strip()


def replace(repl, molecule):
    for f, t in repl:
        for m in re.finditer(f, molecule):
            yield ''.join([m.string[:m.start()], t, m.string[m.end():]])


def mutate(repl, molecule, steps=0):
    yield molecule, steps
    for m in sorted(set(replace(repl, molecule)), key=len):
        yield from mutate(repl, m, steps + 1)


def part1():
    print(len(set(replace(replacements, molecule))))


def part2():
    repl = [(t, f) for f, t in replacements]
    for m, s in mutate(repl, molecule):
        if m == 'e':
            print(s)
            break


part1()
part2()
