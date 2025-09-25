from FileSystemComponent import FileSystemComponent
from File import File
from Directory import Directory


def display_file_system(root: FileSystemComponent) -> None:
    """
    Display the entire file system structure.
    """
    print("File System Structure:")
    print("=" * 50)
    print(root.display())
    print("=" * 50)


def calculate_total_size(component: FileSystemComponent) -> None:
    """
    Calculate and display the total size of a component.
    """
    print(f"Total size of '{component.name}': {component.get_size()} bytes")


def main():
    print("=== Composite Pattern Demo: File System ===\n")
    
    # Create the root directory
    root = Directory("Root")
    
    # Create some files
    readme = File("README.txt", 1024)
    config = File("config.json", 512)
    script = File("script.py", 2048)
    
    # Create subdirectories
    documents = Directory("Documents")
    images = Directory("Images")
    projects = Directory("Projects")
    
    # Create files in Documents
    doc1 = File("report.pdf", 15360)
    doc2 = File("notes.txt", 256)
    
    # Create files in Images
    img1 = File("photo1.jpg", 2048000)
    img2 = File("photo2.png", 1024000)
    
    # Create files in Projects
    project1 = File("main.py", 4096)
    project2 = File("utils.py", 2048)
    
    # Build the file system structure
    print("1. Building file system structure...")
    root.add(readme)
    root.add(config)
    root.add(script)
    root.add(documents)
    root.add(images)
    root.add(projects)
    
    documents.add(doc1)
    documents.add(doc2)
    
    images.add(img1)
    images.add(img2)
    
    projects.add(project1)
    projects.add(project2)
    
    print("File system structure created successfully!\n")
    
    # Display the entire file system
    print("2. Displaying file system structure:")
    display_file_system(root)
    print()
    
    # Calculate sizes
    print("3. Calculating sizes:")
    calculate_total_size(root)
    calculate_total_size(documents)
    calculate_total_size(images)
    calculate_total_size(projects)
    print()
    
    # Demonstrate dynamic operations
    print("4. Dynamic operations:")
    
    # Add a new file to Documents
    new_doc = File("new_document.docx", 8192)
    documents.add(new_doc)
    print(f"Added {new_doc.name} to Documents directory")
    calculate_total_size(documents)
    print()
    
    # Remove a file from Images
    images.remove(img2)
    print(f"Removed {img2.name} from Images directory")
    calculate_total_size(images)
    print()
    
    # Search for a file
    found_file = root.find_file("main.py")
    if found_file:
        print(f"Found file: {found_file.name} ({found_file.get_size()} bytes)")
    else:
        print("File not found")
    print()
    
    # Display final structure
    print("5. Final file system structure:")
    display_file_system(root)
    
    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    main()
