from collections import defaultdict

class BudgetTracker:
    def __init__(self):
        # Store transactions as list of dicts with keys: amount, category, type ('income' or 'expense')
        self.transactions = []

    def add_income(self, amount, category="General"):
        if amount <= 0:
            raise ValueError("Income amount must be positive.")
        self.transactions.append({
            "amount": amount,
            "category": category,
            "type": "income"
        })

    def add_expense(self, amount, category="General"):
        if amount <= 0:
            raise ValueError("Expense amount must be positive.")
        self.transactions.append({
            "amount": amount,
            "category": category,
            "type": "expense"
        })
    
    def get_balance(self):
        income = sum(t["amount"] for t in self.transactions if t["type"] == "income")
        expense = sum(t["amount"] for t in self.transactions if t["type"] == "expense")
        return income - expense

    def get_summary_by_category(self):
        # returns dict with categories as keys and dict with income and expense totals as values
        summary = defaultdict(lambda: {"income": 0.0, "expense": 0.0})
        for t in self.transactions:
            summary[t["category"]][t["type"]] += t["amount"]
        return dict(summary)
    
    def get_total_income(self):
        return sum(t["amount"] for t in self.transactions if t["type"] == "income")

    def get_total_expenses(self):
        return sum(t["amount"] for t in self.transactions if t["type"] == "expense")
