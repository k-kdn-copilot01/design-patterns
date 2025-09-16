import { Logistics } from "./Logistics";
import { Ship } from "./Ship";

/**
 * SeaLogistics - Concrete implementation of Logistics
 * Creates Ship instances for sea transport
 */
export class SeaLogistics extends Logistics {
  createTransport(): Ship {
    return new Ship();
  }
}
