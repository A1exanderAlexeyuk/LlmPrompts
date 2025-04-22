"""
Context class for representing background information in prompts.
"""

from typing import List, Dict, Any, Optional

class Context:
    """
    Represents background information and situational context for a prompt.
    
    The Context class provides structured ways to include background information,
    constraints, domain knowledge, and other contextual elements needed for
    the AI to properly understand and respond to a prompt.
    
    Attributes:
        background (str): General background information
        domain (str): The domain or field this context relates to
        constraints (List[str]): Constraints or limitations to consider
        assumptions (List[str]): Assumptions that can be made
        resources (List[str]): Available resources or data sources
        stakeholders (List[str]): Relevant stakeholders
        additional_info (Dict[str, Any]): Any additional contextual information
    """
    
    def __init__(
        self, 
        background: str = "", 
        domain: str = "",
        constraints: Optional[List[str]] = None,
        assumptions: Optional[List[str]] = None,
        resources: Optional[List[str]] = None,
        stakeholders: Optional[List[str]] = None
    ):
        """
        Initialize a new Context.
        
        Args:
            background (str, optional): General background information
            domain (str, optional): The domain or field this context relates to
            constraints (List[str], optional): Constraints or limitations to consider
            assumptions (List[str], optional): Assumptions that can be made
            resources (List[str], optional): Available resources or data sources
            stakeholders (List[str], optional): Relevant stakeholders
        """
        self.background = background
        self.domain = domain
        self.constraints = constraints or []
        self.assumptions = assumptions or []
        self.resources = resources or []
        self.stakeholders = stakeholders or []
        self.additional_info: Dict[str, Any] = {}
        
    def set_background(self, background: str) -> 'Context':
        """Set the background information."""
        self.background = background
        return self
        
    def set_domain(self, domain: str) -> 'Context':
        """Set the domain or field."""
        self.domain = domain
        return self
        
    def add_constraint(self, constraint: str) -> 'Context':
        """Add a constraint to consider."""
        self.constraints.append(constraint)
        return self
        
    def add_assumption(self, assumption: str) -> 'Context':
        """Add an assumption that can be made."""
        self.assumptions.append(assumption)
        return self
        
    def add_resource(self, resource: str) -> 'Context':
        """Add an available resource or data source."""
        self.resources.append(resource)
        return self
        
    def add_stakeholder(self, stakeholder: str) -> 'Context':
        """Add a relevant stakeholder."""
        self.stakeholders.append(stakeholder)
        return self
        
    def add_additional_info(self, key: str, value: Any) -> 'Context':
        """Add additional contextual information."""
        self.additional_info[key] = value
        return self
        
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the context to a dictionary representation.
        
        Returns:
            Dict[str, Any]: Dictionary representation of the context
        """
        result = {
            "background": self.background,
            "domain": self.domain,
            "constraints": self.constraints,
            "assumptions": self.assumptions,
            "resources": self.resources,
            "stakeholders": self.stakeholders
        }
        
        # Add any additional info
        for key, value in self.additional_info.items():
            result[key] = value
            
        return result
    
    def to_prompt_text(self) -> str:
        """
        Generate formatted text representation of this context for inclusion in a prompt.
        
        Returns:
            str: Formatted context description for a prompt
        """
        lines = []
        
        if self.background:
            lines.append(self.background)
            
        if self.domain:
            lines.append(f"Domain: {self.domain}")
            
        if self.constraints:
            lines.append("\nConstraints:")
            for constraint in self.constraints:
                lines.append(f"- {constraint}")
                
        if self.assumptions:
            lines.append("\nAssumptions:")
            for assumption in self.assumptions:
                lines.append(f"- {assumption}")
                
        if self.resources:
            lines.append("\nAvailable Resources:")
            for resource in self.resources:
                lines.append(f"- {resource}")
                
        if self.stakeholders:
            lines.append("\nStakeholders:")
            for stakeholder in self.stakeholders:
                lines.append(f"- {stakeholder}")
                
        # Add any additional info sections
        for key, value in self.additional_info.items():
            if isinstance(value, list):
                lines.append(f"\n{key}:")
                for item in value:
                    lines.append(f"- {item}")
            else:
                lines.append(f"\n{key}: {value}")
                
        return "\n".join(lines)
    
    @classmethod
    def create_medical_research_context(cls) -> 'Context':
        """Factory method to create a medical research context template."""
        return cls(
            background="The company is developing an innovative drug with proven efficacy in phase III clinical trials.",
            domain="Pharmaceutical research",
            resources=["OMOP CDM data", "Phase III clinical trial results"],
            stakeholders=["Medical Affairs department", "Data Science team", "Clinical researchers"]
        )
    
    @classmethod
    def create_data_analysis_context(cls) -> 'Context':
        """Factory method to create a data analysis context template."""
        return cls(
            background="Analysis of large-scale healthcare data to identify patterns and insights.",
            domain="Healthcare data analytics",
            resources=["OMOP Common Data Model", "Electronic Health Records", "Claims data"],
            constraints=[
                "Data privacy regulations (HIPAA/GDPR)",
                "Limited access to patient-level data"
            ]
        )