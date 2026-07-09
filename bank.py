from account import BankAccount


class Bank:

    def __init__(self):
        self.accounts = {}


    def create_account(self, number, owner, balance=0):

        account = BankAccount(
            number,
            owner,
            balance
        )

        self.accounts[number] = account

        return account


    def find_account(self, number):

        return self.accounts.get(number)
