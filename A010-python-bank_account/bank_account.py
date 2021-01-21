class BankAccount:
    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            print("Cannot deposit that amount: $", amount)
            return self
        
        self.balance += amount
        return self

    def withdraw(self, amount):
        new_balance = self.balance - amount

        if new_balance <= 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self
        
        #withdraw from the account
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Account Balace: ${self.balance}, Interest Rate: {self.int_rate}%")
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self

act1 = BankAccount(0, 1000)
act1.deposit(1000).deposit(500).deposit(500).withdraw(100).yield_interest().display_account_info()

act2 = BankAccount(1.25)
act2.deposit(300).deposit(1).withdraw(100).withdraw(100).withdraw(100).withdraw(3).yield_interest().display_account_info()
