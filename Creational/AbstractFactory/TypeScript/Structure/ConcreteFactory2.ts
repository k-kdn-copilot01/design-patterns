import { AbstractFactory } from "./AbstractFactory";
import { ConcreteProductA2 } from "./ConcreteProductA2";
import { ConcreteProductB2 } from "./ConcreteProductB2";

/**
 * ConcreteFactory2 - Concrete implementation of AbstractFactory
 * Creates products from Family 2
 */
export class ConcreteFactory2 extends AbstractFactory {
  createProductA(): ConcreteProductA2 {
    return new ConcreteProductA2();
  }

  createProductB(): ConcreteProductB2 {
    return new ConcreteProductB2();
  }

  getFamilyName(): string {
    return "Family 2";
  }
}
