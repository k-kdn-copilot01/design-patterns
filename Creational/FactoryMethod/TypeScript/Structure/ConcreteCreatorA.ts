import { Creator } from "./Creator";
import { ConcreteProductA } from "./ConcreteProductA";

/**
 * ConcreteCreatorA - Concrete implementation of Creator
 * Creates ConcreteProductA instances
 */
export class ConcreteCreatorA extends Creator {
  factoryMethod(): ConcreteProductA {
    return new ConcreteProductA();
  }
}
