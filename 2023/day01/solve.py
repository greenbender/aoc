import re
import sys

lines = [line.strip() for line in sys.stdin]


def part1():
    regex = re.compile(r"\d")
    total = 0
    for line in lines:
        numbers = [int(c) for c in regex.findall(line)]
        total += numbers[0] * 10 + numbers[-1]
    print(total)


def part2():
    decimal = "123456789"
    alpha = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    to_int = {v: int(v) for v in decimal}
    to_int.update({v: i + 1 for i, v in enumerate(alpha)})
    regex = re.compile(f"(?=(\\d|{'|'.join(alpha)}))")
    total = 0
    for line in lines:
        numbers = [to_int[c] for c in regex.findall(line)]
        total += numbers[0] * 10 + numbers[-1]
    print(total)


part1()
part2()
