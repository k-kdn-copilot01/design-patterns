from PaymentStrategy import PaymentStrategy


class CreditCardPayment(PaymentStrategy):
    """
    Concrete strategy for credit card payments.
    """
    
    def __init__(self, card_number, cvv, expiry_date):
        """
        Initialize credit card payment strategy.
        
        Args:
            card_number (str): Credit card number
            cvv (str): Card verification value
            expiry_date (str): Card expiry date
        """
        self.card_number = card_number
        self.cvv = cvv
        self.expiry_date = expiry_date
    
    def pay(self, amount):
        """
        Process credit card payment.
        
        Args:
            amount (float): The amount to be paid
            
        Returns:
            dict: Payment result
        """
        # Simulate credit card processing
        masked_card = f"****-****-****-{self.card_number[-4:]}"
        
        print(f"Processing credit card payment of ${amount:.2f}")
        print(f"Card: {masked_card}")
        print(f"CVV: {self.cvv}")
        print(f"Expiry: {self.expiry_date}")
        
        # Simulate processing delay
        import time
        time.sleep(0.5)
        
        # Simulate successful payment
        result = {
            "status": "success",
            "method": "credit_card",
            "amount": amount,
            "transaction_id": f"CC_{int(time.time())}",
            "card_masked": masked_card
        }
        
        print(f"✅ Credit card payment successful! Transaction ID: {result['transaction_id']}")
        return result
    
    def get_payment_method_name(self):
        """
        Get the name of the payment method.
        
        Returns:
            str: Name of the payment method
        """
        return "Credit Card"
