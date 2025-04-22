"""
Department class for representing organizational departments in prompts.
"""

from typing import List, Optional, Dict, Any
from llmprompts.src.roles.role import Role

class Department:
    """
    Represents an organizational department with specific functions and expertise.
    
    Attributes:
        name (str): The name of the department
        mission (str): The department's core mission statement
        functions (list): Key functions or responsibilities of the department
        expertise_areas (list): Areas of specialized knowledge within the department
        description (str): Detailed description of the department's role in the organization
        roles (list): Roles that belong to this department
    """
    
    def __init__(
        self, 
        name: str, 
        mission: Optional[str] = None,
        functions: Optional[List[str]] = None,
        expertise_areas: Optional[List[str]] = None,
        description: Optional[str] = None
    ):
        """
        Initialize a new Department.
        
        Args:
            name (str): The name of the department
            mission (str, optional): The department's core mission statement
            functions (list, optional): Key functions or responsibilities
            expertise_areas (list, optional): Areas of specialized knowledge
            description (str, optional): Detailed description of the department
        """
        self.name = name
        self.mission = mission or ""
        self.functions = functions or []
        self.expertise_areas = expertise_areas or []
        self.description = description or ""
        self.roles: List[Role] = []
        
    def add_function(self, function: str) -> 'Department':
        """Add a function to this department."""
        self.functions.append(function)
        return self
        
    def add_expertise_area(self, expertise_area: str) -> 'Department':
        """Add an expertise area to this department."""
        self.expertise_areas.append(expertise_area)
        return self
    
    def set_description(self, description: str) -> 'Department':
        """Set or update the department description."""
        self.description = description
        return self
    
    def add_role(self, role: Role) -> 'Department':
        """Add a role to this department."""
        self.roles.append(role)
        return self
    
    def get_roles(self) -> List[Role]:
        """Get all roles in this department."""
        return self.roles
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the department to a dictionary representation."""
        return {
            "name": self.name,
            "mission": self.mission,
            "functions": self.functions,
            "expertise_areas": self.expertise_areas,
            "description": self.description,
            "roles": [role.to_dict() for role in self.roles]
        }
    
    def to_prompt_text(self) -> str:
        """
        Generate formatted text representation of this department for inclusion in a prompt.
        
        Returns:
            str: Formatted department description for a prompt
        """
        lines = [f"Department: {self.name}"]
        
        if self.mission:
            lines.append(f"Mission: {self.mission}")
            
        if self.description:
            lines.append(f"\n{self.description}")
            
        if self.functions:
            lines.append("\nKey Functions:")
            for func in self.functions:
                lines.append(f"- {func}")
                
        if self.expertise_areas:
            lines.append("\nAreas of Expertise:")
            for area in self.expertise_areas:
                lines.append(f"- {area}")
        
        if self.roles:
            lines.append("\nDepartment Roles:")
            for role in self.roles:
                # Add role with indentation
                role_text = role.to_prompt_text()
                role_lines = role_text.split('\n')
                indented_role_lines = [f"  {line}" for line in role_lines]
                lines.append('\n'.join(indented_role_lines))
                
        return "\n".join(lines)