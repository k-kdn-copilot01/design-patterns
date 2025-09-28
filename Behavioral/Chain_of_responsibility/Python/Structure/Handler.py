qfrom abc import ABC, abstractmethod
from typing import Optional


class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """
    
    def __init__(self):
        self._next_handler: Optional['Handler'] = None
    
    def set_next(self, handler: 'Handler') -> 'Handler':
        """
        Set the next handler in the chain.
        Returns the handler that was set to allow chaining.
        """
        self._next_handler = handler
        return handler
    
    @abstractmethod
    def handle(self, request: str) -> Optional[str]:
        """
        Handle the request or pass it to the next handler in the chain.
        Returns the result if handled, None if passed to next handler.
        """
        if self._next_handler:
            return self._next_handler.handle(request)
        return None
