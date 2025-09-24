"""
Main demonstration of Proxy pattern with real-world example.
Shows file access control, logging, and caching functionality.
"""

import os
import tempfile
from FileAccess import FileAccessProxy, RealFileAccess


def create_test_files():
    """Create test files for demonstration."""
    # Create a temporary directory for test files
    temp_dir = tempfile.mkdtemp()
    
    # Create test files
    test_file1 = os.path.join(temp_dir, "public.txt")
    test_file2 = os.path.join(temp_dir, "private.txt")
    
    with open(test_file1, 'w', encoding='utf-8') as f:
        f.write("This is a public file that everyone can read.")
    
    with open(test_file2, 'w', encoding='utf-8') as f:
        f.write("This is a private file with sensitive information.")
    
    return temp_dir, test_file1, test_file2


def demonstrate_file_access_proxy():
    """Demonstrate the file access proxy with different user roles."""
    
    print("=== Proxy Pattern Real-World Example: File Access Control ===\n")
    
    # Create test files
    temp_dir, public_file, private_file = create_test_files()
    print(f"Created test files in: {temp_dir}\n")
    
    try:
        # 1. Demonstrate direct access (without proxy)
        print("1. Direct File Access (without proxy):")
        print("-" * 50)
        real_access = RealFileAccess()
        content = real_access.read_file(public_file)
        print(f"Content: {content}\n")
        
        # 2. Demonstrate guest access through proxy
        print("2. Guest Access through Proxy:")
        print("-" * 50)
        guest_proxy = FileAccessProxy("guest")
        
        # Guest can read
        print("Guest reading public file:")
        content = guest_proxy.read_file(public_file)
        print(f"Content: {content}\n")
        
        # Guest cannot write
        print("Guest trying to write file:")
        success = guest_proxy.write_file(public_file, "Modified content")
        print(f"Write successful: {success}\n")
        
        # 3. Demonstrate user access through proxy
        print("3. User Access through Proxy:")
        print("-" * 50)
        user_proxy = FileAccessProxy("user")
        
        # User can read
        print("User reading public file:")
        content = user_proxy.read_file(public_file)
        print(f"Content: {content}\n")
        
        # User can write
        print("User writing to file:")
        success = user_proxy.write_file(public_file, "Content modified by user")
        print(f"Write successful: {success}\n")
        
        # 4. Demonstrate admin access through proxy
        print("4. Admin Access through Proxy:")
        print("-" * 50)
        admin_proxy = FileAccessProxy("admin")
        
        # Admin can read
        print("Admin reading public file:")
        content = admin_proxy.read_file(public_file)
        print(f"Content: {content}\n")
        
        # Admin can write
        print("Admin writing to file:")
        success = admin_proxy.write_file(public_file, "Content modified by admin")
        print(f"Write successful: {success}\n")
        
        # 5. Demonstrate caching functionality
        print("5. Caching Functionality:")
        print("-" * 50)
        print("First read (will be cached):")
        content1 = user_proxy.read_file(public_file)
        print(f"Content: {content1}\n")
        
        print("Second read (from cache):")
        content2 = user_proxy.read_file(public_file)
        print(f"Content: {content2}\n")
        
        # 6. Show access logs
        print("6. Access Logs:")
        print("-" * 50)
        print("Guest access log:")
        for log_entry in guest_proxy.get_access_log():
            print(f"  {log_entry}")
        print()
        
        print("User access log:")
        for log_entry in user_proxy.get_access_log():
            print(f"  {log_entry}")
        print()
        
        print("Admin access log:")
        for log_entry in admin_proxy.get_access_log():
            print(f"  {log_entry}")
        print()
        
        # 7. Demonstrate error handling
        print("7. Error Handling:")
        print("-" * 50)
        print("Trying to read non-existent file:")
        content = user_proxy.read_file("nonexistent.txt")
        print(f"Content: {content}\n")
        
    finally:
        # Clean up test files
        import shutil
        shutil.rmtree(temp_dir)
        print(f"Cleaned up test files in: {temp_dir}")
    
    print("\n=== Real-World Example Demo Complete ===")


def demonstrate_proxy_benefits():
    """Demonstrate the benefits of using Proxy pattern."""
    
    print("\n=== Proxy Pattern Benefits Demonstration ===\n")
    
    print("Benefits of Proxy Pattern:")
    print("1. Access Control: Different user roles have different permissions")
    print("2. Lazy Loading: RealFileAccess is created only when needed")
    print("3. Caching: Frequently accessed files are cached for performance")
    print("4. Logging: All file access attempts are logged for security")
    print("5. Error Handling: Centralized error handling and validation")
    print("6. Interface Consistency: Proxy implements the same interface as RealSubject")
    
    print("\nReal-world use cases:")
    print("- Database connection pooling")
    print("- Web service API rate limiting")
    print("- Image loading with lazy loading and caching")
    print("- Security access control systems")
    print("- Remote object access (RMI, CORBA)")


if __name__ == "__main__":
    demonstrate_file_access_proxy()
    demonstrate_proxy_benefits()
