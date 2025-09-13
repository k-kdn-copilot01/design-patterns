<?php

/**
 * Shape represents a geometric shape prototype
 * Demonstrates cloning with different shape types
 */
abstract class Shape implements Prototype
{
    protected string $color;
    protected int $x;
    protected int $y;
    
    public function __construct()
    {
        $this->color = '';
        $this->x = 0;
        $this->y = 0;
    }
    
    public abstract function clone(): Prototype;
    public abstract function getInfo(): string;
    public abstract function getArea(): float;
    
    public function setColor(string $color): void
    {
        $this->color = $color;
    }
    
    public function setPosition(int $x, int $y): void
    {
        $this->x = $x;
        $this->y = $y;
    }
    
    public function getColor(): string
    {
        return $this->color;
    }
}