from TextEditor import TextEditor
from TextCommand import InsertTextCommand, DeleteTextCommand
from TextEditorInvoker import TextEditorInvoker


def main():
    print("=== Command Pattern Demo: Text Editor with Undo/Redo ===\n")
    
    # Create text editor and invoker
    editor = TextEditor()
    invoker = TextEditorInvoker()
    
    print("Initial state:")
    print(f"Content: '{editor.get_content()}'")
    print(f"Cursor position: {editor.get_cursor_position()}\n")
    
    print("1. Inserting text 'Hello ' at the beginning:")
    insert_hello = InsertTextCommand(editor, "Hello ")
    invoker.execute_command(insert_hello)
    
    print("2. Inserting text 'World!' at the end:")
    insert_world = InsertTextCommand(editor, "World!")
    invoker.execute_command(insert_world)
    
    print("3. Inserting text 'Beautiful ' in the middle:")
    insert_beautiful = InsertTextCommand(editor, "Beautiful ", 6)
    invoker.execute_command(insert_beautiful)
    
    print(f"Current state - History size: {invoker.get_history_size()}")
    print(f"Content: '{editor.get_content()}'\n")
    
    print("4. Undoing last command (removing 'Beautiful '):")
    invoker.undo()
    print(f"Content: '{editor.get_content()}'\n")
    
    print("5. Undoing another command (removing 'World!'):")
    invoker.undo()
    print(f"Content: '{editor.get_content()}'\n")
    
    print("6. Redoing last undone command (adding 'World!' back):")
    invoker.redo()
    print(f"Content: '{editor.get_content()}'\n")
    
    print("7. Deleting text 'Hello ' from the beginning:")
    delete_hello = DeleteTextCommand(editor, 0, 6)
    invoker.execute_command(delete_hello)
    print(f"Content: '{editor.get_content()}'\n")
    
    print("8. Undoing the delete operation:")
    invoker.undo()
    print(f"Content: '{editor.get_content()}'\n")
    
    print("9. Testing multiple undos:")
    print("Undoing all remaining commands...")
    while invoker.get_history_size() > 0:
        invoker.undo()
    
    print(f"Final content: '{editor.get_content()}'")
    print(f"History size: {invoker.get_history_size()}")
    print(f"Redo stack size: {invoker.get_redo_stack_size()}")
    
    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    main()
