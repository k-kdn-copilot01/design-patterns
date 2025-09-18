from prototype import Prototype
import copy

class ConcretePrototypeA(Prototype):
    def __init__(self, field: str):
        self.field = field

    def clone(self):
        # shallow copy
        return copy.copy(self)

    def __str__(self):
        return f"ConcretePrototypeA(field='{self.field}')"
