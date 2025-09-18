public class House {
    private int walls;
    private int doors;
    private int windows;
    private boolean hasGarage;
    private boolean hasSwimmingPool;
    private boolean hasGarden;
    private String roofType;

    public void setWalls(int walls) {
        this.walls = walls;
    }

    public void setDoors(int doors) {
        this.doors = doors;
    }

    public void setWindows(int windows) {
        this.windows = windows;
    }

    public void setHasGarage(boolean hasGarage) {
        this.hasGarage = hasGarage;
    }

    public void setHasSwimmingPool(boolean hasSwimmingPool) {
        this.hasSwimmingPool = hasSwimmingPool;
    }

    public void setHasGarden(boolean hasGarden) {
        this.hasGarden = hasGarden;
    }

    public void setRoofType(String roofType) {
        this.roofType = roofType;
    }

    @Override
    public String toString() {
        return "House{" +
                "walls=" + walls +
                ", doors=" + doors +
                ", windows=" + windows +
                ", hasGarage=" + hasGarage +
                ", hasSwimmingPool=" + hasSwimmingPool +
                ", hasGarden=" + hasGarden +
                ", roofType='" + roofType + '\'' +
                '}';
    }
}