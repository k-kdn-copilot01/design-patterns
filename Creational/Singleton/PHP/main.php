<?php

/**
 * Main script to demonstrate all Singleton implementations
 * 
 * This script shows how to use each type of Singleton pattern
 * and demonstrates that only one instance is created for each type.
 */

// Include all singleton classes
require_once 'LazySingleton.php';
require_once 'EagerSingleton.php';
require_once 'DatabaseConnection.php';

echo "=== Singleton Design Pattern Demo ===\n\n";

// Test Lazy Singleton
echo "1. Testing Lazy Singleton:\n";
$lazy1 = LazySingleton::getInstance();
$lazy2 = LazySingleton::getInstance();

echo "lazy1 === lazy2: " . ($lazy1 === $lazy2 ? "true" : "false") . "\n";
$lazy1->doSomething();
echo "\n";

// Test Eager Singleton
echo "2. Testing Eager Singleton:\n";
$eager1 = EagerSingleton::getInstance();
$eager2 = EagerSingleton::getInstance();

echo "eager1 === eager2: " . ($eager1 === $eager2 ? "true" : "false") . "\n";
$eager1->doSomething();
echo "\n";

// Test Database Connection Singleton
echo "3. Testing Database Connection Singleton:\n";
$db1 = DatabaseConnection::getInstance();
$db2 = DatabaseConnection::getInstance();

echo "db1 === db2: " . ($db1 === $db2 ? "true" : "false") . "\n";
echo "Connection String: " . $db1->getConnectionString() . "\n";

// Demonstrate database operations
$db1->connect();
$db1->executeQuery("SELECT * FROM users");
$db2->executeQuery("SELECT * FROM products"); // Same instance
$db1->disconnect();

// Try to execute query after disconnect
$db2->executeQuery("SELECT * FROM orders");

echo "\n=== Demo Complete ===\n";