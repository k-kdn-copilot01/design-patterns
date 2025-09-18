import { ConcreteFactory1 } from "./ConcreteFactory1";
import { ConcreteFactory2 } from "./ConcreteFactory2";
import { Client } from "./Client";

/**
 * Main - Demonstrates Abstract Factory pattern usage
 * Shows how different factories create compatible product families
 */
function main(): void {
  console.log("=== Abstract Factory Pattern Demo ===\n");

  // Create concrete factories
  const factory1 = new ConcreteFactory1();
  const factory2 = new ConcreteFactory2();

  // Demonstrate individual factory usage
  console.log("--- Individual Factory Usage ---");

  // Use Factory 1
  const client1 = new Client(factory1);
  console.log(client1.workWithProductFamily());
  console.log();

  // Use Factory 2
  const client2 = new Client(factory2);
  console.log(client2.workWithProductFamily());
  console.log();

  console.log("=".repeat(50) + "\n");

  // Demonstrate factory comparison
  console.log("--- Factory Comparison ---");
  console.log(Client.compareFactories([factory1, factory2]));

  console.log("=".repeat(50) + "\n");

  // Demonstrate family consistency
  console.log("--- Family Consistency Check ---");
  console.log("Factory 1:");
  console.log(client1.checkFamilyConsistency());
  console.log("\nFactory 2:");
  console.log(client2.checkFamilyConsistency());

  console.log("\n" + "=".repeat(50) + "\n");

  // Demonstrate dynamic factory switching
  console.log("--- Dynamic Factory Switching ---");
  const dynamicClient = new Client(factory1);
  console.log("Initial factory:", dynamicClient.getFactory().getFamilyName());
  console.log(dynamicClient.workWithProductFamily());
  console.log();

  console.log("Switching to Factory 2...");
  dynamicClient.setFactory(factory2);
  console.log("New factory:", dynamicClient.getFactory().getFamilyName());
  console.log(dynamicClient.workWithProductFamily());

  console.log("\n" + "=".repeat(50) + "\n");

  // Demonstrate product creation details
  console.log("--- Product Creation Details ---");

  const factories = [factory1, factory2];
  factories.forEach((factory, index) => {
    console.log(`\n--- Factory ${index + 1}: ${factory.getFamilyName()} ---`);

    const productA = factory.createProductA();
    const productB = factory.createProductB();

    console.log(`Created Product A: ${productA.constructor.name}`);
    console.log(`- Operation: ${productA.operationA()}`);
    console.log(`- Family: ${productA.getFamily()}`);

    console.log(`Created Product B: ${productB.constructor.name}`);
    console.log(`- Operation: ${productB.operationB()}`);
    console.log(`- Family: ${productB.getFamily()}`);
    console.log(`- Collaboration: ${productB.collaborateWith(productA)}`);
  });

  console.log("\n" + "=".repeat(50) + "\n");

  // Demonstrate working with multiple factories
  console.log("--- Working with Multiple Factories ---");
  const allClients = [new Client(factory1), new Client(factory2)];

  allClients.forEach((client, index) => {
    console.log(
      `\nClient ${index + 1} (${client.getFactory().getFamilyName()}):`
    );
    console.log(client.workWithProductFamily());
  });

  console.log("\n✓ Each factory creates a consistent product family");
  console.log("✓ Products from the same family work together seamlessly");
  console.log("✓ Switching factories changes the entire product family");
}

// Run the demo
if (require.main === module) {
  main();
}
