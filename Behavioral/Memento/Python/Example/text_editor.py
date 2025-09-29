"""
Memento Pattern - Real-world Example: Text Editor with Undo/Redo

This example demonstrates the Memento pattern in a practical scenario:
a text editor with undo/redo functionality.
"""

from typing import List, Optional
import datetime


class TextEditorMemento:
    """
    Memento class that stores the state of the text editor.
    """
    
    def __init__(self, content: str, cursor_position: int, timestamp: datetime.datetime):
        """
        Initialize the memento with editor state.
        
        Args:
            content: The text content
            cursor_position: Position of the cursor
            timestamp: When this state was saved
        """
        self._content = content
        self._cursor_position = cursor_position
        self._timestamp = timestamp
    
    def get_content(self) -> str:
        """Get the saved content."""
        return self._content
    
    def get_cursor_position(self) -> int:
        """Get the saved cursor position."""
        return self._cursor_position
    
    def get_timestamp(self) -> datetime.datetime:
        """Get the timestamp when this state was saved."""
        return self._timestamp
    
    def get_state_info(self) -> str:
        """Get formatted state information."""
        return f"Content: '{self._content[:30]}{'...' if len(self._content) > 30 else ''}' | Cursor: {self._cursor_position} | Time: {self._timestamp.strftime('%H:%M:%S')}"


class TextEditor:
    """
    Originator class - the text editor whose state we want to save/restore.
    """
    
    def __init__(self):
        """Initialize the text editor with empty content."""
        self._content = ""
        self._cursor_position = 0
    
    def get_content(self) -> str:
        """Get the current content."""
        return self._content
    
    def get_cursor_position(self) -> int:
        """Get the current cursor position."""
        return self._cursor_position
    
    def set_content(self, content: str) -> None:
        """
        Set the content and adjust cursor position.
        
        Args:
            content: The new content
        """
        self._content = content
        self._cursor_position = min(self._cursor_position, len(content))
    
    def insert_text(self, text: str) -> None:
        """
        Insert text at the current cursor position.
        
        Args:
            text: Text to insert
        """
        self._content = (self._content[:self._cursor_position] + 
                        text + 
                        self._content[self._cursor_position:])
        self._cursor_position += len(text)
    
    def delete_text(self, length: int = 1) -> None:
        """
        Delete text at the current cursor position.
        
        Args:
            length: Number of characters to delete
        """
        if self._cursor_position > 0:
            delete_start = max(0, self._cursor_position - length)
            self._content = (self._content[:delete_start] + 
                           self._content[self._cursor_position:])
            self._cursor_position = delete_start
    
    def move_cursor(self, position: int) -> None:
        """
        Move cursor to a specific position.
        
        Args:
            position: New cursor position
        """
        self._cursor_position = max(0, min(position, len(self._content)))
    
    def create_memento(self) -> TextEditorMemento:
        """
        Create a memento with the current state.
        
        Returns:
            A new TextEditorMemento with current state
        """
        return TextEditorMemento(
            self._content, 
            self._cursor_position, 
            datetime.datetime.now()
        )
    
    def restore_from_memento(self, memento: TextEditorMemento) -> None:
        """
        Restore state from a memento.
        
        Args:
            memento: The memento to restore from
        """
        self._content = memento.get_content()
        self._cursor_position = memento.get_cursor_position()
    
    def display_state(self) -> str:
        """
        Display the current state in a readable format.
        
        Returns:
            String representation of current state
        """
        # Show content with cursor position indicator
        display_content = self._content.replace('\n', '\\n')
        cursor_indicator = '|' if self._cursor_position == len(self._content) else '^'
        
        result = f"Content: '{display_content}'\n"
        result += f"Cursor:  {' ' * self._cursor_position}{cursor_indicator} (position {self._cursor_position})"
        return result


class UndoRedoManager:
    """
    Caretaker class - manages the undo/redo functionality for the text editor.
    """
    
    def __init__(self, max_history: int = 50):
        """
        Initialize the undo/redo manager.
        
        Args:
            max_history: Maximum number of states to keep in history
        """
        self._history: List[TextEditorMemento] = []
        self._current_index: int = -1
        self._max_history = max_history
    
    def save_state(self, memento: TextEditorMemento) -> None:
        """
        Save a state to history.
        
        Args:
            memento: The memento to save
        """
        # Remove any states after current index (when branching from history)
        self._history = self._history[:self._current_index + 1]
        
        # Add the new state
        self._history.append(memento)
        self._current_index = len(self._history) - 1
        
        # Limit history size
        if len(self._history) > self._max_history:
            self._history.pop(0)
            self._current_index -= 1
    
    def undo(self) -> Optional[TextEditorMemento]:
        """
        Get the previous state for undo operation.
        
        Returns:
            The previous memento, or None if no undo available
        """
        if self._current_index > 0:
            self._current_index -= 1
            return self._history[self._current_index]
        return None
    
    def redo(self) -> Optional[TextEditorMemento]:
        """
        Get the next state for redo operation.
        
        Returns:
            The next memento, or None if no redo available
        """
        if self._current_index < len(self._history) - 1:
            self._current_index += 1
            return self._history[self._current_index]
        return None
    
    def can_undo(self) -> bool:
        """Check if undo is available."""
        return self._current_index > 0
    
    def can_redo(self) -> bool:
        """Check if redo is available."""
        return self._current_index < len(self._history) - 1
    
    def get_history_info(self) -> str:
        """
        Get information about the current history state.
        
        Returns:
            String with history information
        """
        if not self._history:
            return "No history available"
        
        info = f"History: {len(self._history)} states, current: {self._current_index}\n"
        info += "Recent states:\n"
        
        # Show last few states
        start = max(0, self._current_index - 2)
        end = min(len(self._history), self._current_index + 3)
        
        for i in range(start, end):
            marker = " <-- Current" if i == self._current_index else ""
            info += f"  [{i}] {self._history[i].get_state_info()}{marker}\n"
        
        return info.strip()
    
    def clear_history(self) -> None:
        """Clear all history."""
        self._history.clear()
        self._current_index = -1
