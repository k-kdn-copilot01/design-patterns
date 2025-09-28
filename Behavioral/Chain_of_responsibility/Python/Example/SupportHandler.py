from abc import ABC, abstractmethod
from typing import Optional
from SupportTicket import SupportTicket


class SupportHandler(ABC):
    """
    Abstract base class for support handlers in the chain of responsibility.
    Each handler can process tickets of a certain priority level.
    """
    
    def __init__(self, name: str, max_priority_level: int):
        self.name = name
        self.max_priority_level = max_priority_level
        self._next_handler: Optional['SupportHandler'] = None
    
    def set_next(self, handler: 'SupportHandler') -> 'SupportHandler':
        """Set the next handler in the chain"""
        self._next_handler = handler
        return handler
    
    def handle_ticket(self, ticket: SupportTicket) -> bool:
        """
        Handle the ticket if this handler can process it.
        Otherwise, pass it to the next handler in the chain.
        Returns True if handled, False if passed to next handler.
        """
        if ticket.priority.value <= self.max_priority_level:
            self._process_ticket(ticket)
            return True
        elif self._next_handler:
            print(f"{self.name}: Cannot handle {ticket.priority.name} priority. Escalating to {self._next_handler.name}...")
            return self._next_handler.handle_ticket(ticket)
        else:
            print(f"{self.name}: Cannot handle {ticket.priority.name} priority. No higher level support available.")
            return False
    
    @abstractmethod
    def _process_ticket(self, ticket: SupportTicket):
        """Process the ticket - to be implemented by concrete handlers"""
        pass
