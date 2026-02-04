
# - Simple class design:
#     1. Create a Rectangle class with attributes length and width. 
#     Add methods to calculate the area and perimeter of the rectangle. 

#     2. Create a BankAccount class with attributes account_number and balance. 
#     Add methods to deposit and withdraw money from the account. 

#     3. Create a Car class with attributes make, model, and year. 
#     Add methods to get and set the values of the attributes. 

#     4. Create a Product class with attributes name, price, and quantity. 
#     Add methods to calculate the total value of the product (price * quantity) 
#     and add or remove items from the product inventory.


# Example 1
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
    
area = Rectangle(5, 3).area()
perimeter = Rectangle(5, 3).perimeter()
print(f"Area: {area}, Perimeter: {perimeter}")
    
# Example 2
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

bank_account = BankAccount("123456789")
bank_account.deposit(500)
bank_account.withdraw(600)
print(f"Account Number: {bank_account.account_number}, Balance: {bank_account.balance}")

# Example 3
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_make(self):
        return self.make

    def set_make(self, make):
        self.make = make

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

car = Car("Toyota", "Camry", 2020)
print(f"Car Make: {car.get_make()}, Model: {car.get_model()}, Year: {car.get_year()}")

# Example 4
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def add_inventory(self, amount):
        self.quantity += amount

    def remove_inventory(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
        else:
            print("Insufficient inventory")

product = Product("Laptop", 1000, 5)

print("Initial quantity:", product.quantity)
print("Initial total value:", product.total_value())

product.remove_inventory(2)

print("After removal quantity:", product.quantity)
print("After removal total value:", product.total_value())

