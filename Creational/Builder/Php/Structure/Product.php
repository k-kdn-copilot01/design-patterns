<?php

declare(strict_types=1);

class Product
{
    /** @var string[] */
    private array $parts = [];

    public function addPart(string $part): void
    {
        $this->parts[] = $part;
    }

    /**
     * Returns a comma-separated list of built parts.
     */
    public function listParts(): string
    {
        return implode(', ', $this->parts);
    }
}


