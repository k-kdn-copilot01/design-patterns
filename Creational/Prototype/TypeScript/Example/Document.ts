/**
 * Document - Abstract base class for all document types
 * Represents the Prototype interface for document cloning
 */
export abstract class Document {
  public title: string;
  public content: string;
  public metadata: {
    author: string;
    createdAt: Date;
    lastModified: Date;
    version: number;
  };
  public tags: string[];

  constructor(
    title: string = "",
    content: string = "",
    author: string = "",
    version: number = 1
  ) {
    this.title = title;
    this.content = content;
    this.metadata = {
      author,
      createdAt: new Date(),
      lastModified: new Date(),
      version,
    };
    this.tags = [];
  }

  /**
   * Abstract clone method - must be implemented by subclasses
   */
  abstract clone(): Document;

  /**
   * Updates the last modified timestamp
   */
  protected updateLastModified(): void {
    this.metadata.lastModified = new Date();
  }

  /**
   * Adds a tag to the document
   */
  addTag(tag: string): void {
    if (!this.tags.includes(tag)) {
      this.tags.push(tag);
      this.updateLastModified();
    }
  }

  /**
   * Removes a tag from the document
   */
  removeTag(tag: string): void {
    const index = this.tags.indexOf(tag);
    if (index > -1) {
      this.tags.splice(index, 1);
      this.updateLastModified();
    }
  }

  /**
   * Updates the document content
   */
  updateContent(newContent: string): void {
    this.content = newContent;
    this.updateLastModified();
  }

  /**
   * Gets document summary
   */
  getSummary(): string {
    return `Title: ${this.title}\nAuthor: ${this.metadata.author}\nVersion: ${
      this.metadata.version
    }\nTags: [${this.tags.join(", ")}]`;
  }
}
