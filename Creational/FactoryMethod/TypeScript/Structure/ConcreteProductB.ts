import { Product } from "./Product";

/**
 * ConcreteProductB - Concrete implementation of Product
 * Represents a specific type of product created by ConcreteCreatorB
 */
export class ConcreteProductB extends Product {
  operation(): string {
    return "ConcreteProductB operation";
  }
}
