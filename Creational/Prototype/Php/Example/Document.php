<?php

/**
 * Document represents a prototype for cloning documents
 * with various properties and content
 */
class Document implements Prototype
{
    private string $title;
    private string $content;
    private string $author;
    private array $tags;
    private DocumentMetadata $metadata;
    
    public function __construct(string $title, string $content, string $author)
    {
        $this->title = $title;
        $this->content = $content;
        $this->author = $author;
        $this->tags = [];
        $this->metadata = new DocumentMetadata();
        echo "Document created: {$title}\n";
    }
    
    public function clone(): Prototype
    {
        $clone = new self($this->title . " (Copy)", $this->content, $this->author);
        $clone->tags = array_merge([], $this->tags); // Deep copy of tags
        $clone->metadata = $this->metadata->clone(); // Deep copy of metadata
        echo "Document cloned: {$clone->title}\n";
        return $clone;
    }
    
    public function getInfo(): string
    {
        return sprintf(
            "Document[title='%s', author='%s', tags=%s, %s]",
            $this->title,
            $this->author,
            json_encode($this->tags),
            $this->metadata->getInfo()
        );
    }
    
    public function addTag(string $tag): void
    {
        $this->tags[] = $tag;
    }
    
    public function setContent(string $content): void
    {
        $this->content = $content;
        $this->metadata->incrementVersion();
    }
    
    public function getTitle(): string
    {
        return $this->title;
    }
    
    public function getContent(): string
    {
        return $this->content;
    }
    
    public function getTags(): array
    {
        return $this->tags;
    }
    
    public function getMetadata(): DocumentMetadata
    {
        return $this->metadata;
    }
}