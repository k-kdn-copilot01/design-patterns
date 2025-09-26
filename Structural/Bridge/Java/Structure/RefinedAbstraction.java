// RefinedAbstraction adds more behavior but still delegates to the Implementor
public class RefinedAbstraction extends Abstraction {
    public RefinedAbstraction(Implementor implementor) {
        super(implementor);
    }

    public void enhancedOperation(String prefix, String payload) {
        System.out.println("RefinedAbstraction: enhanced operation (" + prefix + ") -> " + payload);
        implementor.operationImpl(prefix + ":" + payload);
    }
}
