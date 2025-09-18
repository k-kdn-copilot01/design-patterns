"""
Real-world example demonstration of the Prototype pattern.

This script demonstrates practical usage of the Prototype pattern in a
configuration management system where we need to create multiple similar
configurations with slight variations.
"""

from config_manager import DatabaseConfig, APIConfig, DocumentTemplate, ConfigManager


def demonstrate_database_configs():
    """Demonstrate creating multiple database configurations."""
    print("=== Database Configuration Demo ===")
    
    # Create base database configuration
    base_db_config = DatabaseConfig(
        host="localhost",
        port=5432,
        database="production_db",
        username="admin",
        password="secure_password"
    )
    
    # Create configurations for different environments
    manager = ConfigManager()
    manager.register_prototype("base_db", base_db_config)
    
    # Development environment
    dev_config = manager.create_config("base_db", {
        "host": "dev-server",
        "database": "dev_db",
        "username": "dev_user",
        "password": "dev_password",
        "connection_pool": {"min_connections": 2, "max_connections": 10}
    })
    
    # Testing environment
    test_config = manager.create_config("base_db", {
        "host": "test-server",
        "database": "test_db",
        "username": "test_user",
        "password": "test_password",
        "ssl": {"enabled": True, "cert_path": "/certs/test.crt"}
    })
    
    # Staging environment
    staging_config = manager.create_config("base_db", {
        "host": "staging-server",
        "database": "staging_db",
        "username": "staging_user",
        "password": "staging_password",
        "connection_pool": {"min_connections": 3, "max_connections": 15}
    })
    
    print("\\nDatabase configurations created:")
    print(f"Development: {dev_config}")
    print(f"Testing: {test_config}")
    print(f"Staging: {staging_config}")
    print(f"Production: {base_db_config}")
    print()


def demonstrate_api_configs():
    """Demonstrate creating multiple API configurations."""
    print("=== API Configuration Demo ===")
    
    # Create base API configuration
    base_api_config = APIConfig(
        base_url="https://api.mycompany.com",
        api_key="prod_key_12345",
        version="v2"
    )
    
    manager = ConfigManager()
    manager.register_prototype("base_api", base_api_config)
    
    # Create configurations for different services
    user_service_config = manager.create_config("base_api", {
        "base_url": "https://users.api.mycompany.com",
        "api_key": "user_service_key",
        "timeout": 15,
        "rate_limit": {"requests_per_minute": 200, "burst_limit": 20}
    })
    
    payment_service_config = manager.create_config("base_api", {
        "base_url": "https://payments.api.mycompany.com",
        "api_key": "payment_service_key",
        "timeout": 60,
        "retry_attempts": 5,
        "rate_limit": {"requests_per_minute": 50, "burst_limit": 5}
    })
    
    analytics_service_config = manager.create_config("base_api", {
        "base_url": "https://analytics.api.mycompany.com",
        "api_key": "analytics_service_key",
        "version": "v1",
        "headers": {
            "User-Agent": "AnalyticsApp/2.0",
            "Accept": "application/json",
            "X-Client-Version": "2.0"
        }
    })
    
    print("\\nAPI configurations created:")
    print(f"User Service: {user_service_config}")
    print(f"Payment Service: {payment_service_config}")
    print(f"Analytics Service: {analytics_service_config}")
    print()


def demonstrate_document_templates():
    """Demonstrate creating multiple document templates."""
    print("=== Document Template Demo ===")
    
    # Create base document template
    base_template = DocumentTemplate(
        title="Company Report Template",
        author="HR Department",
        template_type="report"
    )
    
    # Add some base content
    base_template.add_section("Executive Summary", "This section contains the executive summary...")
    base_template.add_section("Introduction", "This section provides an introduction...")
    
    manager = ConfigManager()
    manager.register_prototype("base_report", base_template)
    
    # Create specialized templates
    quarterly_report = manager.create_config("base_report", {
        "title": "Q4 2023 Quarterly Report",
        "author": "Finance Team",
        "metadata": {"version": "1.1", "category": "quarterly"},
        "formatting": {"font_family": "Times New Roman", "font_size": 11}
    })
    quarterly_report.add_section("Financial Performance", "Q4 financial results...")
    
    annual_report = manager.create_config("base_report", {
        "title": "Annual Report 2023",
        "author": "CEO Office",
        "metadata": {"version": "2.0", "category": "annual"},
        "formatting": {"font_family": "Calibri", "font_size": 12, "line_spacing": 1.2}
    })
    annual_report.add_section("Company Overview", "Company overview and mission...")
    annual_report.add_section("Future Outlook", "Strategic plans for next year...")
    
    project_report = manager.create_config("base_report", {
        "title": "Project Alpha Status Report",
        "author": "Project Manager",
        "template_type": "project",
        "metadata": {"version": "1.0", "category": "project"}
    })
    project_report.add_section("Project Status", "Current project status and milestones...")
    project_report.add_section("Risks and Issues", "Identified risks and mitigation plans...")
    
    print("\\nDocument templates created:")
    print(f"Quarterly Report: {quarterly_report}")
    print(f"Annual Report: {annual_report}")
    print(f"Project Report: {project_report}")
    print()


def demonstrate_independence():
    """Demonstrate that cloned objects are independent."""
    print("=== Object Independence Demo ===")
    
    # Create a prototype with nested data
    original = DocumentTemplate("Original Document", "Original Author")
    original.add_section("Section 1", "Original content")
    
    # Clone the prototype
    cloned = original.clone()
    
    # Modify the cloned object
    cloned.update_config({"title": "Modified Document", "author": "Modified Author"})
    cloned.add_section("Section 2", "New content added to clone")
    
    # Show that original is unchanged
    print("\\nOriginal document sections:")
    for section in original.get_config()["content"]["sections"]:
        print(f"  - {section['title']}: {section['content']}")
    
    print("\\nCloned document sections:")
    for section in cloned.get_config()["content"]["sections"]:
        print(f"  - {section['title']}: {section['content']}")
    
    print(f"\\nOriginal title: {original.get_config()['title']}")
    print(f"Cloned title: {cloned.get_config()['title']}")
    print()


def main():
    """Main function to run all demonstrations."""
    print("=== Prototype Pattern Real-World Example Demo ===\\n")
    
    demonstrate_database_configs()
    demonstrate_api_configs()
    demonstrate_document_templates()
    demonstrate_independence()
    
    print("=== Example Demo Complete ===")


if __name__ == "__main__":
    main()
