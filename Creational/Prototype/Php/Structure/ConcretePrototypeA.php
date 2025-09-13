<?php

/**
 * ConcretePrototypeA Implementation
 * 
 * This class implements shallow cloning. All primitive fields are copied,
 * but object references are shared between the original and clone.
 */
class ConcretePrototypeA implements Prototype
{
    private string $name;
    private int $value;
    private array $data; // This will be shared in shallow clone
    
    public function __construct(string $name, int $value)
    {
        $this->name = $name;
        $this->value = $value;
        $this->data = ["Initial data for " . $name];
        echo "ConcretePrototypeA created: {$name}\n";
    }
    
    public function clone(): Prototype
    {
        $clone = new self($this->name . " (Clone)", $this->value);
        $clone->data = $this->data; // Shallow copy - same reference
        echo "ConcretePrototypeA cloned: {$clone->name}\n";
        return $clone;
    }
    
    public function getInfo(): string
    {
        return sprintf(
            "ConcretePrototypeA[name=%s, value=%d, data=%s]",
            $this->name,
            $this->value,
            implode(", ", $this->data)
        );
    }
    
    public function appendData(string $newData): void
    {
        $this->data[] = $newData;
    }
    
    public function getName(): string
    {
        return $this->name;
    }
    
    public function getValue(): int
    {
        return $this->value;
    }
}