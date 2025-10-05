from Receiver import Receiver
from ConcreteCommand import ConcreteCommand
from Invoker import Invoker


def main():
    print("=== Structure Demo: Command Pattern ===\n")
    
    # Create receiver
    receiver = Receiver("BusinessLogic")
    
    # Create commands
    command1 = ConcreteCommand(receiver, "Save data to database")
    command2 = ConcreteCommand(receiver, "Send email notification")
    command3 = ConcreteCommand(receiver, "Generate report")
    
    # Create invoker
    invoker = Invoker()
    
    print("1. Setting up commands:")
    invoker.set_command(command1)
    invoker.set_command(command2)
    invoker.set_command(command3)
    print("Commands added to invoker\n")
    
    print("2. Executing all commands:")
    invoker.execute_commands()
    print(f"History size: {invoker.get_history_size()}\n")
    
    print("3. Undoing last command:")
    invoker.undo_last_command()
    print(f"History size after undo: {invoker.get_history_size()}\n")
    
    print("4. Undoing all remaining commands:")
    invoker.undo_all_commands()
    print(f"History size after undo all: {invoker.get_history_size()}\n")
    
    print("5. Testing individual command execution:")
    single_command = ConcreteCommand(receiver, "Single operation")
    single_command.execute()
    single_command.undo()
    
    print("\n=== Structure Demo Complete ===")


if __name__ == "__main__":
    main()
