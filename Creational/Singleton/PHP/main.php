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

echo "\n=== Demo Complete ===\n";