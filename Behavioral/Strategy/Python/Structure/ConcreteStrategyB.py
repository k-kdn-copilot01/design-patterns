from Strategy import Strategy


class ConcreteStrategyB(Strategy):
    """
    Concrete Strategies implement the algorithm while following the base Strategy
    interface. The interface makes them interchangeable in the Context.
    """
    
    def execute(self, data):
        """
        Execute Strategy B algorithm.
        
        Args:
            data: Input data for the algorithm
            
        Returns:
            str: Result of Strategy B execution
        """
        result = f"Strategy B: Processing '{data}' with algorithm B"
        print(result)
        return result
