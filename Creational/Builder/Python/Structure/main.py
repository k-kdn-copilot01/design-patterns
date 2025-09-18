"""
Client code that demonstrates the Builder pattern usage.
"""

from builder import ConcreteBuilder1, ConcreteBuilder2
from director import Director


def client_code(director: Director) -> None:
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """
    
    # Builder 1
    builder1 = ConcreteBuilder1()
    director.builder = builder1
    
    print("=== Structure Demo: Builder Pattern ===\n")
    
    print("Standard basic product (Builder 1):")
    director.build_minimal_viable_product()
    product = builder1.product
    print(product)
    
    print("\nStandard full featured product (Builder 1):")
    director.build_full_featured_product()
    product = builder1.product
    print(product)
    
    # Builder 2
    builder2 = ConcreteBuilder2()
    director.builder = builder2
    
    print("\nStandard basic product (Builder 2):")
    director.build_minimal_viable_product()
    product = builder2.product
    print(product)
    
    print("\nStandard full featured product (Builder 2):")
    director.build_full_featured_product()
    product = builder2.product
    print(product)
    
    # Without a director
    print("\nCustom product (without Director):")
    builder1 = ConcreteBuilder1()
    builder1.produce_part_a()
    builder1.produce_part_c()
    product = builder1.product
    print(product)
    
    print("\n=== Structure Demo Complete ===")


if __name__ == "__main__":
    director = Director()
    client_code(director)
