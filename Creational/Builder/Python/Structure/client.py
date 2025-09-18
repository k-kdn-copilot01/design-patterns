from director import Director
from concrete_builder import ConcreteBuilder1, ConcreteBuilder2


class Client:
    """
    The Client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """
    
    def __init__(self):
        self.director = Director()
    
    def demonstrate_builder_pattern(self):
        """Demonstrate the Builder pattern with different builders"""
        print("=== Builder Pattern Demo ===\n")
        
        # Using ConcreteBuilder1
        print("1. Using ConcreteBuilder1:")
        builder1 = ConcreteBuilder1()
        self.director.builder = builder1
        
        print("   Building minimal product:")
        self.director.build_minimal_viable_product()
        product1 = builder1.get_result()
        print(f"   {product1}\n")
        
        print("   Building full featured product:")
        self.director.build_full_featured_product()
        product2 = builder1.get_result()
        print(f"   {product2}\n")
        
        # Using ConcreteBuilder2
        print("2. Using ConcreteBuilder2:")
        builder2 = ConcreteBuilder2()
        self.director.builder = builder2
        
        print("   Building minimal product:")
        self.director.build_minimal_viable_product()
        product3 = builder2.get_result()
        print(f"   {product3}\n")
        
        print("   Building full featured product:")
        self.director.build_full_featured_product()
        product4 = builder2.get_result()
        print(f"   {product4}\n")
        
        # Building custom products
        print("3. Building custom products:")
        print("   Custom product with parts A and C:")
        self.director.build_custom_product(['a', 'c'])
        product5 = builder2.get_result()
        print(f"   {product5}\n")
        
        # Direct builder usage (without Director)
        print("4. Direct builder usage (without Director):")
        builder1 = ConcreteBuilder1()
        product6 = (builder1
                   .build_part_b()
                   .build_part_c()
                   .get_result())
        print(f"   {product6}\n")
        
        print("=== Demo Complete ===")


if __name__ == "__main__":
    client = Client()
    client.demonstrate_builder_pattern()
