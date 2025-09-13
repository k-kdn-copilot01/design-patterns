<?php

/**
 * DocumentMetadata class to demonstrate deep cloning of nested objects
 */
class DocumentMetadata
{
    private DateTime $createdAt;
    private DateTime $lastModified;
    private int $version;
    private string $status;
    
    public function __construct()
    {
        $this->createdAt = new DateTime();
        $this->lastModified = new DateTime();
        $this->version = 1;
        $this->status = "Draft";
    }
    
    public function clone(): DocumentMetadata
    {
        $clone = new self();
        $clone->createdAt = clone $this->createdAt; // Deep copy DateTime
        $clone->lastModified = new DateTime(); // Set new modification time for clone
        $clone->version = 1; // Reset version for clone
        $clone->status = $this->status;
        return $clone;
    }
    
    public function incrementVersion(): void
    {
        $this->version++;
        $this->lastModified = new DateTime();
    }
    
    public function setStatus(string $status): void
    {
        $this->status = $status;
        $this->lastModified = new DateTime();
    }
    
    public function getInfo(): string
    {
        return sprintf(
            "Metadata[version=%d, status='%s', created=%s]",
            $this->version,
            $this->status,
            $this->createdAt->format('Y-m-d H:i:s')
        );
    }
    
    public function getVersion(): int
    {
        return $this->version;
    }
    
    public function getStatus(): string
    {
        return $this->status;
    }
}