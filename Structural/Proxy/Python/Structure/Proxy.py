"""
Proxy class for Proxy pattern.
Controls access to the RealSubject and can add additional functionality.
"""

from Subject import Subject
from RealSubject import RealSubject


class Proxy(Subject):
    """Proxy that controls access to RealSubject."""
    
    def __init__(self):
        """Initialize the proxy with a reference to RealSubject."""
        self._real_subject = None
    
    def request(self) -> str:
        """
        Handle the request by delegating to RealSubject if needed.
        Can add additional functionality like lazy initialization, access control, etc.
        
        Returns:
            str: Result of the request operation
        """
        print("Proxy: Intercepting request...")
        
        # Lazy initialization - create RealSubject only when needed
        if self._real_subject is None:
            print("Proxy: Creating RealSubject instance...")
            self._real_subject = RealSubject()
        
        # Delegate the request to the real subject
        print("Proxy: Delegating request to RealSubject...")
        result = self._real_subject.request()
        
        print("Proxy: Request completed")
        return f"Proxy: {result}"
