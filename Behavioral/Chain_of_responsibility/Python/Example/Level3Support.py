from SupportHandler import SupportHandler
from SupportTicket import SupportTicket


class Level3Support(SupportHandler):
    """
    Level 3 Support handles high priority tickets (system issues, security concerns).
    """
    
    def __init__(self):
        super().__init__("Level 3 Support", 3)  # Can handle priority 1-3 (LOW-HIGH)
    
    def _process_ticket(self, ticket: SupportTicket):
        print(f"⚡ {self.name}: Processing {ticket}")
        print(f"   → Investigating system-level issues and security concerns")
        print(f"   → Ticket #{ticket.id} resolved by Level 3 Support")
        print()
