"""
Prototype Pattern - Structure Demo
Demonstrates shallow vs deep cloning and object independence
"""

from prototype import ConcretePrototypeA, ConcretePrototypeB, Client


def demonstrate_shallow_vs_deep_clone():
    """
    Demonstrates the difference between shallow and deep cloning
    """
    print("=" * 60)
    print("SHALLOW vs DEEP CLONE DEMONSTRATION")
    print("=" * 60)
    
    # Create original object with mutable data
    original = ConcretePrototypeA("Original", ["item1", "item2"])
    print(f"Original: {original.get_info()}")
    
    # Shallow clone
    shallow_clone = original.clone()
    print(f"Shallow Clone: {shallow_clone.get_info()}")
    
    # Deep clone
    deep_clone = original.deep_clone()
    print(f"Deep Clone: {deep_clone.get_info()}")
    
    print("\n--- Testing Reference vs Value ---")
    
    # Test shallow clone - shares mutable objects
    print("\nModifying original data...")
    original.add_data("item3")
    original.value = "Modified Original"
    
    print(f"Original after modification: {original.get_info()}")
    print(f"Shallow Clone after original modification: {shallow_clone.get_info()}")
    print(f"Deep Clone after original modification: {deep_clone.get_info()}")
    
    print("\nNote: Shallow clone shares the 'data' list with original!")
    print("      Deep clone has independent copy of all data.")
    
    # Test deep clone independence
    print("\nModifying deep clone...")
    deep_clone.add_data("deep_item")
    deep_clone.value = "Modified Deep Clone"
    
    print(f"Original: {original.get_info()}")
    print(f"Deep Clone after self modification: {deep_clone.get_info()}")


def demonstrate_client_usage():
    """
    Demonstrates using Client to manage and clone prototypes
    """
    print("\n" + "=" * 60)
    print("CLIENT PROTOTYPE MANAGEMENT")
    print("=" * 60)
    
    # Create client
    client = Client()
    
    # Create and register prototypes
    prototype_a = ConcretePrototypeA("Template A", ["default"])
    prototype_b = ConcretePrototypeB("Template B", {"theme": "dark", "lang": "en"})
    
    client.register_prototype("typeA", prototype_a)
    client.register_prototype("typeB", prototype_b)
    
    print("Registered prototypes:")
    print(f"typeA: {prototype_a.get_info()}")
    print(f"typeB: {prototype_b.get_info()}")
    
    # Create clones using client
    print("\n--- Creating clones via Client ---")
    
    clone_a1 = client.create_object("typeA")
    clone_a2 = client.create_object("typeA")
    clone_b1 = client.create_deep_object("typeB")
    
    print(f"Clone A1: {clone_a1.get_info()}")
    print(f"Clone A2: {clone_a2.get_info()}")
    print(f"Clone B1: {clone_b1.get_info()}")
    
    # Modify clones to show independence
    print("\n--- Modifying clones ---")
    clone_a1.value = "Modified A1"
    clone_a2.value = "Modified A2"
    clone_b1.name = "Modified B1"
    clone_b1.update_config("theme", "light")
    
    print(f"Original typeA: {prototype_a.get_info()}")
    print(f"Modified Clone A1: {clone_a1.get_info()}")
    print(f"Modified Clone A2: {clone_a2.get_info()}")
    print(f"Original typeB: {prototype_b.get_info()}")
    print(f"Modified Clone B1: {clone_b1.get_info()}")


def demonstrate_object_identity():
    """
    Demonstrates object identity and memory addresses
    """
    print("\n" + "=" * 60)
    print("OBJECT IDENTITY DEMONSTRATION")
    print("=" * 60)
    
    original = ConcretePrototypeA("Identity Test", ["shared"])
    clone = original.clone()
    deep_clone = original.deep_clone()
    
    print(f"Original ID: {id(original)} | Object: {original.get_info()}")
    print(f"Clone ID: {id(clone)} | Object: {clone.get_info()}")
    print(f"Deep Clone ID: {id(deep_clone)} | Object: {deep_clone.get_info()}")
    
    print(f"\nOriginal data list ID: {id(original.data)}")
    print(f"Clone data list ID: {id(clone.data)}")
    print(f"Deep clone data list ID: {id(deep_clone.data)}")
    
    print(f"\nAre objects the same? Original == Clone: {original is clone}")
    print(f"Are data lists the same? Original.data == Clone.data: {original.data is clone.data}")
    print(f"Are data lists the same? Original.data == DeepClone.data: {original.data is deep_clone.data}")


def main():
    """
    Main function to run all demonstrations
    """
    print("PROTOTYPE PATTERN - STRUCTURE DEMONSTRATION")
    print("Showcasing clone functionality and object independence")
    
    demonstrate_shallow_vs_deep_clone()
    demonstrate_client_usage()
    demonstrate_object_identity()
    
    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
