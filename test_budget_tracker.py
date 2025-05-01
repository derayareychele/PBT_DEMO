import pytest # type: ignore
from budget_tracker import BudgetTracker

def test_add_income_and_get_balance():
    bt = BudgetTracker()
    bt.add_income(1000, "Salary")
    assert bt.get_balance() == 1000
    bt.add_income(500, "Bonus")
    assert bt.get_balance() == 1500

def test_add_expense_and_get_balance():
    bt = BudgetTracker()
    bt.add_income(1000)
    bt.add_expense(200, "Food")
    assert bt.get_balance() == 800
    bt.add_expense(100)
    assert bt.get_balance() == 700

def test_summary_by_category():
    bt = BudgetTracker()
    bt.add_income(1000, "Salary")
    bt.add_income(100, "Gift")
    bt.add_expense(200, "Food")
    bt.add_expense(50, "Transport")
    summary = bt.get_summary_by_category()
    assert summary["Salary"]["income"] == 1000
    assert summary["Gift"]["income"] == 100
    assert summary["Food"]["expense"] == 200
    assert summary["Transport"]["expense"] == 50

def test_total_income_and_expenses():
    bt = BudgetTracker()
    bt.add_income(500)
    bt.add_income(500)
    bt.add_expense(100)
    assert bt.get_total_income() == 1000
    assert bt.get_total_expenses() == 100

def test_invalid_income_expense_amount():
    bt = BudgetTracker()
    with pytest.raises(ValueError):
        bt.add_income(-100)
    with pytest.raises(ValueError):
        bt.add_expense(0)

def test_balance_after_multiple_transactions():
    bt = BudgetTracker()
    bt.add_income(1000)
    bt.add_expense(200)
    bt.add_income(300)
    bt.add_expense(100)
    assert bt.get_balance() == 1000
