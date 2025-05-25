import math

class Operation:
   # Represents a mathematical operation with its symbol, function, and inputs


    def __init__(self, symbol, func, arity=2):
        self.symbol = symbol
        self.func = func
        self.arity = arity

    ## Apply the stored function to the given input arguments
    def evaluate(self, *args):
        return self.func(*args)
