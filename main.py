import asyncio
import discord



class house():
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.students = []

    def __str__(self):
        return self.name

    def add_points(self, points):
        self.points += points

    def add_student(self, student):
        self.students.append(student)

    def get_points(self):
        return self.points

    def get_students(self):
        return self.students

    def get_name(self):
        return self.name

    def get_info(self):
        return self.name + f" has {self.points} points. The following students are in {self.name}:\n" + "\n".join([x.name for x in self.students])

    def get_student_info(self):
        return self.name + " has the following students:\n" + "\n".join(self.students)

    def get_points_info(self):
        return self.name + f" has {self.points} points."


Hufflepuff = house("Hufflepuff")
Ravenclaw = house("Ravenclaw")
Gryffindor = house("Gryffindor")
Slytherin = house("Slytherin")

class user():
    users = []
    names = []
    ids = {}

    def __init__(self, name, id, house=None, wand=None, points=0, wealth=0, potions=[], spells=['stupefy', 'expelliarmus', 'protego'], items=[], progress=0, enemiesDefeated=0, health=150):
        self.name = name
        self.id = id
        self.house = house
        self.health = health
        self.max_health = health
        self.enemiesDefeated = enemiesDefeated
        self.wand = wand
        self.spells = spells
        self.points = points
        self.level = self.points//30
        self.wealth = wealth
        self.potions = potions
        self.items = items
        self.progress = progress
        user.users.append(self)
        user.names.append(self.name)
        user.ids[self.id] = self
        self.revealed = False

    def add_points(self, points):
        self.points += points

    def add_spell(self, spell):
        self.spells.append(spell)

    def add_potion(self, potion):
        self.potions.append(potion)

    def add_item(self, item):
        self.items.append(item)

    def set_house(self, house):
        self.house = house

    def get_info(self):
        return self.name + " is in " + self.house + f" and has {self.points} points."

    def get_full_info(self):
        return self.name + " is in " + self.house + f" and has {self.points} points. You have the following spells: " + ",".join(self.spells) + "\nYou have the following wand: " + self.wand + "\nYour level is: " + str(self.level) + "\nYour max health is: " + str(self.max_health) + "\nNumber of enemies defeated: " + str(self.enemiesDefeated)

    def get_spell_info(self):
        return self.name + " has the following spells:\n" + "\n".join(self.spells)

    def get_potion_info(self):
        return self.name + " has the following potions:\n" + "\n".join(self.potions)

    def get_item_info(self):
        return self.name + " has the following items:\n" + "\n".join(self.items)

    def get_house_info(self):
        return self.name + " is in " + self.house + "."

    def get_points_info(self):
        return self.name + " has " + self.points + " points."
