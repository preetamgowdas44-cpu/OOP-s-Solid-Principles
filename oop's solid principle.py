#SSP Practice

class book:
    def __init__(self,name,author,price):
        self.name=name
        self.author=author
        self.price=price

class book_details:
    def __init__(self,book):
        print("\n--- Books Details---")
        print(f"Name:- {book.name}")
        print(f"Author:- {book.author}")
        print(f"Price:- {book.price}")

b1=book("Love","Happy",400)
details=book_details(b1)

 #ocp prctice

from abc import ABC, abstractmethod

class product(ABC):
    def __init__(self,name,price):
        self.name=name
        self.price=price

    @abstractmethod
    def calculate_tax(self):
        pass

    def total_price(self):
        return self.price+self.calculate_tax()
    
class food(product):
    def calculate_tax(self):
        return self.price*0.05
    
class electronics(product):
    def calculate_tax(self):
        return self.price*0.18
    
class clothing(product):
    def calculate_tax(self):
        return self.price*0.12
    
def print_bill(Product:product):
    print("\n---Bill Details---")
    print(f"Product name:- {Product.name}")
    print(f"Base Price:- {Product.price}")
    print(f"Tax:- {Product.calculate_tax():.2f}")
    print(f"Total:- {Product.total_price():.2f}\n")
    
items=[
    food("Pizza",140),
    electronics("Wire",100),
    clothing("Shirt",1000)
]

for item  in items:
    print_bill(item)

class Vehicle:
    def mode(self):
        pass

class Bike(Vehicle):
    def mode(self):
        print("Road transport.")

class Boat(Vehicle):
    def mode(self):
        print("Water transport.")

class Aeroplane(Vehicle):
    def mode(self):
        print("Air transport.\n")

b=Bike()
bo=Boat()
a=Aeroplane()

b.mode()
bo.mode()
a.mode()

class Appliance:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

class TV(Appliance):
    def turn_on(self):
        print("TV is turned on.")

    def turn_off(self):
        print("TV is turned off.")

class AC(Appliance):
    def turn_on(self):
        print("AC i tuned on.")

    def turn_off(self):
        print("C is turned off.")

class Remote:
    def __init__(self,appliance:Appliance):
        self.appliance=appliance

    def press_on(self):
        self.appliance.turn_on()

    def press_off(self):
        self.appliance.turn_off()

tv=TV()
ac=AC()

R1=Remote(tv)
R2=Remote(ac)

R1.press_on()
R1.press_off()

R2.press_on()
R2.press_off()