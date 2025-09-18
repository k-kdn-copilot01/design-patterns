<?php

declare(strict_types=1);

require_once __DIR__ . '/Product.php';
require_once __DIR__ . '/Builder.php';

class ConcreteBuilder implements Builder
{
    private Product $product;

    public function __construct()
    {
        $this->reset();
    }

    public function reset(): void
    {
        $this->product = new Product();
    }

    public function buildPartA(): void
    {
        $this->product->addPart('PartA');
    }

    public function buildPartB(): void
    {
        $this->product->addPart('PartB');
    }

    public function buildPartC(): void
    {
        $this->product->addPart('PartC');
    }

    public function getProduct(): Product
    {
        $result = $this->product;
        $this->reset();
        return $result;
    }
}


