"""
Main demonstration of Proxy pattern structure.
Shows the basic implementation and interaction between Proxy and RealSubject.
"""

from Subject import Subject
from RealSubject import RealSubject
from Proxy import Proxy


def demonstrate_proxy_pattern():
    """Demonstrate the Proxy pattern with clear examples."""
    
    print("=== Proxy Pattern Structure Demo ===\n")
    
    # 1. Direct access to RealSubject
    print("1. Direct access to RealSubject:")
    print("-" * 40)
    real_subject = RealSubject()
    result1 = real_subject.request()
    print(f"Result: {result1}\n")
    
    # 2. Access through Proxy
    print("2. Access through Proxy:")
    print("-" * 40)
    proxy = Proxy()
    result2 = proxy.request()
    print(f"Result: {result2}\n")
    
    # 3. Multiple requests through Proxy (shows lazy initialization)
    print("3. Multiple requests through Proxy (lazy initialization):")
    print("-" * 40)
    proxy2 = Proxy()
    print("First request:")
    result3 = proxy2.request()
    print(f"Result: {result3}\n")
    
    print("Second request (RealSubject already exists):")
    result4 = proxy2.request()
    print(f"Result: {result4}\n")
    
    # 4. Demonstrate that Proxy and RealSubject implement the same interface
    print("4. Interface compatibility demonstration:")
    print("-" * 40)
    subjects = [RealSubject(), Proxy()]
    
    for i, subject in enumerate(subjects, 1):
        print(f"Subject {i} ({type(subject).__name__}):")
        result = subject.request()
        print(f"Result: {result}\n")
    
    print("=== Structure Demo Complete ===")


if __name__ == "__main__":
    demonstrate_proxy_pattern()
