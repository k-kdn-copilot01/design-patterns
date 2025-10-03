<?php 

    interface PaymentStrategy {
    public function pay(int $amount);
}

class PaypalPayment implements PaymentStrategy {
    public function pay(int $amount) {
        echo "Thanh toán {$amount} qua PayPal\n";
    }
}

class MomoPayment implements PaymentStrategy {
    public function pay(int $amount) {
        echo "Thanh toán {$amount} qua MoMo\n";
    }
}

class ZaloPayPayment implements PaymentStrategy {
    public function pay(int $amount) {
        echo "Thanh toán {$amount} qua ZaloPay\n";
    }
}

class Checkout {
    private $paymentStrategy;

    public function setPaymentStrategy(PaymentStrategy $paymentStrategy) {
        $this->paymentStrategy = $paymentStrategy;
    }

    public function processOrder(int $amount) {
        if (!$this->paymentStrategy) {
            throw new Exception("Chưa chọn phương thức thanh toán!");
        }
        $this->paymentStrategy->pay($amount);
    }
}

$checkout = new Checkout();

// Thanh toán qua PayPal
$checkout->setPaymentStrategy(new PaypalPayment());
$checkout->processOrder(1000);

// Thanh toán qua MoMo
$checkout->setPaymentStrategy(new MomoPayment());
$checkout->processOrder(2000);

// Thanh toán qua ZaloPay
$checkout->setPaymentStrategy(new ZaloPayPayment());
$checkout->processOrder(3000);

