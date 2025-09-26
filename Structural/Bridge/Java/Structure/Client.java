public class Client {
    public static void runDemo() {
        System.out.println("--- Bridge Pattern: Structure demo ---");
        Implementor implA = new ConcreteImplementorA();
        Implementor implB = new ConcreteImplementorB();

        Abstraction abs = new Abstraction(implA);
        abs.operation("task1"); // uses A

        abs.changeImplementor(implB);
        abs.operation("task2"); // uses B

        RefinedAbstraction ref = new RefinedAbstraction(implA);
        ref.enhancedOperation("prefixX", "payloadX");
    }
}
