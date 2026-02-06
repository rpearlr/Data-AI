from abc import ABC, abstractmethod

class Account(ABC):
    bank_name = "Secure Bank"  
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self._balance = balance     

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited {amount}")

    def get_balance(self):
        return self._balance

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(Account):

    def withdraw(self, amount):  
        if amount <= self._balance:
            self._balance -= amount
            print(f"Savings Withdraw: {amount}")
        else:
            print("Insufficient funds!")

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account):
        self.accounts[account.acc_no] = account

    def get_account(self, acc_no):
        return self.accounts.get(acc_no)

bank = Bank()

acc1 = SavingsAccount(101, "Rhea", 5000)
acc2 = SavingsAccount(102, "Alex", 2000)

bank.create_account(acc1)
bank.create_account(acc2)

while True:
print("\n1.Deposit  2.Withdraw  3.Balance  4.Exit")
choice = int(input("Choice: "))
acc_no = int(input("Account No: "))

account = bank.get_account(acc_no)

if not account:
    print("Account not found")
    continue

if choice == 1:
    amt = float(input("Amount: "))
    account.deposit(amt)

elif choice == 2:
    amt = float(input("Amount: "))
    account.withdraw(amt)

elif choice == 3:
    print("Balance:", account.get_balance())

elif choice == 4:
    break
