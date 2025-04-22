"""
Branch class for organizing structured thinking paths in prompts.
"""

from typing import List, Dict, Any, Optional
from llmprompts.src.roles.thought import Thought

class Branch:
    """
    Represents a branch of structured thinking in a prompt.
    
    The Branch class provides a way to organize related thoughts into coherent
    paths of reasoning, allowing for multiple parallel analytical approaches
    or perspectives to be explored.
    
    Attributes:
        name (str): The name or title of the branch
        description (str): Description of what this branch explores
        thoughts (List[Thought]): The thoughts contained in this branch
        owner (str): The role or persona responsible for this branch
        priority (int): Priority level of this branch (1-5, with 5 being highest)
        tags (List[str]): Tags for categorizing or filtering branches
    """
    
    def __init__(
        self, 
        name: str,
        description: str = "",
        thoughts: Optional[List[Thought]] = None,
        owner: str = "",
        priority: int = 3,
        tags: Optional[List[str]] = None
    ):
        """
        Initialize a new Branch.
        
        Args:
            name (str): The name or title of the branch
            description (str, optional): Description of what this branch explores
            thoughts (List[Thought], optional): The thoughts in this branch
            owner (str, optional): The role or persona responsible
            priority (int, optional): Priority level (1-5)
            tags (List[str], optional): Tags for categorizing or filtering
        """
        self.name = name
        self.description = description
        self.thoughts = thoughts or []
        self.owner = owner
        
        # Ensure priority is within valid range
        self.priority = max(1, min(5, priority))
        
        self.tags = tags or []
        
    def add_thought(self, thought: Thought) -> 'Branch':
        """Add a thought to this branch."""
        self.thoughts.append(thought)
        return self
        
    def add_tag(self, tag: str) -> 'Branch':
        """Add a tag to the branch."""
        self.tags.append(tag)
        return self
        
    def set_description(self, description: str) -> 'Branch':
        """Set the description of what this branch explores."""
        self.description = description
        return self
        
    def set_owner(self, owner: str) -> 'Branch':
        """Set the role or persona responsible for this branch."""
        self.owner = owner
        return self
        
    def set_priority(self, priority: int) -> 'Branch':
        """Set the priority level (1-5)."""
        self.priority = max(1, min(5, priority))
        return self
        
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the branch to a dictionary representation.
        
        Returns:
            Dict[str, Any]: Dictionary representation of the branch
        """
        result = {
            "name": self.name,
            "description": self.description,
            "owner": self.owner,
            "priority": self.priority,
            "tags": self.tags
        }
        
        if self.thoughts:
            result["thoughts"] = [t.to_dict() for t in self.thoughts]
            
        return result
    
    def to_prompt_text(self) -> str:
        """
        Generate formatted text representation of this branch for inclusion in a prompt.
        
        Returns:
            str: Formatted branch description for a prompt
        """
        lines = [f"Branch {self.name}:"]
        
        if self.description:
            lines.append(self.description)
            
        if self.owner:
            lines.append(f"Owner: {self.owner}")
            
        # Add all thoughts in this branch
        for thought in self.thoughts:
            lines.append(thought.to_prompt_text(indent_level=1))
            
        return "\n".join(lines)
    
    @classmethod
    def create_domain_expert_branch(cls) -> 'Branch':
        """Factory method to create a domain expert branch template."""
        from analytical_factory.core.thought import Thought, ThoughtType
        
        branch = cls(
            name="Domain Expert Analysis",
            description="Identifying the most important domain-specific problems that need to be addressed.",
            owner="Medical domain expert",
            priority=5,
            tags=["domain expertise", "medical"]
        )
        
        # Add standard thoughts for this branch
        branch.add_thought(Thought(
            "The most important questions regarding the epidemiology of the disease",
            thought_type=ThoughtType.ANALYSIS,
            order=1.1
        ))
        
        branch.add_thought(Thought(
            "Questions regarding problems with the current approach to treatment",
            thought_type=ThoughtType.ANALYSIS,
            order=1.2
        ))
        
        branch.add_thought(Thought(
            "Medical unmet needs requiring attention and research",
            thought_type=ThoughtType.ANALYSIS,
            order=1.3
        ))
        
        return branch
    
    @classmethod
    def create_epidemiologist_branch(cls) -> 'Branch':
        """Factory method to create an epidemiologist branch template."""
        from analytical_factory.core.thought import Thought, ThoughtType
        
        branch = cls(
            name="Epidemiological Analysis",
            description="Modifying domain expert questions and forming scientific and epidemiological questions for OMOP data.",
            owner="Epidemiologist",
            priority=4,
            tags=["epidemiology", "methodology"]
        )
        
        # Add standard thoughts for this branch
        branch.add_thought(Thought(
            "Forming important epidemiological questions based on the current state of affairs from the literature review",
            thought_type=ThoughtType.METHODOLOGY,
            order=2.1
        ))
        
        branch.add_thought(Thought(
            "Translating domain expert questions into epidemiological questions",
            thought_type=ThoughtType.ANALYSIS,
            order=2.2
        ))
        
        branch.add_thought(Thought(
            "Forming requirements for analysis",
            thought_type=ThoughtType.METHODOLOGY,
            order=2.3
        ))
        
        return branch
    
    @classmethod
    def create_developer_branch(cls) -> 'Branch':
        """Factory method to create a developer branch template."""
        from analytical_factory.core.thought import Thought, ThoughtType
        
        branch = cls(
            name="Technical Implementation",
            description="Forming a detailed method for performing analysis.",
            owner="Developer",
            priority=3,
            tags=["technical", "implementation", "methodology"]
        )
        
        # Add standard thoughts for this branch
        branch.add_thought(Thought(
            "The most suitable tools for analysis",
            thought_type=ThoughtType.RECOMMENDATION,
            order=3.1
        ))
        
        branch.add_thought(Thought(
            "Programmatic approaches for analysis",
            thought_type=ThoughtType.METHODOLOGY,
            order=3.2
        ))
        
        branch.add_thought(Thought(
            "Forming the structure of analysis",
            thought_type=ThoughtType.METHODOLOGY,
            order=3.3
        ))
        
        return branch
    
    @classmethod
    def create_director_branch(cls) -> 'Branch':
        """Factory method to create a director branch template."""
        from analytical_factory.core.thought import Thought, ThoughtType
        
        branch = cls(
            name="Strategic Coordination",
            description="Director performs a coordinating function and asks leading questions.",
            owner="Senior Director",
            priority=5,
            tags=["coordination", "strategy", "oversight"]
        )
        
        # Add standard thoughts for this branch
        branch.add_thought(Thought(
            "To the domain expert for focusing",
            thought_type=ThoughtType.QUESTION,
            order=4.1
        ))
        
        branch.add_thought(Thought(
            "Prioritizes the epidemiologist's questions",
            thought_type=ThoughtType.ANALYSIS,
            order=4.2
        ))
        
        branch.add_thought(Thought(
            "Infrastructure assistance to the developer",
            thought_type=ThoughtType.RECOMMENDATION,
            order=4.3
        ))
        
        return branch