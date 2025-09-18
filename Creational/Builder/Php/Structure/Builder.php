<?php

declare(strict_types=1);

interface Builder
{
    public function reset(): void;
    public function buildPartA(): void;
    public function buildPartB(): void;
    public function buildPartC(): void;
    public function getProduct(): Product;
}


