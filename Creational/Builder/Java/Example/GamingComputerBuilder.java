public class GamingComputerBuilder implements ComputerBuilder {
    private final Computer computer = new Computer();

    public GamingComputerBuilder() {
        computer.setGpu("NVIDIA RTX 4070");
        computer.setPowerSupply("750W Gold");
    }

    @Override
    public ComputerBuilder cpu(String cpuModel) {
        computer.setCpu(cpuModel);
        return this;
    }

    @Override
    public ComputerBuilder ram(int gigabytes) {
        computer.setRamGb(gigabytes);
        return this;
    }

    @Override
    public ComputerBuilder storage(int gigabytes) {
        computer.setStorageGb(gigabytes);
        return this;
    }

    @Override
    public ComputerBuilder gpu(String gpuModel) {
        computer.setGpu(gpuModel);
        return this;
    }

    @Override
    public ComputerBuilder powerSupply(String model) {
        computer.setPowerSupply(model);
        return this;
    }

    @Override
    public ComputerBuilder wifi(boolean enabled) {
        computer.setWifiEnabled(enabled);
        return this;
    }

    @Override
    public ComputerBuilder os(String operatingSystem) {
        computer.setOperatingSystem(operatingSystem);
        return this;
    }

    @Override
    public Computer getResult() {
        return computer;
    }
}