from Book import Book
from LibraryCatalog import LibraryCatalog
from BookIterator import BookIterator, AvailableBooksIterator, GenreIterator


def create_sample_library():
    """
    Creates a sample library with various books.
    
    Returns:
        LibraryCatalog: A catalog with sample books
    """
    catalog = LibraryCatalog()
    
    # Add some sample books
    books = [
        Book("978-0132350884", "Clean Code", "Robert C. Martin", "Programming", 2008),
        Book("978-0201633610", "Design Patterns", "Gang of Four", "Programming", 1994),
        Book("978-0134685991", "Effective Java", "Joshua Bloch", "Programming", 2017),
        Book("978-1982137274", "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 1925),
        Book("978-0061120084", "To Kill a Mockingbird", "Harper Lee", "Fiction", 1960),
        Book("978-0141439518", "Pride and Prejudice", "Jane Austen", "Fiction", 1813),
        Book("978-0307277671", "The Catcher in the Rye", "J.D. Salinger", "Fiction", 1951),
        Book("978-0062315007", "The Alchemist", "Paulo Coelho", "Fiction", 1988),
        Book("978-0743273565", "The Da Vinci Code", "Dan Brown", "Mystery", 2003),
        Book("978-0061120084", "Gone Girl", "Gillian Flynn", "Mystery", 2012),
    ]
    
    for book in books:
        catalog.add_book(book)
    
    # Borrow some books to demonstrate different states
    catalog.find_book_by_isbn("978-0132350884").borrow()  # Clean Code
    catalog.find_book_by_isbn("978-1982137274").borrow()  # The Great Gatsby
    catalog.find_book_by_isbn("978-0743273565").borrow()  # The Da Vinci Code
    
    return catalog


def demonstrate_library_iteration():
    """
    Demonstrates the Iterator pattern with a real-world library management system.
    """
    print("=== Iterator Design Pattern Demo: Library Management System ===\n")
    
    # Create a sample library
    library = create_sample_library()
    print(f"Library created with {library.get_total_books()} books")
    print(f"Available books: {len(library.get_available_books())}")
    print(f"Borrowed books: {len(library.get_borrowed_books())}")
    print()
    
    # 1. Iterate through all books
    print("1. Iterating through ALL books in the library:")
    print("   " + "="*60)
    all_books_iterator = library.create_iterator()
    book_count = 1
    while all_books_iterator.has_next():
        book = all_books_iterator.next()
        print(f"   {book_count:2d}. {book}")
        book_count += 1
    print()
    
    # 2. Iterate through available books only
    print("2. Iterating through AVAILABLE books only:")
    print("   " + "="*60)
    available_iterator = library.create_available_books_iterator()
    available_count = 1
    while available_iterator.has_next():
        book = available_iterator.next()
        print(f"   {available_count:2d}. {book}")
        available_count += 1
    print()
    
    # 3. Iterate through books by genre
    print("3. Iterating through FICTION books:")
    print("   " + "="*60)
    fiction_iterator = library.create_genre_iterator("Fiction")
    fiction_count = 1
    while fiction_iterator.has_next():
        book = fiction_iterator.next()
        print(f"   {fiction_count:2d}. {book}")
        fiction_count += 1
    print()
    
    print("4. Iterating through PROGRAMMING books:")
    print("   " + "="*60)
    programming_iterator = library.create_genre_iterator("Programming")
    programming_count = 1
    while programming_iterator.has_next():
        book = programming_iterator.next()
        print(f"   {programming_count:2d}. {book}")
        programming_count += 1
    print()
    
    # 4. Demonstrate iterator reset functionality
    print("5. Demonstrating iterator reset functionality:")
    print("   " + "="*60)
    iterator = library.create_iterator()
    
    print("   First iteration (first 3 books):")
    for i in range(3):
        if iterator.has_next():
            book = iterator.next()
            print(f"   - {book.title}")
    
    print(f"   Current position: {iterator.get_current_index()}")
    print("   Resetting iterator...")
    iterator.reset()
    print(f"   Position after reset: {iterator.get_current_index()}")
    
    print("   Second iteration (first 3 books again):")
    for i in range(3):
        if iterator.has_next():
            book = iterator.next()
            print(f"   - {book.title}")
    print()
    
    # 5. Demonstrate dynamic collection changes
    print("6. Demonstrating dynamic collection changes:")
    print("   " + "="*60)
    
    # Add a new book
    new_book = Book("978-0134685991", "Python Crash Course", "Eric Matthes", "Programming", 2019)
    library.add_book(new_book)
    print(f"   Added new book: {new_book.title}")
    
    # Create a new iterator to see the new book
    new_iterator = library.create_iterator()
    print("   Updated library contents:")
    while new_iterator.has_next():
        book = new_iterator.next()
        if book.title == "Python Crash Course":
            print(f"   - {book} (NEW!)")
        else:
            print(f"   - {book.title}")
    print()
    
    # 6. Demonstrate error handling
    print("7. Demonstrating error handling:")
    print("   " + "="*60)
    empty_iterator = library.create_genre_iterator("NonExistentGenre")
    print(f"   Has books in 'NonExistentGenre': {empty_iterator.has_next()}")
    
    try:
        empty_iterator.next()
    except StopIteration as e:
        print(f"   Caught StopIteration: {e}")
    
    print("\n=== Library Management Demo Complete ===")


def demonstrate_iterator_benefits():
    """
    Demonstrates the benefits of using the Iterator pattern.
    """
    print("\n=== Iterator Pattern Benefits Demonstration ===\n")
    
    library = create_sample_library()
    
    print("Benefits of Iterator Pattern:")
    print("1. UNIFORM INTERFACE: Same interface for different iteration types")
    print("   - All books iterator")
    print("   - Available books iterator") 
    print("   - Genre-specific iterator")
    print()
    
    print("2. ENCAPSULATION: Internal collection structure is hidden")
    print("   - Client code doesn't need to know how books are stored")
    print("   - Can change internal storage without affecting client code")
    print()
    
    print("3. MULTIPLE ITERATIONS: Can have multiple iterators simultaneously")
    print("   - Each iterator maintains its own state")
    print("   - Independent iteration progress")
    print()
    
    # Demonstrate multiple simultaneous iterations
    iterator1 = library.create_iterator()
    iterator2 = library.create_genre_iterator("Fiction")
    
    print("4. SIMULTANEOUS ITERATIONS:")
    print("   Iterator 1 (All books) - Iterator 2 (Fiction books)")
    print("   " + "-"*50)
    
    for i in range(3):
        if iterator1.has_next():
            book1 = iterator1.next()
            print(f"   {i+1}. {book1.title[:25]:<25}", end="")
        
        if iterator2.has_next():
            book2 = iterator2.next()
            print(f" | {book2.title[:20]}")
        else:
            print(" | (no more fiction)")
    
    print("\n=== Benefits Demonstration Complete ===")


if __name__ == "__main__":
    demonstrate_library_iteration()
    demonstrate_iterator_benefits()
