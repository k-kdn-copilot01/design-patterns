<?php

require_once 'Prototype.php';

/**
 * Concrete Prototype B Implementation
 * 
 * This concrete prototype demonstrates a different type of object that can be cloned.
 * Shows how different classes can implement the same prototype interface.
 */
class ConcretePrototypeB implements Prototype
{
    private string $name;
    private bool $active;
    
    public function __construct(string $name, bool $active)
    {
        $this->name = $name;
        $this->active = $active;
        echo "ConcretePrototypeB created with name: {$name}, active: " . ($active ? 'true' : 'false') . "\n";
    }
    
    public function clone(): Prototype
    {
        $clone = new self($this->name, $this->active);
        echo "ConcretePrototypeB cloned with name: {$this->name}, active: " . ($this->active ? 'true' : 'false') . "\n";
        return $clone;
    }
    
    public function display(): void
    {
        echo "ConcretePrototypeB [name={$this->name}, active=" . ($this->active ? 'true' : 'false') . "]\n";
    }
    
    // Getters for demonstration purposes
    public function getName(): string
    {
        return $this->name;
    }
    
    public function isActive(): bool
    {
        return $this->active;
    }
    
    // Setters to demonstrate independence of clones
    public function setName(string $name): void
    {
        $this->name = $name;
    }
    
    public function setActive(bool $active): void
    {
        $this->active = $active;
    }
    
    // Prevent cloning through magic method
    public function __clone()
    {
        // This method can be used for custom clone behavior if needed
    }
}