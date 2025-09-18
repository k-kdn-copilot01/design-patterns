<?php

declare(strict_types=1);

require_once __DIR__ . '/Meal.php';
require_once __DIR__ . '/MealBuilder.php';
require_once __DIR__ . '/HealthyMealBuilder.php';
require_once __DIR__ . '/FastFoodMealBuilder.php';
require_once __DIR__ . '/MealDirector.php';

class Main
{
    public static function run(): void
    {
        echo "=== Example Demo: Builder Pattern (Meal) ===\n\n";

        $director = new MealDirector();

        echo "1) Healthy Meal via Director (Standard)\n";
        $healthyBuilder = new HealthyMealBuilder();
        $director->setBuilder($healthyBuilder);
        $director->buildStandardMeal();
        $healthyMeal = $healthyBuilder->getMeal();
        echo $healthyMeal->describe() . "\n\n";

        echo "2) Fast Food Kids Meal via Director\n";
        $fastFoodBuilder = new FastFoodMealBuilder();
        $director->setBuilder($fastFoodBuilder);
        $director->buildKidsMeal();
        $kidsMeal = $fastFoodBuilder->getMeal();
        echo $kidsMeal->describe() . "\n\n";

        echo "3) Custom Healthy Meal (Client-defined)\n";
        $healthyBuilder->reset();
        $healthyBuilder->addMain('Grilled Salmon');
        $healthyBuilder->addSide('Quinoa');
        $healthyBuilder->addDrink('Green Tea');
        $customHealthy = $healthyBuilder->getMeal();
        echo $customHealthy->describe() . "\n\n";

        echo "=== Example Demo Complete ===\n";
    }
}

Main::run();


