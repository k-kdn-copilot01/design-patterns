import { Builder } from "./Builder";
import { Product } from "./Product";

/**
 * Director - Controls the construction process
 * Defines the order of construction steps
 */
export class Director {
  private builder: Builder | null = null;

  /**
   * Sets the builder to use
   */
  setBuilder(builder: Builder): void {
    this.builder = builder;
  }

  /**
   * Builds a minimal product (only part A)
   */
  buildMinimalProduct(): Product {
    if (!this.builder) {
      throw new Error("Builder not set");
    }
    this.builder.reset();
    this.builder.buildPartA();
    return this.builder.getProduct();
  }

  /**
   * Builds a full product (all parts)
   */
  buildFullProduct(): Product {
    if (!this.builder) {
      throw new Error("Builder not set");
    }
    this.builder.reset();
    this.builder.buildPartA();
    this.builder.buildPartB();
    this.builder.buildPartC();
    return this.builder.getProduct();
  }

  /**
   * Builds a custom product with specific parts
   */
  buildCustomProduct(parts: ("A" | "B" | "C")[]): Product {
    if (!this.builder) {
      throw new Error("Builder not set");
    }
    this.builder.reset();

    parts.forEach((part) => {
      switch (part) {
        case "A":
          this.builder!.buildPartA();
          break;
        case "B":
          this.builder!.buildPartB();
          break;
        case "C":
          this.builder!.buildPartC();
          break;
      }
    });

    return this.builder.getProduct();
  }
}
