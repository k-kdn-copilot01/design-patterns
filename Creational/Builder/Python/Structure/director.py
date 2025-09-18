from builder import Builder


class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """
    
    def __init__(self):
        self._builder = None
    
    @property
    def builder(self):
        """Get the current builder"""
        return self._builder
    
    @builder.setter
    def builder(self, builder: Builder):
        """Set the builder to use"""
        self._builder = builder
    
    def build_minimal_viable_product(self):
        """Build a minimal viable product with only part A"""
        self._builder.build_part_a()
    
    def build_full_featured_product(self):
        """Build a full featured product with all parts"""
        self._builder.build_part_a()
        self._builder.build_part_b()
        self._builder.build_part_c()
    
    def build_custom_product(self, parts_to_build):
        """Build a custom product with specified parts"""
        if 'a' in parts_to_build:
            self._builder.build_part_a()
        if 'b' in parts_to_build:
            self._builder.build_part_b()
        if 'c' in parts_to_build:
            self._builder.build_part_c()
