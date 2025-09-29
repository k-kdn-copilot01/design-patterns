from abc import ABC, abstractmethod


class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm. The Context uses this interface to call the algorithm
    defined by Concrete Strategies.
    """
    
    @abstractmethod
    def execute(self, data):
        """
        Execute the strategy algorithm.
        
        Args:
            data: Input data for the algorithm
        """
        pass
