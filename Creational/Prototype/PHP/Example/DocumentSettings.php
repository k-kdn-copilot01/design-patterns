<?php

/**
 * DocumentSettings class
 * Cấu hình cho tài liệu
 */
class DocumentSettings
{
    private string $fontFamily;
    private int $fontSize;
    private string $theme;
    private bool $isPublic;
    private array $tags;

    public function __construct(string $fontFamily, int $fontSize, string $theme, bool $isPublic, array $tags = [])
    {
        $this->fontFamily = $fontFamily;
        $this->fontSize = $fontSize;
        $this->theme = $theme;
        $this->isPublic = $isPublic;
        $this->tags = $tags;
    }

    public function getFontFamily(): string
    {
        return $this->fontFamily;
    }

    public function setFontFamily(string $fontFamily): void
    {
        $this->fontFamily = $fontFamily;
    }

    public function getFontSize(): int
    {
        return $this->fontSize;
    }

    public function setFontSize(int $fontSize): void
    {
        $this->fontSize = $fontSize;
    }

    public function getTheme(): string
    {
        return $this->theme;
    }

    public function setTheme(string $theme): void
    {
        $this->theme = $theme;
    }

    public function isPublic(): bool
    {
        return $this->isPublic;
    }

    public function setIsPublic(bool $isPublic): void
    {
        $this->isPublic = $isPublic;
    }

    public function getTags(): array
    {
        return $this->tags;
    }

    public function setTags(array $tags): void
    {
        $this->tags = $tags;
    }

    public function addTag(string $tag): void
    {
        if (!in_array($tag, $this->tags)) {
            $this->tags[] = $tag;
        }
    }

    public function getInfo(): string
    {
        return sprintf(
            "Font: %s (%dpx), Theme: %s, Public: %s, Tags: %s",
            $this->fontFamily,
            $this->fontSize,
            $this->theme,
            $this->isPublic ? 'Yes' : 'No',
            implode(', ', $this->tags)
        );
    }
}
