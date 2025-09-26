package Creational.Facade.Java.Structure;

public class Facade {
    private final SubsystemA a;
    private final SubsystemB b;

    public Facade(SubsystemA a, SubsystemB b) {
        this.a = a;
        this.b = b;
    }

    public String start() {
        return "Start -> " + a.operationA() + " | " + b.operationB();
    }

    public String startComplex() {
        return "Complex -> " + a.operationA() + " | " + b.operationB() + " | Done";
    }
}

