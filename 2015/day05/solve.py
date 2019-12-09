import sys


strings = [l.strip() for l in sys.stdin]


def nice1(string):
    vowels, double = 0, False
    for i in range(len(string)):
        if i > 0:
            if string[i-1:i+1] in ('ab', 'cd', 'pq', 'xy'):
                return False 
            if not double and string[i-1] == string[i]:
                double = True
        if vowels < 3 and string[i] in 'aeiou':
            vowels += 1
    return double and vowels >= 3


def nice2(string):
    triple = pair = False
    for i in range(len(string)):
        if i > 0 and not pair:
            two = string[i-1:i+1]
            if two in string[:i-1] or two in string[i+1:]:
                pair = True
        if i > 1 and not triple:
            three = string[i-2:i+1]
            if three[0] == three[2]:
                triple = True
    return triple and pair
    

def part1():
    print len(filter(nice1, strings))


def part2():
    print len(filter(nice2, strings))


part1()
part2()
