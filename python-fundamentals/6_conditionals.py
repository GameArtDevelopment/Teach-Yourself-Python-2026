# A conditional lets your code run different paths depending on a condition.

# Think of it as: “IF this is true, do this. OTHERWISE, do something else.”

score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")


# if checks a condition True or False
# If True, the indented code runs
# score >= 90 evaluates to "A"
# elif = “else if”
# Python checks top to bottom. First match wins
# else runs when the if condition is false
# Only one branch executes

# Operator	Meaning
# ==	    Equal
# !=	    Not equal
# >	        Greater than
# <	        Less than
# >=	    Greater or equal
# <=	    Less or equal


x = 10

if x != 5:
    print("x is not 5")

# logical operators
age = 23
has_id = True

if age >= 18 and has_id:  # all must be true
    print("Access granted")


is_admin = False
is_editor = True

if is_admin or is_editor:  # at least one must be true
    print("Permission granted")


logged_in = False

if not logged_in:  # reverses condition
    print("Please log in")


# false values (importmant)
# False
# 0
# ""
# None
# []
# {}
# set()

# example
name = ""

if not name:
    print("Name is empty")


# nested conditionals
age = 25

if age >= 18:
    if age >= 21:
        print("You can drink")
    else:
        print("You are an adult")
# avoid deep nesting if possible. Use elif for clarity

# conditional expression(ternary operator). one-line conditional
age = 17

status = "Adult" if age >= 18 else "Minor"
print(status)


# checking membership with in
roles = ["admin", "user"]

if "admin" in roles:
    print("Admin access")

# comparing strings
command = "start"

if command == "start":
    print("Game started")

# readl world example (login logic)
username = "john"
password = "1234"

if username == "john" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")


# guard clauses

# bad code
if logged_in:
    if is_admin:
        print("Access")

# better code


def login():  # I will explain functions later.
    if not logged_in:
        return  # return can be used only wthin a function.

    if is_admin:
        print("Access")

# Conditionals are forks on the road. The program checks a question and chooses a path.


# Best Practices
# Order conditions from specific → general
# Use elif instead of nesting
# Use clear variable names
# Avoid deep nesting

# What Conditionals Unlock
# Game logic
# User validation
# Menu systems
# AI behavior
# Backend rules
