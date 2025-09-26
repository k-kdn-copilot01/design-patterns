package Creational.Facade.Java.Structure;

public class Client {
    public String run() {
        SubsystemA a = new SubsystemA();
        SubsystemB b = new SubsystemB();

        // Direct interaction with subsystems
        String direct = "Direct: " + a.operationA() + " + " + b.operationB();

        // Using the facade
        Facade facade = new Facade(a, b);
        String simple = facade.start();
        String complex = facade.startComplex();

        return String.join(System.lineSeparator(), direct, simple, complex);
    }
}

