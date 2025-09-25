"""
Client code that works with objects via the Target interface.
"""
from Target import Target


class Client:
    """
    The Client contains the existing business logic of the program.
    """
    
    def __init__(self, target: Target):
        """
        Initialize the Client with a Target instance.
        
        Args:
            target: The Target instance to work with
        """
        self.target = target
    
    def make_request(self) -> str:
        """
        The Client can work with any class that follows the Target interface.
        """
        return self.target.request()
