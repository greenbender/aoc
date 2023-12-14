import sys
from itertools import pairwise

grids = []
for block in sys.stdin.read().split("\n\n"):
    grids.append(block.splitlines())


def to_num(line: str) -> int:
    return int(line.replace(".", "0").replace("#", "1"), 2)


def to_rows(grid: list[str]) -> list[int]:
    return [to_num(r) for r in grid]


def to_cols(grid: list[str]) -> list[int]:
    return [to_num("".join(c)) for c in zip(*grid)]


def maybe_reflection(data: list[int]):
    for i, pair in enumerate(pairwise(data)):
        if pair[0] == pair[1]:
            yield i


def test_reflection(data: list[int], i: int) -> bool:
    j = i + 1
    while i >= 0 and j < len(data):
        if data[i] != data[j]:
            return False
        i -= 1
        j += 1
    return True


def part1():
    summary = 0
    for grid in grids:
        cols = to_cols(grid)
        for x in maybe_reflection(cols):
            if test_reflection(cols, x):
                summary += x + 1
        rows = to_rows(grid)
        for y in maybe_reflection(rows):
            if test_reflection(rows, y):
                summary += (y + 1) * 100
    print(summary)


part1()


def maybe_reflection_smudged(data: list[int]):
    for i, pair in enumerate(pairwise(data)):
        xor = pair[0] ^ pair[1]
        if xor.bit_count() <= 1:
            yield i


def test_reflection_smudged(data: list[int], i: int) -> bool:
    smudges = 0
    j = i + 1
    while i >= 0 and j < len(data):
        xor = data[i] ^ data[j]
        smudges += xor.bit_count()
        if smudges > 1:
            return False
        i -= 1
        j += 1
    return smudges == 1


def part2():
    summary = 0
    for grid in grids:
        cols = to_cols(grid)
        for x in maybe_reflection_smudged(cols):
            if test_reflection_smudged(cols, x):
                summary += x + 1
        rows = to_rows(grid)
        for y in maybe_reflection_smudged(rows):
            if test_reflection_smudged(rows, y):
                summary += (y + 1) * 100
    print(summary)


part2()
