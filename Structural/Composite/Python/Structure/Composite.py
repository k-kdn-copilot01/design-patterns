from typing import List
from Component import Component


class Composite(Component):
    """
    The Composite class represents the complex components that may have
    children. Usually, the Composite objects delegate the actual work to
    their children and then "sum-up" the result.
    """
    
    def __init__(self, name: str):
        super().__init__(name)
        self._children: List[Component] = []
    
    def operation(self) -> str:
        """
        The Composite executes its primary logic in a particular way. It
        traverses recursively through all its children, collecting and
        summing their results. Since the composite's children pass these
        calls to their children and so forth, the whole object tree is
        traversed as a result.
        """
        results = []
        for child in self._children:
            results.append(child.operation())
        
        if results:
            return f"Composite({self.name})[{', '.join(results)}]"
        else:
            return f"Composite({self.name})[]"
    
    def add(self, component: Component) -> None:
        """
        A composite object can add or remove other components (both simple or
        complex) to or from its child list.
        """
        self._children.append(component)
        component.set_parent(self)
    
    def remove(self, component: Component) -> None:
        """
        Remove a component from the children list.
        """
        if component in self._children:
            self._children.remove(component)
            component.set_parent(None)
    
    def get_children(self) -> List[Component]:
        """
        Get all child components.
        """
        return self._children.copy()
    
    def is_composite(self) -> bool:
        """
        Composite components can have children.
        """
        return True
