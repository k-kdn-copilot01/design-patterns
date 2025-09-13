<?php

/**
 * PrototypeManager manages a registry of prototypes
 * and provides a way to create new objects by cloning registered prototypes
 */
class PrototypeManager
{
    private array $prototypes = [];
    
    /**
     * Register a prototype with a given name
     */
    public function registerPrototype(string $name, Prototype $prototype): void
    {
        $this->prototypes[$name] = $prototype;
        echo "Prototype registered: {$name}\n";
    }
    
    /**
     * Create a new object by cloning the registered prototype
     */
    public function createPrototype(string $name): Prototype
    {
        if (!isset($this->prototypes[$name])) {
            throw new InvalidArgumentException("Prototype not found: {$name}");
        }
        
        return $this->prototypes[$name]->clone();
    }
    
    /**
     * Remove a prototype from the registry
     */
    public function unregisterPrototype(string $name): void
    {
        unset($this->prototypes[$name]);
        echo "Prototype unregistered: {$name}\n";
    }
    
    /**
     * Get list of registered prototype names
     */
    public function getRegisteredNames(): array
    {
        return array_keys($this->prototypes);
    }
}