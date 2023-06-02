class Bank:
    def __init__(self,holder_name,initial_deposit):
        self.holder_name=holder_name # normally all atribute is public
        self.initial_deposit=initial_deposit
        self.__balance=initial_deposit #privet attribute
        self.transactions=[]
        # self._brance='Banani 12' protected attribute
    def deposit(self,amount):
        self.__balance+=amount
        self.transactions.append(amount)
    def get_balance(self):
        return self.__balance
    def withdraw(self,amount):
        if self.__balance>=amount:
            self.__balance-=amount
            self.transactions.append(amount)
        else:
            print("Insufficient Balance")

bappy=Bank('Bappy',1000)
bappy.deposit(500)
bappy.deposit(10000)
print(bappy.get_balance())
bappy.withdraw(500)
print(bappy.get_balance())

# using dir to print forcefully

print(bappy._Bank__balance)

# encapsulation --> hide details