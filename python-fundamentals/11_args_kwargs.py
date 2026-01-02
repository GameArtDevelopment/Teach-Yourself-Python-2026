# Sometimes you don’t know ahead of time how many arguments a function will receive.

# "*args" and "**kwargs" let your function accept a flexible number of arguments.

# basix *args
def add_numbers(*args):
    print(args)


add_numbers(1, 2, 3)
# "*args" collects all positional arguments
# They arrive as a tuple
# Name args is a convention (can be anything)


# using *args in logic
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total


print(add_numbers(1, 2, 3, 4))

# mixing normal parameters + *args

names = ["Joseph", "Josh", "Ash"]
greeting = "Hello"


def greet(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}")


greet(greeting, *names)
# Regular parameters must come before *args
# "*args" = “Pack extra positional arguments into a tuple”


# "**kwargs" variable keyword arguments

def print_user(**kwargs):
    print(kwargs)


print_user(name="Joseph", age=23, role="Developer")
# "**kwargs" collects named arguments
# They arrive as a dictionary
# Name kwargs is a convention


def print_user(**kwargs):  # using **kwargs in logic
    for key, value in kwargs.items():
        print(key, value)


def create_user(username, **details):  # mixing normal parameters + **kwargs
    print(username)
    print(details)


create_user("joseph", age=23, admin=True)
# "**kwargs" must come last
# "**kwargs" = “Pack extra named arguments into a dictionary”


#  using "*args" + "**kwargs" together
def example(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)


example(1, 2, 3, x=10, y=20)

# parameter order = normal -> *args -> **kwargs


# unpacking with "*" and "**"
nums = [1, 2, 3]
print(add_numbers(*nums))

# unpacking a dictionary into keyword arguments
user = {"name": "Joseph", "age": 23}
print_user(**user)

# pack and unpack
# | Action        | Symbol              |
# | ------------- | ------------------- |
# | Pack values   | "*args", "**kwargs" |
# | Unpack values | "*list", "**dict"   |


# real-world examples
def log(message, **meta):
    print(message)
    for k, v in meta.items():
        print(f"{k}: {v}")


log("Error occurred", code=500, user="joseph")


# forwarding arguments (very common)

def target_function(*args, **kwargs):
    print("Arguments:", args)
    print("Keyword Arguments:", kwargs)


def wrapper(*args, **kwargs):
    return target_function(*args, **kwargs)


# Example usage
wrapper(1, 2, 3, name="Josh", age=30)

# this is important because it's used heavily in frameworks. Decorators depend on this pattern

# "*args" is a tuple, not a list.
# use **kwargs with keyword arguments
# understand the parameter order


# You should use them when...
# Building flexible APIs
# Wrappers & decorators
# Libraries & utilities
# Forwarding arguments


# "*args"    -> extra positional args -> tuple
# "**kwargs" -> extra named args      -> dict
