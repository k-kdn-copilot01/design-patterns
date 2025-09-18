<?php

declare(strict_types=1);

require_once __DIR__ . '/MealBuilder.php';

class MealDirector
{
    private MealBuilder $builder;

    public function setBuilder(MealBuilder $builder): void
    {
        $this->builder = $builder;
    }

    public function buildStandardMeal(): void
    {
        $this->builder->reset();
        $this->builder->addMain('Standard Main');
        $this->builder->addSide('Standard Side');
        $this->builder->addDrink('Standard Drink');
    }

    public function buildKidsMeal(): void
    {
        $this->builder->reset();
        $this->builder->addMain('Small Burger');
        $this->builder->addSide('Small Fries');
        $this->builder->addDrink('Juice');
    }
}


