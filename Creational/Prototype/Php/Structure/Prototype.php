<?php

/**
 * Prototype Interface
 * 
 * Declares the clone method that concrete prototypes must implement.
 * This interface enables objects to be cloned without knowing their concrete types.
 */
interface Prototype
{
    /**
     * Creates and returns a copy of this object
     * @return Prototype A clone of this prototype
     */
    public function clone(): Prototype;
    
    /**
     * Display information about this prototype
     */
    public function display(): void;
}