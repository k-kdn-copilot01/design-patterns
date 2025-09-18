public interface AbstractProductB {
    String usefulFunctionB();
    // The productB can collaborate with ProductA
    String collaborateWith(AbstractProductA collaborator);
}
