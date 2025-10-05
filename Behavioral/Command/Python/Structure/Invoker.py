from typing import List
from Command import Command


class Invoker:
    """
    The Invoker is associated with one or several commands.
    It sends a request to the command.
    """
    
    def __init__(self):
        self._commands: List[Command] = []
        self._history: List[Command] = []
    
    def set_command(self, command: Command) -> None:
        """
        Set a command to be executed.
        """
        self._commands.append(command)
    
    def execute_commands(self) -> None:
        """
        Execute all commands in the list.
        """
        for command in self._commands:
            command.execute()
            self._history.append(command)
        self._commands.clear()
    
    def undo_last_command(self) -> None:
        """
        Undo the last executed command.
        """
        if self._history:
            last_command = self._history.pop()
            last_command.undo()
    
    def undo_all_commands(self) -> None:
        """
        Undo all executed commands in reverse order.
        """
        while self._history:
            self.undo_last_command()
    
    def get_history_size(self) -> int:
        """
        Get the number of commands in history.
        """
        return len(self._history)
