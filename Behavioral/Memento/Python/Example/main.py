"""
Memento Pattern - Real-world Example Demo

This demo shows the Memento pattern in a practical scenario:
a text editor with undo/redo functionality.
"""

from text_editor import TextEditor, UndoRedoManager


def simulate_typing(editor: TextEditor, manager: UndoRedoManager, text: str) -> None:
    """
    Simulate typing text character by character and saving states.
    
    Args:
        editor: The text editor
        manager: The undo/redo manager
        text: Text to type
    """
    print(f"Typing: '{text}'")
    for char in text:
        editor.insert_text(char)
        # Save state after each character
        memento = editor.create_memento()
        manager.save_state(memento)
        print(f"  Added '{char}' -> {editor.get_content()}")
    print()


def simulate_editing_session():
    """
    Simulate a complete editing session with undo/redo operations.
    """
    print("=" * 70)
    print("MEMENTO PATTERN - REAL-WORLD EXAMPLE: TEXT EDITOR")
    print("=" * 70)
    print()
    
    # Create text editor and undo/redo manager
    print("1. Initializing text editor with undo/redo functionality...")
    editor = TextEditor()
    manager = UndoRedoManager(max_history=20)
    
    # Save initial empty state
    initial_memento = editor.create_memento()
    manager.save_state(initial_memento)
    print("✓ Initial empty state saved")
    print(editor.display_state())
    print()
    
    # Simulate typing a document
    print("2. Typing a document...")
    simulate_typing(editor, manager, "Hello")
    simulate_typing(editor, manager, " World!")
    simulate_typing(editor, manager, " This is a test document.")
    
    print("Current state:")
    print(editor.display_state())
    print()
    
    # Move cursor and add more text
    print("3. Moving cursor and adding more text...")
    editor.move_cursor(6)  # Move to after "Hello"
    simulate_typing(editor, manager, "Beautiful ")
    
    print("Current state:")
    print(editor.display_state())
    print()
    
    # Add a new line
    print("4. Adding a new line...")
    editor.move_cursor(len(editor.get_content()))  # Move to end
    simulate_typing(editor, manager, "\nThis is line 2.")
    
    print("Current state:")
    print(editor.display_state())
    print()
    
    # Show history
    print("5. Current history:")
    print(manager.get_history_info())
    print()
    
    # Demonstrate undo operations
    print("6. Demonstrating UNDO operations...")
    undo_count = 0
    while manager.can_undo() and undo_count < 5:
        memento = manager.undo()
        if memento:
            editor.restore_from_memento(memento)
            undo_count += 1
            print(f"Undo #{undo_count}: {editor.get_content()}")
    
    print(f"\nAfter {undo_count} undo operations:")
    print(editor.display_state())
    print()
    
    # Demonstrate redo operations
    print("7. Demonstrating REDO operations...")
    redo_count = 0
    while manager.can_redo() and redo_count < 3:
        memento = manager.redo()
        if memento:
            editor.restore_from_memento(memento)
            redo_count += 1
            print(f"Redo #{redo_count}: {editor.get_content()}")
    
    print(f"\nAfter {redo_count} redo operations:")
    print(editor.display_state())
    print()
    
    # Make some more changes
    print("8. Making additional changes...")
    editor.move_cursor(len(editor.get_content()))
    simulate_typing(editor, manager, "\nThis is line 3 with more content.")
    
    print("Current state:")
    print(editor.display_state())
    print()
    
    # Demonstrate multiple undo/redo cycles
    print("9. Demonstrating multiple undo/redo cycles...")
    
    # Undo back to beginning
    print("Undoing back to beginning...")
    while manager.can_undo():
        memento = manager.undo()
        if memento:
            editor.restore_from_memento(memento)
    
    print("At beginning:")
    print(editor.display_state())
    print()
    
    # Redo to end
    print("Redoing to end...")
    while manager.can_redo():
        memento = manager.redo()
        if memento:
            editor.restore_from_memento(memento)
    
    print("At end:")
    print(editor.display_state())
    print()
    
    # Show final history
    print("10. Final history state:")
    print(manager.get_history_info())
    print()
    
    # Demonstrate practical benefits
    print("11. Practical Benefits Demonstrated:")
    print("   ✓ Undo/Redo functionality works seamlessly")
    print("   ✓ State is preserved at each editing step")
    print("   ✓ Can navigate through entire editing history")
    print("   ✓ Memory efficient (limited history size)")
    print("   ✓ No data loss during undo/redo operations")
    print("   ✓ Timestamps help track when changes were made")
    print()
    
    print("=" * 70)
    print("TEXT EDITOR DEMO COMPLETED")
    print("=" * 70)


def demonstrate_error_recovery():
    """
    Demonstrate how the Memento pattern helps with error recovery.
    """
    print("\n" + "=" * 70)
    print("ERROR RECOVERY SCENARIO")
    print("=" * 70)
    print()
    
    editor = TextEditor()
    manager = UndoRedoManager()
    
    # Save initial state
    manager.save_state(editor.create_memento())
    
    # Simulate user making changes
    print("User types some content...")
    editor.insert_text("Important document content here.")
    manager.save_state(editor.create_memento())
    
    editor.insert_text(" More important information.")
    manager.save_state(editor.create_memento())
    
    print("Current content:", editor.get_content())
    print()
    
    # Simulate accidental deletion or corruption
    print("Simulating accidental content loss...")
    editor.set_content("")  # Accidentally cleared content
    print("Content after accident:", repr(editor.get_content()))
    print()
    
    # Recover using memento
    print("Recovering from last saved state...")
    if manager.can_undo():
        memento = manager.undo()
        if memento:
            editor.restore_from_memento(memento)
            print("✓ Content recovered!")
            print("Recovered content:", editor.get_content())
    print()
    
    print("=" * 70)
    print("ERROR RECOVERY DEMO COMPLETED")
    print("=" * 70)


def main():
    """
    Main function to run both demos.
    """
    simulate_editing_session()
    demonstrate_error_recovery()


if __name__ == "__main__":
    main()
