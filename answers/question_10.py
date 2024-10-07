class BankAccount:

    def __init__(self, balance):
        self._balance = balance

    def deposit(self,amount):
        self._balance += amount

    def withdraw(self,amount):
        if amount < self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self._balance


account1 = BankAccount(1000)
account1.deposit(500)
print(account1.get_balance())
account1.withdraw(200)
print(account1.get_balance())
account1.withdraw(1500)

