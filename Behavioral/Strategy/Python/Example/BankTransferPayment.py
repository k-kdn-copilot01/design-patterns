from PaymentStrategy import PaymentStrategy


class BankTransferPayment(PaymentStrategy):
    """
    Concrete strategy for bank transfer payments.
    """
    
    def __init__(self, account_number, routing_number):
        """
        Initialize bank transfer payment strategy.
        
        Args:
            account_number (str): Bank account number
            routing_number (str): Bank routing number
        """
        self.account_number = account_number
        self.routing_number = routing_number
    
    def pay(self, amount):
        """
        Process bank transfer payment.
        
        Args:
            amount (float): The amount to be paid
            
        Returns:
            dict: Payment result
        """
        # Simulate bank transfer processing
        masked_account = f"****{self.account_number[-4:]}"
        
        print(f"Processing bank transfer of ${amount:.2f}")
        print(f"Account: {masked_account}")
        print(f"Routing: {self.routing_number}")
        
        # Simulate processing delay (bank transfers take longer)
        import time
        time.sleep(1.0)
        
        # Simulate successful payment
        result = {
            "status": "success",
            "method": "bank_transfer",
            "amount": amount,
            "transaction_id": f"BT_{int(time.time())}",
            "account_masked": masked_account
        }
        
        print(f"✅ Bank transfer successful! Transaction ID: {result['transaction_id']}")
        return result
    
    def get_payment_method_name(self):
        """
        Get the name of the payment method.
        
        Returns:
            str: Name of the payment method
        """
        return "Bank Transfer"
