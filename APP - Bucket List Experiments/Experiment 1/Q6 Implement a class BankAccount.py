""" Implement a class BankAccount with private attributes balance and account_number. Provide public
methods to deposit and withdraw money, and to check the balance. Ensure that the balance cannot
be set directly from outside the class.
Concepts Covered: Encapsulation, Private Variable """

class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.__account_number = account_number
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount.")
            
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrew:", amount)
        else:
            print("Invalid withdrawal amount or insufficient balance.")
            
    def check_balance(self):
        return self.__balance
        
account = BankAccount("123456789", 1000)

account.deposit(500)

account.withdraw(300)

print("Current Balance:", account.check_balance())
