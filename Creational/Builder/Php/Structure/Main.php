<?php

declare(strict_types=1);

require_once __DIR__ . '/Director.php';
require_once __DIR__ . '/ConcreteBuilder.php';

class Main
{
    public static function run(): void
    {
        echo "=== Structure Demo: Builder Pattern ===\n\n";

        $director = new Director();
        $builder = new ConcreteBuilder();
        $director->setBuilder($builder);

        echo "Building Minimal Viable Product...\n";
        $director->buildMinimalViableProduct();
        $product1 = $builder->getProduct();
        echo "Product parts: " . $product1->listParts() . "\n\n";

        echo "Building Full Featured Product...\n";
        $director->buildFullFeaturedProduct();
        $product2 = $builder->getProduct();
        echo "Product parts: " . $product2->listParts() . "\n\n";

        echo "Custom build (no Director, client-defined steps)...\n";
        $builder->reset();
        $builder->buildPartA();
        $builder->buildPartC();
        $product3 = $builder->getProduct();
        echo "Product parts: " . $product3->listParts() . "\n";

        echo "\n=== Structure Demo Complete ===\n";
    }
}

Main::run();


