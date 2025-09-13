///**
// * Main class to demonstrate DatabaseConnection Singleton example only
// */
//public class Main {
//    public static void main(String[] args) {
//        System.out.println("=== DatabaseConnection Singleton Demo ===\n");
//
//        // Get instances (should be the same)
//        DatabaseConnection db1 = DatabaseConnection.getInstance();
//        DatabaseConnection db2 = DatabaseConnection.getInstance();
//
//        System.out.println("db1 == db2: " + (db1 == db2));
//        System.out.println("Connection String: " + db1.getConnectionString());
//        System.out.println();
//
//        // Use the database connection
//        db1.connect();
//        db1.executeQuery("SELECT * FROM users");
//        db2.executeQuery("SELECT * FROM products");
//        db1.disconnect();
//
//        // Try executing after disconnect to show guard
//        db2.executeQuery("SELECT * FROM orders");
//
//        System.out.println("\n=== Demo Complete ===");
//    }
//}