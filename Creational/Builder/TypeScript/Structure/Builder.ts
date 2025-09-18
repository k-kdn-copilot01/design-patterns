import { Product } from "./Product";

/**
 * Builder - Abstract interface for creating products
 * Defines the contract for building complex objects step by step
 */
export abstract class Builder {
  protected product: Product = new Product();

  /**
   * Resets the builder to start fresh
   */
  reset(): void {
    this.product = new Product();
  }

  /**
   * Returns the built product
   */
  getProduct(): Product {
    const result = this.product;
    this.reset(); // Reset for next build
    return result;
  }

  /**
   * Abstract methods that concrete builders must implement
   */
  abstract buildPartA(): void;
  abstract buildPartB(): void;
  abstract buildPartC(): void;
}
