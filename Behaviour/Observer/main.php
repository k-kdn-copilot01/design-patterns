<?php 

interface Subject {
    public function attach(Observer $observer);
    public function detach(Observer $observer);
    public function notify(string $message);
}

interface Observer {
    public function update(string $message);
}

class Order implements Subject {
    private $observers = [];

    public function attach(Observer $observer) {
        $this->observers[] = $observer;
    }

    public function detach(Observer $observer) {
        $this->observers = array_filter($this->observers, fn($o) => $o !== $observer);
    }

    public function notify(string $message) {
        foreach ($this->observers as $observer) {
            $observer->update($message);
        }
    }

    public function createOrder(int $orderId) {
        echo "Đơn hàng #{$orderId} đã được tạo\n";
        $this->notify("Đơn hàng #{$orderId} đã tạo thành công");
    }
}

class EmailService implements Observer {
    public function update(string $message) {
        echo "[Email] Gửi email: {$message}\n";
    }
}

class SmsService implements Observer {
    public function update(string $message) {
        echo "[SMS] Gửi SMS: {$message}\n";
    }
}

class LogService implements Observer {
    public function update(string $message) {
        echo "[Log] Ghi log: {$message}\n";
    }
}

$order = new Order();
$order->attach(new EmailService());
$order->attach(new SmsService());
$order->attach(new LogService());

$order->createOrder(101);

