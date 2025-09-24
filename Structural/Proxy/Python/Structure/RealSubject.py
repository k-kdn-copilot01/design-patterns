"""
RealSubject class for Proxy pattern.
Represents the actual object that the proxy represents.
"""

from Subject import Subject


class RealSubject(Subject):
    """The real object that performs the actual work."""
    
    def request(self) -> str:
        """
        Perform the actual request operation.
        
        Returns:
            str: Result of the real operation
        """
        print("RealSubject: Handling request...")
        return "RealSubject: Request completed successfully"
