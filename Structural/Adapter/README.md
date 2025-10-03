# Adapter Pattern – Ví dụ Thanh Toán Đa Nền Tảng

## 🎯 Mục tiêu

* Chuẩn hoá giao diện (interface) cho nhiều dịch vụ thanh toán khác nhau (PayPal, MoMo, ZaloPay).
* Ẩn đi sự khác biệt của từng API, để client chỉ cần gọi theo một **chuẩn chung** (`PaymentProcessor`).
* Dễ dàng mở rộng khi bổ sung thêm cổng thanh toán mới.

---

## 🏗 Cấu trúc Code

### 1. **Target Interface**

```php
interface PaymentProcessor {
    public function pay(int $amount);
}
```

Đây là giao diện chuẩn mà **toàn bộ hệ thống** sử dụng. Client chỉ quan tâm đến nó.

---

### 2. **Adaptees (các dịch vụ thật sự)**

Mỗi cổng thanh toán có cách gọi khác nhau:

* `PaypalService` dùng `sendPayment(float $money)`
* `MomoService` dùng `makeTransaction(int $value)`
* `ZaloPayService` dùng `doPayment(string $amountInText)`

Ví dụ:

```php
class PaypalService {
    public function sendPayment(float $money) {
        echo "Thanh toán {$money} qua PayPal\n";
    }
}
```

---

### 3. **Adapters**

Nhiệm vụ: chuyển đổi interface của từng dịch vụ → interface chuẩn `PaymentProcessor`.

Ví dụ:

```php
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
```

---

### 4. **Client**

```php
function checkout(PaymentProcessor $processor, int $amount) {
    $processor->pay($amount);
}
```

Client **chỉ biết `PaymentProcessor`**, không quan tâm PayPal, MoMo, hay ZaloPay triển khai thế nào.

---