class Bank :
    def __init__(self,balance):
        self.balance =  balance
        
    def withdraw(self,amount) :
        if amount > self.balance :
            raise ValueError("Amount exceeds balance")
        self.balance-=amount
        return self.balance
    
    def deposit(self,amount) :
        self.balance+=amount
        return self.balance