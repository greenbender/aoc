#!/usr/bin/python


import re
import sys
from collections import namedtuple


def to_python(line):
    numbers = re.findall(r'-?\d+', line)
    return Point(*map(int, numbers))


class Point(object):

    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def advance(self):
        self.x += self.dx
        self.y += self.dy

    def retreat(self):
        self.x -= self.dx
        self.y -= self.dy


Data = namedtuple('Data', [
    'left', 'top', 'right', 'bottom',
    'width', 'height',
    'area'
])


def data(points):
    left = min([p.x for p in points])
    top = min([p.y for p in points])
    right = max([p.x for p in points])
    bottom = max([p.y for p in points])
    width = right - left + 1
    height = bottom - top + 1
    area = width * height
    return Data(
        left, top, right, bottom,
        width, height,
        area
    )


points = map(to_python, sys.stdin)


seconds = 0
last = data(points)
while True:
    for point in points:
        point.advance()
    current = data(points)
    if current.area > last.area:
        break
    seconds += 1
    last = current


# last pattern was the most cohesive
for point in points:
    point.retreat()

# part 1
plot = [' '] * last.area
for point in points:
    x = point.x - last.left
    y = point.y - last.top
    plot[y * last.width + x] = '#'
for y in range(last.height):
    for x in range(last.width):
        sys.stdout.write(plot[y * last.width + x])
    sys.stdout.write('\n')


# part 2
print seconds
