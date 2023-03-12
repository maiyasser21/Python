class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    
    def getBalance(self):
        return self.__balance
    def deposit(self,amount):
        return (self.__balance + amount)
    def withdraw(self,amount):
        return (self.__balance - amount)
    
b=BankAccount(1000)
print(f'Balance is {b.getBalance()} after deposit {b.deposit(1000)} after withdraw {b.withdraw(50)}')

