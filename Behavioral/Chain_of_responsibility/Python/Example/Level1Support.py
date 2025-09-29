from SupportHandler import SupportHandler
from SupportTicket import SupportTicket


class Level1Support(SupportHandler):
    """
    Level 1 Support handles low priority tickets (general inquiries, basic issues).
    """
    
    def __init__(self):
        super().__init__("Level 1 Support", 1)  # Can handle priority 1 (LOW)
    
    def _process_ticket(self, ticket: SupportTicket):
        print(f"🎧 {self.name}: Processing {ticket}")
        print(f"   → Providing basic troubleshooting and general assistance")
        print(f"   → Ticket #{ticket.id} resolved by Level 1 Support")
        print()
