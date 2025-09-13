<?php

/**
 * Client Class
 * 
 * This class demonstrates how to use prototypes for object creation.
 * It shows how cloning can be more efficient than creating new objects
 * when the initialization is complex or expensive.
 */
class Client
{
    private Prototype $prototype;
    
    public function __construct(Prototype $prototype)
    {
        $this->prototype = $prototype;
    }
    
    /**
     * Creates a new object by cloning the stored prototype
     */
    public function createObject(): Prototype
    {
        return $this->prototype->clone();
    }
    
    /**
     * Changes the prototype to a different one
     */
    public function setPrototype(Prototype $prototype): void
    {
        $this->prototype = $prototype;
    }
    
    /**
     * Gets information about the current prototype
     */
    public function getPrototypeInfo(): string
    {
        return $this->prototype->getInfo();
    }
}