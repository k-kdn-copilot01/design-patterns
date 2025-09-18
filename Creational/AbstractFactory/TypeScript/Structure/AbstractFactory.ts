import { AbstractProductA } from "./AbstractProductA";
import { AbstractProductB } from "./AbstractProductB";

/**
 * AbstractFactory - Abstract base class for all factories
 * Defines the interface for creating families of related products
 */
export abstract class AbstractFactory {
  /**
   * Creates Product A from the family
   */
  abstract createProductA(): AbstractProductA;

  /**
   * Creates Product B from the family
   */
  abstract createProductB(): AbstractProductB;

  /**
   * Gets the family name this factory creates
   */
  abstract getFamilyName(): string;
}
