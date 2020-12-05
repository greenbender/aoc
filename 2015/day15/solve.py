import sys


ingredients = []
for line in sys.stdin:
    _, _, cap, _, dur, _, fla, _, tex, _, cal = line.split()
    cap, dur, fla, tex, cal = [int(v.rstrip(',')) for v in (cap, dur, fla, tex, cal)]
    ingredients.append((cap, dur, fla, tex, cal))


def receipes(teaspoons, n):
    if not teaspoons or n == 1:
        yield [teaspoons] * n
    else:    
        for tsp in range(teaspoons + 1):
            for tsps in receipes(teaspoons - tsp, n - 1):
                tsps.insert(0, tsp)
                yield tsps


def bake(tsps):
    cap = dur = fla = tex = cal = 0
    for i in range(len(ingredients)):
        cap += ingredients[i][0] * tsps[i]
        dur += ingredients[i][1] * tsps[i]
        fla += ingredients[i][2] * tsps[i]
        tex += ingredients[i][3] * tsps[i]
        cal += ingredients[i][4] * tsps[i]
    return cap, dur, fla, tex, cal


def part1():
    best = 0
    for receipe in receipes(100, len(ingredients)):
        cap, dur, fla, tex, cal = map(lambda v: max(v, 0), bake(receipe))
        score = cap * dur * fla * tex
        best = max(best, score)
    print(best)


def part2():
    best = 0
    for receipe in receipes(100, len(ingredients)):
        cap, dur, fla, tex, cal = map(lambda v: max(v, 0), bake(receipe))
        if cal == 500:
            score = cap * dur * fla * tex
            best = max(best, score)
    print(best)


part1()
part2()
