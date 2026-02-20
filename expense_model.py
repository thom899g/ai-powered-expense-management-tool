from dataclasses import dataclass

@dataclass
class Expense:
    """Represents an individual expense with all relevant attributes."""
    date: str
    description: str
    amount: float
    category: str
    is_billable: bool = False
    needs_review: bool = False
    
    def __post_init__(self):
        """Validates the expense upon initialization."""
        if self.amount <= 0:
            raise ValueError("Amount must be positive.")