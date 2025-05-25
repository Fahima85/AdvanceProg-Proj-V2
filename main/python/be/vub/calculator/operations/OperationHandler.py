import math
from .Operation import Operation  

class OperationHandler:

    def __init__(self):
        self.operations = [
            # Binary operations
            Operation('+', lambda a, b: a + b),
            Operation('-', lambda a, b: a - b),
            Operation('*', lambda a, b: a * b),
            Operation('/', lambda a, b: a / b if b != 0 else float('inf')),
            Operation('^', lambda a, b: a ** b),

            # Unary operations
            Operation('sin', math.sin, arity=1),
            Operation('cos', math.cos, arity=1),
            Operation('tan', math.tan, arity=1),
            Operation('log', lambda a: math.log(a) if a > 0 else float('-inf'), arity=1),
            Operation('sqrt', lambda a: math.sqrt(a) if a >= 0 else float('nan'), arity=1),
            Operation('exp', math.exp, arity=1)
        ]

        self.binary_ops = dict(map(lambda op: (op.symbol, op),filter(lambda op: op.arity == 2, self.operations)))      
        self.unary_ops = dict(map(lambda op: (op.symbol, op),filter(lambda op: op.arity == 1, self.operations)))


    def evaluate_binary(self, symbol, a, b):
        if symbol not in self.binary_ops:
            raise ValueError(f"Unsupported binary operation: {symbol}")
        return self.binary_ops[symbol].evaluate(a, b)

    def evaluate_unary(self, symbol, a):
        if symbol not in self.unary_ops:
            raise ValueError(f"Unsupported unary operation: {symbol}")
        return self.unary_ops[symbol].evaluate(a)