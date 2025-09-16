import { Creator } from "./Creator";
import { ConcreteProductB } from "./ConcreteProductB";

/**
 * ConcreteCreatorB - Concrete implementation of Creator
 * Creates ConcreteProductB instances
 */
export class ConcreteCreatorB extends Creator {
  factoryMethod(): ConcreteProductB {
    return new ConcreteProductB();
  }
}
