import sys


numbers = list(map(int, sys.stdin.readline().split(',')))
boards = [list(map(int, b.split())) for b in sys.stdin.read().strip().split('\n\n')]


def mark(board, n):
    try:
        board[board.index(n)] = None
    except:
        pass


def win(board):
    sentinel = [None, None, None, None, None]
    for y in range(5):
        row = board[y * 5: y * 5 + 5]
        if row == sentinel:
            return True
    for x in range(5):
        col = []
        for y in range(5):
            col.append(board[x + y * 5])
        if col == sentinel:
            return True
    return False


def part1():
    _boards = [list(b) for b in boards]
    for n in numbers:
        for b in _boards:
            mark(b, n)
            if win(b):
                print(sum(v for v in b if v is not None) * n)
                return


def part2():
    _boards = [list(b) for b in boards]
    for n in numbers:
        for b in list(_boards):
            mark(b, n)
            if win(b):
                if len(_boards) == 1:
                    print(sum(v for v in b if v is not None) * n)
                    return
                _boards.remove(b)


part1()
part2()
