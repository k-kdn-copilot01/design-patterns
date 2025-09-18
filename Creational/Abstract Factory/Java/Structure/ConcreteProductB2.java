public class ConcreteProductB2 implements AbstractProductB {
    @Override
    public String usefulFunctionB() {
        return "Result of ConcreteProductB2";
    }

    @Override
    public String collaborateWith(AbstractProductA collaborator) {
        return "ConcreteProductB2 collaborating with (" + collaborator.usefulFunctionA() + ")";
    }
}
