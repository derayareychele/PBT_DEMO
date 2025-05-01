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
    
from collections import defaultdict

class BudgetTracker:
    def __init__(self):
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
        summary = defaultdict(lambda: {"income": 0.0, "expense": 0.0})
        for t in self.transactions:
            summary[t["category"]][t["type"]] += t["amount"]
        return dict(summary)

    def get_total_income(self):
        return sum(t["amount"] for t in self.transactions if t["type"] == "income")

    def get_total_expenses(self):
        return sum(t["amount"] for t in self.transactions if t["type"] == "expense")
    
def select_category(categories):
    print("Please select a category:")
    for i, cat in enumerate(categories, 1):
        print(f"  {i}. {cat}")
    while True:
        choice = input(f"Enter choice (1-{len(categories)}): ").strip()
        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(categories):
                selected = categories[idx-1]
                if selected == "Other":
                    custom = input("Enter custom category name: ").strip()
                    return custom if custom else "Other"
                else:
                    return selected
        print(f"Invalid choice. Please enter a number between 1 and {len(categories)}.")
    
    
def main():
    income_categories = ["Salary", "Freelance", "Investment", "Gift", "Other"]
    expense_categories = ["Rent", "Food", "Utilities", "Transport", "Entertainment", "Other"]

    bt = BudgetTracker()
    print("=== Personal Budget Tracker ===")

    while True:
        print("\nPlease select an option:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Current Balance")
        print("4. View Total Income and Expenses")
        print("5. View Spending Summary by Category")
        print("6. Exit")

        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            try:
                amount = float(input("Enter income amount: ").strip())
                category = select_category(income_categories)
                bt.add_income(amount, category)
                print(f"Income of ${amount:.2f} added under category '{category}'.")
            except ValueError as e:
                print(f"Invalid input: {e}")

        elif choice == "2":
            try:
                amount = float(input("Enter expense amount: ").strip())
                category = select_category(expense_categories)
                bt.add_expense(amount, category)
                print(f"Expense of ${amount:.2f} added under category '{category}'.")
            except ValueError as e:
                print(f"Invalid input: {e}")

        elif choice == "3":
            balance = bt.get_balance()
            print(f"Current balance: ${balance:.2f}")

        elif choice == "4":
            total_income = bt.get_total_income()
            total_expenses = bt.get_total_expenses()
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expenses: ${total_expenses:.2f}")

        elif choice == "5":
            summary = bt.get_summary_by_category()
            if not summary:
                print("No transactions yet.")
            else:
                print("Spending summary by category:")
                for category, amounts in summary.items():
                    print(f"  {category}: Income ${amounts['income']:.2f}, Expense ${amounts['expense']:.2f}")

        elif choice == "6":
            print("Exiting Personal Budget Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if _name_ == "_main_":
    main()