<?php

declare(strict_types=1);

require_once __DIR__ . '/Builder.php';

class Director
{
    private Builder $builder;

    public function setBuilder(Builder $builder): void
    {
        $this->builder = $builder;
    }

    public function buildMinimalViableProduct(): void
    {
        $this->builder->reset();
        $this->builder->buildPartA();
    }

    public function buildFullFeaturedProduct(): void
    {
        $this->builder->reset();
        $this->builder->buildPartA();
        $this->builder->buildPartB();
        $this->builder->buildPartC();
    }
}


