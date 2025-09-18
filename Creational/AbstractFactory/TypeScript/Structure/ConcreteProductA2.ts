import { AbstractProductA } from "./AbstractProductA";

/**
 * ConcreteProductA2 - Concrete implementation of AbstractProductA
 * Represents Product A from Family 2
 */
export class ConcreteProductA2 extends AbstractProductA {
  operationA(): string {
    return "ConcreteProductA2 operation";
  }

  getFamily(): string {
    return "Family 2";
  }
}
