from abc import ABC, abstractmethod

class AbstractProductA(ABC):
    @abstractmethod
    def useful_function_a(self) -> str: pass

class AbstractProductB(ABC):
    @abstractmethod
    def useful_function_b(self) -> str: pass
