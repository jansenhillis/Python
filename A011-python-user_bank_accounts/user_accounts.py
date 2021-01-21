class BankAccount:
    def __init__(self, int_rate = 0, balance = 0):
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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount()

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        new_balance = self.account_balance - amount

        if not new_balance < 0:
            self.account_balance -= amount
        else:
            print("Not enough funds available to withdrawl. Balance Remaining: $", self.account_balance)
        
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self