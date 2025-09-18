import { MaterialUIFactory } from "./MaterialUIFactory";
import { FlatUIFactory } from "./FlatUIFactory";
import { Application } from "./Application";

/**
 * Main - Demonstrates Abstract Factory pattern with real-world UI components example
 * Shows how different UI factories create compatible component families
 */
function main(): void {
  console.log("=== Abstract Factory Pattern - UI Components Example ===\n");

  // Create UI factories
  const materialFactory = new MaterialUIFactory();
  const flatFactory = new FlatUIFactory();

  // Demonstrate individual factory usage
  console.log("--- Individual Factory Usage ---");

  // Use Material Design Factory
  const materialApp = new Application(materialFactory);
  materialApp.createComponent("button", "Save");
  materialApp.createComponent("button", "Cancel");
  materialApp.createComponent("checkbox", "Remember me");
  materialApp.createComponent("checkbox", "Subscribe to newsletter");

  console.log("Material Design Application:");
  console.log(materialApp.renderAll());
  console.log(materialApp.demonstrateInteraction());
  console.log(materialApp.getStatistics());

  console.log("\n" + "=".repeat(60) + "\n");

  // Use Flat Design Factory
  const flatApp = new Application(flatFactory);
  flatApp.createComponent("button", "Submit");
  flatApp.createComponent("button", "Reset");
  flatApp.createComponent("checkbox", "I agree to terms");
  flatApp.createComponent("checkbox", "Send notifications");

  console.log("Flat Design Application:");
  console.log(flatApp.renderAll());
  console.log(flatApp.demonstrateInteraction());
  console.log(flatApp.getStatistics());

  console.log("\n" + "=".repeat(60) + "\n");

  // Demonstrate factory comparison
  console.log("--- Factory Comparison ---");
  const factories = [materialFactory, flatFactory];

  factories.forEach((factory, index) => {
    console.log(`\n--- Factory ${index + 1}: ${factory.getDesignSystem()} ---`);

    const button = factory.createButton("Test Button");
    const checkbox = factory.createCheckbox("Test Checkbox");

    console.log(`Button: ${button.render()}`);
    console.log(`Button Click: ${button.onClick()}`);
    console.log(`Checkbox: ${checkbox.render()}`);
    console.log(`Checkbox Toggle: ${checkbox.toggle()}`);
    console.log(
      `Theme Consistency: ${
        button.getTheme() === checkbox.getTheme() ? "✓" : "✗"
      }`
    );
  });

  console.log("\n" + "=".repeat(60) + "\n");

  // Demonstrate dynamic factory switching
  console.log("--- Dynamic Factory Switching ---");
  const dynamicApp = new Application(materialFactory);
  dynamicApp.createComponent("button", "Initial Button");
  dynamicApp.createComponent("checkbox", "Initial Checkbox");

  console.log("Initial Application (Material Design):");
  console.log(dynamicApp.getStatistics());
  console.log(dynamicApp.renderAll());

  console.log("\nSwitching to Flat Design...");
  dynamicApp.setFactory(flatFactory);
  dynamicApp.clear();
  dynamicApp.createComponent("button", "New Button");
  dynamicApp.createComponent("checkbox", "New Checkbox");

  console.log("New Application (Flat Design):");
  console.log(dynamicApp.getStatistics());
  console.log(dynamicApp.renderAll());

  console.log("\n" + "=".repeat(60) + "\n");

  // Demonstrate theme consistency
  console.log("--- Theme Consistency Check ---");
  const materialApp2 = new Application(materialFactory);
  materialApp2.createComponent("button", "Consistency Test Button");
  materialApp2.createComponent("checkbox", "Consistency Test Checkbox");

  const components = materialApp2.getAllComponents();
  const button = components.find((c) => c.type === "button")?.component as any;
  const checkbox = components.find((c) => c.type === "checkbox")
    ?.component as any;

  console.log(`Button Theme: ${button?.getTheme()}`);
  console.log(`Checkbox Theme: ${checkbox?.getTheme()}`);
  console.log(
    `Themes Match: ${
      button?.getTheme() === checkbox?.getTheme() ? "✓ Yes" : "✗ No"
    }`
  );
  console.log(`Design System: ${materialFactory.getDesignSystem()}`);

  console.log("\n" + "=".repeat(60) + "\n");

  // Demonstrate creating multiple applications
  console.log("--- Multiple Applications Demo ---");
  const applications = [
    new Application(materialFactory),
    new Application(flatFactory),
  ];

  applications.forEach((app, index) => {
    const factory = app.getFactory();
    app.createComponent("button", `${factory.getDesignSystem()} Button`);
    app.createComponent("checkbox", `${factory.getDesignSystem()} Checkbox`);

    console.log(`\n--- Application ${index + 1} ---`);
    console.log(app.getStatistics());
    console.log(app.demonstrateInteraction());
  });

  console.log("\n✓ Each factory creates a consistent component family");
  console.log("✓ Components from the same family have matching themes");
  console.log("✓ Switching factories changes the entire component family");
  console.log("✓ All components work together seamlessly within their family");
}

// Run the demo
if (require.main === module) {
  main();
}
