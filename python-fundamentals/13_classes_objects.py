# Big Picture (Plain English)
# Class -> a blueprint
# Object -> a thing built from the blueprint
# A class defines what something is and what it can do
# An object is an actual instance of that class

# real world analogy
# Class  -> Blueprint
# Object -> Actual house
# you can build many houses with one blueprint

# first class
class Player:
    pass
# Creates a new type called Player
# Right now it has no data or behavior


# creating objects (instances)
player1 = Player()
player2 = Player()
# important
# player1 and player2 are separate objects
# Same class, different memory


class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

# What __init__ Means:
# Runs automatically when you create an object
# Used to initialize data
# self means: (self.name)
# “THIS specific object”
# self refers to the object being created or used
# Python passes it automatically


player = Player("Arthur", 100)
print(player.name)     # Arthur
print(player.health)   # 100


# adding behavior (methods)
class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        self.health -= amount


player = Player("Arthur", 100)
player.take_damage(25)

print(player.health)   # 75

# methods
# Functions inside a class
# Always use self

# object state (why classes matter)
player1 = Player("Arthur", 100)
player2 = Player("Lancelot", 120)

player1.take_damage(50)

print(player1.health)  # 50
print(player2.health)  # 120

# Each object keeps its own state

# default values


class Enemy:
    def __init__(self, name, health=50):
        self.name = name
        self.health = health


goblin = Enemy("Goblin")
orc = Enemy("Orc", 100)

# class variables vs instance variables

# instance variables (unique per object)
# self.health
# class variable (shared)


class Player:
    species = "Human"

    def __init__(self, name):
        self.name = name


print(Player.species)
print(player1.species)

Player.species = "Elf"
# changes it for all players


# methods that return values
class Player:
    def is_alive(self):
        return self.health > 0


if player.is_alive():
    print("Player is alive!")


# objects inside objects (composition)
class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


class Player:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon


sword = Weapon("Excalibur", 50)
player = Player("Arthur", sword)

print(player.weapon.damage)


# Common Beginner Mistakes:
# Forgetting self
# Using class variables accidentally
# Modifying shared data unintentionally
# Thinking class = object

# comparing to Unity game dev
# | Python    | Unity      |
# | --------- | ---------- |
# | Class     | Script     |
# | Object    | GameObject |
# | Method    | Function   |
# | Attribute | Field      |


# A class groups data + behavior
# An object is a living instance of that group

# core pattern to memorize
class Name:
    def __init__(self, data):
        self.data = data

    def method(self):
        pass
