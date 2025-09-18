public class ConcreteHouseBuilder implements HouseBuilder {
    private House house = new House();

    @Override
    public HouseBuilder buildWalls(int walls) {
        house.setWalls(walls);
        return this;
    }

    @Override
    public HouseBuilder buildDoors(int doors) {
        house.setDoors(doors);
        return this;
    }

    @Override
    public HouseBuilder buildWindows(int windows) {
        house.setWindows(windows);
        return this;
    }

    @Override
    public HouseBuilder buildGarage(boolean hasGarage) {
        house.setHasGarage(hasGarage);
        return this;
    }

    @Override
    public HouseBuilder buildSwimmingPool(boolean hasSwimmingPool) {
        house.setHasSwimmingPool(hasSwimmingPool);
        return this;
    }

    @Override
    public HouseBuilder buildGarden(boolean hasGarden) {
        house.setHasGarden(hasGarden);
        return this;
    }

    @Override
    public HouseBuilder buildRoofType(String roofType) {
        house.setRoofType(roofType);
        return this;
    }

    @Override
    public House getResult() {
        return house;
    }
}
