import { Transport } from "./Transport";

/**
 * Ship - Concrete implementation of Transport
 * Represents sea transport vehicle
 */
export class Ship extends Transport {
  deliver(): string {
    return "Delivering goods by sea using Ship";
  }

  getCapacity(): number {
    return 50000; // kg
  }

  getSpeed(): number {
    return 30; // km/h
  }
}
