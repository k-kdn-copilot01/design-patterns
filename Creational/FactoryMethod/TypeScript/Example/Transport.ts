/**
 * Transport - Abstract base class for all transport vehicles
 * Represents the Product in Factory Method pattern
 */
export abstract class Transport {
  abstract deliver(): string;
  abstract getCapacity(): number;
  abstract getSpeed(): number;
}
