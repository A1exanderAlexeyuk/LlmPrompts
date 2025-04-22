"""
Requirement class for representing task requirements in prompts.
"""

from typing import List, Dict, Any, Optional
from enum import Enum

class RequirementType(Enum):
    """Enumeration of different requirement types."""
    FUNCTIONAL = "functional"
    TECHNICAL = "technical"
    ANALYTICAL = "analytical"
    PRESENTATION = "presentation"
    COMPLIANCE = "compliance"
    PERFORMANCE = "performance"
    CONSTRAINT = "constraint"
    QUALITY = "quality"

class RequirementPriority(Enum):
    """Enumeration of requirement priorities."""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    OPTIONAL = "optional"

class Requirement:
    """
    Represents a specific requirement or constraint for a prompt task.
    
    The Requirement class provides a structured way to specify what must be
    included, considered, or adhered to in the response to a prompt.
    
    Attributes:
        description (str): Description of the requirement
        type (RequirementType): The type of requirement
        priority (RequirementPriority): The priority level of the requirement
        rationale (str): Explanation of why this requirement exists
        acceptance_criteria (List[str]): Criteria for determining if requirement is met
        tags (List[str]): Tags for categorizing or filtering requirements
    """
    
    def __init__(
        self, 
        description: str,
        requirement_type: Any = RequirementType.FUNCTIONAL,
        priority: Any = RequirementPriority.MEDIUM,
        rationale: str = "",
        acceptance_criteria: Optional[List[str]] = None,
        tags: Optional[List[str]] = None
    ):
        """
        Initialize a new Requirement.
        
        Args:
            description (str): Description of the requirement
            requirement_type (Union[RequirementType, str], optional): The type of requirement
            priority (Union[RequirementPriority, str], optional): The priority level
            rationale (str, optional): Explanation of why this requirement exists
            acceptance_criteria (List[str], optional): Criteria for determining if met
            tags (List[str], optional): Tags for categorizing or filtering
        """
        self.description = description
        
        # Handle string or enum for requirement_type
        if isinstance(requirement_type, str):
            try:
                self.type = RequirementType(requirement_type)
            except ValueError:
                self.type = RequirementType.FUNCTIONAL
        else:
            self.type = requirement_type
            
        # Handle string or enum for priority
        if isinstance(priority, str):
            try:
                self.priority = RequirementPriority(priority)
            except ValueError:
                self.priority = RequirementPriority.MEDIUM
        else:
            self.priority = priority
            
        self.rationale = rationale
        self.acceptance_criteria = acceptance_criteria or []
        self.tags = tags or []
        
    def add_acceptance_criterion(self, criterion: str) -> 'Requirement':
        """Add an acceptance criterion."""
        self.acceptance_criteria.append(criterion)
        return self
        
    def add_tag(self, tag: str) -> 'Requirement':
        """Add a tag to the requirement."""
        self.tags.append(tag)
        return self
        
    def set_rationale(self, rationale: str) -> 'Requirement':
        """Set the rationale for this requirement."""
        self.rationale = rationale
        return self
        
    def set_priority(self, priority: Any) -> 'Requirement':
        """Set the priority level."""
        if isinstance(priority, str):
            try:
                self.priority = RequirementPriority(priority)
            except ValueError:
                self.priority = RequirementPriority.MEDIUM
        else:
            self.priority = priority
        return self
        
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the requirement to a dictionary representation.
        
        Returns:
            Dict[str, Any]: Dictionary representation of the requirement
        """
        result = {
            "description": self.description,
            "type": self.type.value,
            "priority": self.priority.value,
            "tags": self.tags
        }
        
        if self.rationale:
            result["rationale"] = self.rationale
            
        if self.acceptance_criteria:
            result["acceptance_criteria"] = self.acceptance_criteria
            
        return result
    
    def to_prompt_text(self) -> str:
        """
        Generate formatted text representation of this requirement for inclusion in a prompt.
        
        Returns:
            str: Formatted requirement description for a prompt
        """
        lines = [f"Requirement ({self.priority.value}): {self.description}"]
        
        if self.rationale:
            lines.append(f"Rationale: {self.rationale}")
            
        if self.acceptance_criteria:
            lines.append("Acceptance Criteria:")
            for criterion in self.acceptance_criteria:
                lines.append(f"- {criterion}")
                
        return "\n".join(lines)
    
    @classmethod
    def create_analytical_requirement(cls, description: str) -> 'Requirement':
        """Factory method to create an analytical requirement."""
        return cls(
            description=description,
            requirement_type=RequirementType.ANALYTICAL,
            tags=["analysis", "methodology"]
        )
    
    @classmethod
    def create_compliance_requirement(cls, description: str) -> 'Requirement':
        """Factory method to create a compliance requirement."""
        return cls(
            description=description,
            requirement_type=RequirementType.COMPLIANCE,
            priority=RequirementPriority.CRITICAL,
            tags=["compliance", "regulatory"]
        )
    
    @classmethod
    def create_presentation_requirement(cls, description: str) -> 'Requirement':
        """Factory method to create a presentation requirement."""
        return cls(
            description=description,
            requirement_type=RequirementType.PRESENTATION,
            tags=["format", "presentation", "structure"]
        )