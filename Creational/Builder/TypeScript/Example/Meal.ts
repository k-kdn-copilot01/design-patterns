/**
 * Meal - Represents a complex meal with multiple components
 * This is the product being built
 */
export class Meal {
  private appetizer: string = "";
  private mainCourse: string = "";
  private sideDish: string = "";
  private dessert: string = "";
  private beverage: string = "";
  private extras: string[] = [];

  /**
   * Sets the appetizer
   */
  setAppetizer(appetizer: string): void {
    this.appetizer = appetizer;
  }

  /**
   * Sets the main course
   */
  setMainCourse(mainCourse: string): void {
    this.mainCourse = mainCourse;
  }

  /**
   * Sets the side dish
   */
  setSideDish(sideDish: string): void {
    this.sideDish = sideDish;
  }

  /**
   * Sets the dessert
   */
  setDessert(dessert: string): void {
    this.dessert = dessert;
  }

  /**
   * Sets the beverage
   */
  setBeverage(beverage: string): void {
    this.beverage = beverage;
  }

  /**
   * Adds an extra item
   */
  addExtra(extra: string): void {
    this.extras.push(extra);
  }

  /**
   * Gets the appetizer
   */
  getAppetizer(): string {
    return this.appetizer;
  }

  /**
   * Gets the main course
   */
  getMainCourse(): string {
    return this.mainCourse;
  }

  /**
   * Gets the side dish
   */
  getSideDish(): string {
    return this.sideDish;
  }

  /**
   * Gets the dessert
   */
  getDessert(): string {
    return this.dessert;
  }

  /**
   * Gets the beverage
   */
  getBeverage(): string {
    return this.beverage;
  }

  /**
   * Gets all extras
   */
  getExtras(): string[] {
    return [...this.extras];
  }

  /**
   * Gets the total price (simplified calculation)
   */
  getTotalPrice(): number {
    let price = 0;
    if (this.appetizer) price += 5;
    if (this.mainCourse) price += 15;
    if (this.sideDish) price += 8;
    if (this.dessert) price += 6;
    if (this.beverage) price += 3;
    price += this.extras.length * 2;
    return price;
  }

  /**
   * Gets meal summary
   */
  getSummary(): string {
    const parts: string[] = [];
    if (this.appetizer) parts.push(`Appetizer: ${this.appetizer}`);
    if (this.mainCourse) parts.push(`Main Course: ${this.mainCourse}`);
    if (this.sideDish) parts.push(`Side Dish: ${this.sideDish}`);
    if (this.dessert) parts.push(`Dessert: ${this.dessert}`);
    if (this.beverage) parts.push(`Beverage: ${this.beverage}`);
    if (this.extras.length > 0) parts.push(`Extras: ${this.extras.join(", ")}`);

    return parts.join("\n");
  }

  /**
   * String representation of the meal
   */
  toString(): string {
    return `Meal(${this.getSummary().replace(/\n/g, ", ")})`;
  }
}
