from bank import Bank


bank = Bank()


kamil = bank.create_account(
    "001",
    "Kamil",
    1000
)


ivan = bank.create_account(
    "002",
    "Ivan",
    500
)


kamil.deposit(500)

kamil.transfer(
    ivan,
    300
)


print(
    "Kamil:",
    kamil.get_balance()
)


print(
    "Ivan:",
    ivan.get_balance()
)


print("\nHistory:")
kamil.show_history()
