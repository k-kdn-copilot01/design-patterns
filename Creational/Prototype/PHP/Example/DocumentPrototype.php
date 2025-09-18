<?php

require_once '../Structure/Prototype.php';

class DocumentPrototype implements Prototype
{
    private string $title;
    private string $content;
    private array $metadata;
    private DocumentSettings $settings;

    public function __construct(string $title, string $content, array $metadata, DocumentSettings $settings)
    {
        $this->title = $title;
        $this->content = $content;
        $this->metadata = $metadata;
        $this->settings = $settings;
    }

    public function clone(): DocumentPrototype
    {
        $cloned = clone $this;
        
        // Deep copy cho metadata array
        $cloned->metadata = [];
        foreach ($this->metadata as $key => $value) {
            if (is_object($value)) {
                $cloned->metadata[$key] = clone $value;
            } else {
                $cloned->metadata[$key] = $value;
            }
        }
        
        // Deep copy cho settings object
        $cloned->settings = clone $this->settings;
        
        return $cloned;
    }

    public function getTitle(): string
    {
        return $this->title;
    }

    public function setTitle(string $title): void
    {
        $this->title = $title;
    }

    public function getContent(): string
    {
        return $this->content;
    }

    public function setContent(string $content): void
    {
        $this->content = $content;
    }

    public function getMetadata(): array
    {
        return $this->metadata;
    }

    public function setMetadata(array $metadata): void
    {
        $this->metadata = $metadata;
    }

    public function getSettings(): DocumentSettings
    {
        return $this->settings;
    }

    public function setSettings(DocumentSettings $settings): void
    {
        $this->settings = $settings;
    }

    public function getInfo(): string
    {
        return sprintf(
            "Document: %s\nContent: %s\nMetadata: %s\nSettings: %s",
            $this->title,
            substr($this->content, 0, 50) . '...',
            json_encode($this->metadata),
            $this->settings->getInfo()
        );
    }
}
