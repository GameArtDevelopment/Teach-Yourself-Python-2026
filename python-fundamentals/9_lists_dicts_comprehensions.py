# A comprehension is a compact way to create a collection (list or dictionary) using: A loop, Optional conditionals, An expression
# Think of it as: “Create a collection by transforming/filtering another collection.”

# traditional way
numbers = [1, 2, 3, 4, 5]
squares = []

for n in numbers:
    squares.append(n * n)

# Process: Loop through each number -> Square it -> Append to a new list

squares = [n * n for n in numbers]  # list comprehension

# [ expression   for item in iterable ]
# n * n -> what you want to store
# for n in numbers -> loop source

evens = [n for n in numbers if n % 2 == 0]  # list comprehension w/a condition

# [ item for item in iterable if condition ]
# Only numbers where condition is True are included

# Transform + fliter together
squared_evens = [n * n for n in numbers if n % 2 == 0]


def double(x):  # using functions in comprehensions
    return x * 2


doubles = [double(n) for n in numbers]

# nested loops in list comprehensions
pairs = [(x, y) for x in [1, 2] for y in [3, 4]]

pairs = []  # equivalent loop
for x in [1, 2]:
    for y in [3, 4]:
        pairs.append((x, y))

# conditional expressions
# This if/else is an expression, not a filter.
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]

# For each item, optionally filter it, then transform it.


# traditional dictionary creation
squares = {}

for n in range(5):
    squares[n] = n * n


# dictionary comprehension
squares = {n: n * n for n in range(5)}
# { key_expression : value_expression for item in iterable }


# transforming existing dictionaries
prices = {"apple": 1.0, "banana": 0.5, "orange": 0.8}

taxed_prices = {k: v * 1.1 for k, v in prices.items()}

# filtering dictionary entries
expensive = {k: v for k, v in prices.items() if v > 0.7}

# swapping keys and values
roles = {"john": "admin", "jane": "user"}

swapped = {v: k for k, v in roles.items()}
# values must be unique!


# real world examples
names = [" John ", " Jane ", " Mike "]
cleaned = [name.strip().lower() for name in names]


# API response filtering
users = [
    {"name": "John", "active": True},
    {"name": "Jane", "active": False}
]

active_users = [u for u in users if u["active"]]


# when to use comprehension
# Simple transformations
# Filtering data
# One clear responsibility
# Readable in one line


# recap:
# list comprehension
# [WHAT for ITEM in SOURCE if CONDITION]
# dictionary comprehension
# {KEY: VALUE for ITEM in SOURCE if CONDITION}

# This helps with:
# Cleaner code
# Faster execution
# Pythonic style
# Easier data processing
