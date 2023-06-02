class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        if num2 > num1:
            num1, num2 = num2, num1
        return num1 - num2

    def mul(self, num1, num2):
        return num1 * num2

    def div(self, num1, num2):
        if num2 != 0:
            ans = num1 / num2
            return ans
        else:
            return "Error: Division by zero"


# main function:
def switch():
    calculator = Calculator()
    while True:
        print("1. Press 1 For Add")
        print("2. Press 2 For Sub")
        print("3. Press 3 For Mul")
        print("4. Press 4 For Div")
        print("5. Press 5 to Exit")
        choice = int(input())

        if choice == 5:
            break
        elif choice<1 or choice>4:
            print("Wrong Choice")
            continue
        num1, num2 = map(int, input("Enter two numbers: ").split())

        if choice == 1:
            print(f"Sum = {calculator.add(num1, num2)}")
        elif choice == 2:
            print(f"Subtraction = {calculator.sub(num1, num2)}")
        elif choice == 3:
            print(f"Multiplication = {calculator.mul(num1, num2)}")
        elif choice == 4:
            result = calculator.div(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print(f"Division = {result}")



switch()
