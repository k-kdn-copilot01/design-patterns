import { Chef } from "./Chef";
import { MealBuilder } from "./MealBuilder";
import { Meal } from "./Meal";

/**
 * Restaurant - Client that uses Chef and MealBuilder to create meals
 * Demonstrates the Builder pattern usage in real-world restaurant scenario
 */
export class Restaurant {
  private chef: Chef;
  private orders: Meal[] = [];

  constructor() {
    this.chef = new Chef();
  }

  /**
   * Creates a meal using the specified builder
   * @param builder - The meal builder to use
   * @param mealType - Type of meal to build
   * @param customCourses - Custom courses for custom meal type
   * @param extras - Extra items for special meal
   * @returns The built meal
   */
  createMeal(
    builder: MealBuilder,
    mealType: "light" | "full" | "custom" | "special",
    customCourses?: ("appetizer" | "main" | "side" | "dessert" | "beverage")[],
    extras?: string[]
  ): Meal {
    this.chef.setBuilder(builder);

    let meal: Meal;
    switch (mealType) {
      case "light":
        meal = this.chef.buildLightMeal();
        break;
      case "full":
        meal = this.chef.buildFullMeal();
        break;
      case "custom":
        if (!customCourses) {
          throw new Error(
            "Custom courses must be provided for custom meal type"
          );
        }
        meal = this.chef.buildCustomMeal(customCourses);
        break;
      case "special":
        if (!extras) {
          throw new Error("Extras must be provided for special meal type");
        }
        meal = this.chef.buildSpecialMeal(extras);
        break;
      default:
        throw new Error(`Unknown meal type: ${mealType}`);
    }

    this.orders.push(meal);
    return meal;
  }

  /**
   * Creates multiple meals with different builders
   * @param builders - Array of meal builders to use
   * @returns Array of built meals
   */
  createMultipleMeals(builders: MealBuilder[]): Meal[] {
    const meals: Meal[] = [];

    builders.forEach((builder, index) => {
      console.log(`\n--- Creating Meal ${index + 1} ---`);

      // Create light meal
      const lightMeal = this.createMeal(builder, "light");
      console.log(`Light meal: ${lightMeal.getSummary()}`);
      console.log(`Price: $${lightMeal.getTotalPrice()}`);

      // Create full meal
      const fullMeal = this.createMeal(builder, "full");
      console.log(`\nFull meal: ${fullMeal.getSummary()}`);
      console.log(`Price: $${fullMeal.getTotalPrice()}`);

      // Create custom meal
      const customMeal = this.createMeal(builder, "custom", [
        "appetizer",
        "main",
        "dessert",
      ]);
      console.log(`\nCustom meal: ${customMeal.getSummary()}`);
      console.log(`Price: $${customMeal.getTotalPrice()}`);

      meals.push(lightMeal, fullMeal, customMeal);
    });

    return meals;
  }

  /**
   * Compares meals built by different builders
   * @param builder1 - First builder
   * @param builder2 - Second builder
   * @returns Comparison result
   */
  compareBuilders(builder1: MealBuilder, builder2: MealBuilder): string {
    const meal1 = this.createMeal(builder1, "full");
    const meal2 = this.createMeal(builder2, "full");

    return `Builder Comparison:
Builder 1 Meal: ${meal1.getSummary()}
Price: $${meal1.getTotalPrice()}

Builder 2 Meal: ${meal2.getSummary()}
Price: $${meal2.getTotalPrice()}

Price difference: $${Math.abs(meal1.getTotalPrice() - meal2.getTotalPrice())}`;
  }

  /**
   * Gets all orders
   */
  getAllOrders(): Meal[] {
    return [...this.orders];
  }

  /**
   * Gets total revenue
   */
  getTotalRevenue(): number {
    return this.orders.reduce((total, meal) => total + meal.getTotalPrice(), 0);
  }

  /**
   * Gets order statistics
   */
  getOrderStatistics(): string {
    const totalOrders = this.orders.length;
    const totalRevenue = this.getTotalRevenue();
    const averagePrice = totalOrders > 0 ? totalRevenue / totalOrders : 0;

    return `Restaurant Statistics:
Total Orders: ${totalOrders}
Total Revenue: $${totalRevenue}
Average Order Price: $${averagePrice.toFixed(2)}`;
  }
}
