import sys


def atob26(a):
    return bytearray(map(lambda v: v - ord(b'a'), a.encode('ascii')))


def b26toa(b):
    return bytes(map(lambda v: v + ord(b'a'), b)).decode('ascii')


def _incb26(v, n):
    v += n
    n, v = divmod(v, 26)
    return v, n

 
def incb26(b, n):
    i = len(b) - 1
    while n and i >= 0:
        b[i], n = _incb26(b[i], n)
        i -= 1
    return n


password = atob26(sys.stdin.readline().strip())
iol = atob26('iol')


def check(pwd):
    straight = double = 0
    for i in range(len(pwd)):
        if pwd[i] in iol:
            return False
        if i > 1 and pwd[i-2] + 2 == pwd[i-1] + 1 == pwd[i]:
            straight += 1
        if i > 0 and pwd[i-1] == pwd[i]:
            if i == 1 or (i > 1 and pwd[i-2] != pwd[i-1]):
                double += 1
    return straight > 0 and double > 1


def part1():
    while True:
        if check(password):
            print(b26toa(password))
            break
        if incb26(password, 1):
            print('overflowed')
            break


def part2():
    if incb26(password, 1):
        print('overflowed')
        return
    part1()


part1()
part2()
