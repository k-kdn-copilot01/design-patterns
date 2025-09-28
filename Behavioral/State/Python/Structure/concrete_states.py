"""
State Pattern - Concrete States
Implementation of specific state classes
"""

from state import State


class ConcreteStateA(State):
    """
    Concrete state A implementation.
    """
    
    def handle_request(self, context):
        """
        Handle request in State A.
        Transitions to State B after handling.
        """
        print("Handling request in State A")
        print("Transitioning to State B...")
        from concrete_states import ConcreteStateB
        context.set_state(ConcreteStateB())


class ConcreteStateB(State):
    """
    Concrete state B implementation.
    """
    
    def handle_request(self, context):
        """
        Handle request in State B.
        Transitions to State C after handling.
        """
        print("Handling request in State B")
        print("Transitioning to State C...")
        from concrete_states import ConcreteStateC
        context.set_state(ConcreteStateC())


class ConcreteStateC(State):
    """
    Concrete state C implementation.
    """
    
    def handle_request(self, context):
        """
        Handle request in State C.
        Transitions back to State A after handling.
        """
        print("Handling request in State C")
        print("Transitioning back to State A...")
        from concrete_states import ConcreteStateA
        context.set_state(ConcreteStateA())
