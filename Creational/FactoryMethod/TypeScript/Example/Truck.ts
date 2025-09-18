import { Transport } from "./Transport";

/**
 * Truck - Concrete implementation of Transport
 * Represents road transport vehicle
 */
export class Truck extends Transport {
  deliver(): string {
    return "Delivering goods by road using Truck";
  }

  getCapacity(): number {
    return 10000; // kg
  }

  getSpeed(): number {
    return 80; // km/h
  }
}
