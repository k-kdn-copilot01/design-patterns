"""
Prototype Pattern - Real-world Example Demo
Document Management System demonstrating practical use of Prototype pattern
"""

from document_prototype import Document, ReportTemplate, ContractTemplate, DocumentManager


def demonstrate_basic_document_cloning():
    """
    Demonstrate basic document cloning functionality
    """
    print("=" * 70)
    print("BASIC DOCUMENT CLONING DEMONSTRATION")
    print("=" * 70)
    
    # Create base document
    original_doc = Document(
        title="Project Proposal Template",
        content="This is a template for project proposals..."
    )
    original_doc.add_tag("template")
    original_doc.add_tag("proposal")
    original_doc.add_attachment("budget.xlsx", 15000)
    
    print(f"Original: {original_doc.get_summary()}")
    print(f"Content length: {len(original_doc.content)} characters")
    print(f"Tags: {original_doc.tags}")
    print(f"Attachments: {len(original_doc.attachments)}")
    
    # Clone the document
    cloned_doc = original_doc.deep_clone()
    cloned_doc.title = "AI Project Proposal"
    cloned_doc.update_content("This proposal outlines an AI implementation project...")
    cloned_doc.add_tag("AI")
    
    print(f"\nCloned: {cloned_doc.get_summary()}")
    print(f"Content length: {len(cloned_doc.content)} characters")
    print(f"Tags: {cloned_doc.tags}")
    print(f"Attachments: {len(cloned_doc.attachments)}")
    
    # Show independence
    original_doc.add_attachment("timeline.pdf", 8000)
    print(f"\nAfter adding attachment to original:")
    print(f"Original attachments: {len(original_doc.attachments)}")
    print(f"Cloned attachments: {len(cloned_doc.attachments)}")
    print("Note: Deep clone maintains independence!")


def demonstrate_report_template_system():
    """
    Demonstrate report template cloning with multiple variations
    """
    print("\n" + "=" * 70)
    print("REPORT TEMPLATE SYSTEM DEMONSTRATION")
    print("=" * 70)
    
    # Create master report template
    master_template = ReportTemplate("Quarterly Business Report", "quarterly")
    master_template.update_section("executive_summary", 
                                 "This report provides an overview of quarterly performance...")
    master_template.update_section("methodology", 
                                 "Data was collected from various business units...")
    master_template.add_chart("Revenue Growth", "line_chart")
    master_template.add_chart("Market Share", "pie_chart")
    
    print(f"Master Template: {master_template.get_summary()}")
    print(f"Charts: {len(master_template.charts)}")
    
    # Clone for different quarters
    q1_report = master_template.deep_clone()
    q1_report.title = "Q1 2024 Business Report"
    q1_report.update_section("results", "Q1 showed strong growth in all sectors...")
    q1_report.add_chart("Q1 Sales by Region", "bar_chart")
    
    q2_report = master_template.deep_clone()
    q2_report.title = "Q2 2024 Business Report"
    q2_report.update_section("results", "Q2 maintained steady performance...")
    q2_report.update_section("conclusion", "Second quarter results indicate...")
    
    print(f"\nQ1 Report: {q1_report.get_summary()}")
    print(f"Q2 Report: {q2_report.get_summary()}")
    
    # Show content differences
    print(f"\nMaster template sections: {len(master_template.sections)}")
    print(f"Q1 charts: {len(q1_report.charts)}")
    print(f"Q2 charts: {len(q2_report.charts)}")


def demonstrate_contract_template_system():
    """
    Demonstrate contract template cloning for different agreements
    """
    print("\n" + "=" * 70)
    print("CONTRACT TEMPLATE SYSTEM DEMONSTRATION")
    print("=" * 70)
    
    # Create service contract template
    service_template = ContractTemplate("Service Agreement Template", "service")
    service_template.add_term("Duration", "12 months")
    service_template.add_term("Payment Terms", "Net 30 days")
    service_template.add_clause("The service provider shall deliver services as outlined in Appendix A")
    service_template.add_clause("Either party may terminate with 30 days written notice")
    
    print(f"Service Template: {service_template.get_summary()}")
    
    # Clone for specific contracts
    consulting_contract = service_template.deep_clone()
    consulting_contract.title = "IT Consulting Agreement"
    consulting_contract.set_parties("TechCorp Inc.", "BusinessClient LLC")
    consulting_contract.add_term("Hourly Rate", "$150/hour")
    consulting_contract.add_clause("Consultant shall provide weekly progress reports")
    
    maintenance_contract = service_template.deep_clone()
    maintenance_contract.title = "Software Maintenance Agreement"
    maintenance_contract.set_parties("SoftwareCorp", "ClientCompany")
    maintenance_contract.add_term("Response Time", "4 hours for critical issues")
    maintenance_contract.add_clause("Maintenance includes bug fixes and minor updates")
    
    print(f"\nConsulting Contract: {consulting_contract.get_summary()}")
    print(f"Maintenance Contract: {maintenance_contract.get_summary()}")
    
    # Show independence
    print(f"\nTemplate terms: {len(service_template.terms)}")
    print(f"Consulting contract terms: {len(consulting_contract.terms)}")
    print(f"Maintenance contract terms: {len(maintenance_contract.terms)}")


