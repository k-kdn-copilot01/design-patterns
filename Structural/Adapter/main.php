<?php 

interface PaymentProcessor {
    public function pay(int $amount);
}

class PaypalService {
    public function sendPayment(float $money) {
        echo "Thanh toán {$money} qua PayPal\n";
    }
}

class MomoService {
    public function makeTransaction(int $value) {
        echo "Thanh toán {$value} qua Momo\n";
    }
}

class ZaloPayService {
    public function doPayment(string $amountInText) {
        echo "Thanh toán {$amountInText} qua ZaloPay\n";
    }
}

class PaypalAdapter implements PaymentProcessor {
    private $paypal;
    public function __construct(PaypalService $paypal) {
        $this->paypal = $paypal;
    }
    public function pay(int $amount) {
        $this->paypal->sendPayment($amount);
    }
}

class MomoAdapter implements PaymentProcessor {
    private $momo;
    public function __construct(MomoService $momo) {
        $this->momo = $momo;
    }
    public function pay(int $amount) {
        $this->momo->makeTransaction($amount);
    }
}

class ZaloPayAdapter implements PaymentProcessor {
    private $zalo;
    public function __construct(ZaloPayService $zalo) {
        $this->zalo = $zalo;
    }
    public function pay(int $amount) {
        // ZaloPay yêu cầu string → adapter chuyển đổi
        $this->zalo->doPayment((string)$amount);
    }
}


function checkout(PaymentProcessor $processor, int $amount) {
    $processor->pay($amount);
}

$paypal = new PaypalAdapter(new PaypalService());
$momo   = new MomoAdapter(new MomoService());
$zalo   = new ZaloPayAdapter(new ZaloPayService());

checkout($paypal, 1000);
checkout($momo, 2000);
checkout($zalo, 3000);

