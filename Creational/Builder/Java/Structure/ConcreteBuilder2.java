public class ConcreteBuilder2 implements Builder {
    private FinalObject finalObject = new FinalObject();

    @Override
    public Builder buildPart1(String part1) {
        finalObject.setPart1(part1);
        return this;
    }

    @Override
    public Builder buildPart2(String part2) {
        finalObject.setPart2(part2);
        return this;
    }

    @Override
    public Builder buildPart3(String part3) {
        finalObject.setPart3(part3);
        return this;
    }

    @Override
    public FinalObject getResult() {
        return finalObject;
    }
}
