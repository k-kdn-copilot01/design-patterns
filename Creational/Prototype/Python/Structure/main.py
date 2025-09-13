from prototype import ConcretePrototype, Client

if __name__ == "__main__":
    original = ConcretePrototype(42)
    shallow_clone = Client.clone_prototype(original, deep=False)
    deep_clone = Client.clone_prototype(original, deep=True)

    print("Original id:", id(original))
    print("Shallow clone id:", id(shallow_clone))
    print("Deep clone id:", id(deep_clone))

    print("Original nested id:", id(original.nested))
    print("Shallow clone nested id:", id(shallow_clone.nested))
    print("Deep clone nested id:", id(deep_clone.nested))

    print("--- Modifying shallow clone nested data ---")
    shallow_clone.nested['data'] = 99
    print("Original nested data:", original.nested['data'])
    print("Shallow clone nested data:", shallow_clone.nested['data'])
    print("Deep clone nested data:", deep_clone.nested['data'])
