'''TASK1: Write a class BankAccount with methods deposit() and withdraw() and track
balance.'''

class BankAccount:
    def __init__(self,Account_number,balance):
        self.Account_number=Account_number
        self.balance=balance

    def deposit(self,amount):
        if self.balance>0:
            self.balance+=amount
            print(f"New balance is {self.balance}")
        else:
            print("invalid entry")

    def withdraw(self,amount):
        if self.balance>amount:
            self.balance-=amount
            print(f"Remaining balance is {self.balance}")
        else:
            print(f"insufficient balance")


c1=BankAccount("67890",1000)

c1.withdraw(800)

c1.deposit(200)