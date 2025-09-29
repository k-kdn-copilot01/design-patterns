from SupportHandler import SupportHandler
from SupportTicket import SupportTicket


class Level2Support(SupportHandler):
    """
    Level 2 Support handles medium priority tickets (technical issues, account problems).
    """
    
    def __init__(self):
        super().__init__("Level 2 Support", 2)  # Can handle priority 1-2 (LOW-MEDIUM)
    
    def _process_ticket(self, ticket: SupportTicket):
        print(f"🔧 {self.name}: Processing {ticket}")
        print(f"   → Performing advanced troubleshooting and technical analysis")
        print(f"   → Ticket #{ticket.id} resolved by Level 2 Support")
        print()
