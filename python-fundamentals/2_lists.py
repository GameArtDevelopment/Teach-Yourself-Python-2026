# a list is a container that stores multiple values in a single variable

letters = ["a", "b", "c"]  # a collection of data

print(letters[0])  # accessing items(indexing)
letters.append("e")  # append() adds an item.
print(letters)
letters.insert(3, "d")  # insert() shifts items to the right
print(letters)
letters.pop(0)  # removes by index
print(letters)
letters.remove("e")  # remove by value
print(letters)
print(len(letters))  # list length

# lists store multiple data types. index starts at [0]. lists are mutable(can change).

for letter in letters:  # looping through a list
    print(letter)

if "b" in letters:  # checking if item in list
    print("b is in the list")
# useful for validation

letters.sort()  # sort permanently. changes original list
sorted_letters = sorted(letters)  # sort temporarily. returns a new list

# copying lists the correct way
# without .copy(), both variables reference the same list. changes affect both.
list2 = letters.copy()

# list with mixed data types
admin = ["Joseph", 23, True]

# nested lists (lists inside lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])  # 6
# first index = row, second index = column

# list slicing
numbers = [0, 1, 2, 3, 4, 5]
# format list[start:end]
print(numbers[1:4])   # [1, 2, 3]
print(numbers[:3])    # [0, 1, 2]
print(numbers[3:])    # [3, 4, 5]


# let's put it together
tasks = []

tasks.append("Buy groceries")
tasks.append("Clean house")

for task in tasks:
    print(f"- {task}")

# final thoughts why lists are powerful

# Store collections
# Easy to loop through
# Fast access by index
# Core building block for apps, games, APIs
