"""
Abstract House Builder and concrete implementations for different house types.
"""

from abc import ABC, abstractmethod
from house import House


class HouseBuilder(ABC):
    """
    Abstract builder interface for constructing houses.
    """
    
    @property
    @abstractmethod
    def house(self) -> House:
        pass
    
    @abstractmethod
    def build_foundation(self) -> None:
        pass
    
    @abstractmethod
    def build_walls(self) -> None:
        pass
    
    @abstractmethod
    def build_roof(self) -> None:
        pass
    
    @abstractmethod
    def build_windows(self) -> None:
        pass
    
    @abstractmethod
    def build_doors(self) -> None:
        pass
    
    @abstractmethod
    def build_garage(self) -> None:
        pass
    
    @abstractmethod
    def build_garden(self) -> None:
        pass
    
    @abstractmethod
    def build_pool(self) -> None:
        pass


class ModernHouseBuilder(HouseBuilder):
    """
    Concrete builder for modern houses with contemporary features.
    """
    
    def __init__(self):
        self.reset()
    
    def reset(self):
        self._house = House()
    
    @property
    def house(self) -> House:
        house = self._house
        self.reset()
        return house
    
    def build_foundation(self) -> None:
        self._house.set_foundation("Reinforced concrete slab")
    
    def build_walls(self) -> None:
        self._house.set_walls("Steel frame with glass panels")
    
    def build_roof(self) -> None:
        self._house.set_roof("Flat roof with solar panels")
    
    def build_windows(self) -> None:
        self._house.set_windows("Floor-to-ceiling smart windows")
    
    def build_doors(self) -> None:
        self._house.set_doors("Automatic sliding glass doors")
    
    def build_garage(self) -> None:
        self._house.set_garage("Underground 2-car smart garage")
    
    def build_garden(self) -> None:
        self._house.set_garden("Minimalist zen garden with automated irrigation")
    
    def build_pool(self) -> None:
        self._house.set_pool("Infinity pool with LED lighting")


class TraditionalHouseBuilder(HouseBuilder):
    """
    Concrete builder for traditional houses with classic features.
    """
    
    def __init__(self):
        self.reset()
    
    def reset(self):
        self._house = House()
    
    @property
    def house(self) -> House:
        house = self._house
        self.reset()
        return house
    
    def build_foundation(self) -> None:
        self._house.set_foundation("Stone and mortar foundation")
    
    def build_walls(self) -> None:
        self._house.set_walls("Brick walls with wooden trim")
    
    def build_roof(self) -> None:
        self._house.set_roof("Sloped roof with clay tiles")
    
    def build_windows(self) -> None:
        self._house.set_windows("Wooden frame casement windows")
    
    def build_doors(self) -> None:
        self._house.set_doors("Solid oak doors with brass hardware")
    
    def build_garage(self) -> None:
        self._house.set_garage("Detached 1-car wooden garage")
    
    def build_garden(self) -> None:
        self._house.set_garden("English cottage garden with flowers")
    
    def build_pool(self) -> None:
        self._house.set_pool("Classic rectangular pool with stone deck")


class EcoFriendlyHouseBuilder(HouseBuilder):
    """
    Concrete builder for eco-friendly houses with sustainable features.
    """
    
    def __init__(self):
        self.reset()
    
    def reset(self):
        self._house = House()
    
    @property
    def house(self) -> House:
        house = self._house
        self.reset()
        return house
    
    def build_foundation(self) -> None:
        self._house.set_foundation("Recycled concrete with radiant heating")
    
    def build_walls(self) -> None:
        self._house.set_walls("Bamboo and recycled steel frame with hemp insulation")
    
    def build_roof(self) -> None:
        self._house.set_roof("Green roof with solar panels and wind turbine")
    
    def build_windows(self) -> None:
        self._house.set_windows("Triple-glazed windows with recycled frames")
    
    def build_doors(self) -> None:
        self._house.set_doors("Reclaimed wood doors with natural finish")
    
    def build_garage(self) -> None:
        self._house.set_garage("Electric vehicle charging station")
    
    def build_garden(self) -> None:
        self._house.set_garden("Permaculture garden with rainwater harvesting")
    
    def build_pool(self) -> None:
        self._house.set_pool("Natural swimming pool with biological filtration")
