# basic enumerate
colors = ["red", "green", "blue"]

for index, color in enumerate(colors):
    print(index, color)
# enumerate() returns pairs: (index, value)
# index starts at 0 by default
# Much cleaner and safer

for index, color in enumerate(colors, start=1):  # custom start index
    print(index, color)
# Useful for menus or user-facing lists

# common real world use case (menu)
options = ["Start Game", "Settings", "Quit"]

for i, option in enumerate(options, start=1):
    print(f"{i}. {option}")

# using enumerate with conditions
for i, color in enumerate(colors):
    if color == "green":
        print("Found green at index:", i)
# enumerate = “Give me the item AND its index”

# without zip
names = ["Joseph", "Josh"]
scores = [90, 85]

for i in range(len(names)):
    print(names[i], scores[i])
# Assumes both lists are same length
# Index-based logic
# Harder to read

# basic zip
names = ["Joseph", "Josh"]
scores = [90, 85]

for name, score in zip(names, scores):
    print(name, score)
# zip() pairs items by position
# Stops at the shortest iterable
# Clean and safe

# zipping more than two lists
names = ["Joseph", "Josh"]
scores = [90, 85]
roles = ["Admin", "User"]

for name, score, role in zip(names, scores, roles):
    print(name, score, role)

# creating lists from zip
pairs = list(zip(names, scores))

# unzipping values
pairs = [("Joseph", 90), ("Josh", 85)]

names, scores = zip(*pairs)
# "*" unpacks the pairs
# Very common Python pattern

# zip with dictionaries
keys = ["name", "age"]
values = ["Joseph", 23]

user = dict(zip(keys, values))


# enumerate + zip together (powerful combo)
names = ["Joseph", "Josh"]
scores = [90, 85]

for i, (name, score) in enumerate(zip(names, scores), start=1):
    print(f"{i}. {name} scored {score}")


# | Tool          | Purpose                 |
# | ------------- | ----------------------- |
# | "enumerate()" | Item + index            |
# | "zip()"       | Pair multiple iterables |


# When to Use Each

# Use enumerate when:
# You need the index
# Building menus
# Tracking positions

# Use zip when:
# Combining related lists
# Processing parallel data
# Building dictionaries

# enumerate -> index + item
# zip       -> item + item (+ item...)
