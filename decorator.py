# def decorator(func):
#     def wrapper():
#         print("Before")
#         func()
#         print("After")
#     return wrapper

# @decorator
# def greet():
#     print("Hello")

# greet()


def magic(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@magic
def greet():
    # print("Hello machi")
    print("hello")

greet()



# What are decorators in Python?
# A: A decorator modifies the behavior of a function without changing its code.