from ConcreteHandlerA import ConcreteHandlerA
from ConcreteHandlerB import ConcreteHandlerB
from ConcreteHandlerC import ConcreteHandlerC


def client_code(handler, request):
    """
    The client code is usually suited to work with a single handler.
    In most cases, it is not even aware that the handler is part of a chain.
    """
    print(f"\nClient: Sending request '{request}'")
    result = handler.handle(request)
    if result:
        print(f"Result: {result}")
    else:
        print(f"Result: No handler could process the request '{request}'")


def main():
    print("=== Structure Demo: Chain of Responsibility Pattern ===\n")
    
    # Create the chain of handlers
    handler_a = ConcreteHandlerA()
    handler_b = ConcreteHandlerB()
    handler_c = ConcreteHandlerC()
    
    # Set up the chain: A -> B -> C
    handler_a.set_next(handler_b).set_next(handler_c)
    
    print("Chain setup: ConcreteHandlerA -> ConcreteHandlerB -> ConcreteHandlerC\n")
    
    # Test different requests
    requests = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
    
    for request in requests:
        client_code(handler_a, request)
    
    print("\n=== Testing chain flexibility ===")
    # Test with a different chain order: B -> A -> C
    handler_b2 = ConcreteHandlerB()
    handler_a2 = ConcreteHandlerA()
    handler_c2 = ConcreteHandlerC()
    
    handler_b2.set_next(handler_a2).set_next(handler_c2)
    
    print("\nNew chain setup: ConcreteHandlerB -> ConcreteHandlerA -> ConcreteHandlerC")
    client_code(handler_b2, "Apple")
    client_code(handler_b2, "Banana")
    
    print("\n=== Structure Demo Complete ===")


if __name__ == "__main__":
    main()
