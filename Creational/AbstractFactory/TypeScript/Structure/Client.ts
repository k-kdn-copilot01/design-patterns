import { AbstractFactory } from "./AbstractFactory";
import { AbstractProductA } from "./AbstractProductA";
import { AbstractProductB } from "./AbstractProductB";

/**
 * Client - Uses AbstractFactory to create and work with product families
 * Demonstrates the Abstract Factory pattern usage
 */
export class Client {
  private factory: AbstractFactory;

  constructor(factory: AbstractFactory) {
    this.factory = factory;
  }

  /**
   * Sets a new factory
   */
  setFactory(factory: AbstractFactory): void {
    this.factory = factory;
  }

  /**
   * Gets the current factory
   */
  getFactory(): AbstractFactory {
    return this.factory;
  }

  /**
   * Creates and works with a product family
   * @returns Result of working with the product family
   */
  workWithProductFamily(): string {
    const productA = this.factory.createProductA();
    const productB = this.factory.createProductB();

    let result = `Working with ${this.factory.getFamilyName()}:\n`;
    result += `- Product A: ${productA.operationA()}\n`;
    result += `- Product B: ${productB.operationB()}\n`;
    result += `- Collaboration: ${productB.collaborateWith(productA)}\n`;
    result += `- Family consistency: ${
      productA.getFamily() === productB.getFamily() ? "✓" : "✗"
    }`;

    return result;
  }

  /**
   * Creates multiple product families and compares them
   * @param factories - Array of factories to use
   * @returns Comparison result
   */
  static compareFactories(factories: AbstractFactory[]): string {
    let result = "Factory Comparison:\n\n";

    factories.forEach((factory, index) => {
      const client = new Client(factory);
      result += `--- Factory ${index + 1}: ${factory.getFamilyName()} ---\n`;
      result += client.workWithProductFamily();
      result += "\n\n";
    });

    return result;
  }

  /**
   * Demonstrates product family consistency
   * @returns Consistency check result
   */
  checkFamilyConsistency(): string {
    const productA = this.factory.createProductA();
    const productB = this.factory.createProductB();

    const familyA = productA.getFamily();
    const familyB = productB.getFamily();
    const isConsistent = familyA === familyB;

    return `Family Consistency Check:
- Product A family: ${familyA}
- Product B family: ${familyB}
- Consistent: ${isConsistent ? "✓ Yes" : "✗ No"}`;
  }
}
