public class Computer {
    private String cpu;
    private int ramGb;
    private int storageGb;
    private String gpu;
    private String powerSupply;
    private boolean wifiEnabled;
    private String operatingSystem;

    public void setCpu(String cpu) {
        this.cpu = cpu;
    }

    public void setRamGb(int ramGb) {
        this.ramGb = ramGb;
    }

    public void setStorageGb(int storageGb) {
        this.storageGb = storageGb;
    }

    public void setGpu(String gpu) {
        this.gpu = gpu;
    }

    public void setPowerSupply(String powerSupply) {
        this.powerSupply = powerSupply;
    }

    public void setWifiEnabled(boolean wifiEnabled) {
        this.wifiEnabled = wifiEnabled;
    }

    public void setOperatingSystem(String operatingSystem) {
        this.operatingSystem = operatingSystem;
    }

    @Override
    public String toString() {
        return "Computer{" +
                "cpu='" + cpu + '\'' +
                ", ramGb=" + ramGb +
                ", storageGb=" + storageGb +
                ", gpu='" + gpu + '\'' +
                ", powerSupply='" + powerSupply + '\'' +
                ", wifiEnabled=" + wifiEnabled +
                ", operatingSystem='" + operatingSystem + '\'' +
                '}';
    }
}