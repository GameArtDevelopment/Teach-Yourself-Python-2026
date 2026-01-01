# A function is a reusable block of code that:
# Can receive input (parameters)
# Can send output back (return values)
# Think of a function like a machine:
# You put data in, it gets processed, and it gives you a result back

def greet():
    print("Hello!")
# "def" starts a function definition
# greet is the function name
# () holds parameters (empty here)
# Indented code is the function body


greet()  # calling a function


def greeting(name):  # parameters
    print(f"Hello, {name}!")


greeting("Joseph")
greeting("Josh")

# name is a parameter
# "Joseph" is an argument
# functions become reusable


def add(a, b):  # multiple parameters
    print(a + b)


add(6, 7)
# Parameters are comma-separated
# Order matters (unless using named arguments)


def adding(a, b):  # return values(outputs)
    return a + b  # good practice (try not to use "print()")


result = add(3, 5)
print(result)
# return ends the function
# Returned value can be stored or used elsewhere
# "print()"" only shows output
# "return()" gives data back to your program


def greeter(name="Guest"):  # default parameters
    return f"Hello, {name}!"


print(greeter())
print(greeter("Ashley"))
# Default values are optional
# Must come after required parameters


def user_info(name, age):  # keyword arguments
    return f"{name} is {age} years old"


print(user_info(age=23, name="Joseph"))
# Order doesn’t matter
# Improves readability


def get_dimensions():  # return multiple values (tuples)
    width = 1920
    height = 1080
    return width, height


w, h = get_dimensions()


print(w)  # result = 1920
# Python returns a tuple
# Common pattern in real code


def divide(a, b):  # early returns (guard clauses)
    if b == 0:
        return "Cannot divide by zero"
    return a / b
# Stops function early
# Keeps logic clean


# functions calling functions
def square(x):
    return x * x


def sum_of_squares(a, b):
    return square(a) + square(b)
# Functions can build on each other
# Encourages small, focused functions


# scope (local vs global)
x = 10


def test():
    x = 5
    return x


print(test())
print(x)
# Variables inside functions are local
# Avoid global variables when possible


# real world example (user validation)
def is_valid_user(username, password):
    fake_usernames = ["admin", "user", "test"]

    if username == "" or password == "":
        return False
    if len(password) < 6:
        return False
    if username in fake_usernames:
        return False
    return True


# Get user input
# "input" is used to capture user input from the console or terminal. value = string
username = input("Enter your username: ")
password = input("Enter your password: ")

if is_valid_user(username, password):
    print("Login allowed")
else:
    print("Login denied")


# A function is a named box of logic
# You send values in -> get a result back

# Best Practices:
# One function = one responsibility
# Use clear names (calculate_total)
# Return data, don’t print it
# Keep functions short
