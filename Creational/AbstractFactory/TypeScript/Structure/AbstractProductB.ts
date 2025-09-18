import { AbstractProductA } from "./AbstractProductA";

/**
 * AbstractProductB - Abstract base class for Product B family
 * Defines the interface for all Product B variants
 */
export abstract class AbstractProductB {
  abstract operationB(): string;
  abstract getFamily(): string;
  abstract collaborateWith(productA: AbstractProductA): string;
}
