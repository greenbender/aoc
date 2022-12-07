import sys
from functools import cached_property


class Node:
    def __init__(self, name, size=0, parent=None, dirs=None, files=None):
        self.name = name
        self.size = size
        self.parent = parent
        self.dirs = dirs or {}
        self.files = files or {}

    def walk(self):
        yield self
        for d in self.dirs.values():
            yield from d.walk()

    @cached_property
    def totalSize(self):
        size = self.size
        for f in self.files.values():
            size += f.totalSize
        for d in self.dirs.values():
            size += d.totalSize
        return size

    @classmethod
    def load(cls, fd):
        root = node = cls("/")
        for line in fd:
            if line.startswith("$ cd"):
                _, _, name = line.split()
                if name == "/":
                    node = root
                elif name == "..":
                    assert node.parent
                    node = node.parent
                else:
                    assert name in node.dirs
                    node = node.dirs[name]
            elif line.startswith("$ ls"):
                pass
            elif line.startswith("dir"):
                _, name = line.split()
                node.dirs[name] = Node(name, parent=node)
            else:
                size, name = line.split()
                node.files[name] = Node(name, size=int(size), parent=node)
        return root


root = Node.load(sys.stdin)


# part 1
print(sum(d.totalSize for d in root.walk() if d.totalSize <= 100000))


# part 2
free = 70000000 - root.totalSize
print(min(d.totalSize for d in root.walk() if free + d.totalSize >= 30000000))
