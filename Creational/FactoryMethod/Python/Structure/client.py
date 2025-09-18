"""
Client code that works with creators through their common interface
"""
from creator import Creator


class Client:
    """
    Client class that works with creators
    """
    
    @staticmethod
    def client_code(creator: Creator) -> None:
        """
        Client code that works with an instance of a concrete creator (but through the base interface)
        
        Args:
            creator (Creator): A concrete creator instance
        """
        print(f"Client: I'm not aware of the creator's class, but it still works.")
        print(f"{creator.some_operation()}")
