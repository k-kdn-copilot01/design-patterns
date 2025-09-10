/**
 * DatabaseConnection - Real-world Singleton Example
 * 
 * This demonstrates a practical use case for Singleton pattern:
 * Managing a single database connection throughout the application.
 * Uses thread-safe lazy initialization with synchronized method.
 */
public class DatabaseConnection {
    private static DatabaseConnection instance;
    private String connectionString;
    private boolean isConnected;
    
    // Private constructor to prevent external instantiation
    private DatabaseConnection() {
        this.connectionString = "jdbc:mysql://localhost:3306/mydb";
        this.isConnected = false;
        System.out.println("DatabaseConnection instance created");
    }
    
    // Thread-safe lazy initialization using synchronized method
    public static synchronized DatabaseConnection getInstance() {
        if (instance == null) {
            instance = new DatabaseConnection();
        }
        return instance;
    }
    
    // Connect to database
    public void connect() {
        if (!isConnected) {
            System.out.println("Connecting to database: " + connectionString);
            isConnected = true;
            System.out.println("Database connection established");
        } else {
            System.out.println("Already connected to database");
        }
    }
    
    // Disconnect from database
    public void disconnect() {
        if (isConnected) {
            System.out.println("Disconnecting from database");
            isConnected = false;
            System.out.println("Database connection closed");
        } else {
            System.out.println("No active database connection");
        }
    }
    
    // Execute a query (simulated)
    public void executeQuery(String query) {
        if (isConnected) {
            System.out.println("Executing query: " + query);
            System.out.println("Query executed successfully");
        } else {
            System.out.println("Error: No database connection. Please connect first.");
        }
    }
    
    // Get connection status
    public boolean isConnected() {
        return isConnected;
    }
    
    // Get connection string
    public String getConnectionString() {
        return connectionString;
    }
}