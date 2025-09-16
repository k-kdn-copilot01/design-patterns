import { Document } from "./Document";
import { DocumentRegistry } from "./DocumentRegistry";

/**
 * DocumentManager - Client that uses Document prototypes
 * Demonstrates the Prototype pattern usage in real-world scenario
 */
export class DocumentManager {
  private registry: DocumentRegistry;
  private documents: Document[] = [];

  constructor(registry: DocumentRegistry) {
    this.registry = registry;
  }

  /**
   * Creates a new document from a prototype
   */
  createDocument(type: string, customTitle?: string): Document | null {
    const document = this.registry.createDocument(type);
    if (document && customTitle) {
      document.title = customTitle;
    }
    if (document) {
      this.documents.push(document);
    }
    return document;
  }

  /**
   * Creates multiple documents of the same type
   */
  createMultipleDocuments(
    type: string,
    count: number,
    baseTitle: string
  ): Document[] {
    const documents: Document[] = [];
    for (let i = 1; i <= count; i++) {
      const document = this.registry.createDocument(type);
      if (document) {
        document.title = `${baseTitle} ${i}`;
        this.documents.push(document);
        documents.push(document);
      }
    }
    return documents;
  }

  /**
   * Gets all documents
   */
  getAllDocuments(): Document[] {
    return [...this.documents];
  }

  /**
   * Gets documents by type
   */
  getDocumentsByType(type: string): Document[] {
    return this.documents.filter((doc) => doc.constructor.name === type);
  }

  /**
   * Gets document statistics
   */
  getStatistics(): string {
    const total = this.documents.length;
    const byType = this.documents.reduce((acc, doc) => {
      const type = doc.constructor.name;
      acc[type] = (acc[type] || 0) + 1;
      return acc;
    }, {} as Record<string, number>);

    let stats = `Total documents: ${total}\n`;
    stats += "Documents by type:\n";
    Object.entries(byType).forEach(([type, count]) => {
      stats += `- ${type}: ${count}\n`;
    });

    return stats;
  }
}
