"""
ConcreteSubject - Concrete implementation of Subject
Maintains state and notifies observers when state changes
"""

from Subject import Subject


class ConcreteSubject(Subject):
    """Concrete implementation of Subject with state management"""
    
    def __init__(self):
        super().__init__()
        self._state = None
    
    def get_state(self):
        """Get current state"""
        return self._state
    
    def set_state(self, state) -> None:
        """Set new state and notify observers"""
        print(f"Subject state changing from '{self._state}' to '{state}'")
        self._state = state
        self.notify()
    
    def get_observer_count(self) -> int:
        """Get number of attached observers"""
        return len(self._observers)
