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

class games:
    async def introduction(self, bot, message):
        '''
        This function is used whenever the user wants to login and use the bot.
        '''
        await bot.send(message, "Greetings! Welcome to the whimsical world of PotterBot, where the whispers of ancient spells and the flicker of wands weave tales of wonder reminiscent of Dumbledore's office. Here, amid the hallowed halls of Hogwarts, where portraits come to life and enchanted creatures roam, embark on a journey beyond the pages of the Marauder's Map, where mischief and magic await your command!")
        await bot.send(message, "If you wish to leave at any point in the game, just type 'exit'.")

        if message.author.id in user.ids:
            await bot.send(message, "Welcome back to Hogwarts, " + user.ids[message.author.id].name + "!")
            return user.ids[message.author.id]

        currUser = await self.new_user(bot, message)

        return currUser

    async def new_user(self, bot, message):
        '''
        Function to initiate a new user.
        '''
        await bot.send(message, "Welcome, new user! Please choose your username.")
        response = await bot.recieve(message, check=lambda message1: bot.check(message1, message))
        if response.content == "exit":
            await bot.send(response, "Goodbye.")
            return None

        if response.content in user.names:
            await bot.send(response, "I'm sorry, that username is already taken. Please try again.")
            return await bot.new_user(message)

        u = user(response.content, response.author.id)
        await bot.send(response, "Welcome to Hogwarts, " + response.content + "!")

        return u

    async def plat9_3_4(self, bot, currUser, message):
        '''
        The first level of our game.
        '''

        await bot.send(message, "The Hogwarts Express awaits to transport you to the enchanted realm of Hogwarts.")
        await bot.send(message, "In order to cross the brick wall, please type 'Hogwarts Express' in under 5 seconds.")
        await bot.send(message, "Type 'ready' when you are ready to begin. If you wish to exit, type anything else.")

        response = await bot.recieve(message, check=lambda message1: bot.check(message1, message))

        if response.content == "ready":
            await bot.send(response, "Let the magic begin!")

            while True:
                await bot.send(message, "Your time starts...")
                await asyncio.sleep(1)
                await bot.send(message, "Now!")

                try:
                    response = await bot.wait_for('message', check=lambda message1: bot.check(message, message1), timeout=5.0)

                    if response.content == "exit":
                        await bot.send(message, "Looks like you are in need of a little more practice my friend. Farewell for now, come back to try again soon!")
                        return False

                    if response.content == "Hogwarts Express":
                        await bot.send(message, "Merlin's Beard! You made it! You are ready to board the Hogwarts Express!")
                        return True

                    else:
                        await bot.send(message, "Blimey! That's not the correct phrase. Please try again.")

                except asyncio.TimeoutError:
                    await bot.send(message, "Ahhhh, you didn't make it in time. Please try again.")

                await message.channel.send("Type 'ready' to try again or 'exit' to leave.")
                response = await bot.recieve(message, check=lambda message1: bot.check(message1, message))
                if response.content == "exit":
                    await bot.send(response, "Farewell for now, come back again soon!")
                    return False
                elif response.content == "ready":
                    continue
        else:
            await bot.send(response, "Farewell for now, come back again soon!")
            return False

    async def house_sort(self, bot, currUser, message):
        '''
        Sorts users into different houses based on choice.
        '''
        await bot.send(message, "Ah, but before you venture further into the realm of magic, let us unveil the essence of your true nature. Answer me this: When faced with a challenging dilemma, do you find solace in the warmth of companionship(a), the pursuit of knowledge(b), the thrill of adventure(c), or the allure of power(d)?")

        while True:
            response = await bot.recieve(message, check=lambda message1: bot.check(message1, message))
            if response.content == "exit":
                await bot.send(response, "Farewell for now, come back again soon!")
                return False

            elif response.content == "a":
                currUser.set_house(Hufflepuff)
                Hufflepuff.add_student(currUser)
                await bot.send(response, "Ah, Hufflepuff it is! The house of the loyal and the kind, where friendship and hard work are valued above all. Welcome to the house of the badger!")
                return True

            elif response.content == "b":
                currUser.set_house(Ravenclaw)
                Ravenclaw.add_student(currUser)
                await bot.send(response, "Ah, Ravenclaw it is! The house of the wise and the clever, where wit and intelligence are revered. Welcome to the house of the eagle!")
                return True

            elif response.content == "c":
                currUser.set_house(Gryffindor)
                Gryffindor.add_student(currUser)
                await bot.send(response, "Ah, Gryffindor it is! The house of the brave and the bold, where courage and loyalty reign supreme. Welcome to the house of the lion!")
                return True

            elif response.content == "d":
                currUser.set_house(Slytherin)
                Slytherin.add_student(currUser)
                await bot.send(response, "Ah, Slytherin it is! The house of the cunning and the ambitious, where resourcefulness and determination are prized. Welcome to the house of the serpent!")
                return True

            else:
                await bot.send(response, "I'm sorry, I didn't catch that. Please try again. Type exit to leave the game.")
