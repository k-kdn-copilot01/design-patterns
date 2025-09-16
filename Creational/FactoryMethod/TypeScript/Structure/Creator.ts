import { Product } from "./Product";

/**
 * Creator - Abstract base class for all creators
 * Declares the factory method that returns Product objects
 */
export abstract class Creator {
  /**
   * Factory method - creates Product objects
   * Subclasses must implement this method to return specific Product instances
   */
  abstract factoryMethod(): Product;

  /**
   * Template method that uses the factory method
   * Can contain common logic that works with Product objects
   */
  someOperation(): string {
    const product = this.factoryMethod();
    return `Creator: ${product.operation()}`;
  }
}
