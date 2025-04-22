"""
PromptBuilder class for generating structured prompts.
"""

from typing import List, Optional, Dict, Any, Union
from llmprompts.src.roles.role import Role
from llmprompts.src.contexts.context import Context
from llmprompts.src.roles.branch import Branch
from llmprompts.src.contexts.question import Question
from llmprompts.src.contexts.requirement import Requirement
from llmprompts.src.roles.department import Department

class PromptBuilder:
    """
    Builder for creating structured analytical prompts.
    
    Attributes:
        title (str): The title of the prompt
        roles (list): List of Role objects
        departments (list): List of Department objects
        context (Context): Context object
        branches (list): List of Branch objects
        questions (list): List of Question objects
        requirements (list): List of Requirement objects
        approach (str): Description of the analytical approach
        output_format (str): Description of the expected output format
    """
    
    def __init__(self, title: str):
        """
        Initialize a new PromptBuilder.
        
        Args:
            title (str): The title of the prompt
        """
        self.title = title
        self.roles: List[Role] = []
        self.departments: List[Department] = []
        self.context: Optional[Context] = None
        self.branches: List[Branch] = []
        self.questions: List[Question] = []
        self.requirements: List[Requirement] = []
        self.approach: str = ""
        self.output_format: str = ""
        
    def add_role(self, role: Role) -> 'PromptBuilder':
        """Add a role to the prompt."""
        self.roles.append(role)
        return self
    
    def add_department(self, department: Department) -> 'PromptBuilder':
        """Add a department to the prompt."""
        self.departments.append(department)
        return self
    
    def add_role_to_department(self, role: Role, department_name: str) -> 'PromptBuilder':
        """Add a role to a specific department."""
        for dept in self.departments:
            if dept.name == department_name:
                dept.add_role(role)
                return self
        
        # If department not found, create a new one and add the role
        new_dept = Department(name=department_name)
        new_dept.add_role(role)
        self.departments.append(new_dept)
        return self
    
    def set_context(self, context: Context) -> 'PromptBuilder':
        """Set the context for the prompt."""
        self.context = context
        return self
    
    def add_branch(self, branch: Branch) -> 'PromptBuilder':
        """Add a branch to the prompt."""
        self.branches.append(branch)
        return self
    
    def add_question(self, question: Question) -> 'PromptBuilder':
        """Add a question to the prompt."""
        self.questions.append(question)
        return self
    
    def add_requirement(self, requirement: Requirement) -> 'PromptBuilder':
        """Add a requirement to the prompt."""
        self.requirements.append(requirement)
        return self
    
    def set_approach(self, approach: str) -> 'PromptBuilder':
        """Set the analytical approach description."""
        self.approach = approach
        return self
    
    def set_output_format(self, output_format: str) -> 'PromptBuilder':
        """Set the expected output format."""
        self.output_format = output_format
        return self
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the prompt to a dictionary representation."""
        result = {
            "title": self.title
        }
        
        if self.roles:
            result["roles"] = [role.to_dict() for role in self.roles]
            
        if self.departments:
            result["departments"] = [dept.to_dict() for dept in self.departments]
            
        if self.context:
            result["context"] = self.context.to_dict()
            
        if self.branches:
            result["branches"] = [branch.to_dict() for branch in self.branches]
            
        if self.questions:
            result["questions"] = [question.to_dict() for question in self.questions]
            
        if self.requirements:
            result["requirements"] = [req.to_dict() for req in self.requirements]
            
        if self.approach:
            result["approach"] = self.approach
            
        if self.output_format:
            result["output_format"] = self.output_format
            
        return result
    
    def build(self) -> str:
        """
        Generate the complete prompt text.
        
        Returns:
            str: The formatted prompt text
        """
        sections = []
        
        # Add title
        sections.append(f"# {self.title}")
        sections.append("")
        
        # Add departments (which include their roles)
        if self.departments:
            sections.append("## Organizational Context")
            for dept in self.departments:
                sections.append(dept.to_prompt_text())
                sections.append("")
        
        # Add standalone roles (not part of any department)
        if self.roles:
            sections.append("## Roles")
            for role in self.roles:
                sections.append(role.to_prompt_text())
                sections.append("")
        
        # Add context
        if self.context:
            sections.append("## Context")
            sections.append(self.context.to_prompt_text())
            sections.append("")
        
        # Add branches
        if self.branches:
            sections.append("## Analysis Structure")
            for branch in self.branches:
                sections.append(branch.to_prompt_text())
                sections.append("")
        
        # Add questions
        if self.questions:
            sections.append("## Questions to Address")
            for question in self.questions:
                sections.append(question.to_prompt_text())
                sections.append("")
        
        # Add requirements
        if self.requirements:
            sections.append("## Requirements")
            for req in self.requirements:
                sections.append(req.to_prompt_text())
                sections.append("")
        
        # Add approach
        if self.approach:
            sections.append("## Approach")
            sections.append(self.approach)
            sections.append("")
        
        # Add output format
        if self.output_format:
            sections.append("## Output Format")
            sections.append(self.output_format)
        
        return "\n".join(sections)