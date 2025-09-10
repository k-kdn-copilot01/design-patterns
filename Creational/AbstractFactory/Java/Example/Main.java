/**
 * Main class demonstrating Abstract Factory with UI Toolkit example
 */
public class Main {
    public static void main(String[] args) {
        System.out.println("=== Example Demo: UI Toolkit Abstract Factory ===\n");
        
        // Windows UI
        System.out.println("1. Creating Windows Application:");
        UIFactory winFactory = new WinFactory();
        Application winApp = new Application(winFactory);
        winApp.render();
        winApp.handleUserInteraction();
        
        // Mac UI  
        System.out.println("2. Creating Mac Application:");
        UIFactory macFactory = new MacFactory();
        Application macApp = new Application(macFactory);
        macApp.render();
        macApp.handleUserInteraction();
        
        System.out.println("=== Example Demo Complete ===");
    }
}