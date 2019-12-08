import sys
import itertools


image = map(int, sys.stdin.read().strip())


def layers(image, width, height):
    size = width * height
    while image:
        layer, image = image[:size], image[size:]
        yield layer


def part1():
    info = []
    for layer in layers(image, 25, 6):
        info.append({k: len(list(g)) for k, g in itertools.groupby(sorted(layer))})
    least = min(info, key=lambda i: i[0])
    print least[1] * least[2]


def part2():
    output = [2] * (25 * 6)
    for layer in layers(image, 25, 6):
        for i, v in enumerate(layer):
            if output[i] == 2:
                output[i] = layer[i]
    for y in range(6):
        for x in range(25):
            v = output[y * 25 + x]
            sys.stdout.write('##' if v else '  ')
        sys.stdout.write('\n')


part1()
part2()
