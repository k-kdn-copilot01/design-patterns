public class AdapterPatternDemo {
 
    // Target interface (the interface that the client expects)
    interface Target {
        void request();
    }
 
    // Adaptee (an existing class with an incompatible interface)
    static class Adaptee {
        void specificRequest() {
            System.out.println("Call to specificRequest() of Adaptee");
        }
    }
 
    // Adapter (converts the interface of Adaptee to Target)
    static class Adapter implements Target {
        private Adaptee adaptee;
 
        public Adapter(Adaptee adaptee) {
            this.adaptee = adaptee;
        }
 
        @Override
        public void request() {
            // map the expected interface to the Adaptee’s method
            adaptee.specificRequest();
        }
    }
 
    // Client uses Target (does not care about Adaptee internally)
    public static void main(String[] args) {
        Adaptee adaptee = new Adaptee();
        Target target = new Adapter(adaptee);
 
        // Client only calls request() through the standard interface
        target.request();
    }
}