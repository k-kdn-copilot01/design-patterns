from FileSystemComponent import FileSystemComponent


class File(FileSystemComponent):
    """
    Represents a file in the file system.
    """
    
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self.size = size
    
    def get_size(self) -> int:
        """
        Return the file size.
        """
        return self.size
    
    def display(self, indent: int = 0) -> str:
        """
        Display the file with proper indentation.
        """
        return "  " * indent + f"📄 {self.name} ({self.size} bytes)"
    
    def add(self, component: FileSystemComponent) -> None:
        """
        Files cannot contain other components.
        """
        raise NotImplementedError("Cannot add components to a file")
    
    def remove(self, component: FileSystemComponent) -> None:
        """
        Files cannot contain other components.
        """
        raise NotImplementedError("Cannot remove components from a file")
    
    def get_children(self) -> list:
        """
        Files have no children.
        """
        return []
