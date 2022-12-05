import sys
import collections


Move = collections.namedtuple("Move", ["qty", "src", "dst"])


stacks = [list() for _ in range(9)]
for line in sys.stdin:
    if line.startswith(" 1"):
        break
    for i in range(9):
        c = line[4 * i + 1]
        if c != " ":
            stacks[i].append(c)


sys.stdin.readline()


moves = []
for line in sys.stdin:
    _, qty, _, src, _, dst = line.split()
    moves.append(Move(int(qty), int(src) - 1, int(dst) - 1))


# part 1
stacks1 = [collections.deque(s) for s in stacks]
for move in moves:
    for _ in range(move.qty):
        stacks1[move.dst].appendleft(stacks1[move.src].popleft())
print("".join([s.popleft() for s in stacks1]))


# part 2
stacks2 = [collections.deque(s) for s in stacks]
tmp = collections.deque()
for move in moves:
    for _ in range(move.qty):
        tmp.append(stacks2[move.src].popleft())
    for _ in range(move.qty):
        stacks2[move.dst].appendleft(tmp.pop())
print("".join([s.popleft() for s in stacks2]))
