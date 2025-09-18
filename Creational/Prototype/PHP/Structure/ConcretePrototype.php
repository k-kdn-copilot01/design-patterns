<?php

require_once 'Prototype.php';

/**
 * ConcretePrototype class
 * Implement Prototype interface với shallow copy
 */
class ConcretePrototype implements Prototype
{
    private string $name;
    private array $data;
    private object $reference;

    public function __construct(string $name, array $data, object $reference)
    {
        $this->name = $name;
        $this->data = $data;
        $this->reference = $reference;
    }

    public function clone(): ConcretePrototype
    {
        return clone $this;
    }

    public function getName(): string
    {
        return $this->name;
    }

    public function setName(string $name): void
    {
        $this->name = $name;
    }

    public function getData(): array
    {
        return $this->data;
    }

    public function setData(array $data): void
    {
        $this->data = $data;
    }

    public function getReference(): object
    {
        return $this->reference;
    }

    public function setReference(object $reference): void
    {
        $this->reference = $reference;
    }
}
