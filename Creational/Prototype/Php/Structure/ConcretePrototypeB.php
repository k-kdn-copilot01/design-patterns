<?php

/**
 * ConcretePrototypeB Implementation
 * 
 * This class implements deep cloning. All fields, including object references,
 * are copied to create completely independent objects.
 */
class ConcretePrototypeB implements Prototype
{
    private string $name;
    private int $value;
    private array $data; // This will be deeply copied
    
    public function __construct(string $name, int $value)
    {
        $this->name = $name;
        $this->value = $value;
        $this->data = ["Initial data for " . $name];
        echo "ConcretePrototypeB created: {$name}\n";
    }
    
    public function clone(): Prototype
    {
        $clone = new self($this->name . " (Deep Clone)", $this->value);
        $clone->data = array_merge([], $this->data); // Deep copy - new array
        echo "ConcretePrototypeB deep cloned: {$clone->name}\n";
        return $clone;
    }
    
    public function getInfo(): string
    {
        return sprintf(
            "ConcretePrototypeB[name=%s, value=%d, data=%s]",
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