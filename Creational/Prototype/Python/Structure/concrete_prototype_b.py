from prototype import Prototype
import copy

class ConcretePrototypeB(Prototype):
    def __init__(self, number: int):
        self.number = number

    def clone(self):
        # deep copy
        return copy.deepcopy(self)

    def __str__(self):
        return f"ConcretePrototypeB(number={self.number})"
