#__init__ - Constuctor
# Automatically called when an object is created.
# Used to initialize the object’s attributes.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("Ajay",40)
print(p1.name)
print(p1.age)

# __str__ - String Representation
# Without __str__, printing p1 would give something like <__main__.Person object at 0x...> (useless memory address).
# With __str__, we get a readable description of the object.


class Car:
    def __init__(self,brand, price):
        self.brand = brand
        self.price = price
    
    def __str__(self):
        return (f"The Brand of Car is {self.brand} with a Price is {self.price}")

c1 = Car("BMW",2200000)
print(c1)

