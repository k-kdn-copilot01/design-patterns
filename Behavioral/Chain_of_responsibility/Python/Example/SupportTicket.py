from dataclasses import dataclass
from enum import Enum
from typing import Optional


class TicketPriority(Enum):
    """Enumeration for ticket priorities"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


@dataclass
class SupportTicket:
    """Represents a support ticket with priority and description"""
    id: str
    priority: TicketPriority
    description: str
    customer_name: str
    
    def __str__(self):
        return f"Ticket #{self.id} ({self.priority.name}) - {self.customer_name}: {self.description}"
