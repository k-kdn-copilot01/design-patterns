import { Builder } from "./Builder";

/**
 * ConcreteBuilder2 - Another concrete implementation of Builder
 * Implements different construction steps for Product type 2
 */
export class ConcreteBuilder2 extends Builder {
  /**
   * Builds part A for Product type 2
   */
  buildPartA(): void {
    this.product.addPart("PartA2");
  }

  /**
   * Builds part B for Product type 2
   */
  buildPartB(): void {
    this.product.addPart("PartB2");
  }

  /**
   * Builds part C for Product type 2
   */
  buildPartC(): void {
    this.product.addPart("PartC2");
  }
}
