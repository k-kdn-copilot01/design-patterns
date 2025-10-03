<?php 

// 1. Component (giao diện chung)
interface Coffee {
    public function getCost(): int;
    public function getDescription(): string;
}

// 2. Concrete Component (cà phê cơ bản)
class SimpleCoffee implements Coffee {
    public function getCost(): int {
        return 10;
    }

    public function getDescription(): string {
        return "Cà phê đen";
    }
}

// 3. Base Decorator
abstract class CoffeeDecorator implements Coffee {
    protected $coffee;
    public function __construct(Coffee $coffee) {
        $this->coffee = $coffee;
    }
    public function getCost(): int {
        return $this->coffee->getCost();
    }
    public function getDescription(): string {
        return $this->coffee->getDescription();
    }
}

// 4. Concrete Decorators
class MilkDecorator extends CoffeeDecorator {
    public function getCost(): int {
        return parent::getCost() + 5;
    }
    public function getDescription(): string {
        return parent::getDescription() . ", thêm sữa";
    }
}

class SugarDecorator extends CoffeeDecorator {
    public function getCost(): int {
        return parent::getCost() + 2;
    }
    public function getDescription(): string {
        return parent::getDescription() . ", thêm đường";
    }
}

class CaramelDecorator extends CoffeeDecorator {
    public function getCost(): int {
        return parent::getCost() + 7;
    }
    public function getDescription(): string {
        return parent::getDescription() . ", thêm caramel";
    }
}

$coffee = new SimpleCoffee();
echo $coffee->getDescription() . " | Giá: " . $coffee->getCost() . "\n";

$coffee = new MilkDecorator($coffee);
$coffee = new SugarDecorator($coffee);
$coffee = new CaramelDecorator($coffee);

echo $coffee->getDescription() . " | Giá: " . $coffee->getCost() . "\n";
