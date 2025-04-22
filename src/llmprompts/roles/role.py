"""
Role class for representing expert roles in prompts.
"""

class Role:
    """
    Represents a professional role in a prompt with specific expertise and responsibilities.
    
    Attributes:
        name (str): The name/title of the role (e.g., "Epidemiologist", "Senior Director")
        expertise (str): The domain of expertise for this role
        responsibilities (list): Key responsibilities or functions of this role
        focus_areas (list): Specific areas this role should focus on in analysis
        description (str): Detailed description of the role's perspective and approach
    """
    
    def __init__(self, name, expertise=None, responsibilities=None, focus_areas=None, description=None):
        """
        Initialize a new Role.
        
        Args:
            name (str): The name/title of the role
            expertise (str, optional): The domain of expertise
            responsibilities (list, optional): Key responsibilities
            focus_areas (list, optional): Specific focus areas
            description (str, optional): Detailed description of the role
        """
        self.name = name
        self.expertise = expertise or ""
        self.responsibilities = responsibilities or []
        self.focus_areas = focus_areas or []
        self.description = description or ""
        
    def add_responsibility(self, responsibility):
        """Add a responsibility to this role."""
        self.responsibilities.append(responsibility)
        return self
        
    def add_focus_area(self, focus_area):
        """Add a focus area to this role."""
        self.focus_areas.append(focus_area)
        return self
    
    def set_description(self, description):
        """Set or update the role description."""
        self.description = description
        return self
    
    def to_dict(self):
        """Convert the role to a dictionary representation."""
        return {
            "name": self.name,
            "expertise": self.expertise,
            "responsibilities": self.responsibilities,
            "focus_areas": self.focus_areas,
            "description": self.description
        }
    
    def to_prompt_text(self):
        """
        Generate formatted text representation of this role for inclusion in a prompt.
        
        Returns:
            str: Formatted role description for a prompt
        """
        lines = [f"Role: {self.name}"]
        
        if self.expertise:
            lines.append(f"Expertise: {self.expertise}")
            
        if self.description:
            lines.append(f"\n{self.description}")
            
        if self.responsibilities:
            lines.append("\nResponsibilities:")
            for resp in self.responsibilities:
                lines.append(f"- {resp}")
                
        if self.focus_areas:
            lines.append("\nFocus Areas:")
            for area in self.focus_areas:
                lines.append(f"- {area}")
                
        return "\n".join(lines)    
