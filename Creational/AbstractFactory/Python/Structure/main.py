from concrete_factories import ConcreteFactory1, ConcreteFactory2
from client import Client


def client_code(factory):
    """
    The client code can work with any concrete factory class.
    """
    client = Client(factory)
    client.create_products()
    client.use_products()


if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())
    
    print("\nClient: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())
