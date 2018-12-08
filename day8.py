#!/usr/bin/python


import sys


class Node(object):
    def __init__(self, children, metadata):
        self.children = children
        self.metadata = metadata
    @classmethod
    def load(cls, data):
        nc, c = data.pop(0), []
        nm, m = data.pop(0), []
        for i in range(nc):
            c.append(cls.load(data))
        for i in range(nm):
            m.append(data.pop(0))
        return cls(c, m)
    def metadata_sum(self):
        total = sum(self.metadata)
        for c in self.children:
            total += c.metadata_sum()
        return total
    def value(self):
        if not self.children:
            return sum(self.metadata)
        total = 0
        for entry in self.metadata:
            if entry and len(self.children) >= entry:
                total += self.children[entry-1].value()
        return total
        

data = map(int, sys.stdin.read().split())
node = Node.load(data)


# part 1
print node.metadata_sum()


# part 2
print node.value()
