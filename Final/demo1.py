class Bank:
    def __init__(self):
        self.users = []
        self.admins = []
        self.total_balance = 0
        self.total_loan = 0
        self.loan_features = False

    def create_user(self, name, email, address, nid, opening_deposit, account_type, password):
        account_number = self.generate_account_number()
        user = User(account_number, name, email, address, nid, opening_deposit, account_type, password)
        self.users.append(user)
        self.total_balance += opening_deposit
        return user

    def create_admin(self, name, email, password):
        admin = Admin(name, email, password)
        self.admins.append(admin)
        return admin

    def generate_account_number(self):
        # Logic to generate a unique account number
        pass

    def get_total_balance(self):
        return self.total_balance

    def get_total_loan(self):
        return self.total_loan

    def toggle_loan_features(self):
        self.loan_features = not self.loan_features


class User(Bank):
    def __init__(self, account_number, name, email, address, nid, opening_deposit, account_type, password):
        super().__init__()
        self.account_number = account_number
        self.name = name
        self.email = email
        self.address = address
        self.nid = nid
        self.balance = opening_deposit
        self.account_type = account_type
        self.password = password
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.total_balance += amount
        self.transaction_history.append(f"Deposited {amount}")
        return f"Deposit of {amount} successful. Your new balance is {self.balance}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.total_balance -= amount
            self.transaction_history.append(f"Withdrew {amount}")
            return f"Withdrawal of {amount} successful. Your new balance is {self.balance}"
        else:
            return "Insufficient funds"

    def check_balance(self):
        return f"Your current balance is {self.balance}"

    def transfer(self, amount, bank, recipient_account_number):
        if self.balance >= amount:
            recipient = None
            for user in bank.users:
                if user.account_number == recipient_account_number:
                    recipient = user
                    break

            if recipient is not None:
                self.balance -= amount
                recipient.balance += amount
                self.total_balance -= amount
                recipient.total_balance += amount
                self.transaction_history.append(f"Transferred {amount} to account {recipient_account_number}")
                recipient.transaction_history.append(f"Received {amount} from account {self.account_number}")
                return f"Transfer of {amount} successful. Your new balance is {self.balance}"
            else:
                return "Recipient account not found"
        else:
            return "Insufficient funds"

    def view_transaction_history(self):
        return self.transaction_history


class Admin(User):
    def __init__(self, name, email, password):
        super().__init__("Admin", name, email, "", "", 0, "", password)

    def login(self, email, password):
        return self.email == email and self.password == password


myBank = Bank()
user1 = myBank.create_user("John Doe", "john@example.com", "123 Main St", "1234567890", 100000, "Savings", "72580")
user2 = myBank.create_user("Sarbajit", "sarbajit@example.com", "456 Elm St", "0987654321", 50000, "Current", "73500")
admin = myBank.create_admin("Admin User", "admin@example.com", "adminpass")
print(myBank.get_total_balance())
print(user1.deposit(5000))
print(user2.check_balance())
# print(user1.transfer(20000, myBank, user2.account_number))
print(user2.check_balance())
print(myBank.get_total_balance())
print(user1.view_transaction_history())
print(admin.login("admin@example.com", "adminpass"))
print(admin.login("admin@example.com", "wrongpassword"))
