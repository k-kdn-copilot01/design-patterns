<?php

/**
 * Prototype Interface
 * 
 * This interface defines the contract for objects that can be cloned.
 * The clone() method should create a copy of the current object.
 */
interface Prototype
{
    /**
     * Creates a copy of the current object
     * 
     * @return Prototype A new instance that is a copy of the current object
     */
    public function clone(): Prototype;
    
    /**
     * Returns a string representation of the object for demonstration purposes
     */
    public function getInfo(): string;
}