from Strategy import Strategy
from ConcreteStrategyA import ConcreteStrategyA
from ConcreteStrategyB import ConcreteStrategyB
from Context import Context


def main():
    """
    Demonstrate the Strategy pattern structure.
    """
    print("=== Structure Demo: Strategy Pattern ===\n")
    
    # Create context
    context = Context()
    
    # Test data
    test_data = "Sample Data"
    
    print("1. Using Strategy A:")
    # Set Strategy A
    context.set_strategy(ConcreteStrategyA())
    result_a = context.execute_strategy(test_data)
    print(f"Result: {result_a}\n")
    
    print("2. Switching to Strategy B:")
    # Switch to Strategy B
    context.set_strategy(ConcreteStrategyB())
    result_b = context.execute_strategy(test_data)
    print(f"Result: {result_b}\n")
    
    print("3. Demonstrating strategy interchangeability:")
    # Show that strategies are interchangeable
    strategies = [ConcreteStrategyA(), ConcreteStrategyB()]
    
    for i, strategy in enumerate(strategies, 1):
        context.set_strategy(strategy)
        result = context.execute_strategy(f"Data {i}")
        print(f"   Strategy {i} result: {result}")
    
    print("\n=== Structure Demo Complete ===")


if __name__ == "__main__":
    main()
