from SupportHandler import SupportHandler
from SupportTicket import SupportTicket


class ManagerSupport(SupportHandler):
    """
    Manager Support handles critical priority tickets (system outages, major incidents).
    """
    
    def __init__(self):
        super().__init__("Manager Support", 4)  # Can handle all priorities (LOW-CRITICAL)
    
    def _process_ticket(self, ticket: SupportTicket):
        print(f"🚨 {self.name}: Processing {ticket}")
        print(f"   → Coordinating emergency response and system recovery")
        print(f"   → Ticket #{ticket.id} resolved by Manager Support")
        print()
