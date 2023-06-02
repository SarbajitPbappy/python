class Shop:
    def __init__(self, name):
        self.name = name
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
    
    def remove_product(self, product):
        self.products.remove(product)
        
    def show_products(self):
        for product in self.products:
            print(product)

while True:
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Show Products")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 4:
        break
    elif choice == 1:
        name = input("Enter product name: ")
        product = name
        shop = Shop("My Shop")
        shop.add_product(product)
    elif choice == 2:
        name = input("Enter product name: ")
        product = name
        shop = Shop("My Shop")
        shop.remove_product(product)
    elif choice == 3:
        shop = Shop("My Shop")
        shop.show_products()
    else:
        print("Wrong Choice")
        continue

print("Thank you for shopping with us")
