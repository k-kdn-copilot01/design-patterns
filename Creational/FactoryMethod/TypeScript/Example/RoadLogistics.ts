import { Logistics } from "./Logistics";
import { Truck } from "./Truck";

/**
 * RoadLogistics - Concrete implementation of Logistics
 * Creates Truck instances for road transport
 */
export class RoadLogistics extends Logistics {
  createTransport(): Truck {
    return new Truck();
  }
}
