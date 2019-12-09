import sys


def op_assign(value):
    return value


def op_rshift(value, b):
    return value >> b

    
def op_lshift(value, b):
    return value << b


def op_or(v1, v2):
    return v1 | v2


def op_and(v1, v2):
    return v1 & v2


def op_not(value):
    return ~value


class Literal(object):
    def __init__(self, value):
        self.value = value


class Wire(object):

    def __init__(self):
        self.op = None
        self.inputs = None
        self.__value = None

    @property
    def value(self):
        if self.__value is not None:
            return self.__value
        self.__value = self.op(*[i.value for i in self.inputs])
        return self.__value

    @value.setter
    def value(self, v):
        self.__value = v

    def reset(self):
        self.value = None


class Circuit(object):

    def __init__(self):
        self.wires = {}

    def getWire(self, name):
        return self.wires.setdefault(name, Wire())

    def reset(self):
        for wire in self.wires.values():
            wire.reset()

    def _getLiteral(self, value):
        return Literal(int(value))

    def _getInput(self, value):
        try:
            return self._getLiteral(value)
        except:
            return self.getWire(value)

    def addWire(self, line):
        op, target = [p.strip() for p in line.split(' -> ')]
        target = self.getWire(target)
        if 'NOT' in op:
            _, i0 = op.split()
            target.op = op_not
            target.inputs = [self.getWire(i0)]
        elif 'OR' in op:
            i0, _, i1 = op.split()
            target.op = op_or
            target.inputs = [self._getInput(i0), self._getInput(i1)]
        elif 'AND' in op:
            i0, _, i1 = op.split()
            target.op = op_and
            target.inputs = [self._getInput(i0), self._getInput(i1)]
        elif 'LSHIFT' in op:
            i0, _, i1 = op.split()
            target.op = op_lshift
            target.inputs = [self.getWire(i0), self._getLiteral(i1)]
        elif 'RSHIFT' in op:
            i0, _, i1 = op.split()
            target.op = op_rshift
            target.inputs = [self.getWire(i0), self._getLiteral(i1)]
        else:
            i0 = op
            target.op = op_assign
            target.inputs = [self._getInput(i0)]

    @classmethod
    def load(cls, fd):
        circuit = cls()
        for line in fd:
            circuit.addWire(line)
        return circuit


circuit = Circuit.load(sys.stdin)

    
def part1():
    value = circuit.getWire('a').value
    print value
    return value


def part2(a):
    circuit.reset()
    circuit.getWire('b').value = a
    print circuit.getWire('a').value


part2(part1())
