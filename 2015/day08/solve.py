import sys
import ast


strings = [l.strip() for l in sys.stdin]


def lengths(string):
    chars = len(string)
    code = len(ast.literal_eval(string))
    return chars, code


def encode(string):
    return '"' + string.replace('\\', '\\\\').replace('"', '\\"') + '"'

    
def part1(strings):
    chars = code = 0
    for line in strings:
        ch, co = lengths(line)
        chars += ch
        code += co
    print(chars - code)


def part2(strings):
    encoded = map(encode, strings)
    part1(encoded)


part1(strings)
part2(strings)
