import sys
import os

# Add the Structure directory to the path to import base classes
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Structure'))

from Level1Support import Level1Support
from Level2Support import Level2Support
from Level3Support import Level3Support
from ManagerSupport import ManagerSupport
from SupportTicket import SupportTicket, TicketPriority


def create_support_chain():
    """Create and configure the support chain"""
    level1 = Level1Support()
    level2 = Level2Support()
    level3 = Level3Support()
    manager = ManagerSupport()
    
    # Set up the chain: Level1 -> Level2 -> Level3 -> Manager
    level1.set_next(level2).set_next(level3).set_next(manager)
    
    return level1


def main():
    print("=== Chain of Responsibility Pattern - Support Ticket System ===\n")
    
    # Create the support chain
    support_chain = create_support_chain()
    
    print("Support Chain Setup:")
    print("Level 1 Support -> Level 2 Support -> Level 3 Support -> Manager Support\n")
    
    # Create sample tickets with different priorities
    tickets = [
        SupportTicket("001", TicketPriority.LOW, "How do I change my password?", "John Doe"),
        SupportTicket("002", TicketPriority.MEDIUM, "My account is locked", "Jane Smith"),
        SupportTicket("003", TicketPriority.HIGH, "System is running slowly", "Bob Johnson"),
        SupportTicket("004", TicketPriority.CRITICAL, "Complete system outage", "Alice Brown"),
        SupportTicket("005", TicketPriority.LOW, "Where can I find documentation?", "Charlie Wilson"),
    ]
    
    print("Processing Support Tickets:\n")
    
    for ticket in tickets:
        print(f"📋 New ticket received: {ticket}")
        support_chain.handle_ticket(ticket)
        print("-" * 60)
    
    print("\n=== Testing Chain Flexibility ===")
    print("Creating a different chain order: Level2 -> Level3 -> Manager\n")
    
    # Test with different chain order
    level2_alt = Level2Support()
    level3_alt = Level3Support()
    manager_alt = ManagerSupport()
    
    level2_alt.set_next(level3_alt).set_next(manager_alt)
    
    test_ticket = SupportTicket("006", TicketPriority.MEDIUM, "Test ticket with different chain", "Test User")
    print(f"📋 Processing with alternative chain: {test_ticket}")
    level2_alt.handle_ticket(test_ticket)
    
    print("\n=== Example Demo Complete ===")


if __name__ == "__main__":
    main()
