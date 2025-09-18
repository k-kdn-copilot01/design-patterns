import { RoadLogistics } from "./RoadLogistics";
import { SeaLogistics } from "./SeaLogistics";
import { LogisticsClient } from "./LogisticsClient";
import { Logistics } from "./Logistics";

/**
 * Main - Demonstrates Factory Method pattern with real-world logistics example
 * Shows how different logistics providers create different transport vehicles
 */
function main(): void {
  console.log("=== Factory Method Pattern - Logistics Example ===\n");

  // Create different logistics providers
  const roadLogistics = new RoadLogistics();
  const seaLogistics = new SeaLogistics();

  const distance = 500; // km

  // Plan delivery using road logistics
  console.log("=== Road Logistics ===");
  console.log(LogisticsClient.planDelivery(roadLogistics, distance));
  console.log();

  // Plan delivery using sea logistics
  console.log("=== Sea Logistics ===");
  console.log(LogisticsClient.planDelivery(seaLogistics, distance));
  console.log();

  // Compare different logistics options
  const logisticsOptions = [
    { name: "Road Logistics", logistics: roadLogistics },
    { name: "Sea Logistics", logistics: seaLogistics },
  ];

  console.log(LogisticsClient.compareLogistics(logisticsOptions, distance));

  // Demonstrate dynamic logistics selection
  console.log("=== Dynamic Logistics Selection ===");
  const logisticsProviders = [roadLogistics, seaLogistics];
  const providerNames = ["Road", "Sea"];

  logisticsProviders.forEach((logistics, index) => {
    console.log(
      `\n--- Option ${index + 1}: ${providerNames[index]} Logistics ---`
    );
    console.log(LogisticsClient.planDelivery(logistics, distance));
  });

  // Show how we can work with logistics through their base class
  console.log("\n=== Working with Base Class ===");
  const allLogistics: Array<{ name: string; logistics: Logistics }> = [
    { name: "Road Logistics", logistics: roadLogistics },
    { name: "Sea Logistics", logistics: seaLogistics },
  ];

  allLogistics.forEach(({ name, logistics }) => {
    console.log(`\n${name}:`);
    console.log(LogisticsClient.planDelivery(logistics, distance));
  });
}

// Run the demo
if (require.main === module) {
  main();
}
