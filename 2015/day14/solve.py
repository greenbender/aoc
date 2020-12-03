import sys


reindeer = {}
for line in sys.stdin:
    r, _, _, s, _, _, fd, _, _, _, _, _, _, rd, _ = line.split()
    s, fd, rd = map(int, (s, fd, rd))
    reindeer[r] = (s, fd, rd)


def race(duration):
    distances = {}
    for r, stats in reindeer.items():
        s, fd, rd = stats
        full, partial = divmod(duration, fd + rd)
        distance = (full * fd + min(fd, partial)) * s
        distances[r] = distance
    return distances


def part1(duration):
    print(max(race(duration).values()))


def part2(duration):
    points = {n: 0 for n in reindeer}
    for i in range(1, duration + 1):
        distances = race(i)
        furthest = max(distances.values())
        for n, d in distances.items():
            if d == furthest:
                points[n] += 1
    print(max(points.values()))


part1(2503)
part2(2503)
