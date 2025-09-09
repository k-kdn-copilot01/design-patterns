<?php

/**
 * Eager Singleton Implementation
 * 
 * This implementation creates the instance at class loading time.
 * In PHP, we simulate eager initialization by creating the instance
 * in a static property with immediate initialization.
 */
class EagerSingleton
{
    private static $instance;
    
    // Private constructor to prevent external instantiation
    private function __construct()
    {
        echo "EagerSingleton instance created\n";
    }
    
    // Prevent cloning of the instance
    private function __clone() {}
    
    // Prevent unserializing of the instance
    public function __wakeup() 
    {
        throw new \Exception("Cannot unserialize singleton");
    }
    
    // Static method to initialize the instance eagerly
    private static function initializeInstance()
    {
        if (self::$instance === null) {
            self::$instance = new self();
        }
    }
    
    // Public method to get the instance
    public static function getInstance()
    {
        self::initializeInstance();
        return self::$instance;
    }
    
    // Example method to demonstrate functionality
    public function doSomething()
    {
        echo "EagerSingleton is doing something...\n";
    }
}

// Simulate eager initialization by calling getInstance during class loading
// This ensures the instance is created as soon as the class is first referenced
EagerSingleton::getInstance();