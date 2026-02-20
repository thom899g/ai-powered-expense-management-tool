import logging
from typing import List, Dict

class ExpenseAnalyzer:
    """Analyzes expenses for cost-saving opportunities."""
    
    def __init__(self):
        self.expenses = []
        
    def add_expense(self, expense: Dict) -> None:
        """Add an expense to the analyzer."""
        try:
            expense_obj = Expense(**expense)
            self.expenses.append(expense_obj)
        except Exception as e:
            logging.error(f"Failed to add expense: {e}")
    
    def analyze_category_spending(self):
        """Analyzes spending per category for cost-saving."""
        categories = {}
        for exp in self.expenses:
            key = exp.category
            if key in categories:
                categories[key]['total'] += exp.amount
            else:
                categories[key] = {'total': exp.amount, 'count': 1}
        
        # Identify high spending categories
        high_spending = []
        for cat, data in categories.items():
            if data['total'] > (sum(v['total'] for v in categories.values()) * 0.2):
                high_spending.append(cat)
        
        return high_spending
    
    def detect_anomalies(self) -> List:
        """Detects anomalies or potential fraud."""
        anomalies = []
        for exp in self.expenses:
            if exp.amount > 1000 and not exp.is_billable:
                anomalies.append(exp)
        return anomalies