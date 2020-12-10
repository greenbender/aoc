import sys


adapters = list(sorted(map(int, sys.stdin)))
adapters.append(max(adapters) + 3)


def combos(s):
    '''Get number of combinations for given list of sequential adapters when
    one or two adapters is removed, then perform the same operation recursively
    for each subset of sequential adapters that can be made when two adjacent
    adapters are removed

    Number of combinations calculation:

    Given a list of nodes as shown (x denotes fixed node that can't be removed)

    x-o-o-o ... o-x

    n = number of nodes
    k = number of non-fixed nodes
    k = n - 2

    Number of combinations with one node removed
    c1 = k

    Number of combinations with two nodes removed
    c2 = k(k - 1)/2
         
    Total combinations with one or to nodes removed
    c = c1 + c2
      = k + k(k - 1)/2
      = k(k + 1)/2
      = (n - 2)(n - 1)/2

    NOTE: In my input the recursion would not even have been necessary as I
    only had sequential nodes in groups or 5 or less where recursion doesn't
    yield additional combinations. Infact, given the short nature of the runs
    of sequential nodes in the input hard-coding the combinations into a simple
    switch-like statement would be the fastest solution.
    '''
    n = len(s)
    if n < 3:
        return 0
    c = ((n - 2) * (n -1)) // 2
    for i in range(1, n-2):
        c += combos(s[0:i])
        c += combos(s[i+2:n])
    return c
    

def part1():
    d, l = {}, 0
    for a in adapters:
        v = a - l
        d.setdefault(v, 0)
        d[v] += 1
        l = a
    print(d[1] * d[3])


def part2():
    '''Break adapters into runs of sequential adapters, and the multiply the
    combinations for the sequential runs of adapters together to get the total
    number of combinations'''
    part, l = [], 0
    c = 1
    for a in adapters:
        v = a - l
        part.append(l)
        if v > 1:
            c *= combos(part) + 1
            del part[:]
        l = a
    if part:
        c *= combos(part) + 1
    print(c)


part1()
part2()
