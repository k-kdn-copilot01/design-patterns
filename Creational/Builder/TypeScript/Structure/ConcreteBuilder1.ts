import { Builder } from "./Builder";

/**
 * ConcreteBuilder1 - Concrete implementation of Builder
 * Implements specific construction steps for Product type 1
 */
export class ConcreteBuilder1 extends Builder {
  /**
   * Builds part A for Product type 1
   */
  buildPartA(): void {
    this.product.addPart("PartA1");
  }

  /**
   * Builds part B for Product type 1
   */
  buildPartB(): void {
    this.product.addPart("PartB1");
  }

  /**
   * Builds part C for Product type 1
   */
  buildPartC(): void {
    this.product.addPart("PartC1");
  }
}
