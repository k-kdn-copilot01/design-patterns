import { Product } from "./Product";

/**
 * ConcreteProductA - Concrete implementation of Product
 * Represents a specific type of product created by ConcreteCreatorA
 */
export class ConcreteProductA extends Product {
  operation(): string {
    return "ConcreteProductA operation";
  }
}
