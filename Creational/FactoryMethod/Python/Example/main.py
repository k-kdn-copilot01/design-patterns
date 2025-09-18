from road_logistics import RoadLogistics
from sea_logistics import SeaLogistics
from client import client_code

if __name__ == "__main__":
    print("App: Using RoadLogistics")
    client_code(RoadLogistics())

    print("\nApp: Using SeaLogistics")
    client_code(SeaLogistics())
