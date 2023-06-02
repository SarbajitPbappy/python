class Shopping:
    cart=[] # class attrribute or static attribute
    origin = "India"
    def __init__(self,name,location):
        self.name = 'Dhaka' # instance attribute
        self.location = 'Bangladesh'
    def add_to_cart(self,item,price,ammount):
        remaining=ammount-price
        print(f'Buying {item} for {price} taka and remaining {remaining} taka')
    def show_cart(self):
        print(self.cart)
    def __str__(self):
        return f"{self.name} {self.location}"
    @staticmethod
    def multiply(a,b): #without self direct access
        print(a*b)
    @classmethod
    def kinboNa(self):
        print("Kinbo na")

basumati = Shopping("Basumati","Dhaka")
print(basumati)
basumati.add_to_cart("Rice",50,100)
basumati.show_cart()
Shopping.kinboNa() # class method to get direct access
Shopping.multiply(5,6)# static method to get direct access
basumati.multiply(5,6) 
