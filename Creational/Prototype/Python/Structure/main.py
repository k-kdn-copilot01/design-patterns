from concrete_prototype_a import ConcretePrototypeA
from concrete_prototype_b import ConcretePrototypeB
from client import Client

if __name__ == "__main__":
    original_a = ConcretePrototypeA("Hello")
    client_a = Client(original_a)
    copy_a = client_a.make_copy()

    print("Original A:", original_a)
    print("Copy A:", copy_a)
    print("Same reference?", original_a is copy_a)

    original_b = ConcretePrototypeB(42)
    client_b = Client(original_b)
    copy_b = client_b.make_copy()

    print("Original B:", original_b)
    print("Copy B:", copy_b)
    print("Same reference?", original_b is copy_b)
