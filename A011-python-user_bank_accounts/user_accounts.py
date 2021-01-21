class BankAccount:
    def __init__(self, name, int_rate = 0, balance = 0):
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        if amount < 0:
            print("Cannot deposit that amount: $", amount)
            return None
        
        self.balance += amount
        print("Deposited", amount, "into", self.name)
        return self

    def withdraw(self, amount):
        new_balance = self.balance - amount

        if new_balance < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return None
        
        self.balance -= amount
        print("Withdraw:", amount, "from", self.name)

        return self

    def display_account_info(self):
        print(f"Account Name: {self.name} \nBalance: ${self.balance}, Interest Rate: {self.int_rate}%")
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []

    def create_account(self, new_account):
        self.accounts.append(new_account)

    def display_user_balance(self):
        print(f"Accounts for user: {self.name}")
        print("-" * 30)

        for account in self.accounts:
            account.display_account_info()
            
        print("-" * 30 + "\n")
        return self

    # Helper function for account lookup
    def find_account(self, account_name):
        for account in self.accounts:
            if account_name == account.name:
                return account
        return None
                
    def make_deposit(self, account_name, amount):
        account = self.find_account(account_name)

        if account:
            account.deposit(amount)
        else:
            print("Cannot deposit. Account not found:", account_name)
            return None

        return self

    def make_withdraw(self, account_name, amount):
        account = self.find_account(account_name)

        if account: 
            account.withdraw(amount)
        else:
            print("Cannot withdraw. Account not found:", account_name)
            return None
            
        return self

    def transfer_money(self, from_account_name, other_user, to_account_name, amount):
        from_account = self.find_account(from_account_name)
        to_account = other_user.find_account(to_account_name)

        # if these two accounts exist
        if from_account and to_account:
            #if there's enough balance from the sending account
            if from_account.withdraw(amount):
                to_account.deposit(amount)
            else:
                print("Cannot transfer. Not enough funds available.")
                return None
        else:
            print(f"Cannot transfer. Account: '{from_account_name}'' not found.") if to_account else print(f"Cannot transfer. Account: '{to_account_name}'' not found.")
        return self


user1 = User("User 1", "user@1.com")
user1.create_account(BankAccount(name = "checking", int_rate=0.1, balance=9000))
user1.create_account(BankAccount(name = "savings", int_rate=0.05, balance=10))
user1.create_account(BankAccount(name = "retirement", balance=100000))
user1.display_user_balance()
user1.make_deposit("checking", 1000)
user1.display_user_balance()
user1.make_withdraw("savings", 10)
user1.display_user_balance()
user1.make_withdraw("savings", 10)
user1.display_user_balance()

user2 = User("User 2", "user@2.com")
user2.create_account(BankAccount(name = "bozo", int_rate = 0.3, balance = 0))
user2.display_user_balance()

user1.transfer_money(from_account_name = "checking", other_user = user2, to_account_name = "bozo", amount = 5000)
user1.display_user_balance()
user2.display_user_balance()