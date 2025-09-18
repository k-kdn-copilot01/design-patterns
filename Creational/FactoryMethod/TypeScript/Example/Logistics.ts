import { Transport } from "./Transport";

/**
 * Logistics - Abstract base class for all logistics providers
 * Represents the Creator in Factory Method pattern
 */
export abstract class Logistics {
  /**
   * Factory method - creates Transport objects
   * Subclasses must implement this method to return specific Transport instances
   */
  abstract createTransport(): Transport;

  /**
   * Template method that uses the factory method
   * Contains common logistics operations
   */
  planDelivery(): string {
    const transport = this.createTransport();
    return (
      `Logistics: Planning delivery using ${transport.constructor.name}\n` +
      `- Method: ${transport.deliver()}\n` +
      `- Capacity: ${transport.getCapacity()} kg\n` +
      `- Speed: ${transport.getSpeed()} km/h`
    );
  }

  /**
   * Calculate delivery time based on distance and transport speed
   */
  calculateDeliveryTime(distance: number): string {
    const transport = this.createTransport();
    const time = distance / transport.getSpeed();
    return `Estimated delivery time: ${time.toFixed(
      2
    )} hours for ${distance} km`;
  }
}
