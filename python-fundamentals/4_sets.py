# A set is a collection of unique, unordered values.
# Think of a set like a bag where:
# Duplicates are automatically removed
# Order does not matter

numbers = {1, 2, 3, 4, 4, 5}
print(numbers)

# curly braces creates a set, duplicates are not allowed

empty = {}  # creates empty dictionary
empty1 = set()  # creates empty set

colors = {"green", "blue", "red"}
print(colors[0])  # you cannot index sets
colors.add("yellow")  # add item to set
colors.remove("red")  # remove item from set. error if item is missing
colors.discard("purple")  # safe removal
colors.pop()  # random item removal


if "green" in colors:
    print("Green exists")
 # checking membership is much faster than lists


for color in colors:
    print(color)
# looping through a set


nums = [1, 2, 2, 3, 3, 4]
unique_nums = set(nums)
# removing duplicates from a list

unique_list = list(unique_nums)
# convert back to list


# Set Operations (This is where Sets shine)
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
# union. Combines values

print(a & b)
# insertion. common values

print(a - b)
# difference. values in A not in B

print(a ^ b)
# symmetric difference. in one set only


small = {1, 2}
large = {1, 2, 3, 4}

print(small.issubset(large))     # True
print(large.issuperset(small))  # True
# subset and supersets

frozen = frozenset([1, 2, 3])
# frozen sets (immutabel sets)

# real world examples
# remove duplicate emails
emails = ["a@test.com", "b@test.com", "a@test.com"]
unique_emails = set(emails)

# track logged-in users
active_users = set()

active_users.add("john")
active_users.discard("john")

# set is like a guest list:
# No duplicate names allowed
# Order doesn’t matter
# Fast “is this person here?” checks


# | Feature        | List | Tuple | Set |
# | -------------- | ---- | ----- | --- |
# | Ordered        | yes  | yes   | no  |
# | Mutable        | yes  | no    | yes |
# | Duplicates     | yes  | yes   | no  |
# | Indexing       | yes  | yes   | no  |
# | Speed (lookup) | no   | no    | yes |
