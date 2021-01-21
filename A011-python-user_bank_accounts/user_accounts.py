class BankAccount:
    def __init__(self, name, int_rate = 0, balance = 0):
        self.name = name
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
        
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Account Name: {self.name} \nBalance: ${self.balance}, Interest Rate: {self.int_rate}%")
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self

class User:
    accounts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def create_account(self, new_account):
        self.accounts.append(new_account)

    def display_user_balance(self):
        print(f"Accounts for user: {self.name}")
        for account in self.accounts:
            account.display_account_info()

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

user1 = User("User 1", "user@1.com")
user1.create_account(BankAccount(name = "checking", int_rate=0.1, balance=9000))
user1.create_account(BankAccount(name = "savings", int_rate=0.05, balance=10))
user1.create_account(BankAccount(name = "retirement", balance=100000))
user1.display_user_balance()