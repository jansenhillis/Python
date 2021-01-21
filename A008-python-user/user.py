# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")

    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received

    def make_withdrawal(self, amount):
        new_balance = self.account_balance - amount

        if not new_balance < 0:
            self.account_balance -= amount
            # self.display_user_balance()
        else:
            print("Not enough funds available to withdrawl. Balance Remaining: $", self.account_balance)

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        
        self.display_user_balance()
        other_user.display_user_balance()

# Create 3 instances of the User class  
don = User("Don Smith", "don@smith.com")
michelle = User("Michelle Smith", "michelle@smith.com")
gavin = User("Gavin Smith", "gavin@smith.com")

# Have the first user make 3 deposits and 1 withdrawal and then display their balance  
don.make_deposit(100)
don.make_deposit(200)
don.make_deposit(50)
don.make_withdrawal(250)
don.display_user_balance()

# Have the second user make 2 deposits and 2 withdrawals and then display their balance 
michelle.make_deposit(10)
michelle.make_deposit(90)
michelle.make_withdrawal(50)
michelle.make_withdrawal(10)
michelle.display_user_balance()

# Have the third user make 1 deposits and 3 withdrawals and then display their balance
gavin.make_deposit(1000)
gavin.make_withdrawal(100)
gavin.make_withdrawal(100)
gavin.make_withdrawal(100)
gavin.display_user_balance()

# BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
don.transfer_money(gavin, 99)
