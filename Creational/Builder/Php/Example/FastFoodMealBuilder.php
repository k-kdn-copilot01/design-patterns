<?php

declare(strict_types=1);

require_once __DIR__ . '/MealBuilder.php';

class FastFoodMealBuilder implements MealBuilder
{
    private Meal $meal;

    public function __construct()
    {
        $this->reset();
    }

    public function reset(): void
    {
        $this->meal = new Meal();
    }

    public function addMain(string $name = 'Burger'): void
    {
        $this->meal->setMainDish($name);
    }

    public function addSide(string $name = 'Fries'): void
    {
        $this->meal->setSideDish($name);
    }

    public function addDrink(string $name = 'Soda'): void
    {
        $this->meal->setDrink($name);
    }

    public function getMeal(): Meal
    {
        $result = $this->meal;
        $this->reset();
        return $result;
    }
}


