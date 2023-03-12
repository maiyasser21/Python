class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
        print(f"Hello from the constrctor, the account number is {self.account_number} and the balace is {self.balance}")
    
    def __del__(self):
        print("Hello from the destrcutor")
        
ba=BankAccount(77,9000)
        