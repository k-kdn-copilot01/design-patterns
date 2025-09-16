import { Logistics } from "./Logistics";

/**
 * LogisticsClient - Client that uses Logistics to plan deliveries
 * Demonstrates the Factory Method pattern usage in real-world scenario
 */
export class LogisticsClient {
  /**
   * Client code that works with Logistics objects
   * @param logistics - Logistics instance to work with
   * @param distance - Distance for delivery calculation
   * @returns Result of the logistics operation
   */
  static planDelivery(logistics: Logistics, distance: number): string {
    const deliveryPlan = logistics.planDelivery();
    const timeEstimate = logistics.calculateDeliveryTime(distance);

    return `${deliveryPlan}\n${timeEstimate}`;
  }

  /**
   * Compare different logistics options
   */
  static compareLogistics(
    logisticsOptions: Array<{ name: string; logistics: Logistics }>,
    distance: number
  ): string {
    let comparison = "=== Logistics Comparison ===\n\n";

    logisticsOptions.forEach(({ name, logistics }) => {
      comparison += `--- ${name} ---\n`;
      comparison += LogisticsClient.planDelivery(logistics, distance);
      comparison += "\n\n";
    });

    return comparison;
  }
}
