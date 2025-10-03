<?php

// Singleton

class Logger
{
    private static $instance = null;

    private function __construct()
    {
      
    }

    public static function getInstance()
    {
        if (self::$instance === null) {
            self::$instance = new Logger();
        }
        return self::$instance;
    }

    public function log($message)
    {
        echo $message . PHP_EOL;
    }
}

$logger1 = Logger::getInstance();
$logger2 = Logger::getInstance();
$logger1->log("This is a log message.");
$logger2->log("This is another log message.");

?>