import { Creator } from "./Creator";

/**
 * Client - Uses Creator to create and work with Product objects
 * Demonstrates the Factory Method pattern usage
 */
export class Client {
  /**
   * Client code that works with Creator objects
   * @param creator - Creator instance to work with
   * @returns Result of the operation
   */
  static clientCode(creator: Creator): string {
    return creator.someOperation();
  }
}
