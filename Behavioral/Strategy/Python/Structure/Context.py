from Strategy import Strategy


class Context:
    """
    The Context defines the interface of interest to clients.
    It maintains a reference to a Strategy object and delegates work to it.
    """
    
    def __init__(self, strategy: Strategy = None):
        """
        Initialize the Context with a strategy.
        
        Args:
            strategy: The strategy to use (optional)
        """
        self._strategy = strategy
    
    def set_strategy(self, strategy: Strategy):
        """
        Set a new strategy at runtime.
        
        Args:
            strategy: The new strategy to use
        """
        self._strategy = strategy
    
    def execute_strategy(self, data):
        """
        Execute the current strategy with the given data.
        
        Args:
            data: Input data for the strategy
            
        Returns:
            Result of strategy execution
        """
        if self._strategy is None:
            raise ValueError("No strategy set")
        
        return self._strategy.execute(data)
