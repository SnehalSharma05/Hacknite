import discord


class house():
    def __init__(self, name, url):
        self.name = name
        self.points = 0
        self.students = [" "]
        self.url = url

    def __str__(self):
        return self.name

    def add_points(self, points):
        self.points += points

    def add_student(self, student):
        if hasattr(self, 'students'):
            self.students.append(student)
        else:
            self.students = [student]

    def get_points(self):
        return self.points

    def get_students(self):
        return self.students

    def get_name(self):
        return self.name

    def get_info(self, bot):
        '''
        Retures the name of the house, the number of points it has and the students.
        '''
        self.get_role(bot)
        return f"{self.role.mention}" + f" has {self.points} points. The following students are in {self.name}:\n" + "\n".join([x.name for x in self.students])

    def get_student_info(self):
        return self.name + " has the following students:\n" + "\n".join(self.students)

    def get_points_info(self, bot):
        self.get_role(bot)
        return f"{self.role.mention}" + f" has {self.points} points."

    def get_role(self, bot):
        '''
        Gets the roles for the corresponding house.
        '''

        self.role = discord.utils.get(bot.guild.roles, name=self.name)
        print(f"{self.name} has been alloted its role.")


Hufflepuff = house(
    "Hufflepuff", "https://i.pinimg.com/564x/06/02/a8/0602a8781111f5023f0b64e6a07b2e4d.jpg")
Ravenclaw = house(
    "Ravenclaw", "https://i.pinimg.com/736x/8e/e2/ef/8ee2ef549843570b76a07799f936a674.jpg")
Gryffindor = house(
    "Gryffindor", "https://i.pinimg.com/564x/fb/64/fb/fb64fb2332fe37cd45619cc98ad1232e.jpg")
Slytherin = house(
    "Slytherin", "https://i.pinimg.com/736x/2d/a3/ec/2da3ecce5858288bd939c619cfdb852f.jpg")


class item():
    def __init__(self, name, damage, effect):
        self.name = name
        self.damage = damage
        self.effect = effect


class potions():
    def __init__(self, name, effect, heal):
        self.name = name
        self.effect = effect
        self.heal = 0


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

    def add_points(self, points):
        self.points += points

    def add_spell(self, spell):
        self.spells.append(spell)

    def add_potion(self, potion):
        self.potions.append(potion)

    def add_item(self, item):
        self.items.append(item)

    async def set_house(self, bot, house):
        self.house = house
        await bot.guild.get_member(self.id).add_roles(house.role)

    def get_info(self):
        return self.name + " is in " + self.house.name + f" and has {self.points} points."

    def get_full_info(self):
        return self.name + " is in " + self.house.name + f" and has {self.points} points. You have the following spells: " + ",".join(self.spells) + "\nYou have the following wand: " + self.wand + "\nYour level is: " + str(self.level) + "\nYour max health is: " + str(self.max_health) + "\nNumber of enemies defeated: " + str(self.enemiesDefeated)

    def get_spell_info(self):
        return self.name + " has the following spells:\n" + "\n".join(self.spells)

    def get_potion_info(self):
        return self.name + " has the following potions:\n" + "\n".join(self.potions)

    def get_item_info(self):
        return self.name + " has the following items:\n" + "\n".join(self.items)

    def get_house_info(self):
        return self.name + " is in " + self.house.name + "."

    def get_points_info(self):
        return self.name + " has " + self.points + " points."

    def update_level(self):
        match self.level:
            case 0:
                self.spells = ["stupefy",
                               "expelliarmus", "protego"]
                self.health = 150
                self.max_health = 150
            case 1:
                self.spells = [
                    "stupefy", "expelliarmus", "protego", "reducto"]
                self.health = 175
                self.max_health = 175
            case 2:
                self.spells = [
                    "stupefy", "expelliarmus", "protego", "reducto", "expulso"]
                self.health = 200
                self.max_health = 200
            case 3:
                self.spells = [
                    "stupefy", "expelliarmus", "protego", "reducto", "expulso", "bombarda"]
                self.health = 225
                self.max_health = 225
            case 4:
                self.spells = [
                    "stupefy", "expelliarmus", "protego", "reducto", "expulso", "bombarda", "confringo"]
                self.health = 275
                self.max_health = 275
            case 5:
                self.spells = ["stupefy", "expelliarmus", "protego",
                               "reducto", "expulso", "bombarda", "sectumsempra", "confringo"]
                self.health = 300
                self.max_health = 300
            case 6:
                self.spells = ["stupefy", "expelliarmus", "protego", "reducto",
                               "expulso", "bombarda", "sectumsempra", "confringo", "episkey"]
                self.health = 325
                self.max_health = 325
            case 7:
                self.spells = ["stupefy", "expelliarmus", "protego", "reducto",
                               "expulso", "bombarda", "sectumsempra", "confringo", "fiendfyre", "episkey"]
                self.health = 350
                self.max_health = 350
            case 8:
                self.spells = ["stupefy", "expelliarmus", "protego", "reducto", "expulso",
                               "bombarda", "sectumsempra", "confringo", "fiendfyre", "episkey", "vulnera_sanentur"]
                self.health = 375
                self.max_health = 375
