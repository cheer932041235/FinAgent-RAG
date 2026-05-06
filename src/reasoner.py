"""
Financial Reasoning Modules: Chain-of-Thought (CoT) and Program-of-Thought (PoT)

CoT: step-by-step natural language reasoning for simple lookups and single-step questions.
PoT: generates executable Python code for multi-step arithmetic, executed in a sandboxed
     environment to produce deterministic, auditable results.
"""

from typing import Dict, Tuple, Optional


class ChainOfThoughtReasoner:
    """
    Chain-of-Thought reasoning for financial QA.
    
    Generates step-by-step natural language reasoning chains,
    suitable for lookup and single-step arithmetic questions.
    """
    
    def __init__(self, llm_client, prompt_template: Optional[str] = None):
        self.llm = llm_client
        # Prompt template will be released upon acceptance.
        raise NotImplementedError(
            "Full prompt templates will be released upon paper acceptance. "
            "See Appendix A of the paper for template structure."
        )
    
    def reason(self, question: str, evidence: list) -> Tuple[str, str]:
        """
        Generate CoT reasoning and extract answer.
        
        Returns:
            Tuple of (answer_string, reasoning_chain).
        """
        raise NotImplementedError


class ProgramOfThoughtReasoner:
    """
    Program-of-Thought reasoning for financial QA.
    
    Generates executable Python code that performs precise arithmetic
    operations on extracted financial values. Code is executed in a
    sandboxed environment with restricted builtins.
    
    The sandbox restricts:
        - No file I/O, network access, or system calls
        - Only math, statistics, and basic Python builtins allowed
        - Execution timeout of 10 seconds
        - Result must be assigned to a 'result' variable
    """
    
    def __init__(self, llm_client, prompt_template: Optional[str] = None):
        self.llm = llm_client
        raise NotImplementedError(
            "Full prompt templates and sandbox implementation will be "
            "released upon paper acceptance."
        )
    
    def reason(self, question: str, evidence: list) -> Tuple[str, str]:
        """
        Generate PoT program, execute it, and return the result.
        
        Returns:
            Tuple of (answer_string, generated_program).
        """
        raise NotImplementedError
    
    @staticmethod
    def execute_sandbox(code: str, timeout: int = 10) -> Dict:
        """
        Execute generated Python code in a restricted sandbox.
        
        Args:
            code: Python code string to execute.
            timeout: Maximum execution time in seconds.
            
        Returns:
            Dict with 'result', 'success', 'error' keys.
        """
        raise NotImplementedError
