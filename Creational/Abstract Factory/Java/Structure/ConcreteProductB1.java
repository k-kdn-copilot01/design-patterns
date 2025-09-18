public class ConcreteProductB1 implements AbstractProductB {
    @Override
    public String usefulFunctionB() {
        return "Result of ConcreteProductB1";
    }

    @Override
    public String collaborateWith(AbstractProductA collaborator) {
        return "ConcreteProductB1 collaborating with (" + collaborator.usefulFunctionA() + ")";
    }
}
