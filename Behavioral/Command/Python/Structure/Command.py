from abc import ABC, abstractmethod


class Command(ABC):
    """
    The Command interface declares a method for executing a command.
    """
    
    @abstractmethod
    def execute(self) -> None:
        """
        Execute the command.
        """
        pass
    
    @abstractmethod
    def undo(self) -> None:
        """
        Undo the command.
        """
        pass
