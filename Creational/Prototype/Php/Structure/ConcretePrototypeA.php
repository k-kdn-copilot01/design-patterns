<?php

require_once 'Prototype.php';

/**
 * Concrete Prototype A Implementation
 * 
 * This concrete prototype maintains its own state and can create clones of itself.
 * Demonstrates basic prototype cloning functionality.
 */
class ConcretePrototypeA implements Prototype
{
    private string $data;
    private int $value;
    
    public function __construct(string $data, int $value)
    {
        $this->data = $data;
        $this->value = $value;
        echo "ConcretePrototypeA created with data: {$data}, value: {$value}\n";
    }
    
    public function clone(): Prototype
    {
        $clone = new self($this->data, $this->value);
        echo "ConcretePrototypeA cloned with data: {$this->data}, value: {$this->value}\n";
        return $clone;
    }
    
    public function display(): void
    {
        echo "ConcretePrototypeA [data={$this->data}, value={$this->value}]\n";
    }
    
    // Getters for demonstration purposes
    public function getData(): string
    {
        return $this->data;
    }
    
    public function getValue(): int
    {
        return $this->value;
    }
    
    // Setters to demonstrate independence of clones
    public function setData(string $data): void
    {
        $this->data = $data;
    }
    
    public function setValue(int $value): void
    {
        $this->value = $value;
    }
    
    // Prevent cloning through magic method
    public function __clone()
    {
        // This method can be used for custom clone behavior if needed
    }
}