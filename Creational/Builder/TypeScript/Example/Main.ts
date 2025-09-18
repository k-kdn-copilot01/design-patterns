import { ItalianMealBuilder } from "./ItalianMealBuilder";
import { AsianMealBuilder } from "./AsianMealBuilder";
import { Restaurant } from "./Restaurant";
import { Chef } from "./Chef";

/**
 * Main - Demonstrates Builder pattern with real-world meal construction example
 * Shows how Chef and MealBuilder work together to create different types of meals
 */
function main(): void {
  console.log("=== Builder Pattern - Meal Construction Example ===\n");

  // Create meal builders and restaurant
  const italianBuilder = new ItalianMealBuilder();
  const asianBuilder = new AsianMealBuilder();
  const restaurant = new Restaurant();

  // Demonstrate individual meal creation
  console.log("--- Individual Meal Creation ---");

  // Create light Italian meal
  const lightItalianMeal = restaurant.createMeal(italianBuilder, "light");
  console.log("Light Italian Meal:");
  console.log(lightItalianMeal.getSummary());
  console.log(`Price: $${lightItalianMeal.getTotalPrice()}`);

  // Create full Asian meal
  const fullAsianMeal = restaurant.createMeal(asianBuilder, "full");
  console.log("\nFull Asian Meal:");
  console.log(fullAsianMeal.getSummary());
  console.log(`Price: $${fullAsianMeal.getTotalPrice()}`);

  // Create custom Italian meal
  const customItalianMeal = restaurant.createMeal(italianBuilder, "custom", [
    "appetizer",
    "main",
    "dessert",
  ]);
  console.log("\nCustom Italian Meal (Appetizer + Main + Dessert):");
  console.log(customItalianMeal.getSummary());
  console.log(`Price: $${customItalianMeal.getTotalPrice()}`);

  // Create special Asian meal with extras
  const specialAsianMeal = restaurant.createMeal(
    asianBuilder,
    "special",
    undefined,
    ["Extra soy sauce", "Chopsticks", "Fortune cookie"]
  );
  console.log("\nSpecial Asian Meal with Extras:");
  console.log(specialAsianMeal.getSummary());
  console.log(`Price: $${specialAsianMeal.getTotalPrice()}`);

  console.log("\n" + "=".repeat(60) + "\n");

  // Demonstrate multiple meal creation
  console.log("--- Multiple Meal Creation ---");
  const allMeals = restaurant.createMultipleMeals([
    italianBuilder,
    asianBuilder,
  ]);
  console.log(`\nTotal meals created: ${allMeals.length}`);

  console.log("\n" + "=".repeat(60) + "\n");

  // Demonstrate builder comparison
  console.log("--- Builder Comparison ---");
  console.log(restaurant.compareBuilders(italianBuilder, asianBuilder));

  console.log("\n" + "=".repeat(60) + "\n");

  // Demonstrate step-by-step meal building
  console.log("--- Step-by-Step Meal Building Process ---");
  const chef = new Chef();

  console.log("Building Italian meal step by step:");
  chef.setBuilder(italianBuilder);

  // Show each step by building custom meals
  console.log("Step 1: Building appetizer...");
  const step1Meal = chef.buildCustomMeal(["appetizer"]);
  console.log("Current meal:", step1Meal.getSummary());

  console.log("Step 2: Building appetizer + main course...");
  const step2Meal = chef.buildCustomMeal(["appetizer", "main"]);
  console.log("Current meal:", step2Meal.getSummary());

  console.log("Step 3: Building appetizer + main + side dish...");
  const step3Meal = chef.buildCustomMeal(["appetizer", "main", "side"]);
  console.log("Current meal:", step3Meal.getSummary());

  console.log("Step 4: Building appetizer + main + side + dessert...");
  const step4Meal = chef.buildCustomMeal([
    "appetizer",
    "main",
    "side",
    "dessert",
  ]);
  console.log("Current meal:", step4Meal.getSummary());

  console.log("Step 5: Building full meal with all courses...");
  const finalMeal = chef.buildFullMeal();
  console.log("Final meal:", finalMeal.getSummary());
  console.log("Final price:", `$${finalMeal.getTotalPrice()}`);

  console.log("\n" + "=".repeat(60) + "\n");

  // Demonstrate builder reuse
  console.log("--- Builder Reuse ---");
  console.log("Using same builder multiple times:");

  for (let i = 1; i <= 3; i++) {
    const meal = restaurant.createMeal(italianBuilder, "full");
    console.log(`Build ${i}: ${meal.getSummary()}`);
    console.log(`Price: $${meal.getTotalPrice()}\n`);
  }

  console.log("✓ Builder can be reused multiple times");
  console.log("✓ Each build creates a fresh meal");
  console.log("✓ Chef manages the construction process");

  console.log("\n" + "=".repeat(60) + "\n");

  // Show restaurant statistics
  console.log("--- Restaurant Statistics ---");
  console.log(restaurant.getOrderStatistics());

  console.log("\n" + "=".repeat(60) + "\n");

  // Demonstrate different meal configurations
  console.log("--- Different Meal Configurations ---");

  const configurations = [
    {
      name: "Quick Lunch",
      courses: ["main", "beverage"] as (
        | "appetizer"
        | "main"
        | "side"
        | "dessert"
        | "beverage"
      )[],
    },
    {
      name: "Business Dinner",
      courses: ["appetizer", "main", "side", "dessert", "beverage"] as (
        | "appetizer"
        | "main"
        | "side"
        | "dessert"
        | "beverage"
      )[],
    },
    {
      name: "Date Night",
      courses: ["appetizer", "main", "dessert", "beverage"] as (
        | "appetizer"
        | "main"
        | "side"
        | "dessert"
        | "beverage"
      )[],
    },
    {
      name: "Family Meal",
      courses: ["main", "side", "beverage"] as (
        | "appetizer"
        | "main"
        | "side"
        | "dessert"
        | "beverage"
      )[],
    },
  ];

  configurations.forEach((config, index) => {
    console.log(`\n--- ${config.name} ---`);
    const meal = restaurant.createMeal(
      italianBuilder,
      "custom",
      config.courses
    );
    console.log(meal.getSummary());
    console.log(`Price: $${meal.getTotalPrice()}`);
  });
}

// Run the demo
if (require.main === module) {
  main();
}
