<?php

declare(strict_types=1);

require_once __DIR__ . '/Meal.php';

interface MealBuilder
{
    public function reset(): void;
    public function addMain(string $name): void;
    public function addSide(string $name): void;
    public function addDrink(string $name): void;
    public function getMeal(): Meal;
}


