/**
 * Subject Interface
 * 
 * This interface defines the common operations that both RealSubject and Proxy must implement.
 */
interface Subject {
    void request();
}

/**
 * Real Subject Implementation
 * 
 * This is the actual object that the proxy represents.
 * It contains the real business logic.
 */
class RealSubject implements Subject {
    public RealSubject() {
        System.out.println("RealSubject created");
    }
    
    @Override
    public void request() {
        System.out.println("RealSubject: Processing request");
    }
}

/**
 * Virtual Proxy Implementation
 * 
 * This proxy creates the real subject only when it's first accessed.
 * This is useful for lazy loading of expensive objects.
 */
class VirtualProxy implements Subject {
    private RealSubject realSubject;
    
    @Override
    public void request() {
        // Lazy initialization - create real subject only when needed
        if (realSubject == null) {
            realSubject = new RealSubject();
        }
        realSubject.request();
        System.out.println("VirtualProxy: Request processed by RealSubject");
    }
}

/**
 * Protection Proxy Implementation
 * 
 * This proxy controls access to the real subject.
 * It can add security checks, logging, or other access control mechanisms.
 */
class ProtectionProxy implements Subject {
    private RealSubject realSubject;
    private boolean hasAccess;
    
    public ProtectionProxy(boolean hasAccess) {
        this.hasAccess = hasAccess;
        this.realSubject = new RealSubject();
    }
    
    @Override
    public void request() {
        if (hasAccess) {
            System.out.println("Access granted");
            realSubject.request();
            System.out.println("ProtectionProxy: Request processed by RealSubject");
        } else {
            System.out.println("Access denied");
            System.out.println("ProtectionProxy: Access denied");
        }
    }
}

/**
 * Main class to demonstrate Proxy pattern implementations
 */
public class Main {
    public static void main(String[] args) {
        System.out.println("=== Structure Demo: Proxy Implementations ===\n");
        
        // Virtual Proxy
        System.out.println("1. Virtual Proxy:");
        VirtualProxy virtualProxy = new VirtualProxy();
        virtualProxy.request();
        virtualProxy.request(); // Second call uses existing instance
        System.out.println();
        
        // Protection Proxy
        System.out.println("2. Protection Proxy:");
        ProtectionProxy protectionProxy1 = new ProtectionProxy(true);
        protectionProxy1.request();
        
        ProtectionProxy protectionProxy2 = new ProtectionProxy(false);
        protectionProxy2.request();
        
        System.out.println("\n=== Structure Demo Complete ===");
    }
}
