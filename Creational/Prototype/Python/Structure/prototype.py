from abc import ABC, abstractmethod
import copy

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class ConcretePrototype(Prototype):
    def __init__(self, value):
        self.value = value
        self.nested = {'data': value}

    def clone(self, deep=False):
        if deep:
            return copy.deepcopy(self)
        return copy.copy(self)

class Client:
    @staticmethod
    def clone_prototype(prototype, deep=False):
        return prototype.clone(deep=deep)
