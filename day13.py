#!/usr/bin/python


import sys


class Cart(object):
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.turn = 0


class Element(object):
    def modify(self, cart):
        cart.x += cart.dx
        cart.y += cart.dy


class Curve(Element):
    def __init__(self, transform):
        self.transform = transform
    def modify(self, cart):
        t = self.transform
        cart.dx, cart.dy = (
            cart.dx * t[0] - cart.dy * t[1],
            cart.dx * t[2] + cart.dy * t[3]
        )
        super(Curve, self).modify(cart)


class Intersection(Element):
    transforms = [
        [0,-1,-1, 0],
        [1, 0, 0, 1],
        [0, 1, 1, 0],
    ]
    def modify(self, cart):
        t = self.transforms[cart.turn]
        cart.dx, cart.dy = (
            cart.dx * t[0] - cart.dy * t[1],
            cart.dx * t[2] + cart.dy * t[3]
        )
        cart.turn = (cart.turn + 1) % 3
        super(Intersection, self).modify(cart)


# singletons
straight = Element()
curve_bs = Curve([0,-1, 1, 0])
curve_fs = Curve([0, 1,-1, 0])
intersection = Intersection()


# keep track of where the carts are
class State(object):
    def __init__(self, element, cart=None):
        self.element = element
        self.cart = cart


def parse_track(fd):
    carts = []
    track = [[None] * 150 for i in range(150)]
    for y, line in enumerate(fd):
        for x, c in enumerate(line):
            if c == '\\':
                track[y][x] = State(curve_bs)
            elif c == '/':
                track[y][x] = State(curve_fs)
            elif c == '+':
                track[y][x] = State(intersection)
            elif c in ['-', '|']:
                track[y][x] = State(straight)
            elif c == '>':
                cart = Cart(x, y, 1, 0)
                carts.append(cart)
                track[y][x] = State(straight, cart)
            elif c == '<':
                cart = Cart(x, y, -1, 0)
                carts.append(cart)
                track[y][x] = State(straight, cart)
            elif c == '^':
                cart = Cart(x, y, 0, -1)
                carts.append(cart)
                track[y][x] = State(straight, cart)
            elif c == 'v':
                cart = Cart(x, y, 0, 1)
                carts.append(cart)
                track[y][x] = State(straight, cart)
    return carts, track


def drive(carts, track):
    first_crash = True
    while True:
        crashed_carts = []
        for cart in sorted(carts, key=lambda c: (c.y, c.x)):

            if cart in crashed_carts:
                continue

            # move the cart 
            s0 = track[cart.y][cart.x]
            s0.element.modify(cart)
            s0.cart = None

            # check for a crash
            s1 = track[cart.y][cart.x]
            if s1.cart:
            
                # part 1
                if first_crash:
                    first_crash = False
                    print '%d,%d' % (cart.x, cart.y)

                # remove carts
                crashed_carts.extend([cart, s1.cart])
                s1.cart = None

            # update the track state
            else:
                s1.cart = cart

        # remove crashed carts
        for cart in crashed_carts:
            carts.remove(cart)

        # part 2
        if len(carts) == 1:
            print '%d,%d' % (carts[0].x, carts[0].y)
            break
    


carts, track = parse_track(sys.stdin)
drive(carts, track)
