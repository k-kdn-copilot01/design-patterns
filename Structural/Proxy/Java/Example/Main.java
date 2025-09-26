/**
 * Image Interface
 * 
 * This interface defines the common operations for both RealImage and ImageProxy.
 */
interface Image {
    void display();
}

/**
 * Real Image Implementation
 * 
 * This represents an expensive image object that takes time to load.
 * In a real application, this would load an actual image file.
 */
class RealImage implements Image {
    private String filename;
    
    public RealImage(String filename) {
        this.filename = filename;
        loadImageFromDisk();
    }
    
    private void loadImageFromDisk() {
        System.out.println("Loading image: " + filename + " from disk...");
        // Simulate loading time
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        System.out.println("Image loaded: " + filename);
    }
    
    @Override
    public void display() {
        System.out.println("Displaying image: " + filename);
    }
}

/**
 * Image Proxy Implementation
 * 
 * This proxy provides lazy loading for expensive image objects.
 * The actual image is only loaded when it's first displayed.
 */
class ImageProxy implements Image {
    private RealImage realImage;
    private String filename;
    
    public ImageProxy(String filename) {
        this.filename = filename;
        System.out.println("ImageProxy created for: " + filename);
    }
    
    @Override
    public void display() {
        // Lazy loading - create real image only when first displayed
        if (realImage == null) {
            realImage = new RealImage(filename);
        }
        realImage.display();
    }
}

/**
 * Main class to demonstrate Image Proxy pattern
 */
public class Main {
    public static void main(String[] args) {
        System.out.println("=== Proxy Design Pattern Demo ===\n");
        
        // Test Image Proxy with lazy loading
        System.out.println("1. Testing Image Proxy (Lazy Loading):");
        ImageProxy imageProxy = new ImageProxy("sample.jpg");
        
        System.out.println("First display call (will load image):");
        imageProxy.display();
        
        System.out.println("\nSecond display call (uses cached image):");
        imageProxy.display();
        
        System.out.println("\n2. Testing Multiple Images:");
        ImageProxy image1 = new ImageProxy("image1.jpg");
        ImageProxy image2 = new ImageProxy("image2.jpg");
        
        System.out.println("Displaying image1:");
        image1.display();
        
        System.out.println("Displaying image2:");
        image2.display();
        
        System.out.println("\n=== Demo Complete ===");
    }
}
