"""
House class - a complex product with multiple components.
"""

class House:
    """
    A complex product representing a house with various components.
    """
    
    def __init__(self):
        self.foundation = None
        self.walls = None
        self.roof = None
        self.windows = None
        self.doors = None
        self.garage = None
        self.garden = None
        self.pool = None
    
    def set_foundation(self, foundation: str):
        """Set the foundation type."""
        self.foundation = foundation
    
    def set_walls(self, walls: str):
        """Set the walls material."""
        self.walls = walls
    
    def set_roof(self, roof: str):
        """Set the roof type."""
        self.roof = roof
    
    def set_windows(self, windows: str):
        """Set the windows type."""
        self.windows = windows
    
    def set_doors(self, doors: str):
        """Set the doors type."""
        self.doors = doors
    
    def set_garage(self, garage: str):
        """Set the garage type."""
        self.garage = garage
    
    def set_garden(self, garden: str):
        """Set the garden type."""
        self.garden = garden
    
    def set_pool(self, pool: str):
        """Set the pool type."""
        self.pool = pool
    
    def get_description(self) -> str:
        """Get a detailed description of the house."""
        description = []
        description.append(f"🏠 House Description:")
        description.append(f"  • Foundation: {self.foundation}")
        description.append(f"  • Walls: {self.walls}")
        description.append(f"  • Roof: {self.roof}")
        description.append(f"  • Windows: {self.windows}")
        description.append(f"  • Doors: {self.doors}")
        
        if self.garage:
            description.append(f"  • Garage: {self.garage}")
        if self.garden:
            description.append(f"  • Garden: {self.garden}")
        if self.pool:
            description.append(f"  • Pool: {self.pool}")
        
        return "\n".join(description)
