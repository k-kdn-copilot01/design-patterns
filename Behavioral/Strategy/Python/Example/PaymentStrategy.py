from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    """
    Abstract base class for payment strategies.
    Defines the interface that all payment methods must implement.
    """
    
    @abstractmethod
    def pay(self, amount):
        """
        Process payment with the specific strategy.
        
        Args:
            amount (float): The amount to be paid
            
        Returns:
            dict: Payment result with status and details
        """
        pass
    
    @abstractmethod
    def get_payment_method_name(self):
        """
        Get the name of the payment method.
        
        Returns:
            str: Name of the payment method
        """
        pass
