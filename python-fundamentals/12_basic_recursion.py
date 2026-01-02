# Recursion is when a function calls itself to solve a smaller version of the same problem.

# Think of it like: “To solve this problem, first solve a smaller version of it.”

# Every recursive function MUST have:
# Base Case -> when to STOP
# Recursive Case -> the self-call that gets closer to the base case
# Without a base case -> infinite loop -> crash.

# example: counting down
def countdown(n):
    if n == 0:          # Base case
        print("Done!")
        return

    print(n)
    countdown(n - 1)    # Recursive call


# countdown(3)
# -> print(3)
# -> countdown(2)
# -> print(2)
# -> countdown(1)
# -> print(1)
# -> countdown(0)
# -> Done!


# Explanation: Each call reduces "n", Eventually hits the base case, Stack “unwinds” back up


# factorial example
# 5! = 5 × 4 × 3 × 2 × 1

# recursive code
def factorial(n):
    if n == 1:              # Base case
        return 1
    return n * factorial(n - 1)

# how it works:
# factorial(4)
# = 4 * factorial(3)
# = 4 * 3 * factorial(2)
# = 4 * 3 * 2 * factorial(1)
# = 24


# base case comes first
def good(n):
    if n == 0:
        return
    good(n - 1)


# recursion vs loops

def sum_loop(n):  # loop version
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def sum_recursive(n):  # recursive version
    if n == 1:
        return 1
    return n + sum_recursive(n - 1)

# Loops -> iterative
# Recursion -> self-calling


# returning values
def recurse(n):
    if n == 0:
        return 0
    return n + recurse(n - 1)


# real world example: file system traversal
def walk_tree(folder):
    for item in folder:
        if item.is_file:
            print(item.name)
        else:
            walk_tree(item.children)

# Why Recursion Fits: Folders contain folders and problem structure is self-similar

# When you should use recursion
# Tree structures
# Nested data
# Divide-and-conquer algorithms
# Backtracking problems

# remember:
# Recursion is like Russian nesting dolls
# Each call opens a smaller doll
# Until you hit the smallest one (base case)


# final pattern to mermorize
def recursive_function(n):  # "n" = problem
    # Base case: if n is 0 or 1, return 1
    if n <= 1:
        return 1  # result

    # Recursive case (smaller problem)
    return n * recursive_function(n - 1)


# Example usage
result = recursive_function(5)
print(result)  # Output: 120

# This unlocks:
# Tree & graph algorithms
# Parsing nested data
# Game AI
# Algorithms like quicksort, DFS
