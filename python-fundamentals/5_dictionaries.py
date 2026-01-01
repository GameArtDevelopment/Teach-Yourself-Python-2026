# A dictionary stores data as key → value pairs.
# Think of a dictionary like a real dictionary:
# You look up a word (key)
# You get a definition (value)

# creating a dictionary
user = {
    "name": "Joseph",
    "age": 23,
    "is_admin": True
}

# Curly braces {} create a dictionary
# Keys and values are separated by :
# Each pair is separated by a comma

# accessing values by key. If key does not exist = error
print(user["name"])
print(user["age"])

# safe access
print(user.get("name"))
print(user.get("email", "Not provided"))
# .get() prevents crashes
# Returns None or a default value if missing

# adding and updating values
user["email"] = "joseph@email.com"
user["age"] = 46

# removing items
del user["is_admin"]

age = user.pop("age")  # pop() removes and returns the value

# check if a key exists not values
if "name" in user:
    print("Name exists")


# loop through dicts
for key in user:
    print(key)

# loop through values
for value in user.values():
    print(value)
# loop through both
for key, value in user.items():
    print(key, value)

# dict length
print(len(user))

# nested dict
player = {
    "name": "Hero",
    "stats": {
        "health": 100,
        "mana": 50
    }
}

print(player["stats"]["health"])
# Common in games and APIs
# Access using chained keys


# dict with lists
inventory = {
    "gold": 250,
    "items": ["sword", "shield", "potion"]
}

inventory["items"].append("armor")

# common dict methods
user.keys()
user.values()
user.items()
user.clear()


# dict comprehension (advanced but nit powerful)
squares = {x: x*x for x in range(5)}
# result = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# real world example
settings = {
    "volume": 80,
    "fullscreen": True,
    "difficulty": "normal"
}

# API data (very common)
response = {
    "status": 200,
    "data": {
        "user": "John",
        "active": True
    }
}

# when to use dict
# Named data
# Fast lookups
# Structured data
# Game states
# User profiles
# API responses


# A dictionary is like a labeled storage box
# You grab items by label, not position.
