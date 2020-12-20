import sys


rules = {}
for line in sys.stdin:
    line = line.strip()
    if not line:
        break
    rule, reqs = line.split(': ', 1)
    rule = int(rule)
    if reqs == '"a"':
        rules[rule] = 'a'
    elif reqs == '"b"':
        rules[rule] = 'b'
    else:
        rules[rule] = []
        for opt in reqs.split(' | '):
            refs = list(map(int, opt.split(' ')))
            rules[rule].append(refs)


messages = [l.strip() for l in sys.stdin]


def validate(msg):
    def _validate(msg, r):
        if not msg:
            return False, msg
        opts = rules[r]
        if isinstance(opts, str):
            if opts == 'a' and msg[0] != 'a':
                return False, msg
            if opts == 'b' and msg[0] != 'b':
                return False, msg
            return True, msg[1:]
        else:
            for opt in opts:
                v, m = True, msg
                for i, ref in enumerate(opt):
                    v, m = _validate(m, ref)
                    if not v or r == ref == 11 and not m:
                        break
                if v:
                    return True, m
            return False, msg
    v, m = _validate(msg, 0)
    return v and m == ''


def part1():
    print(len(list(filter(validate, messages))))


def part2():
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    part1()


part1()
part2()
