import collections
import copy


monkeys = [
    {
        "items": collections.deque([89, 73, 66, 57, 64, 80]),
        "op": lambda v: v * 3,
        "test": lambda v: 6 if v % 13 == 0 else 2,
        "inspections": 0,
    },
    {
        "items": collections.deque([83, 78, 81, 55, 81, 59, 69]),
        "op": lambda v: v + 1,
        "test": lambda v: 7 if v % 3 == 0 else 4,
        "inspections": 0,
    },
    {
        "items": collections.deque([76, 91, 58, 85]),
        "op": lambda v: v * 13,
        "test": lambda v: 1 if v % 7 == 0 else 4,
        "inspections": 0,
    },
    {
        "items": collections.deque([71, 72, 74, 76, 68]),
        "op": lambda v: v * v,
        "test": lambda v: 6 if v % 2 == 0 else 0,
        "inspections": 0,
    },
    {
        "items": collections.deque([98, 85, 84]),
        "op": lambda v: v + 7,
        "test": lambda v: 5 if v % 19 == 0 else 7,
        "inspections": 0,
    },
    {
        "items": collections.deque([78]),
        "op": lambda v: v + 8,
        "test": lambda v: 3 if v % 5 == 0 else 0,
        "inspections": 0,
    },
    {
        "items": collections.deque([86, 70, 60, 88, 88, 78, 74, 83]),
        "op": lambda v: v + 4,
        "test": lambda v: 1 if v % 11 == 0 else 2,
        "inspections": 0,
    },
    {
        "items": collections.deque([81, 58]),
        "op": lambda v: v + 5,
        "test": lambda v: 3 if v % 17 == 0 else 5,
        "inspections": 0,
    },
]


# part 1
monkeys1 = copy.deepcopy(monkeys)
for i in range(20):
    for monkey in monkeys1:
        while monkey["items"]:
            item = monkey["items"].popleft()
            item = monkey["op"](item)
            item //= 3
            dst = monkey["test"](item)
            monkeys1[dst]["items"].append(item)
            monkey["inspections"] += 1
monkeys1.sort(key=lambda m: m["inspections"], reverse=True)
print(monkeys1[0]["inspections"] * monkeys1[1]["inspections"])


# part 2
divisor = 13 * 3 * 7 * 2 * 19 * 5 * 11 * 17
monkeys2 = copy.deepcopy(monkeys)
for i in range(10000):
    for monkey in monkeys2:
        while monkey["items"]:
            item = monkey["items"].popleft()
            item = monkey["op"](item)
            item %= divisor
            dst = monkey["test"](item)
            monkeys2[dst]["items"].append(item)
            monkey["inspections"] += 1
monkeys2.sort(key=lambda m: m["inspections"], reverse=True)
print(monkeys2[0]["inspections"] * monkeys2[1]["inspections"])
