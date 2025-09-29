"""
Main - Demo of Observer Pattern Structure
Demonstrates the basic Observer pattern implementation
"""

from Subject import Subject, Observer
from ConcreteSubject import ConcreteSubject
from ConcreteObserver import ConcreteObserver


def main():
    print("=== Observer Pattern Structure Demo ===\n")
    
    # Create subject
    print("1. Creating Subject:")
    subject = ConcreteSubject()
    print(f"   Subject created with {subject.get_observer_count()} observers\n")
    
    # Create observers
    print("2. Creating Observers:")
    observer1 = ConcreteObserver("Observer-1")
    observer2 = ConcreteObserver("Observer-2")
    observer3 = ConcreteObserver("Observer-3")
    print(f"   Created observers: {observer1.get_name()}, {observer2.get_name()}, {observer3.get_name()}\n")
    
    # Attach observers
    print("3. Attaching Observers:")
    subject.attach(observer1)
    subject.attach(observer2)
    subject.attach(observer3)
    print(f"   Total observers attached: {subject.get_observer_count()}\n")
    
    # Change state and notify
    print("4. Changing Subject State:")
    subject.set_state("Initial State")
    print()
    
    # Change state again
    print("5. Changing Subject State Again:")
    subject.set_state("Updated State")
    print()
    
    # Detach one observer
    print("6. Detaching One Observer:")
    subject.detach(observer2)
    print(f"   Total observers remaining: {subject.get_observer_count()}\n")
    
    # Change state with fewer observers
    print("7. Changing State with Fewer Observers:")
    subject.set_state("Final State")
    print()
    
    # Show observer states
    print("8. Observer States:")
    print(f"   {observer1.get_name()}: last known state = '{observer1.get_last_known_state()}'")
    print(f"   {observer2.get_name()}: last known state = '{observer2.get_last_known_state()}'")
    print(f"   {observer3.get_name()}: last known state = '{observer3.get_last_known_state()}'")
    
    print("\n=== Structure Demo Complete ===")


if __name__ == "__main__":
    main()
