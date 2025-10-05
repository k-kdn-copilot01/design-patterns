from abc import ABC, abstractmethod


class TextCommand(ABC):
    """
    Abstract base class for text editor commands.
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


class InsertTextCommand(TextCommand):
    """
    Command to insert text into the editor.
    """
    
    def __init__(self, editor, text: str, position: int = None):
        self._editor = editor
        self._text = text
        self._position = position
        self._actual_position = None
        self._executed = False
    
    def execute(self) -> None:
        """
        Execute the insert text command.
        """
        if not self._executed:
            self._actual_position = self._position if self._position is not None else self._editor.get_cursor_position()
            self._editor.insert_text(self._text, self._position)
            self._executed = True
    
    def undo(self) -> None:
        """
        Undo the insert text command.
        """
        if self._executed and self._actual_position is not None:
            # Delete the inserted text at the position where it was actually inserted
            self._editor.delete_text(self._actual_position, len(self._text))
            self._executed = False


class DeleteTextCommand(TextCommand):
    """
    Command to delete text from the editor.
    """
    
    def __init__(self, editor, start: int, length: int):
        self._editor = editor
        self._start = start
        self._length = length
        self._deleted_text = ""
        self._executed = False
    
    def execute(self) -> None:
        """
        Execute the delete text command.
        """
        if not self._executed:
            self._deleted_text = self._editor.delete_text(self._start, self._length)
            self._executed = True
    
    def undo(self) -> None:
        """
        Undo the delete text command.
        """
        if self._executed and self._deleted_text:
            self._editor.insert_text(self._deleted_text, self._start)
            self._executed = False
