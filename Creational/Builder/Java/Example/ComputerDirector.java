public class ComputerDirector {
    public void buildBasicPC(ComputerBuilder builder, String cpu, int ramGb, int storageGb, boolean wifi, String os) {
        builder
                .cpu(cpu)
                .ram(ramGb)
                .storage(storageGb)
                .wifi(wifi)
                .os(os);
    }
}