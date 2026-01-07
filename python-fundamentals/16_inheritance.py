# Inheritance lets one class reuse and extend another class.
# A child class is a specialized version of a parent class .

# without inheritance
class Player:
    def attack(self):
        print("Player attacks")


class Enemy:
    def attack(self):
        print("Enemy attacks")
# Duplicate logic = maintenance nightmare.

# basic inheritance


class Character:
    def move(self):
        print("Character moves")


class Player(Character):
    pass


p = Player()
p.move()   # Inherited from Character
# Player automatically has everything from Character

# parent class (base class)


class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        self.health -= amount

# child subclass


class Player(Character):
    def heal(self, amount):
        self.health += amount


player = Player("Arthur", 100)
player.take_damage(30)
player.heal(20)
# Uses both parent and child behavior


# overriding methods (very important)
class Enemy(Character):
    def attack(self):
        print("Enemy attacks viciously!")


enemy = Enemy("Goblin", 50)
enemy.attack()
# Parent method is ignored if overridden.


# somtimes you want to extend, not replace.
# calling the parent method (super())
class Boss(Character):
    def take_damage(self, amount):
        print("Boss enraged!")
        super().take_damage(amount)


boss = Boss("Dragon", 300)
boss.take_damage(50)
# "super()" calls the parent version.


# correct way to inherit
class Player(Character):
    def __init__(self, name, health):
        super().__init__(name, health)

# adding a new child-only data


class Mage(Character):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.mana = mana


# use multiple inheritance carfefully. Can become confusing fast
class Flyable:
    def fly(self):
        print("Flying")


class Dragon(Character, Flyable):
    pass


# rule
# Inheritance should follow the “is-a” relationship.
# Player is a Character
# Mage is a Character
# and
# Parent = general rules
# Child = specialized behavior


# polymorphism
def attack(character):
    character.attack()


attack(Player())
attack(Enemy())
# Same interface, different behavior.

# composition vs inheritance
# use this


class Player:
    def __init__(self, weapon):
        self.weapon = weapon

# vs this


class Player(Weapon):
    pass


# | Python      | Unity              |
# | ----------- | ------------------ |
# | Base class  | Base MonoBehaviour |
# | Child class | Derived script     |
# | "super()"   | "base."            |
# | Override    | "override" keyword |


# core pattern to memorize
class Parent:
    pass


class Child(Parent):
    pass
