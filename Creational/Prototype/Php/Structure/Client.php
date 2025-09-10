<?php

require_once 'Prototype.php';

/**
 * Client Class
 * 
 * The client works with prototypes through the Prototype interface.
 * It can clone objects without knowing their concrete types.
 */
class Client
{
    private Prototype $prototype;
    
    public function __construct(Prototype $prototype)
    {
        $this->prototype = $prototype;
    }
    
    /**
     * Creates a clone of the stored prototype
     * @return Prototype A clone of the prototype
     */
    public function createClone(): Prototype
    {
        return $this->prototype->clone();
    }
    
    /**
     * Sets a new prototype to be cloned
     * @param Prototype $prototype The new prototype to store
     */
    public function setPrototype(Prototype $prototype): void
    {
        $this->prototype = $prototype;
    }
    
    /**
     * Displays the current prototype
     */
    public function displayPrototype(): void
    {
        echo "Current prototype: ";
        $this->prototype->display();
    }
}