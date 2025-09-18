import { MealBuilder } from "./MealBuilder";

/**
 * AsianMealBuilder - Concrete builder for Asian meals
 * Implements specific construction steps for Asian cuisine
 */
export class AsianMealBuilder extends MealBuilder {
  /**
   * Builds Asian appetizer
   */
  buildAppetizer(): void {
    this.meal.setAppetizer("Spring Rolls with sweet chili sauce");
  }

  /**
   * Builds Asian main course
   */
  buildMainCourse(): void {
    this.meal.setMainCourse("Teriyaki Chicken with rice");
  }

  /**
   * Builds Asian side dish
   */
  buildSideDish(): void {
    this.meal.setSideDish("Miso Soup");
  }

  /**
   * Builds Asian dessert
   */
  buildDessert(): void {
    this.meal.setDessert("Mango Sticky Rice");
  }

  /**
   * Builds Asian beverage
   */
  buildBeverage(): void {
    this.meal.setBeverage("Green Tea");
  }
}
