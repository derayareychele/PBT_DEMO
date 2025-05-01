import pytest # type: ignore
from budget_tracker import BudgetTracker

def test_add_income_and_get_balance():
    bt = BudgetTracker()
    bt.add_income(1000, "Salary")
    assert bt.get_balance() == 1000
    bt.add_income(500, "Bonus")
    assert bt.get_balance() == 1500