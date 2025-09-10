<?php

// Include example class
require_once 'DatabaseConnection.php';

/**
 * Main class to demonstrate Singleton design pattern with real-world example
 * 
 * This class shows how to use the DatabaseConnection Singleton pattern
 * and demonstrates that only one instance is created.
 */
class Main
{
    public static function run()
    {
        echo "=== Singleton Design Pattern Demo ===\n\n";
        
        // Test Database Connection Singleton
        echo "Testing Database Connection Singleton:\n";
        $db1 = DatabaseConnection::getInstance();
        $db2 = DatabaseConnection::getInstance();
        
        echo "db1 === db2: " . ($db1 === $db2 ? 'true' : 'false') . "\n";
        echo "Connection String: " . $db1->getConnectionString() . "\n";
        
        // Demonstrate database operations
        $db1->connect();
        $db1->executeQuery("SELECT * FROM users");
        $db2->executeQuery("SELECT * FROM products"); // Same instance
        $db1->disconnect();
        
        // Try to execute query after disconnect
        $db2->executeQuery("SELECT * FROM orders");
        
        echo "\n=== Demo Complete ===\n";
    }
}

// Run the demo
Main::run();