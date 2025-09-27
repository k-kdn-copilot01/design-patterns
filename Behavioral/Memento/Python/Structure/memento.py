"""
Memento Pattern - Core Classes

The Memento pattern provides the ability to restore an object to its previous state.
This module contains the core classes: Memento, Originator, and Caretaker.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class Memento:
    """
    The Memento class stores the state of the Originator.
    It provides methods to retrieve the saved state.
    """
    
    def __init__(self, state: Dict[str, Any]):
        """
        Initialize the Memento with a state dictionary.
        
        Args:
            state: Dictionary containing the state to be saved
        """
        self._state = state.copy()  # Create a deep copy to prevent external modifications
    
    def get_state(self) -> Dict[str, Any]:
        """
        Retrieve the saved state.
        
        Returns:
            Dictionary containing the saved state
        """
        return self._state.copy()  # Return a copy to prevent external modifications


class Originator:
    """
    The Originator class creates and uses Mementos to save and restore its state.
    It knows how to save itself into a Memento and how to restore from a Memento.
    """
    
    def __init__(self, initial_state: Optional[Dict[str, Any]] = None):
        """
        Initialize the Originator with an optional initial state.
        
        Args:
            initial_state: Optional dictionary containing initial state
        """
        self._state = initial_state or {}
    
    def set_state(self, key: str, value: Any) -> None:
        """
        Set a specific state value.
        
        Args:
            key: The state key
            value: The state value
        """
        self._state[key] = value
    
    def get_state(self, key: str) -> Any:
        """
        Get a specific state value.
        
        Args:
            key: The state key
            
        Returns:
            The state value or None if key doesn't exist
        """
        return self._state.get(key)
    
    def get_all_state(self) -> Dict[str, Any]:
        """
        Get all current state.
        
        Returns:
            Dictionary containing all current state
        """
        return self._state.copy()
    
    def create_memento(self) -> Memento:
        """
        Create a Memento containing the current state.
        
        Returns:
            A new Memento object with the current state
        """
        return Memento(self._state)
    
    def restore_from_memento(self, memento: Memento) -> None:
        """
        Restore the state from a Memento.
        
        Args:
            memento: The Memento to restore from
        """
        self._state = memento.get_state()
    
    def display_state(self) -> str:
        """
        Display the current state in a readable format.
        
        Returns:
            String representation of the current state
        """
        if not self._state:
            return "State is empty"
        
        state_str = "Current State:\n"
        for key, value in self._state.items():
            state_str += f"  {key}: {value}\n"
        return state_str.strip()


class Caretaker:
    """
    The Caretaker class is responsible for keeping track of multiple Mementos.
    It can save, retrieve, and manage the history of Mementos.
    """
    
    def __init__(self):
        """Initialize the Caretaker with an empty list of Mementos."""
        self._mementos: List[Memento] = []
        self._current_index: int = -1
    
    def save_memento(self, memento: Memento) -> None:
        """
        Save a Memento to the history.
        
        Args:
            memento: The Memento to save
        """
        # Remove any mementos after current index (when branching from history)
        self._mementos = self._mementos[:self._current_index + 1]
        
        # Add the new memento
        self._mementos.append(memento)
        self._current_index = len(self._mementos) - 1
    
    def get_memento(self, index: int) -> Optional[Memento]:
        """
        Get a Memento by index.
        
        Args:
            index: The index of the Memento to retrieve
            
        Returns:
            The Memento at the specified index, or None if index is invalid
        """
        if 0 <= index < len(self._mementos):
            return self._mementos[index]
        return None
    
    def get_current_memento(self) -> Optional[Memento]:
        """
        Get the current Memento.
        
        Returns:
            The current Memento, or None if no Mementos exist
        """
        if 0 <= self._current_index < len(self._mementos):
            return self._mementos[self._current_index]
        return None
    
    def get_previous_memento(self) -> Optional[Memento]:
        """
        Get the previous Memento in history.
        
        Returns:
            The previous Memento, or None if at the beginning
        """
        if self._current_index > 0:
            self._current_index -= 1
            return self._mementos[self._current_index]
        return None
    
    def get_next_memento(self) -> Optional[Memento]:
        """
        Get the next Memento in history.
        
        Returns:
            The next Memento, or None if at the end
        """
        if self._current_index < len(self._mementos) - 1:
            self._current_index += 1
            return self._mementos[self._current_index]
        return None
    
    def get_history_size(self) -> int:
        """
        Get the number of saved Mementos.
        
        Returns:
            The number of Mementos in history
        """
        return len(self._mementos)
    
    def get_current_index(self) -> int:
        """
        Get the current index in history.
        
        Returns:
            The current index
        """
        return self._current_index
    
    def clear_history(self) -> None:
        """Clear all Mementos from history."""
        self._mementos.clear()
        self._current_index = -1
    
    def display_history(self) -> str:
        """
        Display the history of Mementos.
        
        Returns:
            String representation of the history
        """
        if not self._mementos:
            return "No history available"
        
        history_str = f"History ({len(self._mementos)} snapshots):\n"
        for i, memento in enumerate(self._mementos):
            marker = " <-- Current" if i == self._current_index else ""
            history_str += f"  [{i}] {memento.get_state()}{marker}\n"
        return history_str.strip()
