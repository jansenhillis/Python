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
    accounts = []

    def __init__(self, name, email, accounts):
        self.name = name
        self.email = email

    def create_account(new_account):
        accounts.append(new_account)
        print(accounts)

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account.balance}")
        return self

    def make_deposit(self, amount):
        self.account.balance += amount
        return self

    def make_withdrawal(self, amount):
        new_balance = self.account.balance - amount

        if not new_balance < 0:
            self.account.balance -= amount
        else:
            print("Not enough funds available to withdrawl. Balance Remaining: $", self.account_balance)
        
        return self

    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.account.balance += amount
        return self

user1 = User("User 1", "user@1.com", BankAccount(0.05, 1000))
user1.display_user_balance()