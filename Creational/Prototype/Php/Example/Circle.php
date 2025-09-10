<?php

require_once 'Shape.php';

/**
 * Circle - Concrete Prototype
 * 
 * A concrete shape that can be cloned. Demonstrates prototype pattern
 * with a real geometric shape including specific properties.
 */
class Circle extends Shape
{
    private int $radius;
    
    private static bool $silentMode = false;
    
    public static function setSilentMode(bool $silent): void
    {
        self::$silentMode = $silent;
    }
    
    public function __construct(string $color = '', int $x = 0, int $y = 0, int $radius = 0)
    {
        parent::__construct($color, $x, $y);
        $this->radius = $radius;
        if ($color !== '' && !self::$silentMode) { // Only show message when not in silent mode
            echo "Circle created: " . $this->toString() . "\n";
        }
    }
    
    public function clone(): Shape
    {
        $clone = new Circle($this->color, $this->x, $this->y, $this->radius);
        return $clone;
    }
    
    public function draw(): void
    {
        echo "Drawing Circle at ({$this->x},{$this->y}) with radius {$this->radius} in {$this->color}\n";
    }
    
    public function getArea(): float
    {
        return pi() * $this->radius * $this->radius;
    }
    
    public function getRadius(): int
    {
        return $this->radius;
    }
    
    public function setRadius(int $radius): void
    {
        $this->radius = $radius;
    }
    
    public function equals(Shape $shape): bool
    {
        if (!($shape instanceof Circle) || !parent::equals($shape)) {
            return false;
        }
        return $shape->radius === $this->radius;
    }
    
    public function toString(): string
    {
        return "Circle[color={$this->color}, x={$this->x}, y={$this->y}, radius={$this->radius}]";
    }
}