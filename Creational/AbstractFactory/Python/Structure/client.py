from abstract_factory import AbstractFactory

class Client:
    def __init__(self, factory: AbstractFactory):
        self.product_a = factory.create_product_a()
        self.product_b = factory.create_product_b()

    def run(self):
        print(f"{self.product_a.useful_function_a()} + {self.product_b.useful_function_b()}")
