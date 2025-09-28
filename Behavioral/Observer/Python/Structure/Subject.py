"""
Subject (Observable) - Core class in Observer pattern
Defines the interface for objects that can be observed
"""

from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
    """Abstract Observer interface"""
    
    @abstractmethod
    def update(self, subject) -> None:
        """Update method called by Subject when state changes"""
        pass


class Subject(ABC):
    """Abstract Subject (Observable) interface"""
    
    def __init__(self):
        self._observers: List[Observer] = []
    
    def attach(self, observer: Observer) -> None:
        """Attach an observer to the subject"""
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"Observer attached. Total observers: {len(self._observers)}")
    
    def detach(self, observer: Observer) -> None:
        """Detach an observer from the subject"""
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"Observer detached. Total observers: {len(self._observers)}")
    
    def notify(self) -> None:
        """Notify all observers about state change"""
        print(f"Notifying {len(self._observers)} observers...")
        for observer in self._observers:
            observer.update(self)
    
    @abstractmethod
    def get_state(self):
        """Get current state of the subject"""
        pass
