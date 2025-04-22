"""
Thought class for representing structured thinking components in prompts.
"""

from typing import List, Dict, Any, Optional
from enum import Enum

class ThoughtType(Enum):
    """Enumeration of different thought types."""
    ANALYSIS = "analysis"
    HYPOTHESIS = "hypothesis"
    CONSIDERATION = "consideration"
    LIMITATION = "limitation"
    IMPLICATION = "implication"
    RECOMMENDATION = "recommendation"
    QUESTION = "question"
    OBSERVATION = "observation"
    INSIGHT = "insight"
    METHODOLOGY = "methodology"

class Thought:
    """
    Represents a structured thinking component in a prompt.
    
    The Thought class provides a way to represent specific thinking steps,
    considerations, or analytical components that should be included in
    the reasoning process.
    
    Attributes:
        content (str): The main content of the thought
        type (ThoughtType): The type of thought
        order (int): The order/sequence number of this thought
        sub_thoughts (List['Thought']): Nested sub-thoughts
        references (List[str]): References or sources supporting this thought
        tags (List[str]): Tags for categorizing or filtering thoughts
    """
    
    def __init__(
        self, 
        content: str,
        thought_type: Any = ThoughtType.CONSIDERATION,
        order: int = 0,
        sub_thoughts: Optional[List['Thought']] = None,
        references: Optional[List[str]] = None,
        tags: Optional[List[str]] = None
    ):
        """
        Initialize a new Thought.
        
        Args:
            content (str): The main content of the thought
            thought_type (Union[ThoughtType, str], optional): The type of thought
            order (int, optional): The order/sequence number
            sub_thoughts (List[Thought], optional): Nested sub-thoughts
            references (List[str], optional): References or sources
            tags (List[str], optional): Tags for categorizing or filtering
        """
        self.content = content
        
        # Handle string or enum for thought_type
        if isinstance(thought_type, str):
            try:
                self.type = ThoughtType(thought_type)
            except ValueError:
                self.type = ThoughtType.CONSIDERATION
        else:
            self.type = thought_type
            
        self.order = order
        self.sub_thoughts = sub_thoughts or []
        self.references = references or []
        self.tags = tags or []
        
    def add_sub_thought(self, thought: 'Thought') -> 'Thought':
        """Add a sub-thought."""
        self.sub_thoughts.append(thought)
        return self
        
    def add_reference(self, reference: str) -> 'Thought':
        """Add a reference or source."""
        self.references.append(reference)
        return self
        
    def add_tag(self, tag: str) -> 'Thought':
        """Add a tag to the thought."""
        self.tags.append(tag)
        return self
        
    def set_order(self, order: int) -> 'Thought':
        """Set the order/sequence number."""
        self.order = order
        return self
        
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the thought to a dictionary representation.
        
        Returns:
            Dict[str, Any]: Dictionary representation of the thought
        """
        result = {
            "content": self.content,
            "type": self.type.value,
            "order": self.order,
            "tags": self.tags
        }
        
        if self.references:
            result["references"] = self.references
            
        if self.sub_thoughts:
            result["sub_thoughts"] = [t.to_dict() for t in self.sub_thoughts]
            
        return result
    
    def to_prompt_text(self, indent_level: int = 0) -> str:
        """
        Generate formatted text representation of this thought for inclusion in a prompt.
        
        Args:
            indent_level (int, optional): Indentation level for formatting
            
        Returns:
            str: Formatted thought text for a prompt
        """
        indent = "  " * indent_level
        
        # Format with order number if available
        if self.order > 0:
            header = f"{indent}Thought {self.order}: {self.content}"
        else:
            header = f"{indent}Thought: {self.content}"
            
        lines = [header]
        
        # Add references if available
        if self.references:
            ref_text = ", ".join(self.references)
            lines.append(f"{indent}References: {ref_text}")
            
        # Add sub-thoughts with increased indentation
        for sub_thought in self.sub_thoughts:
            lines.append(sub_thought.to_prompt_text(indent_level + 1))
            
        return "\n".join(lines)
    
    @classmethod
    def create_analysis(cls, content: str, order: int = 0) -> 'Thought':
        """Factory method to create an analysis thought."""
        return cls(
            content=content,
            thought_type=ThoughtType.ANALYSIS,
            order=order,
            tags=["analysis"]
        )
    
    @classmethod
    def create_consideration(cls, content: str, order: int = 0) -> 'Thought':
        """Factory method to create a consideration thought."""
        return cls(
            content=content,
            thought_type=ThoughtType.CONSIDERATION,
            order=order,
            tags=["consideration"]
        )
    
    @classmethod
    def create_recommendation(cls, content: str, order: int = 0) -> 'Thought':
        """Factory method to create a recommendation thought."""
        return cls(
            content=content,
            thought_type=ThoughtType.RECOMMENDATION,
            order=order,
            tags=["recommendation"]
        )
    
    @classmethod
    def create_limitation(cls, content: str, order: int = 0) -> 'Thought':
        """Factory method to create a limitation thought."""
        return cls(
            content=content,
            thought_type=ThoughtType.LIMITATION,
            order=order,
            tags=["limitation", "constraint"]
        )