from concrete_factories import ConcreteFactory1, ConcreteFactory2
from client import Client

def main():
    factory1 = ConcreteFactory1()
    client1 = Client(factory1)
    client1.run()

    factory2 = ConcreteFactory2()
    client2 = Client(factory2)
    client2.run()

if __name__ == "__main__":
    main()
