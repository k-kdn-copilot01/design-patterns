import { Document } from "./Document";

/**
 * ReportDocument - Concrete implementation of Document
 * Represents a report document that can be cloned
 */
export class ReportDocument extends Document {
  public sections: Array<{ title: string; content: string }>;
  public attachments: string[];
  public reportType: string;

  constructor(
    title: string = "",
    content: string = "",
    author: string = "",
    reportType: string = "General"
  ) {
    super(title, content, author);
    this.sections = [];
    this.attachments = [];
    this.reportType = reportType;
  }

  /**
   * Creates a deep clone of this report document
   */
  clone(): ReportDocument {
    const cloned = new ReportDocument(
      this.title,
      this.content,
      this.metadata.author,
      this.reportType
    );

    // Deep clone metadata
    cloned.metadata = {
      author: this.metadata.author,
      createdAt: new Date(this.metadata.createdAt.getTime()),
      lastModified: new Date(this.metadata.lastModified.getTime()),
      version: this.metadata.version,
    };

    // Deep clone arrays
    cloned.tags = [...this.tags];
    cloned.sections = this.sections.map((section) => ({
      title: section.title,
      content: section.content,
    }));
    cloned.attachments = [...this.attachments];

    return cloned;
  }

  /**
   * Adds a new section to the report
   */
  addSection(title: string, content: string): void {
    this.sections.push({ title, content });
    this.updateLastModified();
  }

  /**
   * Adds an attachment to the report
   */
  addAttachment(filename: string): void {
    if (!this.attachments.includes(filename)) {
      this.attachments.push(filename);
      this.updateLastModified();
    }
  }

  /**
   * Gets detailed report information
   */
  getDetailedInfo(): string {
    return `${this.getSummary()}\nReport Type: ${this.reportType}\nSections: ${
      this.sections.length
    }\nAttachments: ${this.attachments.length}`;
  }
}
