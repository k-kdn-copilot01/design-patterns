<?php

/**
 * Shape - Abstract Prototype
 * 
 * Base class for all geometric shapes that can be cloned.
 * Demonstrates a real-world use case for the Prototype pattern.
 */
abstract class Shape
{
    protected string $color;
    protected int $x;
    protected int $y;
    
    public function __construct(string $color = '', int $x = 0, int $y = 0)
    {
        $this->color = $color;
        $this->x = $x;
        $this->y = $y;
    }
    
    public abstract function clone(): Shape;
    
    public abstract function draw(): void;
    
    public abstract function getArea(): float;
    
    // Getters and setters
    public function getColor(): string
    {
        return $this->color;
    }
    
    public function setColor(string $color): void
    {
        $this->color = $color;
    }
    
    public function getX(): int
    {
        return $this->x;
    }
    
    public function setX(int $x): void
    {
        $this->x = $x;
    }
    
    public function getY(): int
    {
        return $this->y;
    }
    
    public function setY(int $y): void
    {
        $this->y = $y;
    }
    
    public function move(int $x, int $y): void
    {
        $this->x = $x;
        $this->y = $y;
    }
    
    public function equals(Shape $shape): bool
    {
        return $shape->color === $this->color && 
               $shape->x === $this->x && 
               $shape->y === $this->y;
    }
    
    // Prevent cloning through magic method
    public function __clone()
    {
        // This method can be used for custom clone behavior if needed
    }
}