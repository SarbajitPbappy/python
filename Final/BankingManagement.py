import random
import string
class Bank:
    def __init__(self):
        self.users = []
        self.admins = []
        self.total_balance = 0
        self.total_loan = 0
        self.loan_features = True

    def create_user(self, name, email, address, nid, opening_deposit, account_type,password):
        user = User(name, email, address, nid, opening_deposit, account_type,password)
        self.users.append(user)
        self.total_balance += opening_deposit
        return user

    def create_admin(self, name, email, password):
        admin = Admin(name, email, password)
        self.admins.append(admin)

    def get_total_balance(self):
        return self.total_balance

    def get_total_loan(self):
        return self.total_loan

    def toggle_loan_features(self):
        self.loan_features = not self.loan_features


class User:
    def __init__(self, name, email, address, nid, opening_deposit, account_type,password):
        self.name = name
        self.email = email
        self.address = address
        self.nid = nid
        self.opening_deposit = opening_deposit
        self.account_type = account_type
        self.password = password
        self.account_number = self.generate_account_number()
        self.balance = self.opening_deposit
        self.transaction_history = []

    def generate_account_number(self):
        account_number = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=10))
        return account_number

    def deposit(self, amount):
        self.balance += amount
        return f"Your new balance is {self.balance}"

    def withdraw(self, amount,bank):
        if bank.total_balance < 0:
            return "Bankrupt!! Vikka Daw"
        if self.balance < amount:
            return "Insufficient Balance"
        else:
            self.balance -= amount
            return f"Your new balance is {self.balance}"

    def check_balance(self):
        return f"Your current balance is {self.balance}"

    def transfer(self, amount, bank, recipient_account_number):
        if self.balance < amount:
            return "Insufficient Balance"
        recipient = None
        for user in bank.users:
            if user.account_number == recipient_account_number:
                recipient = user
                break
        if recipient is None:
            return "Recipient account not found"
        self.balance -= amount
        recipient.balance += amount
        self.transaction_history.append(
            f"Transferred {amount} to {recipient.name} ({recipient_account_number})")
        recipient.transaction_history.append(
            f"Received {amount} from {self.name} ({self.account_number})")

        return f"Successfully transferred {amount} to {recipient.name} ({recipient_account_number})"

    def transaction_history(self):
        for transaction in self.transaction_history:
            print(transaction)

    def take_loan(self, bank):
        if not bank.loan_features:
            if self.balance < 10000:
                if bank.total_balance < self.balance * 2:
                    return "You are not eligible for a loan"
        else:
            loan_amount = self.balance * 2
            self.balance += loan_amount
            bank.total_loan += loan_amount
            bank.total_balance -= loan_amount
            return f"Loan taken successfully. Your new balance is {self.balance}"


class Admin:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def login(self, email, password):
        return self.email == email and self.password == password


def admin_login(bank):
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    for admin in bank.admins:
        if admin.login(email, password):
            return True
    return False


myBank = Bank()

while True:
    print("Welcome to the Bank")
    print("1. Admin Login")
    print("2. User Login")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        admin_login_choice = input("Are you an admin? (y/n): ")
        if admin_login_choice == 'y':
            if admin_login(myBank):
                print("Login Successful")
                while True:
                    print("Options:")
                    print("1. Check total balance of the bank")
                    print("2. Check total loan of the bank")
                    print("3. Turn on/off loan features")
                    print("4. Logout")
                    admin_choice = int(input("Enter your choice: "))

                    if admin_choice == 1:
                        print(f"Total balance of the bank is {myBank.get_total_balance()}")
                    elif admin_choice == 2:
                        print(f"Total loan of the bank is {myBank.get_total_loan()}")
                    elif admin_choice == 3:
                        myBank.toggle_loan_features()
                        if myBank.loan_features:
                            print("Loan features turned on")
                        else:
                            print("Loan features turned off")
                    elif admin_choice == 4:
                        print("Logged out successfully")
                        break
                    else:
                        print("Invalid Choice")
            else:
                print("Login Failed")
        elif admin_login_choice == 'n':
            print("You are not an admin")
            create_admin_choice = input("Do you want to create an admin account? (y/n): ")
            if create_admin_choice == 'y':
                name = input("Enter your name: ")
                email = input("Enter your email: ")
                password = input("Enter your password: ")
                myBank.create_admin(name, email, password)
                print("Admin account created successfully")
            elif create_admin_choice == 'n':
                print("Thank You")
            else:
                print("Invalid Choice")
        else:
            print("Invalid Choice")

    elif choice == 2:
        print("1. Create an account")
        print("2. Login to your account")
        user_choice = int(input("Enter your choice: "))

        if user_choice == 1:
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            nid = input("Enter your NID: ")
            opening_deposit = int(input("Enter your opening deposit: "))
            account_type = input("Enter your account type: ")
            password = input("Enter your password: ")
            user = myBank.create_user(name, email, address, nid, opening_deposit, account_type,password)
            print("Your account has been created successfully")
            print(f"Your account number is {user.account_number}")

        elif user_choice == 2:
            account_number = input("Enter your account number: ")
            user = None
            for u in myBank.users:
                if u.account_number == account_number:
                    user = u
                    break
            if user is None:
                print("User not found")
                continue
            password = input("Enter your password: ")
            if user.password != password:
                print("Invalid Password")
                continue
            print("Login Successful")
            while True:
                print("Options:")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Transfer")
                print("5. Take Loan")
                print("6. Transaction History")
                print("7. Logout")
                user_choice = int(input("Enter your choice: "))

                if user_choice == 1:
                    amount = int(input("Enter amount to deposit: "))
                    print(user.deposit(amount))
                elif user_choice == 2:
                    amount = int(input("Enter amount to withdraw: "))
                    print(user.withdraw(Bank,amount))
                elif user_choice == 3:
                    print(user.check_balance())
                elif user_choice == 4:
                    amount = int(input("Enter amount to transfer: "))
                    bank = myBank
                    recipient_account_number = input("Enter recipient account number: ")
                    print(user.transfer(amount, bank, recipient_account_number))
                elif user_choice == 5:
                    print(user.take_loan(myBank))
                elif user_choice == 6:
                    user.transaction_history()
                elif user_choice == 7:
                    print("Logged out successfully")
                    break
                else:
                    print("Invalid Choice")

    elif choice == 3:
        print("Thank You")
        break

    else:
        print("Invalid Choice")
