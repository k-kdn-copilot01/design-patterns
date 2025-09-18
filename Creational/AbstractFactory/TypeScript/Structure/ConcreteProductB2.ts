import { AbstractProductB } from "./AbstractProductB";
import { AbstractProductA } from "./AbstractProductA";

/**
 * ConcreteProductB2 - Concrete implementation of AbstractProductB
 * Represents Product B from Family 2
 */
export class ConcreteProductB2 extends AbstractProductB {
  operationB(): string {
    return "ConcreteProductB2 operation";
  }

  getFamily(): string {
    return "Family 2";
  }

  collaborateWith(productA: AbstractProductA): string {
    return `ConcreteProductB2 collaborating with ${productA.constructor.name}`;
  }
}
