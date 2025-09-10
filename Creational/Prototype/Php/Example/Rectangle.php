<?php

require_once 'Shape.php';

/**
 * Rectangle - Concrete Prototype
 * 
 * Another concrete shape that demonstrates the prototype pattern
 * with different properties than Circle.
 */
class Rectangle extends Shape
{
    private int $width;
    private int $height;
    
    public function __construct(string $color = '', int $x = 0, int $y = 0, int $width = 0, int $height = 0)
    {
        parent::__construct($color, $x, $y);
        $this->width = $width;
        $this->height = $height;
        if ($color !== '') { // Only show message for non-empty constructor calls
            echo "Rectangle created: " . $this->toString() . "\n";
        }
    }
    
    public function clone(): Shape
    {
        $clone = new Rectangle($this->color, $this->x, $this->y, $this->width, $this->height);
        return $clone;
    }
    
    public function draw(): void
    {
        echo "Drawing Rectangle at ({$this->x},{$this->y}) with size {$this->width}x{$this->height} in {$this->color}\n";
    }
    
    public function getArea(): float
    {
        return $this->width * $this->height;
    }
    
    public function getWidth(): int
    {
        return $this->width;
    }
    
    public function setWidth(int $width): void
    {
        $this->width = $width;
    }
    
    public function getHeight(): int
    {
        return $this->height;
    }
    
    public function setHeight(int $height): void
    {
        $this->height = $height;
    }
    
    public function equals(Shape $shape): bool
    {
        if (!($shape instanceof Rectangle) || !parent::equals($shape)) {
            return false;
        }
        return $shape->width === $this->width && $shape->height === $this->height;
    }
    
    public function toString(): string
    {
        return "Rectangle[color={$this->color}, x={$this->x}, y={$this->y}, width={$this->width}, height={$this->height}]";
    }
}