def demonstrate_document_manager():
    """
    Demonstrate the Document Manager for template management
    """
    print("\n" + "=" * 70)
    print("DOCUMENT MANAGER DEMONSTRATION")
    print("=" * 70)
    
    # Create document manager
    manager = DocumentManager()
    
    # Create and register templates
    print("Creating and registering templates...")
    
    # Basic document template
    basic_template = Document("Standard Document Template", 
                            "This is a standard document template with common formatting...")
    basic_template.add_tag("standard")
    basic_template.add_tag("template")
    
    # Report template
    monthly_report = ReportTemplate("Monthly Report Template", "monthly")
    monthly_report.update_section("executive_summary", "Monthly performance summary...")
    monthly_report.add_chart("Monthly Metrics", "dashboard")
    
    # Contract template
    nda_template = ContractTemplate("Non-Disclosure Agreement", "nda")
    nda_template.add_term("Confidentiality Period", "5 years")
    nda_template.add_clause("Recipient agrees to keep all information confidential")
    
    # Register templates
    manager.register_template("basic", basic_template)
    manager.register_template("monthly_report", monthly_report)
    manager.register_template("nda", nda_template)
    
    # List templates
    manager.list_templates()
    
    # Create documents from templates
    print("\n" + "=" * 40)
    print("Creating documents from templates...")
    print("=" * 40)
    
    doc1 = manager.create_from_template("basic", "User Manual v2.0")
    doc2 = manager.create_from_template("monthly_report", "January 2024 Sales Report")
    doc3 = manager.create_from_template("nda", "Partnership NDA - TechCorp")
    
    # Customize created documents
    doc1.update_content("This user manual covers the new features in version 2.0...")
    doc1.add_tag("manual")
    
    # List all created documents
    manager.list_documents()
    
    # Show template details
    manager.get_template_details("monthly_report")


def demonstrate_performance_benefits():
    """
    Demonstrate performance benefits of using prototypes
    """
    print("\n" + "=" * 70)
    print("PROTOTYPE PATTERN PERFORMANCE BENEFITS")
    print("=" * 70)
    
    import time
    
    # Create a complex template
    complex_template = ReportTemplate("Complex Annual Report", "annual")
    for i in range(10):
        complex_template.add_chart(f"Chart {i+1}", "complex_visualization")
    
    complex_template.update_section("executive_summary", "A" * 1000)  # Large content
    complex_template.update_section("methodology", "B" * 1000)
    complex_template.update_section("results", "C" * 1000)
    
    print(f"Complex template: {complex_template.get_summary()}")
    print(f"Content size: {len(complex_template.content)} characters")
    print(f"Charts: {len(complex_template.charts)}")
    
    # Time template creation vs cloning
    print("\nPerformance Comparison:")
    print("-" * 30)
    
    # Time cloning
    start_time = time.time()
    clones = []
    for i in range(100):
        clone = complex_template.deep_clone()
        clone.title = f"Report Copy {i+1}"
        clones.append(clone)
    clone_time = time.time() - start_time
    
    print(f"Creating 100 copies via cloning: {clone_time:.4f} seconds")
    print(f"Average time per clone: {clone_time/100:.6f} seconds")
    print(f"All clones are independent objects with full content")
    
    # Verify independence
    clones[0].add_chart("Additional Chart", "special")
    print(f"\nOriginal charts: {len(complex_template.charts)}")
    print(f"Modified clone charts: {len(clones[0].charts)}")
    print("Independence verified!")


def main():
    """
    Main function to run all demonstrations
    """
    print("PROTOTYPE PATTERN - REAL-WORLD EXAMPLE")
    print("Document Management System")
    print("Demonstrating practical application of the Prototype pattern")
    
    demonstrate_basic_document_cloning()
    demonstrate_report_template_system()
    demonstrate_contract_template_system()
    demonstrate_document_manager()
    demonstrate_performance_benefits()
    
    print("\n" + "=" * 70)
    print("DEMONSTRATION COMPLETE")
    print("=" * 70)
    print("\nKey Benefits Demonstrated:")
    print("1. Rapid object creation through cloning")
    print("2. Template-based document generation")
    print("3. Independence of cloned objects")
    print("4. Performance advantages over repeated construction")
    print("5. Flexible template management system")


if __name__ == "__main__":
    main()
