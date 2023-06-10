import string
import random

# Bank Class


class Bank:
    def __init__(self):
        self.users = []
        self.admins = []
        self.bank_total_balance = 0
        self.bank_total_loan = 0
        self.loan_features = False

    def create_user(self, name, email, phone, address, nid, initialDeposit, password):
        user = User(name, email, phone, address, nid, initialDeposit, password, self)
        self.users.append(user)
        self.bank_total_balance += initialDeposit
        return user

    def create_admin(self, name, email, password):
        admin = Admin(name, email, password)
        self.admins.append(admin)
        return admin

    def get_total_balance(self):
        return self.bank_total_balance

    def get_total_loan(self):
        return self.bank_total_loan

    def enaORdisa_loan_features(self):  # Corrected method name
        self.loan_features = not self.loan_features
        if self.loan_features:
            return "Loan features are currently available"
        else:
            return "Loan features are currently unavailable"


# User class


class User:
    def __init__(self, name, email, phone, address, nid, initialDeposit, password, bank):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.nid = nid
        self.password = password
        self.account_number = self.generate_account_number()
        self.balance = initialDeposit
        self.transaction_history = []
        self.bank = bank
        self.loanTaken=False

    # generate account number
    def generate_account_number(self):
        return ''.join(random.choices(string.digits + string.ascii_uppercase, k=5))

    # deposit money
    def deposit(self, amount):
        self.balance += amount
        self.bank.bank_total_balance += amount
        self.transaction_history.append(f"Deposited {amount}")
        return f"Deposit of {amount} successful. Your new balance is {self.balance}"

    # withdraw money
    def withdraw(self, amount):
        if self.bank.bank_total_balance < amount:
            return f"BankRupt!!!"
        elif self.balance >= amount:
            self.balance -= amount
            self.bank.bank_total_balance -= amount
            self.transaction_history.append(f"Withdrew {amount}")
            return f"Withdrawal of {amount} successful. Your new balance is {self.balance}"
        else:
            return f"Insufficient balance"

    # transfer money
    def transfer(self, amount, recipient):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(
                f"Transferred {amount} to {recipient.name}")
            return f"{self.name} transferred {amount} to {recipient.name} successfully. Your new balance is {self.balance}"
        else:
            return f"{self.name}, you do not have enough balance to transfer {amount} to {recipient.name}."

    # check balance
    def check_balance(self):
        if self.loanTaken==True:
            return f"{self.name}'s loan is {self.balance * 2}"
        else:
            return f"{self.name}'s current balance is {self.balance}"

    # get transaction history
    def get_transaction_history(self):
        if len(self.transaction_history) > 0:
            return f"{self.name}'s transaction history is {self.transaction_history}"
        else:
            return "No transaction found"

    # get loan
    def get_loan(self):
        if self.bank.bank_total_balance >= self.balance * 2 and self.bank.loan_features:
            self.loanTaken=True
            self.bank.bank_total_loan += self.balance * 2
            self.bank.bank_total_balance -= self.balance * 2
            self.transaction_history.append(f"Loan Taken {self.balance * 2}")
            return f"{self.name}, you have successfully taken a loan of {self.balance * 2}"
        else:
            self.loanTaken=False
            return f"{self.name}, loan not available! Bank balance is not enough for a loan or loan features are not available"

# Admin class


class Admin:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def login(self, email, password):
        if self.email == email and self.password == password:
            return True
        else:
            return False


# admin login check
def admin_login_check(bank, email, password):
    for admin in bank.admins:
        if admin.login(email, password):
            return f"Welcome {admin.name}"
    return "Authentication failed. Invalid email or password."


# user login check
def user_login_check(bank, accountNumber, password):
    for user in bank.users:
        if user.account_number == accountNumber and user.password == password:
            return f"Welcome {user.name}"
    return "Authentication failed. Invalid account number or password."


# main function
bank = Bank()

# creating admins
admin1 = bank.create_admin("admin1", "admin1@gmail.com", "a1")
admin2 = bank.create_admin("admin2", "admin2@gmail.com", "a2")

# checking for admin login
print(admin_login_check(bank, "admin2@gmail.com", "a1"))
print("---------------")
print(admin_login_check(bank, "admin1@gmail.com", "a1"))
print("---------------")

# creating users
user1 = bank.create_user("Sarbajit", "sarbajit@gmail.com", "01315352270", "Savar", "3312420387", 1001, "s1")
user2 = bank.create_user("Bappy", "bappy@gmail.com", "01811638564", "Asulia", "3312420388", 1002, "b1")

# user account numbers
print(f"{user1.name}'s account number is {user1.account_number}")
print("---------------")
print(f"{user2.name}'s account number is {user2.account_number}")
print("---------------")

# checking for user login
print(user_login_check(bank, user1.account_number, "s1"))
print("---------------")
print(user_login_check(bank, user2.account_number, "b2"))
print("---------------")

# check bank total balance
print(f"Bank total balance is {bank.get_total_balance()}")
print("---------------")

# deposit
print(user1.deposit(100))
print("---------------")
print(user2.deposit(200))
print("---------------")

# check bank total balance
print(f"Bank total balance is {bank.get_total_balance()}")
print("---------------")

# withdraw
print(user1.withdraw(50))
print("---------------")
print(user2.withdraw(100))
print("---------------")

# check bank total balance
print(f"Bank total balance is {bank.get_total_balance()}")
print("---------------")

# transfer
print(user1.transfer(50, user2))
print("---------------")
print(user2.transfer(100, user1))
print("---------------")
print(user1.transfer(2000, user2))
print("---------------")

# check bank total balance
print(f"Bank total balance is {bank.get_total_balance()}")
# there is no change in bank total balance because of transfer!!!
print("---------------")

# loan features
print(bank.enaORdisa_loan_features())
print("---------------")
# print(bank.enaORdisa_loan_features())
print("---------------")

# get loan
print(user1.get_loan())
print("---------------")
print(user2.get_loan())
print("---------------")

# check bank total balance
print(f"Bank total balance is {bank.get_total_balance()}")
print("---------------")

# check balance
print(user1.check_balance())
print("---------------")
print(user2.check_balance())
print("---------------")

# bank total loan
print(f"Bank total loan is {bank.get_total_loan()}")
print("---------------")

# bank balance
print(f"Bank total balance is {bank.get_total_balance()}")
print("---------------")

# transaction history
print(user1.get_transaction_history())
print("---------------")
print(user2.get_transaction_history())
print("---------------")

# withdraw to see Bank condition
print(user1.check_balance())
print("---------------")
print(user1.withdraw(1000))
print("---------------")

# create a new user and try to get a loan
user3 = bank.create_user("Sakib", "sakib@gmail.com", "01811638569", "Asulia", "3312420389", 1003, "s3")
print(user3.get_loan())
print("---------------")

# check bank total balance
print(f"Bank total balance is {bank.get_total_balance()}")
print("---------------")
