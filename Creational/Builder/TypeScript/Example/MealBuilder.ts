import { Meal } from "./Meal";

/**
 * MealBuilder - Abstract builder for creating meals
 * Defines the interface for building complex meals step by step
 */
export abstract class MealBuilder {
  protected meal: Meal = new Meal();

  /**
   * Resets the builder to start fresh
   */
  reset(): void {
    this.meal = new Meal();
  }

  /**
   * Returns the built meal
   */
  getMeal(): Meal {
    const result = this.meal;
    this.reset(); // Reset for next build
    return result;
  }

  /**
   * Abstract methods that concrete builders must implement
   */
  abstract buildAppetizer(): void;
  abstract buildMainCourse(): void;
  abstract buildSideDish(): void;
  abstract buildDessert(): void;
  abstract buildBeverage(): void;
}
