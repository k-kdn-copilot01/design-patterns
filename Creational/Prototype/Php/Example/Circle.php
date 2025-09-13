<?php

/**
 * Circle implementation of Shape prototype
 */
class Circle extends Shape
{
    private float $radius;
    
    public function __construct(float $radius = 0, string $color = '', int $x = 0, int $y = 0)
    {
        parent::__construct();
        $this->radius = $radius;
        $this->color = $color;
        $this->x = $x;
        $this->y = $y;
        if ($radius > 0) {
            echo "Circle created: radius={$radius}, color={$color}\n";
        }
    }
    
    public function clone(): Prototype
    {
        $clone = new self($this->radius, $this->color, $this->x, $this->y);
        echo "Circle cloned: radius={$this->radius}, color={$this->color}\n";
        return $clone;
    }
    
    public function getInfo(): string
    {
        return sprintf(
            "Circle[radius=%.1f, color='%s', position=(%d,%d), area=%.2f]",
            $this->radius,
            $this->color,
            $this->x,
            $this->y,
            $this->getArea()
        );
    }
    
    public function getArea(): float
    {
        return pi() * $this->radius * $this->radius;
    }
    
    public function getRadius(): float
    {
        return $this->radius;
    }
    
    public function setRadius(float $radius): void
    {
        $this->radius = $radius;
    }
}