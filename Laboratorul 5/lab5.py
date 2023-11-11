# ex 1: Create a class hierarchy for shapes, starting with a base class Shape. Then, create subclasses like Circle, 
# Rectangle, and Triangle. Implement methods to calculate area and perimeter for each shape.
import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, a1, a2, a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    def area(self):
        s = (self.a1 + self.a2 + self.a3) / 2
        # heron
        return math.sqrt(s * (s - self.a1) * (s - self.a2) * (s - self.a3))

    def perimeter(self):
        return self.a1 + self.a2 + self.a3
    
print("\nEX 1:\n")
circle = Circle(5)
print("Arie cerc:", circle.area())
print("Perimetru cerc:", circle.perimeter())

rectangle = Rectangle(4, 6)
print("Arie dreptunghi:", rectangle.area())
print("Perimetru dreptunghi:", rectangle.perimeter())

triangle = Triangle(3, 4, 5)
print("Arie triunghi:", triangle.area())
print("Perimetru triunghi:", triangle.perimeter())

# ex 2: Design a bank account system with a base class Account and subclasses SavingsAccount and CheckingAccount. 
# Implement methods for deposit, withdrawal, and interest calculation.

class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def calculate_interest(self):
        pass

class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: ${interest}. New balance: ${self.balance}")

class CheckingAccount(Account):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("You don't have enough money.")

print("\nEX 2:\n")
savings_account = SavingsAccount(account_number="RO123D", balance=1000)
savings_account.deposit(8000)
savings_account.calculate_interest()
savings_account.withdraw(1500)

checking_account = CheckingAccount(account_number="EN123456", balance=6789)
checking_account.withdraw(1203)
checking_account.withdraw(100)

# ex 3: Create a base class Vehicle with attributes like make, model, and year, and then create subclasses for specific 
# types of vehicles like Car, Motorcycle, and Truck. Add methods to calculate mileage or towing capacity based on the vehicle type.
print("\nEX 3:\n")

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
    
    def calculate_mileage(self):
        return 10  #10L/100 km ????


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year)
        self.num_wheels = num_wheels

    def calculate_mileage(self):
        return 6  #6L/100 km ????


class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def calculate_mileage(self):
        return 15  # ????
    
    def display_info(self):
        return f"{super().display_info()} with a towing capacity of {self.towing_capacity} pounds"


car = Car("Hyundai", "Tucson", 2023)
motorcycle = Motorcycle("Harley-Davidson", "Street Glide", 2022, 2)
truck = Truck("Ford", "F-150", 2022, 10000)

print(car.display_info()) 
print(motorcycle.display_info()) 
print(truck.display_info())  

# ex 4: Build an employee hierarchy with a base class Employee. Create subclasses for different types of employees like 
# Manager, Engineer, and Salesperson. Each subclass should have attributes like salary and methods related to their roles.

print("\nEX 4:\n")

class Employee:
    def __init__(self, name):
        self.name = name
        self.salary = 0

    def display_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department
        self.salary = 7500  

    def assign_Tasks(self):
        print(f"Manager {self.name} assigns tasks for the {self.department} department.")

class Engineer(Employee):
    def __init__(self, name, programming_language):
        super().__init__(name)
        self.programming_language = programming_language
        self.salary = 6000  

    def write_code(self):
        print(f"Engineer {self.name} is writing code in {self.programming_language}.")

class Salesperson(Employee):
    def __init__(self, name, projects_Sold):
        super().__init__(name)
        self.projects_Sold = projects_Sold
        self.salary = 50000  

    def meet_clients(self):
        print(f"Salesperson {self.name} sold {self.projects_Sold} projects.")

manager1 = Manager("Jane Doe", "PR")
engineer1 = Engineer("Maria Colson", "Python")
salesperson1 = Salesperson("David Marshall", 123)

manager1.display_details()
manager1.assign_Tasks()

engineer1.display_details()
engineer1.write_code()

salesperson1.display_details()
salesperson1.meet_clients()

# ex 5: Create a class hierarchy for animals, starting with a base class Animal. Then, create subclasses like Mammal, 
# Bird, and Fish. Add properties and methods to represent characteristics unique to each animal group.
print("\nEX 5:\n")

class Animal:
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    def __init__(self, name, has_tail):
        super().__init__(name)
        self.has_tail = has_tail 

    def give_birth(self):
        print(f"{self.name} is giving birth to live young.")

class Bird(Animal):
    def __init__(self, name, feather_color):
        super().__init__(name)
        self.feather_color = feather_color

    def fly(self):
        print(f"{self.name} is flying. You can see its {self.feather_color} color.")

class Fish(Animal):
    def __init__(self, name, scale_type):
        super().__init__(name)
        self.scale_type = scale_type

    def swim(self):
        print(f"{self.name} is swimming with {self.scale_type} scales.")


lion = Mammal(name="Lion", has_tail="Yes")
eagle = Bird(name="Eagle", feather_color="grey")
shark = Fish(name="Shark", scale_type="Cartilaginous")

print(f"{lion.name} is a mammal with tail:", {lion.has_tail})
print(f"{eagle.name} is a bird with a wingspan of color {eagle.feather_color}.")
print(f"{shark.name} is a fish with {shark.scale_type} scales.")

lion.give_birth()  
eagle.fly()       
shark.swim()      

#ex 6: Design a library catalog system with a base class LibraryItem and subclasses for different types of items like Book,
#  DVD, and Magazine. Include methods to check out, return, and display information about each item.
print("\nEX 6:\n")

class LibraryItem:
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.checked_out = False

    def display_info(self):
        print(f"Item ID: {self.item_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {'Checked Out' if self.checked_out else 'Available'}")

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            print(f"{self.title} has been checked out.")
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} is not checked out.")


class Book(LibraryItem):
    def __init__(self, title, author, item_id, num_pages):
        super().__init__(title, author, item_id)
        self.num_pages = num_pages


class DVD(LibraryItem):
    def __init__(self, title, director, item_id, duration):
        super().__init__(title, director, item_id)
        self.duration = duration


class Magazine(LibraryItem):
    def __init__(self, title, publisher, item_id, issue_number):
        super().__init__(title, publisher, item_id)
        self.issue_number = issue_number


book = Book(title="Ion", author="Liviu Rebreanu", item_id="B001", num_pages=224)
dvd = DVD(title="Inception", director="Christopher Nolan", item_id="D001", duration="2 hours 28 minutes")
magazine = Magazine(title="National Geographic", publisher="National Geographic Society", item_id="M001", issue_number=255)

book.display_info()
dvd.display_info()
magazine.display_info()

book.check_out()
dvd.check_out()
magazine.return_item()

book.display_info()
dvd.display_info()
magazine.display_info()
