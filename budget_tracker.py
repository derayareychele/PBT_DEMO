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