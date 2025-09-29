"""
State Pattern - Core Structure
Abstract base class for all states
"""

from abc import ABC, abstractmethod


class State(ABC):
    """
    Abstract base class for all states.
    Defines the interface that all concrete states must implement.
    """
    
    @abstractmethod
    def handle_request(self, context):
        """
        Handle a request in the current state.
        
        Args:
            context: The context object that contains the state
        """
        pass


class Context:
    """
    Context class that maintains a reference to the current state
    and delegates state-specific behavior to the current state object.
    """
    
    def __init__(self, initial_state):
        """
        Initialize the context with an initial state.
        
        Args:
            initial_state: The initial state object
        """
        self._state = initial_state
    
    def set_state(self, state):
        """
        Change the current state.
        
        Args:
            state: The new state object
        """
        self._state = state
        print(f"State changed to: {type(state).__name__}")
    
    def request(self):
        """
        Delegate the request to the current state.
        """
        self._state.handle_request(self)
    
    def get_state(self):
        """
        Get the current state.
        
        Returns:
            The current state object
        """
        return self._state
