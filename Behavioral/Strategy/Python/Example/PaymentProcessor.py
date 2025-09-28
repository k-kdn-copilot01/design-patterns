from PaymentStrategy import PaymentStrategy


class PaymentProcessor:
    """
    Context class that uses different payment strategies.
    This class represents a payment processor that can handle different
    payment methods using the Strategy pattern.
    """
    
    def __init__(self, payment_strategy: PaymentStrategy = None):
        """
        Initialize the payment processor with a payment strategy.
        
        Args:
            payment_strategy: The payment strategy to use (optional)
        """
        self._payment_strategy = payment_strategy
        self.payment_history = []
    
    def set_payment_strategy(self, payment_strategy: PaymentStrategy):
        """
        Set a new payment strategy at runtime.
        
        Args:
            payment_strategy: The new payment strategy to use
        """
        self._payment_strategy = payment_strategy
        print(f"Payment method changed to: {payment_strategy.get_payment_method_name()}")
    
    def process_payment(self, amount):
        """
        Process payment using the current strategy.
        
        Args:
            amount (float): The amount to be paid
            
        Returns:
            dict: Payment result
        """
        if self._payment_strategy is None:
            raise ValueError("No payment method selected")
        
        print(f"\n--- Processing Payment ---")
        print(f"Amount: ${amount:.2f}")
        print(f"Method: {self._payment_strategy.get_payment_method_name()}")
        
        # Process the payment
        result = self._payment_strategy.pay(amount)
        
        # Add to payment history
        self.payment_history.append(result)
        
        print(f"--- Payment Complete ---\n")
        return result
    
    def get_payment_history(self):
        """
        Get the payment history.
        
        Returns:
            list: List of payment records
        """
        return self.payment_history
    
    def get_total_paid(self):
        """
        Get the total amount paid across all transactions.
        
        Returns:
            float: Total amount paid
        """
        return sum(payment['amount'] for payment in self.payment_history)
