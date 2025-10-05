from typing import List
from TextCommand import TextCommand


class TextEditorInvoker:
    """
    Invoker for text editor commands with undo/redo functionality.
    """
    
    def __init__(self):
        self._command_history: List[TextCommand] = []
        self._redo_stack: List[TextCommand] = []
    
    def execute_command(self, command: TextCommand) -> None:
        """
        Execute a command and add it to history.
        """
        command.execute()
        self._command_history.append(command)
        # Clear redo stack when new command is executed
        self._redo_stack.clear()
        print("Command executed and added to history")
    
    def undo(self) -> None:
        """
        Undo the last executed command.
        """
        if self._command_history:
            last_command = self._command_history.pop()
            last_command.undo()
            self._redo_stack.append(last_command)
            print("Last command undone")
        else:
            print("No commands to undo")
    
    def redo(self) -> None:
        """
        Redo the last undone command.
        """
        if self._redo_stack:
            command_to_redo = self._redo_stack.pop()
            command_to_redo.execute()
            self._command_history.append(command_to_redo)
            print("Command redone")
        else:
            print("No commands to redo")
    
    def get_history_size(self) -> int:
        """
        Get the number of commands in history.
        """
        return len(self._command_history)
    
    def get_redo_stack_size(self) -> int:
        """
        Get the number of commands in redo stack.
        """
        return len(self._redo_stack)
