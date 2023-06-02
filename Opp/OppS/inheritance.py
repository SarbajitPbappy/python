# based class/parent class/common attribute and functionalites
# derived class,child class,uncommon attribute and functionalities

# common
class Device:
    def __init__(self,brand,color,price,origin) -> None:
        self.brand=brand
        self.color=color
        self.price=price
        self.origin=origin
    def run(self):
        return f'running {self.brand}'
# inheritance   
class Phone(Device):
    def __init__(self,brand,price,color,origin,dual_sim) -> None:
        self.dual_sim=dual_sim
        super().__init__(brand,price,color,origin)
    def phone_call(self,number,text):
        return f'sending sms to {number}\nMessage: {text}'
    def __repr__(self) -> str:
        return f'Phone {self.dual_sim}'
    
    
# inheritance

my_phone=Phone('Samsung',19500,'Red','China',True)
print(my_phone.phone_call(123456789,'Hello'))
print(my_phone.run())
print(my_phone.brand)
print(my_phone)