import asyncio
import discord
from assets.constants import *
import random
from classes import *

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
    async def Ollivanders(self, bot, currUser, message):
        '''
        Assigns a wand to the player.
        '''
        # supplies

        await bot.send(message, "Now that you have been sorted into your house, it is time to equip yourself with the tools of the trade. You will need a wand, a spellbook, and a potion to begin your journey.")
        await bot.send(message, "Let's head to Ollivanders where you will choose your wand, or to put it better, a wand will choose you!")
        await bot.send(message, "Please type 'wand' to proceed to Ollivanders.")

        while True:
            response = await bot.recieve(message, check=lambda message1: bot.check(message, message1))
            if response.content == "exit":
                await bot.send(response, "Farewell for now, come back again soon!")
                return False
            elif response.content == "wand":
                break
            else:
                await bot.send(response, "I'm sorry, I didn't catch that. Please try again.")

        await bot.send(message, "Welcome to Ollivanders, the finest wand shop in all of Diagon Alley! Let's see which wand chooses you.")
        await bot.send(message, "Please type 'ready' when you are ready to begin or type 'exit' to leave.")

        response = await bot.recieve(message, check=lambda message1: bot.check(message, message1))

        if response.content == "exit":
            await bot.send(response, "Farewell for now, come back again soon!")
            return False

        if response.content == "ready":
            await bot.send(message, "Let's begin then, shall we?")
            await bot.send(message, f"Hmmmm, let's see... maybe this one?")

            while True:
                length_choice = random.choice(length)
                wood_choice = random.choice(wood)
                core_choice = random.choice(core)

                await asyncio.sleep(1)

                await bot.send(message, f"{wood_choice}, {core_choice} core, {length_choice} inches")
                selected = random.sample(creatures, 3)

                await bot.send(message, f"In order to test your subconscious connection with the wand, chose one out of these 3 magical creatures: {selected[0]}, {selected[1]} or {selected[2]}.")

                response = await bot.recieve(message, check=lambda message1: bot.check(message, message1))
                if response.content == "exit":
                    await bot.send(response, "Farewell for now, come back again soon!")
                    return False

                if response.content == random.choice(selected):
                    await bot.send(message, "Congratulations your choice matched! The wand has chosen you!")
                    currUser.wand = f"{wood_choice}, {core_choice} core, {length_choice} inches"
                    await bot.send(message, "You have successfully acquired your wand!")
                    return True

                elif response.content not in selected:
                    await bot.send(message, "Please choose a creature from the list.")
                else:
                    await bot.send(message, "Not quite, let's try another one")
    async def duel(self, bot, currUser, message):
        accepted = False
        opponent_id = message.content.split(" ")[1][2:-1]
        await message.channel.send(f'''{currUser.name} has challenged {message.content.split(" ")[1]} to a duel! Do you accept {message.content.split(" ")[1]}? (yes/no)''')
        while (True):
            response = await bot.wait_for('message')
            if response.author.id == int(opponent_id) and response.channel.name == "potterbot-dueling-club" and response.content == "yes":
                accepted = True
                opponent = bot.getUser(response)
                break
            elif response.author.id == int(opponent_id) and response.channel.name == "potterbot-dueling-club" and response.content == "no":
                await message.channel.send("The duel has been declined.")
                return None
            elif response.channel.name == "potterbot-dueling-club":
                if response.author.id == int(opponent_id):
                    await message.channel.send("Invalid response.")
                elif response.content.find("~duel") != -1:
                    await message.channel.send("Pending duel request has been cancelled ")
                    break

        while True and accepted:
            await message.channel.send(f"{currUser.name}'s health points: {currUser.health}")
            await message.channel.send("|||||" + "|" * (currUser.health) * 3)
            await message.channel.send(f'''{currUser.name}'s spells: {",".join(currUser.spells)}\n ''')
            await message.channel.send(f"{opponent.name}'s health points: {opponent.health}")
            await message.channel.send("|||||" + "|" * (opponent.health) * 3)
            await message.channel.send(f'''{opponent.name}'s spells: {",".join(opponent.spells)}\n ''')
            print(currUser.id)
            print(opponent.id)
            if currUser.health <= 0:
                await message.channel.send(f"{currUser.name} has been defeated! Better luck next time.")
                opponent.points += 10
                opponent.level = opponent.points//30
                opponent.house.points += 5
                currUser.points -= 10
                currUser.level = currUser.points//30
                currUser.house.points -= 5
                break
            if opponent.health <= 0:
                await message.channel.send(f"{opponent.name} has been defeated! Better luck next time.")
                currUser.points += 10
                currUser.level = currUser.points//30
                currUser.house.points += 5
                opponent.points -= 10
                opponent.level = opponent.points//30
                opponent.house.points -= 5
                break
            fighters = {opponent.id: {"me": opponent,"opponent": currUser}, currUser.id: {"me": currUser,"opponent": opponent}}
            while True:
                response1 = await bot.wait_for('message')
                if response1.author.id == currUser.id or response1.author.id == opponent.id:
                    break
            print(response1.author.id)
            if response1.content == "exit":
                await response1.channel.send("Farewell for now, come back again soon!")
                break
            if response1.content in fighters[response1.author.id]["me"].spells:
                block = False
                spell = eval(f"{response1.content}")
                if spell.heal == 0:
                    try:
                        response2 = await bot.wait_for('message', timeout=3.0)
                    except asyncio.TimeoutError:
                        response2 = False
                    if response2:
                        if response2.author.id == fighters[response1.author.id]["opponent"].id:
                            if response2.content in fighters[response1.author.id]["opponent"].spells and response2.content == "protego":
                                await response1.channel.send(fighters[response1.author.id]["opponent"].name + " has cast Protego and blocked the spell!")
                                block = True
                if not block:
                    await response1.channel.send(fighters[response1.author.id]["me"].name + " has cast " + response1.content + " successfully!")
                    damage_amount = spell.damage
                    heal_amount = spell.heal
                    if damage_amount > 0:
                        fighters[response1.author.id]["opponent"].health -= damage_amount
                        await response1.channel.send(fighters[response1.author.id]["opponent"].name + " has taken " + str(damage_amount) + " damage!")
                    if heal_amount > 0:
                        await response1.channel.send(fighters[response1.author.id]["me"].name + " has healed for " + str(heal_amount) + " health points!")
                        if fighters[response1.author.id]["me"].health + heal_amount > fighters[response1.author.id]["me"].max_health:
                            fighters[response1.author.id]["me"].health = fighters[response1.author.id]["me"].max_health
                        else:
                            fighters[response1.author.id]["me"].health += heal_amount
        currUser.health = currUser.max_health
        opponent.health = opponent.max_health
        opponent.update_level()
        bot.save(opponent)