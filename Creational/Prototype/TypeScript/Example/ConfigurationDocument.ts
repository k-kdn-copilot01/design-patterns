import { Document } from "./Document";

/**
 * ConfigurationDocument - Concrete implementation of Document
 * Represents a configuration document that can be cloned
 */
export class ConfigurationDocument extends Document {
  public settings: Map<string, any>;
  public environment: string;
  public dependencies: string[];

  constructor(
    title: string = "",
    content: string = "",
    author: string = "",
    environment: string = "development"
  ) {
    super(title, content, author);
    this.settings = new Map();
    this.dependencies = [];
    this.environment = environment;
  }

  /**
   * Creates a deep clone of this configuration document
   */
  clone(): ConfigurationDocument {
    const cloned = new ConfigurationDocument(
      this.title,
      this.content,
      this.metadata.author,
      this.environment
    );

    // Deep clone metadata
    cloned.metadata = {
      author: this.metadata.author,
      createdAt: new Date(this.metadata.createdAt.getTime()),
      lastModified: new Date(this.metadata.lastModified.getTime()),
      version: this.metadata.version,
    };

    // Deep clone arrays and maps
    cloned.tags = [...this.tags];
    cloned.dependencies = [...this.dependencies];
    cloned.settings = new Map(this.settings);

    return cloned;
  }

  /**
   * Sets a configuration setting
   */
  setSetting(key: string, value: any): void {
    this.settings.set(key, value);
    this.updateLastModified();
  }

  /**
   * Gets a configuration setting
   */
  getSetting(key: string): any {
    return this.settings.get(key);
  }

  /**
   * Adds a dependency
   */
  addDependency(dependency: string): void {
    if (!this.dependencies.includes(dependency)) {
      this.dependencies.push(dependency);
      this.updateLastModified();
    }
  }

  /**
   * Gets detailed configuration information
   */
  getDetailedInfo(): string {
    const settingsStr = Array.from(this.settings.entries())
      .map(([key, value]) => `${key}: ${JSON.stringify(value)}`)
      .join(", ");
    return `${this.getSummary()}\nEnvironment: ${
      this.environment
    }\nDependencies: [${this.dependencies.join(
      ", "
    )}]\nSettings: {${settingsStr}}`;
  }
}
