from PaymentStrategy import PaymentStrategy


class PayPalPayment(PaymentStrategy):
    """
    Concrete strategy for PayPal payments.
    """
    
    def __init__(self, email):
        """
        Initialize PayPal payment strategy.
        
        Args:
            email (str): PayPal email address
        """
        self.email = email
    
    def pay(self, amount):
        """
        Process PayPal payment.
        
        Args:
            amount (float): The amount to be paid
            
        Returns:
            dict: Payment result
        """
        # Simulate PayPal processing
        print(f"Processing PayPal payment of ${amount:.2f}")
        print(f"PayPal Email: {self.email}")
        
        # Simulate processing delay
        import time
        time.sleep(0.3)
        
        # Simulate successful payment
        result = {
            "status": "success",
            "method": "paypal",
            "amount": amount,
            "transaction_id": f"PP_{int(time.time())}",
            "email": self.email
        }
        
        print(f"✅ PayPal payment successful! Transaction ID: {result['transaction_id']}")
        return result
    
    def get_payment_method_name(self):
        """
        Get the name of the payment method.
        
        Returns:
            str: Name of the payment method
        """
        return "PayPal"
