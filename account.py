"""
BankAccount logic
"""

import datetime


class BankAccount():
    def __init__(self, balance: float) -> None:
        self.balance = balance
        self.transaction_history = []

    def create_transaction_history_entry(self, amount, balance):
        """
        Formats an entry for the transaction log.
        """
        current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return {"time": current_time, "amount": amount, "balance": balance}

    def deposit(self, amount: float) -> None:
        """
        Adds money to the account
        """
        self.balance += amount
        self.transaction_history.append(self.create_transaction_history_entry(amount, self.balance))

    def withdraw(self, amount: float) -> None:
        """
        Subtracts money from the account.
        """
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(self.create_transaction_history_entry(-amount, self.balance))
        else:
            raise ValueError(f"Insufficient funds to withdraw £{amount:.2f}")


    def transfer(self, amount, other_account) -> None:
        """
        Moves money from one account to another.
        """
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(self.create_transaction_history_entry(-amount, self.balance))
            other_account.balance += amount
            other_account.transaction_history.append(self.create_transaction_history_entry(+amount, other_account.balance))
        else:
            raise ValueError(f"Insufficient funds to transfer £{amount:.2f}")


if __name__ == "__main__":
    reuben_account = BankAccount(0.00)
    alex_account = BankAccount(200.00)
    alex_account.transfer(100.00, reuben_account)