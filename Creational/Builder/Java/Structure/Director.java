public class Director {
    public void constructSimpleHouse(HouseBuilder builder) {
        builder.buildWalls(4)
                .buildDoors(1)
                .buildWindows(2)
                .buildGarage(false)
                .buildSwimmingPool(false)
                .buildGarden(false)
                .buildRoofType("gabled");
    }

    public void constructLuxuryHouse(HouseBuilder builder) {
        builder.buildWalls(6)
                .buildDoors(2)
                .buildWindows(8)
                .buildGarage(true)
                .buildSwimmingPool(true)
                .buildGarden(true)
                .buildRoofType("hipped");
    }
}
