"""
ConcreteObserver - Concrete implementation of Observer
Responds to state changes in the Subject
"""

from Subject import Observer


class ConcreteObserver(Observer):
    """Concrete implementation of Observer"""
    
    def __init__(self, name: str):
        self._name = name
        self._subject_state = None
    
    def update(self, subject) -> None:
        """Update method called when subject state changes"""
        self._subject_state = subject.get_state()
        print(f"Observer '{self._name}' received update: state = '{self._subject_state}'")
    
    def get_name(self) -> str:
        """Get observer name"""
        return self._name
    
    def get_last_known_state(self):
        """Get last known state from subject"""
        return self._subject_state
