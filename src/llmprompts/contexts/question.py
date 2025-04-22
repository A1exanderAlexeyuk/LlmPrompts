"""
Question class for representing structured questions in prompts.
"""

from typing import List, Dict, Any, Optional, Union
from enum import Enum

class QuestionType(Enum):
    """Enumeration of different question types."""
    OPEN_ENDED = "open_ended"
    ANALYTICAL = "analytical"
    COMPARATIVE = "comparative"
    DIAGNOSTIC = "diagnostic"
    PREDICTIVE = "predictive"
    CAUSAL = "causal"
    EXPLORATORY = "exploratory"
    CONFIRMATORY = "confirmatory"
    STRATEGIC = "strategic"
    TECHNICAL = "technical"

class QuestionCategory(Enum):
    """Enumeration of different question categories."""
    EPIDEMIOLOGY = "epidemiology"
    CLINICAL = "clinical"
    TECHNICAL = "technical"
    BUSINESS = "business"
    RESEARCH = "research"
    OPERATIONAL = "operational"
    REGULATORY = "regulatory"
    ETHICAL = "ethical"
    GENERAL = "general"

class Question:
    """
    Represents a structured question in a prompt.
    
    The Question class provides a way to represent questions with additional
    metadata such as type, category, and follow-up questions.
    
    Attributes:
        text (str): The question text
        type (QuestionType): The type of question
        category (QuestionCategory): The category of the question
        follow_ups (List['Question']): Follow-up questions
        context (str): Additional context specific to this question
        importance (int): Importance rating (1-5, with 5 being most important)
        tags (List[str]): Tags for categorizing or filtering questions
    """
    
    def __init__(
        self, 
        text: str,
        question_type: Union[QuestionType, str] = QuestionType.OPEN_ENDED,
        category: Union[QuestionCategory, str] = QuestionCategory.GENERAL,
        follow_ups: Optional[List['Question']] = None,
        context: str = "",
        importance: int = 3,
        tags: Optional[List[str]] = None
    ):
        """
        Initialize a new Question.
        
        Args:
            text (str): The question text
            question_type (Union[QuestionType, str], optional): The type of question
            category (Union[QuestionCategory, str], optional): The category of the question
            follow_ups (List[Question], optional): Follow-up questions
            context (str, optional): Additional context specific to this question
            importance (int, optional): Importance rating (1-5)
            tags (List[str], optional): Tags for categorizing or filtering
        """
        self.text = text
        
        # Handle string or enum for question_type
        if isinstance(question_type, str):
            try:
                self.type = QuestionType(question_type)
            except ValueError:
                self.type = QuestionType.OPEN_ENDED
        else:
            self.type = question_type
            
        # Handle string or enum for category
        if isinstance(category, str):
            try:
                self.category = QuestionCategory(category)
            except ValueError:
                self.category = QuestionCategory.GENERAL
        else:
            self.category = category
            
        self.follow_ups = follow_ups or []
        self.context = context
        
        # Ensure importance is within valid range
        self.importance = max(1, min(5, importance))
        
        self.tags = tags or []
        
    def add_follow_up(self, question: 'Question') -> 'Question':
        """Add a follow-up question."""
        self.follow_ups.append(question)
        return self
        
    def add_tag(self, tag: str) -> 'Question':
        """Add a tag to the question."""
        self.tags.append(tag)
        return self
        
    def set_context(self, context: str) -> 'Question':
        """Set additional context for this question."""
        self.context = context
        return self
        
    def set_importance(self, importance: int) -> 'Question':
        """Set the importance rating (1-5)."""
        self.importance = max(1, min(5, importance))
        return self
        
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the question to a dictionary representation.
        
        Returns:
            Dict[str, Any]: Dictionary representation of the question
        """
        result = {
            "text": self.text,
            "type": self.type.value,
            "category": self.category.value,
            "importance": self.importance,
            "tags": self.tags
        }
        
        if self.context:
            result["context"] = self.context
            
        if self.follow_ups:
            result["follow_ups"] = [q.to_dict() for q in self.follow_ups]
            
        return result
    
    def to_prompt_text(self, indent_level: int = 0) -> str:
        """
        Generate formatted text representation of this question for inclusion in a prompt.
        
        Args:
            indent_level (int, optional): Indentation level for formatting
            
        Returns:
            str: Formatted question text for a prompt
        """
        indent = "  " * indent_level
        lines = [f"{indent}Question: {self.text}"]
        
        if self.context:
            lines.append(f"{indent}Context: {self.context}")
            
        # Add follow-up questions with increased indentation
        if self.follow_ups:
            lines.append(f"{indent}Follow-up questions:")
            for follow_up in self.follow_ups:
                lines.append(follow_up.to_prompt_text(indent_level + 1))
                
        return "\n".join(lines)
    
    @classmethod
    def create_epidemiological_question(cls, text: str) -> 'Question':
        """Factory method to create an epidemiological question."""
        return cls(
            text=text,
            question_type=QuestionType.ANALYTICAL,
            category=QuestionCategory.EPIDEMIOLOGY,
            tags=["epidemiology", "population health"]
        )
    
    @classmethod
    def create_clinical_question(cls, text: str) -> 'Question':
        """Factory method to create a clinical question."""
        return cls(
            text=text,
            question_type=QuestionType.DIAGNOSTIC,
            category=QuestionCategory.CLINICAL,
            tags=["clinical", "treatment", "diagnosis"]
        )
    
    @classmethod
    def create_technical_question(cls, text: str) -> 'Question':
        """Factory method to create a technical question."""
        return cls(
            text=text,
            question_type=QuestionType.TECHNICAL,
            category=QuestionCategory.TECHNICAL,
            tags=["technical", "implementation", "data"]
        )