<?php

require_once '../Structure/Prototype.php';
require_once 'DocumentPrototype.php';

class DocumentManager
{
    private array $templates = [];

    public function registerTemplate(string $name, Prototype $prototype): void
    {
        $this->templates[$name] = $prototype;
    }

    public function createDocument(string $templateName): ?Prototype
    {
        if (!isset($this->templates[$templateName])) {
            return null;
        }

        return $this->templates[$templateName]->clone();
    }

    public function createMultipleDocuments(string $templateName, int $count): array
    {
        $documents = [];
        for ($i = 0; $i < $count; $i++) {
            $documents[] = $this->createDocument($templateName);
        }
        return $documents;
    }

    public function getAvailableTemplates(): array
    {
        return array_keys($this->templates);
    }
}
