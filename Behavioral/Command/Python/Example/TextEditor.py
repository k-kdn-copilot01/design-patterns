class TextEditor:
    """
    TextEditor represents the receiver in the Command pattern.
    It contains the actual business logic for text operations.
    """
    
    def __init__(self):
        self._content = ""
        self._cursor_position = 0
    
    def insert_text(self, text: str, position: int = None) -> None:
        """
        Insert text at the specified position.
        """
        if position is None:
            position = self._cursor_position
        
        self._content = self._content[:position] + text + self._content[position:]
        self._cursor_position = position + len(text)
        print(f"Inserted '{text}' at position {position}")
        print(f"Content: '{self._content}'")
        print(f"Cursor position: {self._cursor_position}\n")
    
    def delete_text(self, start: int, length: int) -> str:
        """
        Delete text from start position with specified length.
        Returns the deleted text for undo purposes.
        """
        if start < 0 or start >= len(self._content):
            return ""
        
        end = min(start + length, len(self._content))
        deleted_text = self._content[start:end]
        self._content = self._content[:start] + self._content[end:]
        self._cursor_position = start
        print(f"Deleted '{deleted_text}' from position {start}")
        print(f"Content: '{self._content}'")
        print(f"Cursor position: {self._cursor_position}\n")
        return deleted_text
    
    def get_content(self) -> str:
        """
        Get the current content.
        """
        return self._content
    
    def get_cursor_position(self) -> int:
        """
        Get the current cursor position.
        """
        return self._cursor_position
