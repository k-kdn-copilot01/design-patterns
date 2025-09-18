from concrete_creator_a import ConcreteCreatorA
from concrete_creator_b import ConcreteCreatorB
from client import client_code

if __name__ == "__main__":
    print("App: Using ConcreteCreatorA")
    client_code(ConcreteCreatorA())

    print("\nApp: Using ConcreteCreatorB")
    client_code(ConcreteCreatorB())
