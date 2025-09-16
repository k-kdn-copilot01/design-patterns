import { MealBuilder } from "./MealBuilder";

/**
 * ItalianMealBuilder - Concrete builder for Italian meals
 * Implements specific construction steps for Italian cuisine
 */
export class ItalianMealBuilder extends MealBuilder {
  /**
   * Builds Italian appetizer
   */
  buildAppetizer(): void {
    this.meal.setAppetizer("Bruschetta with tomatoes and basil");
  }

  /**
   * Builds Italian main course
   */
  buildMainCourse(): void {
    this.meal.setMainCourse("Spaghetti Carbonara");
  }

  /**
   * Builds Italian side dish
   */
  buildSideDish(): void {
    this.meal.setSideDish("Caesar Salad");
  }

  /**
   * Builds Italian dessert
   */
  buildDessert(): void {
    this.meal.setDessert("Tiramisu");
  }

  /**
   * Builds Italian beverage
   */
  buildBeverage(): void {
    this.meal.setBeverage("Chianti Wine");
  }
}
