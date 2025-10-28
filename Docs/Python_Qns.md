**Q1. What are Python’s key features?**

&nbsp;- Python is easy to read and write

&nbsp;- It is a dynamic typed language and has a automatic memory management

&nbsp;- has a large standard library

&nbsp;- it is a platform independent

&nbsp;- it supports multiple paradigms(oop, functional, procedural)



**Q2. What is the difference between a list, tuple, and set?**



* **List:** Ordered, Mutable, allow duplicates.
* **Tuple:** Ordered, Immutable, allow duplicates.
* **Set:** Inordered, Mutable, Doesnot allow Duplicates



**Q3. What is the difference between is and == ?**



* **is** checks if two variables refer to same object in memory.
* **==** checks if two of the values are same.  



**eg:**

a = \[1,2]

b = \[1,2]



print(a is b) -> False

print(a == b) -> True



c = 1

d = 1



print( c is d ) -> true

print( c == d) -> true



**Q4. What are mutable and immutable types?** 



* Mutable -> Can be changed after the creation(list, set, dict)
* Immutable -> Cannot be changed after the creation(Tuple, string, int)



**Q5. What is the difference between shallow and deep copy?**

 

* Shallow Copy -> Copies references of nested Objects.
* Deep Copy -> Creates a Complete independent Copy. 



eg:



import copy

a = \[\[1,2],\[3,4]]

b = copy.deepcopy(a)



b\[0]\[0]=99



print(a) -> \[\[1,2],\[3,4]]

print(b) -> \[\[99,2],\[3,4]]



**Q6. What are decorators in Python?**



* Decorator Modifies the behaviour of the function without changing the code.

eg:



def decorator(func):

&nbsp;  def wrapper():

&nbsp;	print(before)

&nbsp;	func()

&nbsp;	print(after)

&nbsp;  return wrapper



@decorator

def greet():

&nbsp; print("Hello")



greet()



**o/p:**

&nbsp;	Before

&nbsp;	Hello

&nbsp;	After



**Q7. What is the difference between \_\_init\_\_ and \_\_str\_\_?**



* **\_\_init\_\_:** Initializes the object(constructor)
* **\_\_str\_\_:** Returns the string representation of the object



**Q8. How does Python handle exceptions?**



* Using try...except...finally:
* Used to handle the exception 



| Keyword   | Purpose                                               |

| --------- | ----------------------------------------------------- |

| `try`     | Code that might raise an exception                    |

| `except`  | Handle specific exceptions                            |

| `else`    | Execute if no exception occurs                        |

| `finally` | Always execute, used for cleanup (like closing files) |



try:

&nbsp;   x = 1 / 0

except ZeroDivisionError:

&nbsp;   print("Error: Division by zero")

finally:

&nbsp;   print("Done")



**Q9.What is Object-Oriented Programming ?**



Object-Oriented Programming(OOP) is a programming paradigm based on the concept of "Objects" which contains data (attributes) and behaviours (methods)

Python supports OOps through class and objects



**Q10.What is a Class and an Object in Python?**

* **class:** A blueprint for creating objects
* **Object:** An instance of a class with its own data

eg:

class Car:

&nbsp;   def \_\_init\_\_(self,brand,color):

&nbsp;	self.brand = brand

&nbsp;	self.color = color



c1 = Car("Audi","Blue")

print(c1.brand)



**Q11.What is the difference between \_\_init\_\_ and a normal method?**



* \_\_init\_\_ is a constructor called automatically when a object is created
* Normal Methods must be called explicitly



**Q12.What are instance, class, and static variables?**



* **Instance variable:** Specific to each object
* **Class Variable:** shared by all objects
* **Static Variables**: declared inside a class but not tied to instances



eg:

class Student:

&nbsp;   school = "ABC School"  # Class variable

&nbsp;   def \_\_init\_\_(self, name):

&nbsp;       self.name = name   # Instance variable



**Q13.What is the difference between instance, class, and static methods?**



* **Instance Method:** works with instance variables (self)
* **Class Method:** works with class variables(cls)
* **static Method:** Doesn't use self or cls

eg:

class Example:

&nbsp;   count = 0

&nbsp;   def \_\_init\_\_(self):

&nbsp;       Example.count += 1



&nbsp;   @classmethod

&nbsp;   def show\_count(cls):

&nbsp;       print(cls.count)



&nbsp;   @staticmethod

&nbsp;   def greet():

&nbsp;       print("Hello!")



**Q14.What are the four pillars of OOP ?**



* **Encapsulation -** binding data and methods together
* **Abstraction -** hiding implementation details
* **Inheritance -** acquiring properties from another class
* **Polymorphism -** same function name with different behaviour



**Q15.Explain Encapsulation with an example.**



* Encapsulation hides internal data using private/protected attributes.



eg:

class Bank:

&nbsp;   def \_\_init\_\_(self, balance):

&nbsp;       self.\_\_balance = balance  # private



&nbsp;   def deposit(self, amount):

&nbsp;       self.\_\_balance += amount



&nbsp;   def get\_balance(self):

&nbsp;       return self.\_\_balance



**Q16.How is Abstraction achieved in Python?**



* Using the abc module (Abstract Base Classes).



eg:

from abc import ABC, abstractmethod



class Shape(ABC):

&nbsp;   @abstractmethod

&nbsp;   def area(self):

&nbsp;       pass



**Q17.What is Inheritance and how is it implemented?**



* Inheritance allows one class to use properties and methods of another.



eg:

class Parent:

&nbsp;   def greet(self):

&nbsp;       print("Hello from Parent")



class Child(Parent):

&nbsp;   def greet(self):

&nbsp;       print("Hello from Child")



**Q18.What is Polymorphism in Python?**



* Same method name but different behavior depending on the object.

eg:

class Bird:

&nbsp;   def fly(self): print("Flies high")



class Airplane:

&nbsp;   def fly(self): print("Flies with engines")



for obj in \[Bird(), Airplane()]:

&nbsp;   obj.fly()



**Q19.What is Method Overriding?**



* When a subclass defines a method that already exists in its parent class.



**Q20.What is Method Overloading? Does Python support it?**



* Python doesn’t support it directly (like Java), but you can simulate it using default arguments or \*args.



**Q21.What are super() and its use?**



* Used to call parent class methods or constructors.



eg:

class A:

&nbsp;   def \_\_init\_\_(self):

&nbsp;       print("A")



class B(A):

&nbsp;   def \_\_init\_\_(self):

&nbsp;       super().\_\_init\_\_()

&nbsp;       print("B")



**Q22.What are Magic (Dunder) Methods?**



* Special methods with double underscores like \_\_init\_\_, \_\_str\_\_, \_\_add\_\_.
* Used to override built-in behavior.



eg:

class Book:

&nbsp;   def \_\_init\_\_(self, pages):

&nbsp;       self.pages = pages

&nbsp;   def \_\_add\_\_(self, other):

&nbsp;       return self.pages + other.pages





**Q23.What is the difference between shallow copy and deep copy?**



* **Shallow copy:** Copies only references of nested objects.
* **Deep copy:** Copies all objects recursively.



eg:

import copy

a = \[\[1, 2], \[3, 4]]

b = copy.copy(a)

c = copy.deepcopy(a)



**Q24.How does Python achieve data hiding?**



Using \_protected or \_\_private naming conventions.

(\_\_variable gets name-mangled as \_ClassName\_\_variable)





