<?php

declare(strict_types=1);

require_once __DIR__ . '/Director.php';
require_once __DIR__ . '/ConcreteBuilder.php';

class Client
{
    public function run(): void
    {
        $director = new Director();
        $builder = new ConcreteBuilder();
        $director->setBuilder($builder);

        $director->buildMinimalViableProduct();
        $product1 = $builder->getProduct();

        $director->buildFullFeaturedProduct();
        $product2 = $builder->getProduct();

        $builder->reset();
        $builder->buildPartA();
        $builder->buildPartC();
        $product3 = $builder->getProduct();
        // Values are returned to the caller via products above
    }
}


