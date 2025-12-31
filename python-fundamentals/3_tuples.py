# A tuple is a collection of values just like a list, but with one critical difference: Tuples are immutable — once created, they cannot be changed.

# tuples use parentheses (), items are comma-seperated, order matters.
coordinates = (10, 20)

# accessing tuple items(indexing)
print(coordinates[0])  # 10

# use tuples when data should be: fixed, read-only, predictable, and safe from modification

DAYS_OF_THE_WEEK = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

# looping thorugh tuples
cars = ("BMW", "Honda", "Tesla")

for car in cars:
    print(car)

# checking membership
if "Honda" in cars:
    print("Car exists")


# tuple unpacking (very powerful)
admin = ("Joseph", 23, "Developer")

name, age, job = admin

print(name)
print(age)
print(job)


# returning multiple values from function
def get_admin():
    return ("Joseph", 23)


name, age = get_admin()


# tuples inside lists (common pattern)
users = [
    ("Joseph", "Admin"),
    ("Jane", "User"),
    ("Mike", "Moderator")
]

# nested tuples
grid = (
    (1, 2),
    (3, 4)
)

print(grid[1][0])  # 3

# if data needs to change, structure is unclear, and items need to be added/removed -> use lists instead.
