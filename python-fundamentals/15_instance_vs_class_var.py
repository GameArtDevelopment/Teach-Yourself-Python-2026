# Instance variables -> belong to one object
# Class variables -> shared by all objects of that class


# instance variables(most common) are created using "self"
class Player:
    def __init__(self, name, health):
        self.name = name        # instance variable
        self.health = health    # instance variable


p1 = Player("Arthur", 100)
p2 = Player("Lancelot", 120)

p1.health -= 30
print(p1.health)  # 70
print(p2.health)  # 120
# each object gets its own copy


# class variables(shared data) are defined inside the class, outside the "__init__"

class Player:
    species = "Human"     # class variable

    def __init__(self, name):
        self.name = name


p1 = Player("Arthur")
p2 = Player("Lancelot")

print(p1.species)  # Human
print(p2.species)  # Human
# One variable, shared across all objects

# python looks up variables -> 1. p1(instance variable) 2. Player(class variable)

# changing variables via the class(affects all)
Player.species = "Elf"

print(p1.species)  # Elf
print(p2.species)  # Elf

# changing via instance(creates NEW instance variables). does not change the class variable.
p1.species = "Dwarf"

print(p1.species)  # Dwarf
print(p2.species)  # Elf


# Visual difference
# Player class:
#  |- species = "Elf"

# p1 object:
#  |- species = "Dwarf"   <- shadows class variable

# p2 object:
#  |- (no species)

# Use Instance Variables When:
# Data belongs to ONE object
# Player health, name, position
# Inventory items
# example:
# self.health
# self.score

# Use Class Variables When:
# Data is shared
# Constants
# Global counters
# Configuration values
# exmaple:
# MAX_HEALTH = 100
# enemy_count = 0


# exmaple: counting objects
class Enemy:
    count = 0     # class variable

    def __init__(self):
        Enemy.count += 1


e1 = Enemy()
e2 = Enemy()

print(Enemy.count)  # 2


# rule of thumb
# If it describes ONE thing, use an instance variable
# If it describes ALL things, use a class variable

# Unity comparison
# | Python            | Unity C#         |
# | ----------------- | ---------------- |
# | instance variable | Serialized Field |
# | class variable    | static field     |
# | self              | this             |

# correct usage
class Player:
    MAX_HEALTH = 100

    def __init__(self, name):
        self.name = name
        self.health = Player.MAX_HEALTH
