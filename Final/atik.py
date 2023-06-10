class User:
    def __init__(self, email, password, open_deposit):
        self.email = email
        self.password = password
        self.open_deposit = open_deposit
        self.balance = 0
        self.transaction_history = []

    def Deposit(self, amount):
        self.balance += amount
        my_bank.total_balance += amount
        self.transaction_history.append(f"{self.email} deposit {amount} taka ")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"You withdrawn: {amount} taka")
        else:
            print(
                f'(Insufficient balance in your account. please deposit more than {amount - self.balance} taka")'
            )

    def transfer(self, email, amount):
        receive = my_bank.create_user_by_email(email)
        if receive is not False:
            if amount < self.balance:
                self.balance -= amount
                receive.balance += amount
                self.transaction_history.append(f"Transferred: {amount} to {email}")
            else:
                print("Insufficient balance")
        else:
            print("Sorry, this user is not found")

    def check_available_balance(self):
        print(f"{self.email} this email current available balance is: {self.balance}")

    def take_loan(self):
        if my_bank.loan_feature or not my_bank.total_balance < self.balance * 2:
            loan_amount = 2 * self.balance
            my_bank.total_balance -= loan_amount
            self.balance += loan_amount
            my_bank.total_loan_amount += loan_amount
            self.transaction_history.append(
                f" {loan_amount} taka loan you taken from bank"
            )
        else:
            print("Not available for loan")


class Bank:
    def __init__(self):
        self.users = []
        self.admins = []
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature = True

    def create_account(self, email, password, open_deposit):
        user = User(email, password, open_deposit)
        self.total_balance += open_deposit
        self.users.append(user)
        return user

    def create_admin(self, email, password, nid, phn_nbr):
        admin = Admin(email, password, nid, phn_nbr)
        self.admins.append(admin)

    def create_user_by_email(self, email):
        for user in self.users:
            if user.email == email:
                return user
        return False

    def create_admin_by_email_nid(self, email, nid):
        for admin in self.admins:
            if admin.email == email:
                return admin
        return None

    def total_bank_balance(self):
        return self.total_balance

    def total_bank_loan_amount(self):
        return self.total_loan_amount

    def toggle_loan_feature(self):
        self.loan_feature = not self.loan_feature


class Admin(User):
    def __init__(self, email, password, nid, phn_nbr):
        super().__init__(email, password, 0)
        self.nid = nid
        self.phn_nbr = phn_nbr

    def check_total_bank_balance(self):
        print("Total bank balance is ", my_bank.total_bank_balance())

    def check_total_loan_amount(self):
        print("Total loan balance is ", my_bank.total_bank_loan_amount())

    def toggle_loan_feature(self):
        my_bank.toggle_loan_feature()


my_bank = Bank()

my_bank.create_account("atik@.com", "password1", 1000)
my_bank.create_account("hasan@.com", "password2", 1000)
my_bank.create_account("ayaan@.com", "password1", 1000)
my_bank.create_admin("admin@.com", "adminpassword", 9387, 1877166142)

atik = my_bank.create_user_by_email("atik@.com")
hasan = my_bank.create_user_by_email("hasan@.com")
ayaan = my_bank.create_user_by_email("ayaan@.com")

atik.Deposit(5000)
ayaan.Deposit(4000)
hasan.Deposit(2000)
atik.check_available_balance()
ayaan.check_available_balance()
hasan.check_available_balance()
ayaan.transfer("atik@.com", 1000)
ayaan.check_available_balance()
atik.check_available_balance()
hasan.take_loan()
ayaan.take_loan()
hasan.check_available_balance()
print(atik.transaction_history)
print(ayaan.transaction_history)
print(hasan.transaction_history)

admin = my_bank.create_admin_by_email_nid("admin@.com", 9387)
admin.check_total_bank_balance()
admin.check_total_loan_amount()
admin.toggle_loan_feature()
