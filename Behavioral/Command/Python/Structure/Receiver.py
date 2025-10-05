class Receiver:
    """
    The Receiver class contains some business logic.
    """
    
    def __init__(self, name: str = "Receiver"):
        self.name = name
    
    def action(self, message: str = "default action") -> None:
        """
        Perform some business logic.
        """
        print(f"{self.name}: Executing action - {message}")
    
    def undo_action(self, message: str = "default action") -> None:
        """
        Undo some business logic.
        """
        print(f"{self.name}: Undoing action - {message}")
