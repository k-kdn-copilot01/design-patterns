"""
Prototype Pattern - Real-world Example
Document Management System using Prototype pattern
"""

from abc import ABC, abstractmethod
import copy
from datetime import datetime
from typing import List, Dict, Any


class DocumentPrototype(ABC):
    """
    Abstract base class for all document prototypes
    """
    
    @abstractmethod
    def clone(self):
        """Clone the document"""
        pass
    
    @abstractmethod
    def get_summary(self):
        """Get document summary"""
        pass


class Document(DocumentPrototype):
    """
    Base Document class with common properties
    """
    
    def __init__(self, title: str, content: str = "", metadata: Dict[str, Any] = None):
        self.title = title
        self.content = content
        self.metadata = metadata or {}
        self.created_at = datetime.now()
        self.modified_at = datetime.now()
        self.version = 1
        self.tags = []
        self.attachments = []
    
    def clone(self):
        """Create a shallow copy of the document"""
        cloned = copy.copy(self)
        cloned.created_at = datetime.now()
        cloned.modified_at = datetime.now()
        cloned.version = 1
        return cloned
    
    def deep_clone(self):
        """Create a deep copy of the document"""
        cloned = copy.deepcopy(self)
        cloned.created_at = datetime.now()
        cloned.modified_at = datetime.now()
        cloned.version = 1
        return cloned
    
    def get_summary(self):
        return f"Document: '{self.title}' (v{self.version}, {len(self.content)} chars)"
    
    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)
    
    def add_attachment(self, filename: str, size: int):
        self.attachments.append({"filename": filename, "size": size, "added_at": datetime.now()})
    
    def update_content(self, new_content: str):
        self.content = new_content
        self.modified_at = datetime.now()
        self.version += 1


class ReportTemplate(Document):
    """
    Report template with specific structure and formatting
    """
    
    def __init__(self, title: str, report_type: str = "monthly"):
        super().__init__(title)
        self.report_type = report_type
        self.sections = {
            "executive_summary": "",
            "introduction": "",
            "methodology": "",
            "results": "",
            "conclusion": "",
            "recommendations": ""
        }
        self.charts = []
        self.tables = []
        self.setup_default_content()
    
    def setup_default_content(self):
        """Setup default report structure"""
        self.content = f"""
# {self.title}
Report Type: {self.report_type.title()}
Generated: {self.created_at.strftime('%Y-%m-%d %H:%M')}

## Executive Summary
{self.sections['executive_summary']}

## Introduction
{self.sections['introduction']}

## Methodology
{self.sections['methodology']}

## Results
{self.sections['results']}

## Conclusion
{self.sections['conclusion']}

## Recommendations
{self.sections['recommendations']}
"""
        self.add_tag("report")
        self.add_tag(self.report_type)
    
    def update_section(self, section: str, content: str):
        if section in self.sections:
            self.sections[section] = content
            self.setup_default_content()  # Regenerate content
    
    def add_chart(self, chart_title: str, chart_type: str):
        self.charts.append({"title": chart_title, "type": chart_type})
    
    def get_summary(self):
        return f"Report: '{self.title}' ({self.report_type}, {len(self.sections)} sections, {len(self.charts)} charts)"


class ContractTemplate(Document):
    """
    Contract template with legal structure
    """
    
    def __init__(self, title: str, contract_type: str = "service"):
        super().__init__(title)
        self.contract_type = contract_type
        self.parties = {"party_a": "", "party_b": ""}
        self.terms = {}
        self.clauses = []
        self.signatures = {}
        self.setup_default_content()
    
    def setup_default_content(self):
        """Setup default contract structure"""
        self.content = f"""
CONTRACT: {self.title}
Type: {self.contract_type.title()} Agreement

PARTIES:
Party A: {self.parties['party_a']}
Party B: {self.parties['party_b']}

TERMS AND CONDITIONS:
{self._format_terms()}

CLAUSES:
{self._format_clauses()}

Date: {self.created_at.strftime('%Y-%m-%d')}
"""
        self.add_tag("contract")
        self.add_tag(self.contract_type)
        self.add_tag("legal")
    
    def _format_terms(self):
        if not self.terms:
            return "Terms to be defined..."
        return "\n".join([f"- {key}: {value}" for key, value in self.terms.items()])
    
    def _format_clauses(self):
        if not self.clauses:
            return "Clauses to be added..."
        return "\n".join([f"{i+1}. {clause}" for i, clause in enumerate(self.clauses)])
    
    def set_parties(self, party_a: str, party_b: str):
        self.parties["party_a"] = party_a
        self.parties["party_b"] = party_b
        self.setup_default_content()
    
    def add_term(self, key: str, value: str):
        self.terms[key] = value
        self.setup_default_content()
    
    def add_clause(self, clause: str):
        self.clauses.append(clause)
        self.setup_default_content()
    
    def get_summary(self):
        return f"Contract: '{self.title}' ({self.contract_type}, {len(self.terms)} terms, {len(self.clauses)} clauses)"


class DocumentManager:
    """
    Document manager that handles prototype registration and cloning
    """
    
    def __init__(self):
        self.templates = {}
        self.documents = []
    
    def register_template(self, name: str, template: DocumentPrototype):
        """Register a document template"""
        self.templates[name] = template
        print(f"Template '{name}' registered: {template.get_summary()}")
    
    def create_from_template(self, template_name: str, new_title: str = None) -> DocumentPrototype:
        """Create a new document from a template"""
        if template_name not in self.templates:
            raise ValueError(f"Template '{template_name}' not found")
        
        template = self.templates[template_name]
        new_doc = template.deep_clone()
        
        if new_title:
            new_doc.title = new_title
            if hasattr(new_doc, 'setup_default_content'):
                new_doc.setup_default_content()
        
        self.documents.append(new_doc)
        return new_doc
    
    def list_templates(self):
        """List all available templates"""
        print("\nAvailable Templates:")
        print("-" * 40)
        for name, template in self.templates.items():
            print(f"- {name}: {template.get_summary()}")
    
    def list_documents(self):
        """List all created documents"""
        print("\nCreated Documents:")
        print("-" * 40)
        for i, doc in enumerate(self.documents, 1):
            print(f"{i}. {doc.get_summary()}")
            print(f"   Created: {doc.created_at.strftime('%Y-%m-%d %H:%M')}")
            print(f"   Tags: {', '.join(doc.tags)}")
    
    def get_template_details(self, template_name: str):
        """Get detailed information about a template"""
        if template_name in self.templates:
            template = self.templates[template_name]
            print(f"\nTemplate Details: {template_name}")
            print("=" * 50)
            print(f"Summary: {template.get_summary()}")
            print(f"Created: {template.created_at.strftime('%Y-%m-%d %H:%M')}")
            print(f"Tags: {', '.join(template.tags)}")
            print(f"Content Preview:\n{template.content[:200]}...")
        else:
            print(f"Template '{template_name}' not found")
