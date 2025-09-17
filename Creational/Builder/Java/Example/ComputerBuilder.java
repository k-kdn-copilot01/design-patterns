public interface ComputerBuilder {
    ComputerBuilder cpu(String cpuModel);

    ComputerBuilder ram(int gigabytes);

    ComputerBuilder storage(int gigabytes);

    ComputerBuilder gpu(String gpuModel);

    ComputerBuilder powerSupply(String model);

    ComputerBuilder wifi(boolean enabled);

    ComputerBuilder os(String operatingSystem);

    Computer getResult();
}