import { ConcreteCreatorA } from "./ConcreteCreatorA";
import { ConcreteCreatorB } from "./ConcreteCreatorB";
import { Client } from "./Client";

/**
 * Main - Demonstrates Factory Method pattern usage
 * Shows how different creators produce different products
 */
function main(): void {
  console.log("=== Factory Method Pattern Demo ===\n");

  // Create different creators
  const creatorA = new ConcreteCreatorA();
  const creatorB = new ConcreteCreatorB();

  // Use creators to create products and perform operations
  console.log("Client: Using ConcreteCreatorA:");
  console.log(Client.clientCode(creatorA));
  console.log();

  console.log("Client: Using ConcreteCreatorB:");
  console.log(Client.clientCode(creatorB));
  console.log();

  // Demonstrate that we can work with creators through their base class
  const creators: Array<{ name: string; creator: any }> = [
    { name: "ConcreteCreatorA", creator: creatorA },
    { name: "ConcreteCreatorB", creator: creatorB },
  ];

  console.log("Client: Working with creators through base class:");
  creators.forEach(({ name, creator }) => {
    console.log(`${name}: ${Client.clientCode(creator)}`);
  });
}

// Run the demo
if (require.main === module) {
  main();
}
