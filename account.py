class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self._balance = balance
        self.history = []

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.history.append(
                f"Deposit: +{amount}"
            )
            return True

        return False

    def withdraw(self, amount):
        if amount <= 0:
            return False

        if amount > self._balance:
            return False

        self._balance -= amount
        self.history.append(
            f"Withdraw: -{amount}"
        )

        return True

    def transfer(self, other_account, amount):
        if self.withdraw(amount):
            other_account.deposit(amount)

            self.history.append(
                f"Transfer to {other_account.account_number}: {amount}"
            )

            return True

        return False


    def get_balance(self):
        return self._balance


    def show_history(self):
        for operation in self.history:
            print(operation)
