from Strategy import Strategy


class ConcreteStrategyA(Strategy):
    """
    Concrete Strategies implement the algorithm while following the base Strategy
    interface. The interface makes them interchangeable in the Context.
    """
    
    def execute(self, data):
        """
        Execute Strategy A algorithm.
        
        Args:
            data: Input data for the algorithm
            
        Returns:
            str: Result of Strategy A execution
        """
        result = f"Strategy A: Processing '{data}' with algorithm A"
        print(result)
        return result
