import datetime
from expense import Expense
from income import Income

class Budget:
    def __init__(self):
        self.expenses = []
        self.incomes = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def add_income(self, description, amount):
        today = datetime.date.today().isoformat()
        income = Income(today, description, amount)
        self.incomes.append(income)
        print("수익이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def list_incomes(self):
        if not self.incomes:
            print("수익 내역이 없습니다.\n")
            return
        print("\n[수익 목록]")
        for idx, i in enumerate(self.incomes, 1):
            print(f"{idx}. {i}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")
        return total

    def total_income(self):
        total = sum(i.amount for i in self.incomes)
        print(f"총 수익: {total}원\n")
        return total

    def net_income(self):
        income = self.total_income()
        expense = self.total_spent()
        net = income - expense
        print(f"순이익: {net}원\n")
        return net
