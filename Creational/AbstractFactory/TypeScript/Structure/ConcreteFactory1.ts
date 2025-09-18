import { AbstractFactory } from "./AbstractFactory";
import { ConcreteProductA1 } from "./ConcreteProductA1";
import { ConcreteProductB1 } from "./ConcreteProductB1";

/**
 * ConcreteFactory1 - Concrete implementation of AbstractFactory
 * Creates products from Family 1
 */
export class ConcreteFactory1 extends AbstractFactory {
  createProductA(): ConcreteProductA1 {
    return new ConcreteProductA1();
  }

  createProductB(): ConcreteProductB1 {
    return new ConcreteProductB1();
  }

  getFamilyName(): string {
    return "Family 1";
  }
}
