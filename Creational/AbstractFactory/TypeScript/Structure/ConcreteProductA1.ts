import { AbstractProductA } from "./AbstractProductA";

/**
 * ConcreteProductA1 - Concrete implementation of AbstractProductA
 * Represents Product A from Family 1
 */
export class ConcreteProductA1 extends AbstractProductA {
  operationA(): string {
    return "ConcreteProductA1 operation";
  }

  getFamily(): string {
    return "Family 1";
  }
}
