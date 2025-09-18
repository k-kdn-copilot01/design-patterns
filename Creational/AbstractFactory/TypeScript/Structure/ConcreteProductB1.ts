import { AbstractProductB } from "./AbstractProductB";
import { AbstractProductA } from "./AbstractProductA";

/**
 * ConcreteProductB1 - Concrete implementation of AbstractProductB
 * Represents Product B from Family 1
 */
export class ConcreteProductB1 extends AbstractProductB {
  operationB(): string {
    return "ConcreteProductB1 operation";
  }

  getFamily(): string {
    return "Family 1";
  }

  collaborateWith(productA: AbstractProductA): string {
    return `ConcreteProductB1 collaborating with ${productA.constructor.name}`;
  }
}
