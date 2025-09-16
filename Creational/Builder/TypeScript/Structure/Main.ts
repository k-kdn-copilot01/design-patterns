import { ConcreteBuilder1 } from "./ConcreteBuilder1";
import { ConcreteBuilder2 } from "./ConcreteBuilder2";
import { Client } from "./Client";
import { Director } from "./Director";

/**
 * Main - Demonstrates Builder pattern usage
 * Shows how Director and Builder work together to create products
 */
function main(): void {
  console.log("=== Builder Pattern Demo ===\n");

  // Create builders and client
  const builder1 = new ConcreteBuilder1();
  const builder2 = new ConcreteBuilder2();
  const client = new Client();

  // Demonstrate individual product creation
  console.log("--- Individual Product Creation ---");

  // Build minimal product with builder 1
  const minimalProduct1 = client.createProduct(builder1, "minimal");
  console.log(`Minimal product (Builder 1): ${minimalProduct1}`);
  console.log(`Parts: ${minimalProduct1.listParts()}`);
  console.log(`Part count: ${minimalProduct1.getPartCount()}`);

  // Build full product with builder 2
  const fullProduct2 = client.createProduct(builder2, "full");
  console.log(`\nFull product (Builder 2): ${fullProduct2}`);
  console.log(`Parts: ${fullProduct2.listParts()}`);
  console.log(`Part count: ${fullProduct2.getPartCount()}`);

  // Build custom product with builder 1
  const customProduct1 = client.createProduct(builder1, "custom", ["A", "B"]);
  console.log(`\nCustom product (Builder 1, A+B): ${customProduct1}`);
  console.log(`Parts: ${customProduct1.listParts()}`);

  console.log("\n" + "=".repeat(50) + "\n");

  // Demonstrate multiple product creation
  console.log("--- Multiple Product Creation ---");
  const allProducts = client.createMultipleProducts([builder1, builder2]);
  console.log(`\nTotal products created: ${allProducts.length}`);

  console.log("\n" + "=".repeat(50) + "\n");

  // Demonstrate builder comparison
  console.log("--- Builder Comparison ---");
  console.log(client.compareBuilders(builder1, builder2));

  console.log("\n" + "=".repeat(50) + "\n");

  // Demonstrate step-by-step building
  console.log("--- Step-by-Step Building Process ---");
  const director = new Director();

  console.log("Building product step by step with Builder 1:");
  director.setBuilder(builder1);

  // Show each step by building custom products
  console.log("Step 1: Building part A...");
  const step1Product = director.buildCustomProduct(["A"]);
  console.log("Current product:", step1Product);

  console.log("Step 2: Building parts A + B...");
  const step2Product = director.buildCustomProduct(["A", "B"]);
  console.log("Current product:", step2Product);

  console.log("Step 3: Building all parts A + B + C...");
  const finalProduct = director.buildFullProduct();
  console.log("Final product:", finalProduct);
  console.log("Final parts:", finalProduct.listParts());

  console.log("\n" + "=".repeat(50) + "\n");

  // Demonstrate builder reuse
  console.log("--- Builder Reuse ---");
  console.log("Using same builder multiple times:");

  for (let i = 1; i <= 3; i++) {
    const product = client.createProduct(builder1, "full");
    console.log(`Build ${i}: ${product}`);
  }

  console.log("\n✓ Builder can be reused multiple times");
  console.log("✓ Each build creates a fresh product");
  console.log("✓ Director manages the construction process");
}

// Run the demo
if (require.main === module) {
  main();
}
