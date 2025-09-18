import { ConcretePrototypeA } from "./ConcretePrototypeA";
import { ConcretePrototypeB } from "./ConcretePrototypeB";
import { Client } from "./Client";
import { Prototype } from "./Prototype";

/**
 * Main - Demonstrates Prototype pattern usage
 * Shows shallow vs deep cloning and reference comparison
 */
function main(): void {
  console.log("=== Prototype Pattern Demo ===\n");

  // Test ConcretePrototypeA
  console.log("--- Testing ConcretePrototypeA ---");
  const prototypeA = new ConcretePrototypeA("Original A", 100, "nested value");
  console.log(`Original: ${prototypeA}`);

  // Shallow clone
  const shallowCloneA = prototypeA.clone();
  console.log(`Shallow clone: ${shallowCloneA}`);

  // Deep clone
  const deepCloneA = prototypeA.deepClone();
  console.log(`Deep clone: ${deepCloneA}`);

  // Reference comparison
  console.log(Client.compareReferences(prototypeA, shallowCloneA));
  console.log(
    Client.compareCloningTypes(prototypeA, shallowCloneA, deepCloneA)
  );

  // Modify nested object to show shallow vs deep difference
  console.log("\n--- Modifying nested object ---");
  prototypeA.nestedObject.value = "modified value";
  console.log(`Original after modification: ${prototypeA}`);
  console.log(`Shallow clone after original modification: ${shallowCloneA}`);
  console.log(`Deep clone after original modification: ${deepCloneA}`);

  console.log("\n" + "=".repeat(50) + "\n");

  // Test ConcretePrototypeB
  console.log("--- Testing ConcretePrototypeB ---");
  const prototypeB = new ConcretePrototypeB(
    "Document B",
    ["item1", "item2"],
    2
  );
  console.log(`Original: ${prototypeB}`);

  // Shallow clone
  const shallowCloneB = prototypeB.clone();
  console.log(`Shallow clone: ${shallowCloneB}`);

  // Deep clone
  const deepCloneB = prototypeB.deepClone();
  console.log(`Deep clone: ${deepCloneB}`);

  // Reference comparison
  console.log(Client.compareReferences(prototypeB, shallowCloneB));
  console.log(
    Client.compareCloningTypes(prototypeB, shallowCloneB, deepCloneB)
  );

  // Modify array to show shallow vs deep difference
  console.log("\n--- Modifying array ---");
  prototypeB.addItem("item3");
  console.log(`Original after adding item: ${prototypeB}`);
  console.log(`Shallow clone after original modification: ${shallowCloneB}`);
  console.log(`Deep clone after original modification: ${deepCloneB}`);

  console.log("\n" + "=".repeat(50) + "\n");

  // Demonstrate working with prototypes through interface
  console.log("--- Working with Prototype interface ---");
  const prototypes: Prototype[] = [prototypeA, prototypeB];

  prototypes.forEach((prototype, index) => {
    console.log(`\nPrototype ${index + 1}:`);
    console.log(Client.clientCode(prototype));
  });

  // Demonstrate registry pattern
  console.log("\n--- Prototype Registry Demo ---");
  const registry = new Map<string, Prototype>();
  registry.set("typeA", prototypeA);
  registry.set("typeB", prototypeB);

  console.log("Available prototypes in registry:");
  registry.forEach((prototype, key) => {
    console.log(`- ${key}: ${prototype.constructor.name}`);
  });

  console.log("\nCloning from registry:");
  const clonedFromRegistry = registry.get("typeA")?.clone();
  if (clonedFromRegistry) {
    console.log(`Cloned from registry: ${clonedFromRegistry}`);
  }
}

// Run the demo
if (require.main === module) {
  main();
}
