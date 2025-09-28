from ConcreteCollection import ConcreteCollection


def demonstrate_iterator_pattern():
    """
    Demonstrates the Iterator design pattern with basic structure implementations.
    """
    print("=== Structure Demo: Iterator Design Pattern ===\n")
    
    # Create a concrete collection
    collection = ConcreteCollection()
    
    # Add some items to the collection
    items = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
    for item in items:
        collection.add_item(item)
    
    print(f"Collection created with {collection.get_size()} items: {items}")
    print()
    
    # Create an iterator for the collection
    iterator = collection.create_iterator()
    
    print("1. Forward iteration:")
    print("   Iterating through the collection:")
    while iterator.has_next():
        item = iterator.next()
        print(f"   - {item}")
    print()
    
    # Reset the iterator
    print("2. Reset and iterate again:")
    iterator.reset()
    print("   Iterator reset to beginning")
    print("   Iterating through the collection again:")
    while iterator.has_next():
        item = iterator.next()
        print(f"   - {item}")
    print()
    
    # Demonstrate iterator state
    print("3. Iterator state demonstration:")
    iterator.reset()
    print(f"   Initial index: {iterator.get_current_index()}")
    
    # Move through a few items
    for i in range(3):
        if iterator.has_next():
            item = iterator.next()
            print(f"   After getting '{item}': index = {iterator.get_current_index()}")
    
    print(f"   Has more items: {iterator.has_next()}")
    print()
    
    # Demonstrate error handling
    print("4. Error handling demonstration:")
    iterator.reset()
    # Consume all items
    while iterator.has_next():
        iterator.next()
    
    print("   All items consumed")
    print(f"   Has more items: {iterator.has_next()}")
    
    try:
        iterator.next()
    except StopIteration as e:
        print(f"   Caught StopIteration: {e}")
    
    print("\n=== Structure Demo Complete ===")


if __name__ == "__main__":
    demonstrate_iterator_pattern()
