import sys

grids = []
for block in sys.stdin.read().split("\n\n"):
    grids.append(block.splitlines())


def to_num(line: str) -> int:
    return int(line.replace(".", "0").replace("#", "1"), 2)


def to_rows(grid: list[str]) -> list[int]:
    return [to_num(r) for r in grid]


def to_cols(grid: list[str]) -> list[int]:
    return [to_num("".join(c)) for c in zip(*grid)]


def is_reflection(data: list[int], i: int, smudges: int = 0) -> bool:
    j = i + 1
    s = 0
    while i >= 0 and j < len(data):
        xor = data[i] ^ data[j]
        s += xor.bit_count()
        if s > smudges:
            return False
        i -= 1
        j += 1
    return s == smudges


def reflections(data: list[int], smudges: int = 0):
    for i in range(len(data) - 1):
        if is_reflection(data, i, smudges):
            yield i


def part1():
    summary = 0
    for grid in grids:
        cols = to_cols(grid)
        for x in reflections(cols):
            summary += x + 1
        rows = to_rows(grid)
        for y in reflections(rows):
            summary += (y + 1) * 100
    print(summary)


part1()


def part2():
    summary = 0
    for grid in grids:
        cols = to_cols(grid)
        for x in reflections(cols, smudges=1):
            summary += x + 1
        rows = to_rows(grid)
        for y in reflections(rows, smudges=1):
            summary += (y + 1) * 100
    print(summary)


part2()
