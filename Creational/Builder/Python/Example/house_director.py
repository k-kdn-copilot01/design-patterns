"""
House Director that orchestrates different house construction sequences.
"""

from house_builder import HouseBuilder


class HouseDirector:
    """
    The Director knows which building steps to execute to get a working product.
    It defines several construction sequences for different types of houses.
    """
    
    def __init__(self):
        self._builder = None
    
    @property
    def builder(self) -> HouseBuilder:
        return self._builder
    
    @builder.setter
    def builder(self, builder: HouseBuilder) -> None:
        self._builder = builder
    
    def build_basic_house(self) -> None:
        """
        Build a basic house with essential components only.
        """
        print("🔨 Building basic house...")
        self.builder.build_foundation()
        self.builder.build_walls()
        self.builder.build_roof()
        self.builder.build_windows()
        self.builder.build_doors()
        print("✅ Basic house completed!")
    
    def build_family_house(self) -> None:
        """
        Build a family house with garage and garden.
        """
        print("🔨 Building family house...")
        self.builder.build_foundation()
        self.builder.build_walls()
        self.builder.build_roof()
        self.builder.build_windows()
        self.builder.build_doors()
        self.builder.build_garage()
        self.builder.build_garden()
        print("✅ Family house completed!")
    
    def build_luxury_house(self) -> None:
        """
        Build a luxury house with all premium features.
        """
        print("🔨 Building luxury house...")
        self.builder.build_foundation()
        self.builder.build_walls()
        self.builder.build_roof()
        self.builder.build_windows()
        self.builder.build_doors()
        self.builder.build_garage()
        self.builder.build_garden()
        self.builder.build_pool()
        print("✅ Luxury house completed!")
