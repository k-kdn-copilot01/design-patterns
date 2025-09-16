import { MealBuilder } from "./MealBuilder";
import { Meal } from "./Meal";

/**
 * Chef - Director that controls the meal construction process
 * Defines the order of construction steps for different meal types
 */
export class Chef {
  private builder: MealBuilder | null = null;

  /**
   * Sets the meal builder to use
   */
  setBuilder(builder: MealBuilder): void {
    this.builder = builder;
  }

  /**
   * Builds a light meal (appetizer + main course + beverage)
   */
  buildLightMeal(): Meal {
    if (!this.builder) {
      throw new Error("Meal builder not set");
    }
    this.builder.reset();
    this.builder.buildAppetizer();
    this.builder.buildMainCourse();
    this.builder.buildBeverage();
    return this.builder.getMeal();
  }

  /**
   * Builds a full meal (all courses)
   */
  buildFullMeal(): Meal {
    if (!this.builder) {
      throw new Error("Meal builder not set");
    }
    this.builder.reset();
    this.builder.buildAppetizer();
    this.builder.buildMainCourse();
    this.builder.buildSideDish();
    this.builder.buildDessert();
    this.builder.buildBeverage();
    return this.builder.getMeal();
  }

  /**
   * Builds a custom meal with specific courses
   */
  buildCustomMeal(
    courses: ("appetizer" | "main" | "side" | "dessert" | "beverage")[]
  ): Meal {
    if (!this.builder) {
      throw new Error("Meal builder not set");
    }
    this.builder.reset();

    courses.forEach((course) => {
      switch (course) {
        case "appetizer":
          this.builder!.buildAppetizer();
          break;
        case "main":
          this.builder!.buildMainCourse();
          break;
        case "side":
          this.builder!.buildSideDish();
          break;
        case "dessert":
          this.builder!.buildDessert();
          break;
        case "beverage":
          this.builder!.buildBeverage();
          break;
      }
    });

    return this.builder.getMeal();
  }

  /**
   * Builds a special meal with extras
   */
  buildSpecialMeal(extras: string[]): Meal {
    if (!this.builder) {
      throw new Error("Meal builder not set");
    }
    this.builder.reset();

    // Build full meal first
    this.builder.buildAppetizer();
    this.builder.buildMainCourse();
    this.builder.buildSideDish();
    this.builder.buildDessert();
    this.builder.buildBeverage();

    // Add extras
    const meal = this.builder.getMeal();
    extras.forEach((extra) => meal.addExtra(extra));

    return meal;
  }
}
