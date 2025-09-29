from PaymentStrategy import PaymentStrategy
from CreditCardPayment import CreditCardPayment
from PayPalPayment import PayPalPayment
from BankTransferPayment import BankTransferPayment
from PaymentProcessor import PaymentProcessor


def main():
    """
    Demonstrate the Strategy pattern with a real-world payment processing example.
    """
    print("=== Strategy Pattern Demo: Payment Processing System ===\n")
    
    # Create payment processor
    processor = PaymentProcessor()
    
    # Create different payment strategies
    credit_card = CreditCardPayment("1234567890123456", "123", "12/25")
    paypal = PayPalPayment("user@example.com")
    bank_transfer = BankTransferPayment("987654321", "123456789")
    
    # Test different payment scenarios
    print("🛒 Shopping Cart Checkout Simulation\n")
    
    # Scenario 1: Credit Card Payment
    print("1. Customer chooses Credit Card payment:")
    processor.set_payment_strategy(credit_card)
    result1 = processor.process_payment(99.99)
    
    # Scenario 2: PayPal Payment
    print("2. Customer switches to PayPal payment:")
    processor.set_payment_strategy(paypal)
    result2 = processor.process_payment(49.50)
    
    # Scenario 3: Bank Transfer for large amount
    print("3. Customer chooses Bank Transfer for large purchase:")
    processor.set_payment_strategy(bank_transfer)
    result3 = processor.process_payment(500.00)
    
    # Scenario 4: Multiple payments with different methods
    print("4. Processing multiple orders with different payment methods:")
    
    # Order 1: Credit Card
    processor.set_payment_strategy(credit_card)
    processor.process_payment(25.99)
    
    # Order 2: PayPal
    processor.set_payment_strategy(paypal)
    processor.process_payment(75.00)
    
    # Order 3: Bank Transfer
    processor.set_payment_strategy(bank_transfer)
    processor.process_payment(200.00)
    
    # Display payment summary
    print("📊 Payment Summary:")
    print("=" * 50)
    
    history = processor.get_payment_history()
    total_paid = processor.get_total_paid()
    
    print(f"Total transactions: {len(history)}")
    print(f"Total amount paid: ${total_paid:.2f}")
    print("\nTransaction Details:")
    
    for i, payment in enumerate(history, 1):
        print(f"  {i}. {payment['method']}: ${payment['amount']:.2f} - {payment['transaction_id']}")
    
    print("\n=== Demo Complete ===")
    print("\n💡 Key Benefits of Strategy Pattern:")
    print("   • Easy to add new payment methods")
    print("   • Runtime strategy switching")
    print("   • Clean separation of payment logic")
    print("   • Each payment method is independently testable")


if __name__ == "__main__":
    main()
