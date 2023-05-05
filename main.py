class Calculator:
    def __init__(self):
            self.a = int(input("Enter the value "))
            self.b = int(input("Enter the value "))
            self.choice = str(input("Your choice (+, -, *, /) "))
       
    def multiply(self):
        return self.a * self.b
        

    def subtract(self):
        return self.a - self.b

    def add(self):
        return self.a + self.b

    def divide(self):
        try:
            return self.a / self.b

        except ZeroDivisionError:
            print("Zero cannot be divided by zero")



def main():
    cal = Calculator()
    if cal.choice == "*":
        print(cal.multiply())

    elif cal.choice == "-":
        print(cal.subtract())

    elif cal.choice == "/":
        print(cal.divide())

    elif cal.choice == "+":
        print(cal.add())
        
    else:
        print("error")

    
if __name__ == "__main__":
    main()