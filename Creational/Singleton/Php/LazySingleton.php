<?php

/**
 * Lazy Singleton Implementation
 * 
 * This implementation creates the instance only when it's first needed.
 * Warning: This is NOT thread-safe and should only be used in single-threaded environments.
 */
class LazySingleton
{
    private static $instance = null;
    
    // Private constructor to prevent external instantiation
    private function __construct()
    {
        echo "LazySingleton instance created\n";
    }
    
    // Prevent cloning of the instance
    private function __clone() {}
    
    // Prevent unserializing of the instance
    public function __wakeup()
    {
        throw new Exception("Cannot unserialize a singleton.");
    }
    
    // Public method to get the instance (lazy initialization)
    public static function getInstance()
    {
        if (self::$instance === null) {
            self::$instance = new self();
        }
        return self::$instance;
    }
    
    // Example method to demonstrate functionality
    public function doSomething()
    {
        echo "LazySingleton is doing something...\n";
    }
}