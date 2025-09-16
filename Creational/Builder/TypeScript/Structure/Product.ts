/**
 * Product - Represents the complex object being built
 * Contains all the parts that can be assembled
 */
export class Product {
  private parts: string[] = [];

  /**
   * Adds a part to the product
   */
  addPart(part: string): void {
    this.parts.push(part);
  }

  /**
   * Lists all parts of the product
   */
  listParts(): string {
    return `Product parts: ${this.parts.join(", ")}`;
  }

  /**
   * Gets the number of parts
   */
  getPartCount(): number {
    return this.parts.length;
  }

  /**
   * Gets all parts as an array
   */
  getParts(): string[] {
    return [...this.parts];
  }

  /**
   * Clears all parts (for resetting)
   */
  clear(): void {
    this.parts = [];
  }

  /**
   * String representation of the product
   */
  toString(): string {
    return `Product(${this.parts.join(", ")})`;
  }
}
