"""
Memento Pattern - Structure Demo

This demo shows the basic structure and usage of the Memento pattern.
It demonstrates how to save and restore object states using Mementos.
"""

from memento import Originator, Caretaker


def main():
    """
    Demonstrate the Memento pattern with a simple example.
    """
    print("=" * 60)
    print("MEMENTO PATTERN - STRUCTURE DEMO")
    print("=" * 60)
    print()
    
    # Create an Originator (the object whose state we want to save/restore)
    print("1. Creating Originator with initial state...")
    originator = Originator({
        'name': 'John Doe',
        'age': 30,
        'position': 'Developer',
        'salary': 75000
    })
    print(originator.display_state())
    print()
    
    # Create a Caretaker to manage Mementos
    print("2. Creating Caretaker to manage state history...")
    caretaker = Caretaker()
    print()
    
    # Save initial state
    print("3. Saving initial state...")
    initial_memento = originator.create_memento()
    caretaker.save_memento(initial_memento)
    print("✓ Initial state saved")
    print(caretaker.display_history())
    print()
    
    # Modify the state
    print("4. Modifying state (promotion)...")
    originator.set_state('position', 'Senior Developer')
    originator.set_state('salary', 90000)
    originator.set_state('age', 31)  # Birthday
    print(originator.display_state())
    print()
    
    # Save the modified state
    print("5. Saving modified state...")
    promotion_memento = originator.create_memento()
    caretaker.save_memento(promotion_memento)
    print("✓ Modified state saved")
    print(caretaker.display_history())
    print()
    
    # Make more changes
    print("6. Making more changes (department transfer)...")
    originator.set_state('position', 'Team Lead')
    originator.set_state('salary', 110000)
    originator.set_state('department', 'Engineering')
    print(originator.display_state())
    print()
    
    # Save this state too
    print("7. Saving department transfer state...")
    transfer_memento = originator.create_memento()
    caretaker.save_memento(transfer_memento)
    print("✓ Department transfer state saved")
    print(caretaker.display_history())
    print()
    
    # Demonstrate restoration - go back to previous state
    print("8. Restoring to previous state (before department transfer)...")
    previous_memento = caretaker.get_previous_memento()
    if previous_memento:
        originator.restore_from_memento(previous_memento)
        print("✓ Restored to previous state")
        print(originator.display_state())
        print(caretaker.display_history())
        print()
    
    # Demonstrate restoration - go back to initial state
    print("9. Restoring to initial state...")
    initial_restore = caretaker.get_memento(0)  # Get first memento
    if initial_restore:
        originator.restore_from_memento(initial_restore)
        print("✓ Restored to initial state")
        print(originator.display_state())
        print(caretaker.display_history())
        print()
    
    # Demonstrate forward navigation
    print("10. Moving forward in history...")
    next_memento = caretaker.get_next_memento()
    if next_memento:
        originator.restore_from_memento(next_memento)
        print("✓ Moved forward to next state")
        print(originator.display_state())
        print(caretaker.display_history())
        print()
    
    # Show final summary
    print("11. Final Summary:")
    print(f"   - Total snapshots saved: {caretaker.get_history_size()}")
    print(f"   - Current position in history: {caretaker.get_current_index()}")
    print("   - Pattern demonstrates:")
    print("     * Saving object state at different points")
    print("     * Restoring to any previous state")
    print("     * Navigating through state history")
    print("     * Maintaining state integrity")
    print()
    
    print("=" * 60)
    print("MEMENTO PATTERN DEMO COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    main()
