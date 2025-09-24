from Component import Component


class Leaf(Component):
    """
    The Leaf class represents the end objects of a composition. A leaf can't
    have any children.
    
    Usually, it's the Leaf objects that do the actual work, whereas Composite
    objects only delegate to their sub-components.
    """
    
    def __init__(self, name: str):
        super().__init__(name)
    
    def operation(self) -> str:
        """
        Leaf components implement the operation method directly.
        """
        return f"Leaf({self.name})"
    
    def add(self, component: Component) -> None:
        """
        Leaf components cannot have children, so this method raises an exception.
        """
        raise NotImplementedError("Cannot add components to a leaf")
    
    def remove(self, component: Component) -> None:
        """
        Leaf components cannot have children, so this method raises an exception.
        """
        raise NotImplementedError("Cannot remove components from a leaf")
    
    def get_children(self) -> list:
        """
        Leaf components have no children, so this returns an empty list.
        """
        return []
