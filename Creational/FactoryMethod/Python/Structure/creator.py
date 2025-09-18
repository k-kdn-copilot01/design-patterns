from abc import ABC, abstractmethod
from product import Product

class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        return f"Creator: working with {product.operation()}"
