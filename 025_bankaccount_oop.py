class BankAccount:
    # specified the account owner name;
    # balance always starts out as 0.0
    def __init__(self, name):
        self.owner = name
        self.balance = 0.0
 
    def getBalance(self):
        return self.balance
 
    # withdraw: subtract the amount from balance
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
 
    # deposit: add the amount to balance
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    


