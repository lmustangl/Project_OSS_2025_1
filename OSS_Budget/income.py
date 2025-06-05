class Income:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"[{self.date}] {self.description}: {self.amount}원"
