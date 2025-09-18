import { Document } from "./Document";

/**
 * DocumentRegistry - Registry for managing document prototypes
 * Demonstrates the Prototype pattern with a registry
 */
export class DocumentRegistry {
  private prototypes: Map<string, Document> = new Map();

  /**
   * Registers a document prototype
   */
  register(key: string, prototype: Document): void {
    this.prototypes.set(key, prototype);
  }

  /**
   * Creates a clone from a registered prototype
   */
  createDocument(key: string): Document | null {
    const prototype = this.prototypes.get(key);
    return prototype ? prototype.clone() : null;
  }

  /**
   * Gets all registered prototype keys
   */
  getAvailableTypes(): string[] {
    return Array.from(this.prototypes.keys());
  }

  /**
   * Gets information about a specific prototype
   */
  getPrototypeInfo(key: string): string | null {
    const prototype = this.prototypes.get(key);
    return prototype ? prototype.getSummary() : null;
  }
}
