
# __init__ -> sets up the object when it’s created
# self -> refers to the specific object being worked on

# __init__ is a special method(called a constructor).

# It runs automatically when you create a new object.

class Player:
    def __init__(self):
        print("Player created!")


p = Player()
# You did not call __init__ manually
# Python called it for you

# without __init__:
player = Player()
player.name = "Arthur"
player.health = 100

# with __init__:


class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health


player = Player("Arthur", 100)
# Cleaner
# Safer
# Guarantees required data exists


# self means -> the specific object
player1 = Player("Arthur", 100)
player2 = Player("Lancelot", 120)

# self is player1 OR player2 depending on who called it

# why python needs "self"
# class Player:
#     def take_damage(self, amount):
#         self.health -= amount
# when you write
# player.take_damage(10)
# python secretly turns it into:
# Player.take_damage(player, 10)

# self.variable vs normal variables
# class Player:
#     def __init__(self, name):
#         self.name = name

# | Code        | Meaning              |
# | ----------- | -------------------- |
# | "name"      | Local variable       |
# | "self.name" | Stored on the object |

# correct way
# self.name = name
# self in Every Method (Not Just __init__)


class Player:
    def heal(self, amount):
        self.health += amount


# example:
# player = Player("Arthur", 100)
# in memory (visualization)
# player
#  |- name: "Arthur"
#  |- health: 100
# each object gets it's own copy

# common beginner mistakes:
# forgetting self, forgetting self when storing data, calling methods incorrectly,


# how this maps to Unity
# | Python     | Unity C#                |
# | ---------- | ----------------------- |
# | "self"     | "this"                  |
# | "__init__" | "Start()" / constructor |
# | Class      | Script                  |
# | Object     | GameObject              |


# minimal pattern to mermorize
# class Thing:
#     def __init__(self, value):
#         self.value = value

#     def show(self):
#         print(self.value)


# __init__ = setup instructions
# self = the object being set up
