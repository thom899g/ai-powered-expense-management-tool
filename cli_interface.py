from nlp_processor import NLPCategorizer
from expense_analyzer import ExpenseAnalyzer
import csv

def main():
    categorizer = NLPCategorizer()
    analyzer = ExpenseAnalyzer()
    
    # Sample expenses for testing
    expenses_data = [
        {'date': '2023-10-05', 'description': 'Lunch at 星巴克', 'amount': 15.5},
        {'date': '2023-10-04', 'description': 'Office Supplies', 'amount': 250}
    ]
    
    # Categorize each expense
    for data in expenses_data:
        category = categorizer.categorize_expense(data['description'])
        data['category'] = category
        analyzer.add_expense(data)
    
    # Analyze and output results
    high_spending = analyzer.analyze_category_spending()
    anomalies = analyzer.detect_anomalies()
    
    print("High Spending Categories:", high_spending)
    print("Anomalies Found:", len(anomalies))
    
if __name__ == "__main__":
    main()