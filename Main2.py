class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance}"

    def __add__(self, other):
        if isinstance(other, BankAccount):
            new_balance = self.balance + other.balance
            return BankAccount(f"{self.account_holder} & {other.account_holder}", new_balance)
        return NotImplemented

# Example usage
account_1 = BankAccount("Alice", 500)
account_2 = BankAccount("Bob", 300)

print(account_1)
print(account_2)

merged_account = account_1 + account_2
print(merged_account)
