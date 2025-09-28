from Command import Command
from Receiver import Receiver


class ConcreteCommand(Command):
    """
    Concrete Commands implement various types of requests.
    """
    
    def __init__(self, receiver: Receiver, message: str = "default message"):
        self._receiver = receiver
        self._message = message
        self._previous_message = None
    
    def execute(self) -> None:
        """
        Execute the command by calling the receiver's action method.
        """
        self._previous_message = self._message
        self._receiver.action(self._message)
    
    def undo(self) -> None:
        """
        Undo the command by calling the receiver's undo_action method.
        """
        if self._previous_message:
            self._receiver.undo_action(self._previous_message)
