<?php

declare(strict_types=1);

class Meal
{
    private string $mainDish = '';
    private string $sideDish = '';
    private string $drink = '';

    public function setMainDish(string $mainDish): void
    {
        $this->mainDish = $mainDish;
    }

    public function setSideDish(string $sideDish): void
    {
        $this->sideDish = $sideDish;
    }

    public function setDrink(string $drink): void
    {
        $this->drink = $drink;
    }

    public function describe(): string
    {
        $parts = [];
        if ($this->mainDish !== '') $parts[] = "Main: {$this->mainDish}";
        if ($this->sideDish !== '') $parts[] = "Side: {$this->sideDish}";
        if ($this->drink !== '') $parts[] = "Drink: {$this->drink}";
        return implode(', ', $parts);
    }
}


