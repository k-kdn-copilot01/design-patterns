"""
Main demonstration of the Prototype pattern structure.

This script demonstrates:
1. Creating prototypes
2. Shallow vs Deep copying
3. Reference vs Value comparison
4. Using the Client class to manage prototypes
"""

from prototype import ConcretePrototype, Client


def demonstrate_basic_cloning():
    """Demonstrate basic cloning functionality."""
    print("=== Basic Cloning Demo ===")
    
    # Create original prototype
    original = ConcretePrototype("Original", {"value": 42, "nested": {"key": "value"}})
    print(f"Original: {original}")
    print()
    
    # Create shallow copy
    shallow_copy = original.clone(deep=False)
    print(f"Shallow copy: {shallow_copy}")
    print()
    
    # Create deep copy
    deep_copy = original.clone(deep=True)
    print(f"Deep copy: {deep_copy}")
    print()
    
    # Demonstrate reference vs value
    print("=== Reference vs Value Comparison ===")
    print(f"Original id: {id(original)}")
    print(f"Shallow copy id: {id(shallow_copy)}")
    print(f"Deep copy id: {id(deep_copy)}")
    print(f"Original == Shallow copy: {original == shallow_copy}")
    print(f"Original == Deep copy: {original == deep_copy}")
    print()
    
    # Demonstrate shallow vs deep copy behavior
    print("=== Shallow vs Deep Copy Behavior ===")
    print("Modifying nested data in shallow copy...")
    shallow_copy.set_data("nested", {"modified": True})
    print(f"Original nested data: {original.get_data('nested')}")
    print(f"Shallow copy nested data: {shallow_copy.get_data('nested')}")
    print()
    
    print("Modifying nested data in deep copy...")
    deep_copy.set_data("nested", {"deep_modified": True})
    print(f"Original nested data: {original.get_data('nested')}")
    print(f"Deep copy nested data: {deep_copy.get_data('nested')}")
    print()


def demonstrate_client_usage():
    """Demonstrate using the Client class to manage prototypes."""
    print("=== Client Usage Demo ===")
    
    # Create client
    client = Client()
    print()
    
    # Create and register prototypes
    config_prototype = ConcretePrototype("Config", {
        "database_url": "localhost:5432",
        "api_key": "secret123",
        "settings": {"timeout": 30, "retries": 3}
    })
    
    document_prototype = ConcretePrototype("Document", {
        "title": "Default Document",
        "content": "Default content",
        "metadata": {"author": "System", "version": "1.0"}
    })
    
    client.register_prototype("config", config_prototype)
    client.register_prototype("document", document_prototype)
    print()
    
    # List registered prototypes
    client.list_prototypes()
    print()
    
    # Create objects from prototypes
    print("Creating objects from prototypes:")
    config1 = client.create_from_prototype("config", deep=True)
    config2 = client.create_from_prototype("config", deep=False)
    document1 = client.create_from_prototype("document", deep=True)
    print()
    
    # Demonstrate independence of cloned objects
    print("=== Object Independence Demo ===")
    config1.set_data("database_url", "production:5432")
    config1.set_data("settings", {"timeout": 60, "retries": 5})
    
    print(f"Config1: {config1}")
    print(f"Config2: {config2}")
    print(f"Original config: {config_prototype}")
    print()


def main():
    """Main function to run all demonstrations."""
    print("=== Prototype Pattern Structure Demo ===\n")
    
    demonstrate_basic_cloning()
    demonstrate_client_usage()
    
    print("=== Structure Demo Complete ===")


if __name__ == "__main__":
    main()
