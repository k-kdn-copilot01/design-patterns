import { Director } from "./Director";
import { Builder } from "./Builder";
import { Product } from "./Product";

/**
 * Client - Uses Director and Builder to create products
 * Demonstrates the Builder pattern usage
 */
export class Client {
  private director: Director;

  constructor() {
    this.director = new Director();
  }

  /**
   * Creates a product using the specified builder
   * @param builder - The builder to use
   * @param productType - Type of product to build
   * @returns The built product
   */
  createProduct(
    builder: Builder,
    productType: "minimal" | "full" | "custom",
    customParts?: ("A" | "B" | "C")[]
  ): Product {
    this.director.setBuilder(builder);

    switch (productType) {
      case "minimal":
        return this.director.buildMinimalProduct();
      case "full":
        return this.director.buildFullProduct();
      case "custom":
        if (!customParts) {
          throw new Error(
            "Custom parts must be provided for custom product type"
          );
        }
        return this.director.buildCustomProduct(customParts);
      default:
        throw new Error(`Unknown product type: ${productType}`);
    }
  }

  /**
   * Demonstrates building multiple products with different builders
   * @param builders - Array of builders to use
   * @returns Array of built products
   */
  createMultipleProducts(builders: Builder[]): Product[] {
    const products: Product[] = [];

    builders.forEach((builder, index) => {
      console.log(`\n--- Building with Builder ${index + 1} ---`);

      // Build minimal product
      const minimalProduct = this.createProduct(builder, "minimal");
      console.log(`Minimal product: ${minimalProduct}`);

      // Build full product
      const fullProduct = this.createProduct(builder, "full");
      console.log(`Full product: ${fullProduct}`);

      // Build custom product
      const customProduct = this.createProduct(builder, "custom", ["A", "C"]);
      console.log(`Custom product (A, C): ${customProduct}`);

      products.push(minimalProduct, fullProduct, customProduct);
    });

    return products;
  }

  /**
   * Compares products built by different builders
   * @param builder1 - First builder
   * @param builder2 - Second builder
   * @returns Comparison result
   */
  compareBuilders(builder1: Builder, builder2: Builder): string {
    const product1 = this.createProduct(builder1, "full");
    const product2 = this.createProduct(builder2, "full");

    return `Builder Comparison:
Builder 1 Product: ${product1}
Builder 2 Product: ${product2}
Same parts: ${product1.getParts().join(",") === product2.getParts().join(",")}
Part count difference: ${Math.abs(
      product1.getPartCount() - product2.getPartCount()
    )}`;
  }
}
