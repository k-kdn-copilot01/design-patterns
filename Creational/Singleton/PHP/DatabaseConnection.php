<?php

/**
 * DatabaseConnection - Real-world Singleton Example
 * 
 * This demonstrates a practical use case for Singleton pattern:
 * Managing a single database connection throughout the application.
 * In PHP web applications, this is commonly used for PDO connections.
 */
class DatabaseConnection
{
    private static $instance = null;
    private $connectionString;
    private $isConnected;
    
    // Private constructor to prevent external instantiation
    private function __construct()
    {
        $this->connectionString = "mysql:host=localhost;dbname=mydb;charset=utf8";
        $this->isConnected = false;
        echo "DatabaseConnection instance created\n";
    }
    
    // Prevent cloning of the instance
    private function __clone() {}
    
    // Prevent unserializing of the instance
    public function __wakeup() 
    {
        throw new \Exception("Cannot unserialize singleton");
    }
    
    // Thread-safe lazy initialization (PHP is single-threaded per request)
    public static function getInstance()
    {
        if (self::$instance === null) {
            self::$instance = new self();
        }
        return self::$instance;
    }
    
    // Connect to database
    public function connect()
    {
        if (!$this->isConnected) {
            echo "Connecting to database: " . $this->connectionString . "\n";
            $this->isConnected = true;
            echo "Database connection established\n";
        } else {
            echo "Already connected to database\n";
        }
    }
    
    // Disconnect from database
    public function disconnect()
    {
        if ($this->isConnected) {
            echo "Disconnecting from database\n";
            $this->isConnected = false;
            echo "Database connection closed\n";
        } else {
            echo "No active database connection\n";
        }
    }
    
    // Execute a query (simulated)
    public function executeQuery($query)
    {
        if ($this->isConnected) {
            echo "Executing query: " . $query . "\n";
            echo "Query executed successfully\n";
        } else {
            echo "Error: No database connection. Please connect first.\n";
        }
    }
    
    // Get connection status
    public function isConnected()
    {
        return $this->isConnected;
    }
    
    // Get connection string
    public function getConnectionString()
    {
        return $this->connectionString;
    }
}