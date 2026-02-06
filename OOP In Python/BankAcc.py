class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
    def deposit (self, amount):
        self.balance = self.balance+amount
        print(f"Deposit Successfully, New Balance: {self.balance}")
    def withdraw(self,amount):
        if (amount>self.balance):
            print("Insufficient Fund")
            return
        self.balance = self.balance - amount
        print (f"Withdraw Successful, New Balance: {self.balance}")
    def showbalance(self):
        print(f"Current Balance in the Account {self.account_number} is {self.balance}")

acc = BankAccount(98765,'Ben', 67890)
acc.showbalance()
acc.deposit(3000)
acc.withdraw(2000)
acc.withdraw(1000)