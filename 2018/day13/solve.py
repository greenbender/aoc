#!/usr/bin/python


import sys


class Cart(object):

    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.turn = 0

    def move(self):
        self.x += self.dx
        self.y += self.dy


class Straight(object):

    def modify(self, cart):
        pass


class Curve(Straight):

    def __init__(self, transform):
        self.transform = transform

    def modify(self, cart):
        t = self.transform
        cart.dx, cart.dy = (
            cart.dx * t[0] - cart.dy * t[1],
            cart.dx * t[2] + cart.dy * t[3]
        )


class Intersection(Straight):
    transforms = [
        [0, -1, -1,  0],
        [1,  0,  0,  1],
        [0,  1,  1,  0],
    ]

    def modify(self, cart):
        t = self.transforms[cart.turn]
        cart.dx, cart.dy = (
            cart.dx * t[0] - cart.dy * t[1],
            cart.dx * t[2] + cart.dy * t[3]
        )
        cart.turn = (cart.turn + 1) % 3


# singletons
straight = Straight()
curve_bs = Curve([0, -1,  1,  0])
curve_fs = Curve([0,  1, -1,  0])
intersection = Intersection()


class Track(object):

    def __init__(self, carts, track, state):
        self.carts = carts
        self.track = track
        self.state = state

    def tick(self):
        skip = []
        for cart in sorted(self.carts, key=lambda c: (c.y, c.x)):
            if cart in skip:
                continue

            self.state[cart.y][cart.x] = None
            cart.move()

            # crash
            victim = self.state[cart.y][cart.x]
            if victim:
                self.state[cart.y][cart.x] = None
                crashed = (victim, cart)
                for c in crashed:
                    skip.append(c)
                    self.carts.remove(c)
                yield crashed

            else:
                self.state[cart.y][cart.x] = cart
                self.track[cart.y][cart.x].modify(cart)

    @classmethod
    def load(cls, fd):
        carts = []
        track = [[None] * 150 for i in range(150)]
        state = [[None] * 150 for i in range(150)]
        for y, line in enumerate(fd):
            for x, c in enumerate(line):
                if c == '\\':
                    track[y][x] = curve_bs
                elif c == '/':
                    track[y][x] = curve_fs
                elif c == '+':
                    track[y][x] = intersection
                elif c in ['-', '|']:
                    track[y][x] = straight
                elif c == '>':
                    cart = Cart(x, y, 1, 0)
                    carts.append(cart)
                    track[y][x] = straight
                    state[y][x] = cart
                elif c == '<':
                    cart = Cart(x, y, -1, 0)
                    carts.append(cart)
                    track[y][x] = straight
                    state[y][x] = cart
                elif c == '^':
                    cart = Cart(x, y, 0, -1)
                    carts.append(cart)
                    track[y][x] = straight
                    state[y][x] = cart
                elif c == 'v':
                    cart = Cart(x, y, 0, 1)
                    carts.append(cart)
                    track[y][x] = straight
                    state[y][x] = cart
        return cls(carts, track, state)


first = True
track = Track.load(sys.stdin)
while len(track.carts) > 1:
    for victim, cart in track.tick():

        # part 1
        if first:
            first = False
            print '%d,%d' % (cart.x, cart.y)


# part 2
print '%d,%d' % (track.carts[0].x, track.carts[0].y)
