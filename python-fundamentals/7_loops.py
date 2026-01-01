# A loop repeats a block of code until a condition is met.
# Think of a loop like:
# “Do this again and again until I say stop.”


# "for loop" is used to iterate over a collection
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# fruit is a temporary variable
# Each loop assigns the next item in the list to fruit
# Stops automatically when the list ends


# looping with "range()"
for i in range(5):
    print(i)
# range(5) generates numbers 0 → 4
# Common for counters and indexes

# custom range
for i in range(2, 10, 2):
    print(i)
# start = 2
# stop = 10 (exclusive)
# step = 2

# "while" loop runs as long as the condition is true
count = 0

while count < 3:
    print(count)
    count += 1
# Condition checked before every loop
# Must update the condition to avoid infinite loops

# infinite loops and how to stop them
while True:
    command = input("Type 'quit' to exit: ")
    if command == "quit":
        break
# True never becomes false
# break exits the loop manually

# "break" exits loop and "continue" skip iteration
for num in range(10):
    if num == 5:
        break
    print(num)

for num in range(5):
    if num == 2:
        continue
    print(num)

# looping through dictionaries
user = {"name": "Joseph", "age": 23}

for key, value in user.items():
    print(key, value)

# nested loops
for row in range(3):
    for col in range(3):
        print(row, col)
# Inner loop runs fully for each outer loop iteration
# Common in grids, matrices, game maps

# looping with index (enumerate)
colors = ["red", "green", "blue"]

for index, color in enumerate(colors):
    print(index, color)
# enumerate() gives both index and value
# Cleaner than range(len(list))


# looping multiple lists (zip)
names = ["Joseph", "Josh"]
scores = [90, 85]

for name, score in zip(names, scores):
    print(name, score)

# "else" with loops (rare but useful)
for n in range(3):
    print(n)
else:
    print("Loop completed normally")
# "else" runs only if loop did NOT break

# list comprehensions (pythonic)
squares = [x * x for x in range(5)]
# Shorter, faster, cleaner
# Avoid overusing when readability suffers

# common mistakes:
# Forgetting to update while condition
# Off-by-one errors in range()
# Modifying a list while looping over it


# real-world examples (menu loop)
while True:
    print("1. Add task")
    print("2. Quit")

    choice = input("Choose: ")

    if choice == "1":
        print("Task added")
    elif choice == "2":
        break

# A loop is a machine. It repeats work until a condition changes

# | Use Case              | Loop            |
# | --------------------- | --------------- |
# | Loop through items    | "for"           |
# | Loop until condition  | "while"         |
# | Fixed number of times | "for + range()" |
# | Infinite menu         | "while True"    |


# "for" loops iterate over collections
# "while" loops repeat until a condition fails
# "break" exits loops
# "continue" skips iterations
# Loops power automation and logic
