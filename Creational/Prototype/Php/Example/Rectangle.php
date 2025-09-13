<?php

/**
 * Rectangle implementation of Shape prototype
 */
class Rectangle extends Shape
{
    private float $width;
    private float $height;
    
    public function __construct(float $width = 0, float $height = 0, string $color = '', int $x = 0, int $y = 0)
    {
        parent::__construct();
        $this->width = $width;
        $this->height = $height;
        $this->color = $color;
        $this->x = $x;
        $this->y = $y;
        if ($width > 0 && $height > 0) {
            echo "Rectangle created: {$width}x{$height}, color={$color}\n";
        }
    }
    
    public function clone(): Prototype
    {
        $clone = new self($this->width, $this->height, $this->color, $this->x, $this->y);
        echo "Rectangle cloned: {$this->width}x{$this->height}, color={$this->color}\n";
        return $clone;
    }
    
    public function getInfo(): string
    {
        return sprintf(
            "Rectangle[width=%.1f, height=%.1f, color='%s', position=(%d,%d), area=%.2f]",
            $this->width,
            $this->height,
            $this->color,
            $this->x,
            $this->y,
            $this->getArea()
        );
    }
    
    public function getArea(): float
    {
        return $this->width * $this->height;
    }
    
    public function getWidth(): float
    {
        return $this->width;
    }
    
    public function getHeight(): float
    {
        return $this->height;
    }
    
    public function setWidth(float $width): void
    {
        $this->width = $width;
    }
    
    public function setHeight(float $height): void
    {
        $this->height = $height;
    }
}