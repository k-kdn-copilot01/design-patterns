public interface HouseBuilder {
    HouseBuilder buildWalls(int walls);
    HouseBuilder buildDoors(int doors);
    HouseBuilder buildWindows(int windows);
    HouseBuilder buildGarage(boolean hasGarage);
    HouseBuilder buildSwimmingPool(boolean hasSwimmingPool);
    HouseBuilder buildGarden(boolean hasGarden);
    HouseBuilder buildRoofType(String roofType);
    House getResult();
}