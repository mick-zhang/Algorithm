class SavingsAccount:
    
    interest_rate = 1.04
    
    def __init__(self, first, last, accountName, balance):
        self.first = first
        self.last = last
        self.accountName = accountName
        self.balance = balance
        
    def fullname(self):
        return self.first + " " + self.last
    
    def accountname(self):
        return self.accountName
        
    def apply_interest(self):
        self.balance = int(self.balance * self.interest_rate)
        return self.balance
        
    def checkBalance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdrawal(self, amount):
        self.balance -= amount
        return self.balance
        
    def __str__(self):
        return self.first + " " + self.last + "'s " +  self.accountName + " account balance: " + str(self.balance)
    
    def __repr__(self):
        return self.first + " " + self.last + "'s " +  self.accountName + " account balance: " + str(self.balance)
    
class ChequingAccount(SavingsAccount):
    
    interest_rate = 1.01
    
    def __init__(self, first, last, accountName, balance):
        super(ChequingAccount,self).__init__(first, last, accountName, balance)
        
def main():        
    john_1 = SavingsAccount("John", "Smith", "Savings", 5000)
    john_2 = ChequingAccount("John", "Smith", "Chequing", 1000)
    larry_1 = SavingsAccount("Larry", "Wilson", "Savings", 20000)
    larry_2 = ChequingAccount("Larry", "Wilson", "Chequing", 12000)
    
    result = [john_1.fullname(), john_1.accountname(), john_1.checkBalance(),
              john_1.apply_interest(), john_1.deposit(5000), john_1.withdrawal(100),
              john_2.fullname(), john_2.accountname(), john_2.checkBalance(),
              john_2.apply_interest(), john_2.deposit(5000), john_2.withdrawal(100),
              larry_1.fullname(), larry_1.accountname(), larry_1.checkBalance(),
              larry_1.apply_interest(), larry_1.deposit(5000), larry_1.withdrawal(100),
              larry_2.fullname(), larry_2.accountname(), larry_2.checkBalance(),
              larry_2.apply_interest(), larry_2.deposit(5000), larry_2.withdrawal(100)]
    
    for results in result:
        print(results)

main()
