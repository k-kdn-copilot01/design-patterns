<?php

require_once 'Prototype.php';

class Client
{
    private Prototype $prototype;

    public function __construct(Prototype $prototype)
    {
        $this->prototype = $prototype;
    }

    public function createClone(): Prototype
    {
        return $this->prototype->clone();
    }

    public function createMultipleClones(int $count): array
    {
        $clones = [];
        for ($i = 0; $i < $count; $i++) {
            $clones[] = $this->createClone();
        }
        return $clones;
    }
}
