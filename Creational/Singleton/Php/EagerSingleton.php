<?php

/**
 * Eager Singleton Implementation
 * 
 * This implementation creates the instance at class loading time.
 * In PHP, this is simulated by using a static variable with initialization.
 */
class EagerSingleton
{
    private static $instance = null;
    private static $initialized = false;
    
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
        throw new Exception("Cannot unserialize a singleton.");
    }
    
    // Static initialization (simulating eager loading)
    private static function initialize()
    {
        if (!self::$initialized) {
            self::$instance = new self();
            self::$initialized = true;
        }
    }
    
    // Public method to get the instance
    public static function getInstance()
    {
        if (self::$instance === null) {
            self::initialize();
        }
        return self::$instance;
    }
    
    // Example method to demonstrate functionality
    public function doSomething()
    {
        echo "EagerSingleton is doing something...\n";
    }
}

// Initialize the eager singleton when the class is loaded
EagerSingleton::getInstance();