"""
Adapter makes the Adaptee's interface compatible with the Target's interface.
"""
from Target import Target
from Adaptee import Adaptee


class Adapter(Target):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface through multiple inheritance.
    """
    
    def __init__(self, adaptee: Adaptee):
        """
        Initialize the Adapter with an Adaptee instance.
        
        Args:
            adaptee: The Adaptee instance to adapt
        """
        self.adaptee = adaptee
    
    def request(self) -> str:
        """
        The Adapter translates the specific request to the general request.
        """
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"
