import sys
import json


document = json.load(sys.stdin)


def add_numbers(obj, ignore=None):
    if isinstance(obj, int):
        return obj
    elif isinstance(obj, list):
        return sum(add_numbers(v, ignore) for v in obj)
    elif isinstance(obj, dict):
        if ignore and ignore in obj.values():
            return 0
        return sum(add_numbers(v, ignore) for v in obj.values())
    return 0


def part1():
    print(add_numbers(document))


def part2():
    print(add_numbers(document, ignore='red'))


part1()
part2()
