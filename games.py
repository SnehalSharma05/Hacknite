import asyncio
import discord
import random
from assets.constants import *
from assets.enemies import *
import random
from classes import *
from EmbedMsg import *


class games:
    async def introduction(self, bot, message):
        '''
        This function is used whenever the user wants to login and use the bot.
        '''
        msg = "***Greetings! Welcome to the whimsical world of PotterBot, where the whispers of ancient spells and the flicker of wands weave tales of wonder reminiscent of Dumbledore's office. Here, amid the hallowed halls of Hogwarts, where portraits come to life and enchanted creatures roam, embark on a journey beyond the pages of the Marauder's Map, where mischief and magic await your command!***"
        em = embedMessage(colour=discord.Colour.blue(),
                          image="https://i.pinimg.com/originals/25/ce/3f/25ce3f11dda654caab19841c389b2878.gif",
                          description=msg, title="Welcome to Hogwarts")
        await bot.create_embed(em, message)

        msg = "***If you wish to leave at any point in the game, just type 'exit'.***"
        em = embedMessage(colour=discord.Colour.blue(), description=msg)
        await bot.create_embed(em, message)

        if message.author.id in user.ids:
            msg = f"***Welcome back to Hogwarts, {user.ids[message.author.id].name}!***"
            em = embedMessage(colour=discord.Colour.blue(), description=msg)
            await bot.create_embed(em, message)
            return user.ids[message.author.id]

        currUser = await self.new_user(bot, message)

        return currUser

    async def new_user(self, bot, message):
        '''
        Function to initiate a new user.
        '''
        msg = "***Welcome, new user! Please choose your username.***"
        em = embedMessage(colour=discord.Colour.blue(
        ), image="https://i.pinimg.com/564x/84/55/7c/84557c07e99c33dc9c65a0d105aeb195.jpg", description=msg)
        await bot.create_embed(em, message)

        while True:
            response = await bot.recieve(message, check=lambda message1: bot.check(message1, message))
            if response.content == "exit" and response.channel.name == "general":
                msg = "***Farewell for now, come back again soon!***"
                em = embedMessage(colour=discord.Colour.blue(), description=msg)
                await bot.create_embed(em, message)
                return None
            elif response.channel.name == "general":
                if response.content in user.names:
                    msg = "***I'm sorry, that username is already taken. Please try again.***"
                    em = embedMessage(colour=discord.Colour.blue(), description=msg)
                    await bot.create_embed(em, message)
                    return await bot.new_user(message)

                u = user(response.content, response.author.id)
                msg =  f"***Welcome to Hogwarts, {response.content}!***"
                em = embedMessage(colour=discord.Colour.blue(), description=msg)
                await bot.create_embed(em, message)

                return u
            else:
                msg = "***A game is already in progress in the channel 'general'. Do you want to exit the game? (yes/anything else)***"
                em = embedMessage(colour=discord.Colour.blue(), description=msg)
                await bot.create_embed(em, message)
                response = await bot.recieve(message, check=lambda message1: bot.check(message1, message))
                if response.content == "yes":
                    msg = "***Farewell for now, come back again soon!***"
                    em = embedMessage(colour=discord.Colour.blue(), description=msg)
                    await bot.create_embed(em, message)
                    return None

    async def plat9_3_4(self, bot, currUser, message):
        '''
        The first level of our game.
        '''

        msg = """
        ***The Hogwarts Express awaits to transport you to the enchanted realm of Hogwarts.
        In order to cross the brick wall, please type 'Hogwarts Express' in under 5 seconds.
        Type 'ready' when you are ready to begin. If you wish to exit, type anything else.***
        """

        em = embedMessage(colour=discord.Colour.red(), description=msg,
                          image="https://i.pinimg.com/originals/48/c4/b0/48c4b08c488bb6b888eb72eb0230b34b.gif")
        await bot.create_embed(em, message)
        em.set_image(url=None)

        response = await bot.recieve(message, check=lambda message1: bot.check(message1, message))

        if response.content == "ready":

            msg = "***Let the magic begin!***"
            em.description = msg
            await bot.create_embed(em, message)

            while True:
                await bot.send(message, "**Your time starts...**")
                await asyncio.sleep(1)
                await bot.send(message, "**Now!**")

                try:
                    response = await bot.wait_for('message', check=lambda message1: bot.check(message, message1), timeout=5.0)

                    if response.content == "exit":
                        msg = "***Looks like you are in need of a little more practice my friend. Farewell for now, come back to try again soon!***"
                        em.description = msg
                        await bot.create_embed(em, message)
                        return False

                    if response.content == "Hogwarts Express":
                        msg = "***Merlin's Beard! You made it! You are ready to board the Hogwarts Express!***"
                        em.description = msg
                        await bot.create_embed(em, message)
                        return True

                    else:
                        msg = "***Blimey! That's not the correct phrase. Please try again.***"
                        em.description = msg
                        await bot.create_embed(em, message)

                except asyncio.TimeoutError:
                    msg = "***Ahhhh, you didn't make it in time. Please try again.***"
                    em.description = msg
                    await bot.create_embed(em, message)

                msg = "***Type 'ready' to try again or 'exit' to leave.***"
                em.description = msg
                await bot.create_embed(em, message)

                response = await bot.recieve(message, check=lambda message1: bot.check(message1, message))
                if response.content == "exit":
                    msg = "***Farewell for now, come back again soon!***"
                    em.description = msg
                    await bot.create_embed(em, message)
                    return False
                elif response.content == "ready":
                    continue
        else:
            msg = "***Farewell for now, come back again soon!***"
            em.description = msg
            await bot.create_embed(em, message)
            return False

    async def house_sort(self, bot, currUser, message):
        '''
        Sorts users into different houses based on choice.
        '''

        msg = " *** Ah, but before you venture further into the realm of magic, let us unveil the essence of your true nature. Answer me this: When faced with a challenging dilemma, do you find solace in:***\n *(a) the warmth of companionship,*\n *(b) the pursuit of knowledge,*\n *(c) the thrill of adventure, or,*\n *(d) the allure of power?*"
        em = embedMessage(colour=discord.Colour.orange(), title="The Sorting Ceremony", description=msg,
                          image="https://i.pinimg.com/originals/8f/29/26/8f292677875dc83ce30c40c94a72c0e3.gif")
        await bot.create_embed(em, message)

        while True:
            response = await bot.recieve(message, check=lambda message1: bot.check(message1, message))
            if response.content == "exit" and response.channel.name == "general":
                msg = "***Farewell for now, come back again soon!***"
                em = embedMessage(
                    colour=discord.Colour.orange(), description=msg)
                await bot.create_embed(em, message)
                return False
            elif response.channel.name == "general":
                if response.content == "a":
                    await currUser.set_house(bot, "Hufflepuff")
                    Hufflepuff.add_student(currUser)
                    msg = "*** Ah, Hufflepuff it is! The house of the loyal and the kind, where friendship and hard work are valued above all. Welcome to the house of the badger!***"
                    em = embedMessage(colour=discord.Colour.yellow(), description=msg, title="Hufflepuff",
                                      image=eval(currUser.house).url)
                    await bot.create_embed(em, message)
                    return True

                elif response.content == "b":
                    await currUser.set_house(bot, "Ravenclaw")
                    Ravenclaw.add_student(currUser)
                    msg = "*** Ah, Ravenclaw it is! The house of the wise and the clever, where wit and intelligence are revered. Welcome to the house of the eagle!***"
                    em = embedMessage(colour=discord.Colour.blue(), description=msg, title="Ravenclaw",
                                      image=eval(currUser.house).url)
                    await bot.create_embed(em, message)
                    return True

                elif response.content == "c":
                    await currUser.set_house(bot, "Gryffindor")
                    Gryffindor.add_student(currUser)
                    msg = "*** Ah, Gryffindor it is! The house of the brave and the bold, where courage and loyalty reign supreme. Welcome to the house of the lion!***"
                    em = embedMessage(colour=discord.Colour.red(), description=msg, title="Gryffindor",
                                      image=eval(currUser.house).url)
                    await bot.create_embed(em, message)
                    return True

                elif response.content == "d":
                    await currUser.set_house(bot, "Slytherin")
                    Slytherin.add_student(currUser)
                    msg = "*** Ah, Slytherin it is! The house of the cunning and the ambitious, where resourcefulness and determination are prized. Welcome to the house of the serpent!***"
                    em = embedMessage(colour=discord.Colour.green(), description=msg, title="Slytherin",
                                      image=eval(currUser.house).url)
                    await bot.create_embed(em, message)
                    return True

                else:
                    msg = "***I'm sorry, I didn't catch that. Please try again. Type exit to leave the game.***"
                    em = embedMessage(
                        colour=discord.Colour.orange(), description=msg)
                    await bot.create_embed(em, message)

            else:
                msg = "A game is already in progress in the channel 'general'. Do you want to exit the game? (yes/anything else)"
                em = embedMessage(
                    colour=discord.Colour.orange(), description=msg)
                await bot.create_embed(em, message)
                response = await bot.recieve(message, check=lambda message1: bot.check(message1, message))
                if response.content == "yes":
                    msg = "***Farewell for now, come back again soon!***"
                    em = embedMessage(
                        colour=discord.Colour.orange(), description=msg)
                    await bot.create_embed(em, message)
                    return False

    async def Ollivanders(self, bot, currUser, message):
        '''
        Assigns a wand to the player.
        '''

        msgs = """
        ***Congratulations on being sorted into your house! Now it's time to equip yourself with the tools of the trade. You will need a wand!
        Let's head to Ollivanders where you will choose your wand, or to put it better, a wand will choose you!
        Please type 'wand' to proceed to Ollivanders.***
        """

        author = "Garrick Ollivanders"
        author_icon = "https://i.pinimg.com/564x/6a/7b/c4/6a7bc4448eb1632df3ee78359f3149fb.jpg"

        em = embedMessage(colour=discord.Colour.from_rgb(135, 62, 35), description=msgs,
                          image="https://i.pinimg.com/564x/d3/81/13/d38113d3bbdd1a136fa3d83b6ca8a5b0.jpg", author=author, author_url=author_icon)
        await bot.create_embed(em, message)
        em.set_image(url=None)

        while True:
            response = await bot.recieve(message, check=lambda message1: bot.check(message, message1))
            if response.content == "exit" and response.channel.name == "general":
                msg = "Farewell for now, come back again soon!"
                em.description = msg
                await bot.create_embed(em, message)
                return False
            elif response.channel.name == "general":
                if response.content == "wand":
                    break
                else:
                    msg = "I'm sorry, I didn't catch that. Please try again."
                    em.description = msg
                    await bot.create_embed(em, message)
            else:
                msg = "A game is already in progress in the channel 'general'. Do you want to exit the game? (yes/anything else)"
                em.description = msg
                await bot.create_embed(em, message)
                response = await bot.recieve(message, check=lambda message1: bot.check(message1, message))
                if response.content == "yes":
                    msg = "Farewell for now, come back again soon!"
                    em.description = msg
                    await bot.create_embed(em, message)
                    return False

        msg = """
        ***Welcome to Ollivanders, the finest wand shop in all of Diagon Alley! Let's see which wand chooses you.
        Please type 'ready' when you are ready to begin or type 'exit' to leave.***
        """
        em = embedMessage(colour=discord.Colour.from_rgb(135, 62, 35), description=msg, author=author, author_url=author_icon,
                          image="https://i.pinimg.com/564x/96/cb/72/96cb72d67bef839ccba6d5af4a9c328d.jpg")
        await bot.create_embed(em, message)
        em.set_image(url=None)

        response = await bot.recieve(message, check=lambda message1: bot.check(message, message1))

        if response.content == "exit":
            msg = "Farewell for now, come back again soon!"
            em.description = msg
            await bot.create_embed(em, message)
            return False

        if response.content == "ready":
            msg = """
            ***Let's begin then, shall we?
            Hmmm, let's see... maybe this one?***
            """
            em.description = msg
            await bot.create_embed(em, message)

            while True:
                length_choice = random.choice(length)
                wood_choice = random.choice(wood)
                core_choice = random.choice(core)

                await asyncio.sleep(1)
                msg = f"***{wood_choice}, {core_choice} core, {length_choice} inches***"
                em.description = msg
                await bot.create_embed(em, message)
                selected = random.sample(creatures, 3)
                msg = f"***In order to test your subconscious connection with the wand, chose one out of these 3 magical creatures: {selected[0]}, {selected[1]} or {selected[2]}.***"
                em.description = msg
                await bot.create_embed(em, message)

                response = await bot.recieve(message, check=lambda message1: bot.check(message, message1))
                if response.content == "exit":
                    msg = "***Farewell for now, come back again soon!***"
                    em.description = msg
                    await bot.create_embed(em, message)
                    return False

                if response.content == random.choice(selected):
                    currUser.wand = f"{wood_choice}, {core_choice} core, {length_choice} inches"
                    msg = f"***Congratulations! You have successfully acquired your wand: {currUser.wand}!***"
                    em.description = msg
                    await bot.create_embed(em, message)
                    return True

                elif response.content not in selected:
                    msg = "***Please choose a creature from the list.***"
                    em.description = msg
                    await bot.create_embed(em, message)
                else:
                    msg = "***Not quite, let's try another one***"
                    em.description = msg
                    await bot.create_embed(em, message)

    async def duel(self, bot, currUser, message):
        accepted = False
        opponent_id = message.content.split(" ")[1][2:-1]
        msg = f'''***{currUser.name} has challenged {message.content.split(" ")[1]} to a duel! Do you accept {message.content.split(" ")[1]}? (yes/no)***'''
        em = embedMessage(colour=discord.Colour.blue(), description=msg,
                          image="https://i.pinimg.com/originals/23/00/03/230003875d5f21c81cc43704d3861f16.gif")
        await bot.create_embed(em, message)
        while (True):
            response = await bot.recieve(message)
            if response.author.id == int(opponent_id) and response.channel.name == "dueling-club" and response.content == "yes":
                accepted = True
                bot.notFreeUser.append(int(opponent_id))
                opponent = bot.getUser(response)
                if (opponent == None or opponent.progress < 4):
                    em = embedMessage(color=discord.Colour.blue(), description="***You have not completed the introductory quests, please finish them first.***")
                    await bot.create_embed(em, message)
                    return None

                break
            elif response.author.id == int(opponent_id) and response.channel.name == "dueling-club" and response.content == "no":
                msg = "***The duel has been declined.***"
                em = embedMessage(
                    colour=discord.Colour.blue(), description=msg)
                await bot.create_embed(em, message)
                return None
            elif response.channel.name == "dueling-club":
                if response.author.id == int(opponent_id):
                    msg = "***Invalid response***"
                    em = embedMessage(
                        colour=discord.Colour.blue(), description=msg)
                    await bot.create_embed(em, message)
                elif response.content.find("~duel") != -1:
                    msg = "***Pending duel request has been cancelled.***"
                    em = embedMessage(
                        colour=discord.Colour.blue(), description=msg)
                    await bot.create_embed(em, message)
                    break

        while True and accepted:
            msg = f'''***{currUser.name}'s health points: {currUser.health}***\n'''+("🟩" + "🟩" * (currUser.health // 6))+f'''\n***{currUser.name}'s spells: {",".join(currUser.spells)}***\n''' +"\n"+ f"***{opponent.name}'s health points: {opponent.health}***\n" + ("🟩" + "🟩" * (opponent.health // 6)) + f'''***\n{opponent.name}'s spells: {",".join(opponent.spells)}\n***'''
            em = embedMessage(colour=discord.Colour.blue(), description=msg)
            await bot.create_embed(em, message)
            print(currUser.id)
            print(opponent.id)
            if currUser.health <= 0:
                msg = f"***{currUser.name} has been defeated! Better luck next time.***"
                em = embedMessage(
                    colour=discord.Colour.blue(), description=msg)
                await bot.create_embed(em, message)
                opponent.points += 10
                opponent.level = opponent.points//30
                eval(opponent.house).add_points(5)
                currUser.points -= 10
                currUser.level = currUser.points//30
                eval(currUser.house).add_points(-5)
                break
            if opponent.health <= 0:
                msg = f"***{opponent.name} has been defeated! Better luck next time.***"
                em = embedMessage(
                    colour=discord.Colour.blue(), description=msg)
                await bot.create_embed(em, message)
                currUser.points += 10
                currUser.level = currUser.points//30
                eval(currUser.house).add_points(5)
                opponent.points -= 10
                opponent.level = opponent.points//30
                eval(opponent.house).add_points(-5)
                break
            fighters = {opponent.id: {"me": opponent, "opponent": currUser}, currUser.id: {
                "me": currUser, "opponent": opponent}}
            while True:
                response1 = await bot.wait_for('message')
                if response1.author.id == currUser.id or response1.author.id == opponent.id:
                    break
            print(response1.author.id)
            if response1.content == "exit" and response1.channel.name == "dueling-club":
                msg = "***Farewell for now, come back again soon!***"
                em = embedMessage(
                    colour=discord.Colour.blue(), description=msg)
                await bot.create_embed(em, message)
                break
            elif response1.channel.name == "dueling-club":
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
                                    msg = "***" + \
                                        fighters[response1.author.id]["opponent"].name + \
                                        " has cast Protego and blocked the spell!***"
                                    em = embedMessage(colour=discord.Colour.blue(
                                    ), description=msg, image="https://i.pinimg.com/originals/b7/b6/78/b7b678bdc295fb6dcaac5a5a630b9fa4.gif")
                                    await bot.create_embed(em, message)
                                    block = True
                    if not block:
                        await response1.channel.send(fighters[response1.author.id]["me"].name + " has cast " + response1.content + " successfully!")
                        damage_amount = spell.damage
                        heal_amount = spell.heal
                        if damage_amount > 0:
                            fighters[response1.author.id]["opponent"].health -= damage_amount
                            msg = "***"+fighters[response1.author.id]["opponent"].name + \
                                " has taken " + \
                                str(damage_amount) + " damage!***"
                            em = embedMessage(
                                colour=discord.Colour.red(), description=msg)
                            await bot.create_embed(em, message)
                        if heal_amount > 0:
                            msg = "***" + fighters[response1.author.id]["me"].name + \
                                " has healed for " + \
                                str(heal_amount) + " health points!***"
                            em = embedMessage(
                                colour=discord.Colour.green(), description=msg)
                            await bot.create_embed(em, message)
                            if fighters[response1.author.id]["me"].health + heal_amount > fighters[response1.author.id]["me"].max_health:
                                fighters[response1.author.id]["me"].health = fighters[response1.author.id]["me"].max_health
                            else:
                                fighters[response1.author.id]["me"].health += heal_amount
                else:
                    msg = "***You do not have that spell.***"
                    em = embedMessage(
                        colour=discord.Colour.red(), description=msg)
                    await bot.create_embed(em, message)
            else:
                msg = "***A game is already in progress in the channel 'dueling-club'. Do you want to exit the duel? (yes/anything else)***"
                em = embedMessage(colour=discord.Colour.red(), description=msg)
                await bot.create_embed(em, message)
                response1 = await bot.recieve(message, check=lambda message1: bot.check(message1, message))
                if response1.content == "yes":
                    msg = "***Farewell for now, come back again soon!***"
                    em = embedMessage(
                        colour=discord.Colour.blue(), description=msg)
                    await bot.create_embed(em, message)
                    break
        currUser.health = currUser.max_health
        opponent.health = opponent.max_health
        opponent.update_level()
        bot.notFreeUser.remove(int(opponent.id))
        bot.save(opponent)

    async def staircase(self, bot, currUser, message):
        total_stairs = 20
        moves_left = total_stairs//2
        stairs_left = total_stairs
        cap_steps = total_stairs//3

        msg = f"***You and your friend are running late to class and you've just stepped onto the moving staircases. You now get {moves_left} moves to climb up {total_stairs} stairs to make it to your Transfiguration lesson on time.*** \n ***Here's what you have to do:*** \n***Type in the number of stairs you wanna climb at a time and then play a game of 7 up 7 down to see if you were successful. Mind your step! You don't wanna step onto a trick stair which will cause you to get stuck on that stair for the next move.***\n***Consecuently that move will be skipped (total moves reduces by 2)***\n ***Max steps that can be crossed per move is {cap_steps}. All the best!***"
        em = embedMessage(colour=discord.Colour.orange(), description=msg, title = "Moving Staircases", image="https://i.pinimg.com/originals/20/70/1d/20701db00f0e3bc9c358ed296d254b32.gif")
        await bot.create_embed(em, message)
        msg = "***If you don't know how 7 Up 7 Down works, enter '7' to learn now. Otherwise, type 'play' to start the game.***"
        em = embedMessage(colour=discord.Colour.orange(), description=msg)
        await bot.create_embed(em, message)

        while True:
            response = await bot.wait_for('message', check=lambda message1: bot.check(message, message1))
            if response.channel.name == "general":
                if response.content == "exit":
                    msg = "***Farewell for now, come back again soon!***"
                    em = embedMessage(colour=discord.Colour.orange(), description=msg)
                    await bot.create_embed(em, message)
                    return False

                elif response.content == "play":
                    break

                elif response.content == "7":
                    msg = "***The random number generator generates a number between 1 to 12. You have to guess if the number is >=7 or <7 (Enter a number >=7 or <7 to guess respectively). If your guess is correct, you move up your chosen number of steps; but if your guess is wrong, you fall down the chosen number of steps.***"
                    em = embedMessage(colour=discord.Colour.orange(), description=msg)
                    await bot.create_embed(em, message)
                    msg = "***Now that the rules are , let's proceed to the game.***"
                    em = embedMessage(colour=discord.Colour.orange(), description=msg)
                    await bot.create_embed(em, message)
                    break

                else:
                    msg = "***I'm sorry, I didn't catch that. Please try again.***"
                    em = embedMessage(colour=discord.Colour.orange(), description=msg)
                    await bot.create_embed(em, message)
            else:
                msg = "***A game is already in progress in the channel 'general'. Do you want to exit the game? (yes/anything else)***"
                em = embedMessage(colour=discord.Colour.orange(), description=msg)
                await bot.create_embed(em, message)
                response = await bot.wait_for('message', check=lambda message1: bot.check(message1, message))
                if response.content == "yes":
                    msg = "***Farewell for now, come back again soon!***"
                    em = embedMessage(colour=discord.Colour.orange(), description=msg)
                    await bot.create_embed(em, message)
                    return False

        trick = False

        while moves_left > 0 and stairs_left > 0:
            trick = random.choice([True, False, False, False, False, False])

            while True:
                msg = "***How many steps do you wanna take at a time?***"
                em = embedMessage(colour=discord.Colour.orange(), description=msg)
                await bot.create_embed(em, message)
                response = await bot.wait_for('message', check=lambda message1: bot.check(message1, message))
                n = response.content
                if n.isdigit() and int(n) > 0 and int(n) <= cap_steps:
                    break
                else:
                    msg = f"***Please enter a valid number from 1-{cap_steps}.***"
                    em = embedMessage(colour=discord.Colour.orange(), description=msg)
                    await bot.create_embed(em, message)

            while True:
                msg = "***Let's see if the odds are in your favour! Pick a number between 1 to 12 (both included).***"
                em = embedMessage(colour=discord.Colour.orange(), description=msg)
                await bot.create_embed(em, message)
                response = await bot.wait_for('message', check=lambda message1: bot.check(message1, message))
                guess = response.content

                if response.content == "exit":
                    msg = "***Farewell for now, come back again soon!***"
                    em = embedMessage(colour=discord.Colour.orange(), description=msg)
                    await bot.create_embed(em, message)
                    return False

                elif guess.isdigit():
                    if int(guess) >= 1 and int(guess) <= 12:
                        break
                    else:
                        msg = "***Please enter a valid guess from 1-12.***"
                        em = embedMessage(colour=discord.Colour.orange(), description=msg)
                        await bot.create_embed(em, message)

                else:
                    msg = "***Please enter a valid guess.***"
                    em = embedMessage(colour=discord.Colour.orange(), description=msg)
                    await bot.create_embed(em, message)

            random_no = random.randint(1, 12)

            if trick == True:
                increment_steps = random.randint(1, int(n))
                msg = f"***Oh no! You stepped on a trick step on the {increment_steps} step.***"
                em = embedMessage(colour=discord.Colour.orange(), description=msg)
                await bot.create_embed(em, message)
                stairs_left = min(stairs_left + increment_steps, total_stairs)
                moves_left -= 1

            if not trick and ((random_no >= 7 and int(guess) >= 7) or (random_no < 7 and int(guess) < 7)):
                msg = f"***Congrats! You have climbed {n} steps.***"
                em = embedMessage(colour=discord.Colour.orange(), description=msg)
                await bot.create_embed(em, message)
                stairs_left = max(0, stairs_left - int(n))

            elif not trick:
                msg = f"***Alas! You have fallen down {n} steps. Better luck next time.***"
                em = embedMessage(colour=discord.Colour.orange(), description=msg)
                await bot.create_embed(em, message)
                stairs_left = min(stairs_left + int(n), total_stairs)

            moves_left -= 1
            msg = f"***You now have to climb {stairs_left} stairs in {moves_left} moves.***"
            em = embedMessage(colour=discord.Colour.orange(), description=msg)
            await bot.create_embed(em, message)

            if (moves_left*cap_steps < stairs_left):
                amsg = f"***Oh no, you don't have enough moves!***"
                em = embedMessage(colour=discord.Colour.orange(), description=msg)
                await bot.create_embed(em, message)
                break

        if stairs_left == 0:
            msg = f"***Phew! You've managed to maneuver the magical staircases to reach class on time. Now Professor McGonagall won't transfigure you into a pocket watch!***"
            em = embedMessage(colour=discord.Colour.orange(), description=msg, image = "https://i.pinimg.com/564x/a6/07/a1/a607a1e0670ae4e4fcda1d0e8775144a.jpg")
            await bot.create_embed(em, message)
            return True

        else:
            msg = f"***Oh no! You couldn't maneuver the staircases on time and now you're late to class. Your excuse was lame and Professor McGonagall has deducted 5 house points from {eval(currUser.house).get_name()}.***"
            em = embedMessage(colour=discord.Colour.orange(), description=msg)
            await bot.create_embed(em, message)

            author = "Professor McGonagall"
            author_icon = "https://i.pinimg.com/564x/ba/b5/4f/bab54fac65ecc60ec383fd0d5a731b55.jpg"
            msg = "***Perhaps, it'd be more useful if I were to transfigure you into a pocket-watch. That way, at least one of you might be on time.***"
            em = embedMessage(colour=discord.Colour.green(), description=msg,image="https://i.pinimg.com/564x/5a/f9/b3/5af9b3ab462f2de8f55df8326a5d5d31.jpg", author=author, author_url=author_icon)
            await bot.create_embed(em, message)
            eval(currUser.house).add_points(-5)
            return True

    async def key(self, client, currUser, message):
        em = embedMessage(colour=discord.Colour.gold(
        ), description="***Would you like to buy a key for 50 Galleons to continue the game?***", image="https://i.pinimg.com/originals/cd/bd/36/cdbd362b1b01e785b9be089b8fb95fa7.gif")
        await client.create_embed(em, message)

        while True:
            response = await client.wait_for('message', check=lambda message1: client.check(message1, message))
            if response.channel.name == message.channel.name:
                if response.content == "exit":
                    em.description = "***Farewell for now, come back again soon!***"
                    await client.create_embed(em, message)
                    return False

                elif response.content.lower() == "yes":
                    if currUser.wealth < 50:
                        em.description = f"***Uh oh! You only have {currUser.wealth} Galleons in your Gringotts account. You lose.***"
                        await client.create_embed(em, message)
                        key = 0
                        break
                    else:
                        currUser.wealth -= 50
                        key = 1
                        em.description = "***Congrats! You have successfully purchased the key and are now free to continue the game.***"
                        await client.create_embed(em, message)
                        break
                elif response.content.lower() == "no":
                    key = 0
                    em.description = "***Good game, see you soon!***"
                    await client.create_embed(em, message)
                    break

                else:
                    em.description = "***Please answer with only yes or no.***"
                    await client.create_embed(em, message)
            else:
                em.description = "***A game is already in progress in another channel. Do you want to exit the game? (yes/anything else)***"
                await client.create_embed(em, message)

                response = await client.wait_for('message', check=lambda message1: client.check(message1, message))
                if response.content == "yes":
                    em.description = "***Farewell for now, come back again soon!***"
                    await client.create_embed(em, message)

        return key

    async def WordChain(self, client, currUser, message):
        words = terms + spells + characters + creatures
        done = []
        msg = "***Welcome to WordChain, a game where you put your vocabulary of the Wizarding World to the test!***\n ***Basically, you've to type a Harry Potter related word that starts with the ending letter of the last word. You and the Potterbot take turns. Be careful to not repeat any word.***"
        em = embedMessage(colour=discord.Colour.orange(), description=msg, image = "https://i.pinimg.com/564x/9a/fa/b1/9afab1f6432397855e25f7dfc05a4470.jpg", title = "Word Chain")
        await client.create_embed(em, message)

        msg = "***You get to start! Please type your word.***"
        em = embedMessage(colour=discord.Colour.orange(), description=msg)
        await client.create_embed(em, message)
        while True:
            response = await client.wait_for('message', check=lambda message1: client.check(message1, message))
            if response.content == "exit" and response.channel.name == "mini-games":
                msg = "***Farewell for now, come back again soon!***"
                em = embedMessage(colour=discord.Colour.orange(), description=msg)
                await client.create_embed(em, message)
                return False
            elif response.channel.name == "mini-games":
                if response.content.title() not in words:
                    msg = "***That word is not related to Harry Potter. You lose.***"
                    em = embedMessage(colour=discord.Colour.orange(), description=msg)
                    await client.create_embed(em, message)
                    key = await self.key(client, currUser, message)
                    if key == 0:
                        break

                elif len(done) > 0:
                    if response.content[0].lower() != myword[-1]:
                        msg = f"***Your word does not start with '{myword[-1].upper()}'. You've lost.***"
                        em = embedMessage(colour=discord.Colour.orange(), description=msg)
                        await client.create_embed(em, message)
                        key = await self.key(client, currUser, message)
                        if key == 0:
                            break

                if response.content.title() in done:
                    msg = "***Oops! That word is already done. You lose.***"
                    em = embedMessage(colour=discord.Colour.orange(), description=msg)
                    await client.create_embed(em, message)
                    key = await self.key(client, currUser, message)
                    if key == 0:
                        break

                else:
                    done.append(response.content.title())
                    valid = [x for x in words if x[0] ==
                             response.content[-1].upper() and x not in done]
                    myword = random.choices(valid)[0]
                    done.append(myword)
                    await response.channel.send(myword)
            else:
                msg = "***A game is already in progress. Do you want to exit Word Chain? (yes/anything else)***"
                em = embedMessage(colour=discord.Colour.orange(), description=msg)
                await client.create_embed(em, message)
                response = await client.wait_for('message', check=lambda message1: client.check(message1, message))
                if response.content == "yes":
                    msg = "***Farewell for now, come back again soon!***"
                    em = embedMessage(colour=discord.Colour.orange(), description=msg)
                    await client.create_embed(em, message)
                    return False
                continue
        msg = f"***You've earned {len(done)//2} galleons and {len(done) // 2} points for your house!***"
        em = embedMessage(colour=discord.Colour.orange(), description=msg)
        await client.create_embed(em, message)
        eval(currUser.house).add_points(len(done) // 2)
        currUser.wealth += len(done) // 2
        return True

    async def Trivia(self, client, currUser, message):
        msg = "***7 years of calling Hogwarts home and here you are...***\n ***Finally putting all your years of top level magical eductaion to the test!***\n***And not just any test - the most important one of 'em of all, the test that'll decide your future in the Wizarding World - the NEWTs!***\n***I hope you've done your revision! Good luck!***"
        em = embedMessage(colour=discord.Colour.orange(), description=msg, title = "Nastily Exhausting Wizarding Tests", image = "https://i.pinimg.com/564x/65/5f/eb/655feb6696b676e263fb8a6c5992e58e.jpg")
        await client.create_embed(em, message)
        ques_done = []
        s = 0
        while True:
            while True:
                ques, ans = random.choice(list(trivia.items()))
                if ques not in ques_done:
                    ques_done.append(ques)
                    break
                else:
                    continue
            await message.channel.send(ques)
            response = await client.wait_for('message', check=lambda message1: client.check(message1, message))
            if response.content == "exit" and response.channel.name == "newts":
                msg = "***Farewell for now, come back again soon!***"
                em = embedMessage(colour=discord.Colour.orange(), description=msg)
                await client.create_embed(em, message)
                return False
            elif response.channel.name == "newts":
                if response.content.title() in ans:
                    msg = "***You're correct!***"
                    em = embedMessage(colour=discord.Colour.orange(), description=msg)
                    await client.create_embed(em, message)
                    s += 1

                else:
                    msg = f"***That's not right. The correct answer is {ans[0]}.***"
                    em = embedMessage(colour=discord.Colour.orange(), description=msg)
                    await client.create_embed(em, message)
                    key = await self.key(client, currUser, message)
                    if key == 0:
                        break
            else:
                msg = "***A game is already in progress. Do you want to exit trivia? (yes/anything else)***"
                em = embedMessage(colour=discord.Colour.orange(), description=msg)
                await client.create_embed(em, message)
                response = await client.wait_for('message', check=lambda message1: client.check(message1, message))
                if response.content == "yes":
                    msg = "***Farewell for now, come back again soon***!"
                    em = embedMessage(colour=discord.Colour.orange(), description=msg)
                    await client.create_embed(em, message)
                    return False
                continue

        msg = f"***You were right {s} times!***\n***You've earned {s} points for your house!***"
        em = embedMessage(colour=discord.Colour.orange(), description=msg)
        await client.create_embed(em, message)
        eval(currUser.house).add_points(s)
        return True

    async def crossword(self, client, currUser, message):

        chosen_one = random.choice(list(cross.keys()))
        s = 0

        msg = "***🎲 Solve a crossword right from the pages of the Daily Prophet! 🧩***\n ***Get ready to exercise your brain cells and embark on an exciting journey through words and clues. Challenge yourself with our collection of mind-bending crossword puzzles designed to test your vocabulary, wit, and problem-solving skills.***\n***Whether you're a seasoned wordsmith or a casual puzzler, there's something here for everyone. So, grab a cup of coffee, sharpen your pencils, and let's dive into the world of crosswords!***\n***Are you up for the challenge? Let's play! 🚀***"
        em = embedMessage(colour=discord.Colour.dark_gray(), description=msg, title = "Crossword", image = "https://i.pinimg.com/564x/94/3e/b9/943eb9647decd2b38d3a4fb3ac81589f.jpg")
        await client.create_embed(em, message)

        msg = "***You can type your answers in any order, but the format must be 'question_number answer'. For example, if the answer to the first question is Harry Potter, type '1 HarryPotter'. ***\n ***For the crosswords that have both across and down on the same number, follow the following format: For example, if the answer for 1 across is HarryPotter, type '1a HarryPotter'. And '1d Hermione' if the answer for 1 down is Hermione.***\n***Please don't put a space between 2 words in your answer.The answers are not case sensitive.***\n ***Type 'I'm done' when you wish to end the game and reveal the answers.***"
        em = embedMessage(colour=discord.Colour.dark_gray(), description=msg)
        await client.create_embed(em, message)

        msg = "***Here's your crossword!***"
        em = embedMessage(colour=discord.Colour.dark_gray(), description=msg)
        await client.create_embed(em, message)
        await message.channel.send("", file=discord.File(chosen_one))
        user_answers = {}
        for i in cross[chosen_one]:
            user_answers[i] = ''

        while True:
            response = await client.wait_for('message', check=lambda message1: client.check(message1, message))
            if user_answers == cross[chosen_one]:
                msg = "***Congrats! You've successfully solved the crossword.***"
                em = embedMessage(colour=discord.Colour.dark_gray(), description=msg)
                await client.create_embed(em, message)

                msg = f"***You've earned {len(user_answers)} galleons and {len(user_answers)} points for your house!***"
                em = embedMessage(colour=discord.Colour.dark_gray(), description=msg)
                await client.create_embed(em, message)
                eval(currUser.house).add_points(len(user_answers))
                currUser.wealth += len(user_answers)*2
                return True
            elif response.channel.name == "mini-games":
                if response.content == "exit":
                    msg = "***Farewell for now, come back again soon!***"
                    em = embedMessage(colour=discord.Colour.dark_gray(), description=msg)
                    await client.create_embed(em, message)
                    return False

                elif response.content.lower() == "i'm done":
                    answers = ''
                    for i in cross[chosen_one]:
                        answers += f"{i} : {cross[chosen_one][i]}\n"
                    em = embedMessage(colour=discord.Colour.dark_gray(), description=answers)
                    await client.create_embed(em, message)
                    msg = f"***You've earned {s} points for your house!***"
                    em = embedMessage(colour=discord.Colour.dark_gray(), description=msg)
                    await client.create_embed(em, message)
                    eval(currUser.house).add_points(len(user_answers))
                    return True

                n = response.content.find(' ')

                try:
                    if response.content[n + 1:].title() == cross[chosen_one][response.content[0:n]]:
                        s+=1
                        msg = "***You're right, of course!***"
                        em = embedMessage(colour=discord.Colour.dark_gray(), description=msg)
                        await client.create_embed(em, message)
                        user_answers[response.content[0:n]
                                     ] = response.content[n + 1:].title()
                    else:
                        msg = "***That's not right. Try again.***"
                        em = embedMessage(colour=discord.Colour.dark_gray(), description=msg)
                        await client.create_embed(em, message)
                        user_answers[response.content[0:n]
                                     ] = response.content[n + 1:].title()

                except KeyError:
                    if (n == -1):
                        msg = f"***There is no {response.content}***"
                        em = embedMessage(colour=discord.Colour.dark_gray(), description=msg)
                        await client.create_embed(em, message)

                    elif (response.content[n - 1].isdigit()):
                        msg = f"***{response.content[0:n]} has both across and down. Please specify which one you're answering.***"
                        em = embedMessage(colour=discord.Colour.dark_gray(), description=msg)
                        await client.create_embed(em, message)

                    else:
                        msg = f"***There is no {response.content[0:n]}***"
                        em = embedMessage(colour=discord.Colour.dark_gray(), description=msg)
                        await client.create_embed(em, message)
            else:
                msg = "***A game is already in progress. Do you want to exit crossword? (yes/anything else)***"
                em = embedMessage(colour=discord.Colour.dark_gray(), description=msg)
                await client.create_embed(em, message)
                response = await client.wait_for('message', check=lambda message1: client.check(message1, message))
                if response.content == "yes":
                    msg = "***Farewell for now, come back again soon!***"
                    em = embedMessage(colour=discord.Colour.dark_gray(), description=msg)
                    await client.create_embed(em, message)
                    return False

    async def botDuel(self, bot, currUser, message):
        opponent = enemies[currUser.enemiesDefeated]
        msg = f"***You have entered the forbidden forest and your opponent is {opponent.name}***"
        em = embedMessage(colour=discord.Colour.blue(), description=msg,image="https://i.pinimg.com/564x/89/a3/14/89a314433a85e74bbce03ab3b31a7b8b.jpg")
        await bot.create_embed(em, message)
        while True:
            await message.channel.send(f"{currUser.name}'s health points: {currUser.health}")
            await message.channel.send(f'''{"|||||" + "|" * (0 if currUser.health < 0 else currUser.health) * 3} \n {currUser.name}'s spells: {",".join(currUser.spells)}\n ''')
            await message.channel.send(f"{opponent.name}'s health points: {opponent.health}")
            if opponent.name not in ["Basilisk", "Werewolf", "Acromantula"]:
                msg = f'''***{currUser.name}'s health points: {0 if currUser.health < 0 else currUser.health}***\n''' + (
                            "🟩" + "🟩" * (
                            (
                                0 if currUser.health < 0 else currUser.health) // 6)) + f'''\n***{currUser.name}'s spells: {",".join(currUser.spells)}***\n''' + "\n" + f"***{opponent.name}'s health points: {0 if opponent.health < 0 else opponent.health}***\n" + (
                              "🟩" + "🟩" * (
                              (
                                  0 if opponent.health < 0 else opponent.health) // 6)) + f'''***\n{opponent.name}'s spells: {",".join(spell.name for spell in opponent.spells)},protego\n***'''
                em = embedMessage(colour=discord.Colour.blue(), description=msg)
                await bot.create_embed(em, message)
            else:
                msg = f'''***{currUser.name}'s health points: {0 if currUser.health < 0 else currUser.health}***\n''' + (
                            "🟩" + "🟩" * (
                            (
                                0 if currUser.health < 0 else currUser.health) // 6)) + f'''\n***{currUser.name}'s spells: {",".join(currUser.spells)}***\n''' + "\n" + f"***{opponent.name}'s health points: {0 if opponent.health < 0 else opponent.health}***\n" + (
                              "🟩" + "🟩" * (
                              (
                                  0 if opponent.health < 0 else opponent.health) // 6)) + f'''***\n{opponent.name}'s damage: {opponent.damage}\n***'''
                em = embedMessage(colour=discord.Colour.blue(), description=msg)
                await bot.create_embed(em, message)
                msg = "***Type 'dodge' to dodge an attack.***"
                em = embedMessage(colour=discord.Colour.blue(), description=msg)
                await bot.create_embed(em, message)
            print(currUser.id)
            if currUser.health <= 0:
                msg = "***Oh no, you have been defeated! Better luck next time.***"
                em = embedMessage(colour=discord.Colour.red(), description=msg)
                await bot.create_embed(em, message)
                return False
            elif opponent.health <= 0:
                msg = f"***Merlin's beard! {opponent.name} has been defeated! You have won the duel!***"
                em = embedMessage(colour=discord.Colour.green(), description=msg)
                await bot.create_embed(em, message)
                currUser.enemiesDefeated += 1
                currUser.health = currUser.max_health
                currUser.points += 10
                currUser.level = currUser.points // 30
                eval(currUser.house).add_points(5)
                return True
            response1 = await bot.recieve(message, check=lambda message1: bot.check(message1, message))
            if response1.content == "exit":
                msg = "***Farewell for now, come back again soon!***"
                em = embedMessage(colour=discord.Colour.blue(), description=msg)
                await bot.create_embed(em, message)
                return None
            if response1.content in currUser.spells:
                spell = eval(f"{response1.content}")
                if random.random() < opponent.prob:
                    if opponent.name not in ["Basilisk", "Werewolf", "Acromantula"]:
                        msg = "***"+opponent.name + " has cast Protego and blocked the spell!***"
                        em = embedMessage(colour=discord.Colour.red(), description=msg,image="https://i.pinimg.com/originals/b7/b6/78/b7b678bdc295fb6dcaac5a5a630b9fa4.gif")
                        await bot.create_embed(em, message)
                    else:
                        msg = "***"+opponent.name + " has dodged the spell!***"
                        em = embedMessage(colour=discord.Colour.red(), description=msg)
                        await bot.create_embed(em, message)
                else:
                    msg = "***You have cast " + response1.content + " successfully!***"
                    em = embedMessage(colour=discord.Colour.green(), description=msg)
                    await bot.create_embed(em, message)
                    damage_amount = spell.damage
                    heal_amount = spell.heal
                    if damage_amount > 0:
                        opponent.health -= damage_amount
                        msg = "***" + opponent.name + " has taken " + str(damage_amount) + " damage!***"
                        em = embedMessage(colour=discord.Colour.green(), description=msg)
                        await bot.create_embed(em, message)
                    if heal_amount > 0:
                        msg = "***You have healed for " + str(heal_amount) + " health points!***"
                        em = embedMessage(colour=discord.Colour.green(), description=msg)
                        await bot.create_embed(em, message)
                        if currUser + heal_amount > currUser.max_health:
                            currUser.health = currUser.max_health
                        else:
                            currUser.health += heal_amount
                    if currUser.health <= 0:
                        msg = "***Oh no, you have been defeated! Better luck next time.***"
                        em = embedMessage(colour=discord.Colour.red(), description=msg)
                        await bot.create_embed(em, message)
                        return False
                    elif opponent.health <= 0:
                        msg = f"***Merlin's beard! {opponent.name} has been defeated! You have won the duel!***"
                        em = embedMessage(colour=discord.Colour.green(), description=msg)
                        await bot.create_embed(em, message)
                        currUser.enemiesDefeated += 1
                        currUser.health = currUser.max_health
                        currUser.points += 10
                        currUser.level = currUser.points // 30
                        eval(currUser.house).add_points(5)
                        return True
                if opponent.name not in ["Basilisk", "Werewolf", "Acromantula"]:
                    oppSpell = random.choice(opponent.spells)
                    if random.random() < opponent.prob:
                        msg = f"***{oppSpell.name}***"
                        em = embedMessage(colour=discord.Colour.red(), description=msg,author=opponent.name)
                        await bot.create_embed(em, message)
                        if oppSpell.heal == 0:
                            response1 = await bot.recieve(message, check=lambda message1: bot.check(message1, message), timeout=3.0)
                            if response1 != None:
                                if response1.content == "exit":
                                    msg = "***Farewell for now, come back again soon!***"
                                    em = embedMessage(colour=discord.Colour.blue(), description=msg)
                                    await bot.create_embed(em, message)
                                    return False
                                elif response1.content == "protego":
                                    msg = "***You have cast Protego and blocked the spell!***"
                                    em = embedMessage(colour=discord.Colour.green(), description=msg,image="https://i.pinimg.com/originals/b7/b6/78/b7b678bdc295fb6dcaac5a5a630b9fa4.gif")
                                    await bot.create_embed(em, message)
                                else:
                                    msg = f"***{opponent.name} has cast {oppSpell.name} successfully!***"
                                    em = embedMessage(colour=discord.Colour.red(), description=msg)
                                    await bot.create_embed(em, message)
                                    damage_amount = oppSpell.damage
                                    if damage_amount > 0:
                                        currUser.health -= damage_amount
                                        msg = f"***You have taken {damage_amount} damage!***"
                                        em = embedMessage(colour=discord.Colour.red(), description=msg)
                                        await bot.create_embed(em, message)

                            else:
                                msg = f"***{opponent.name} has cast {oppSpell.name} successfully!***"
                                em = embedMessage(colour=discord.Colour.red(), description=msg)
                                await bot.create_embed(em, message)
                                damage_amount = oppSpell.damage
                                if damage_amount > 0:
                                    currUser.health -= damage_amount
                                    msg = f"***You have taken {damage_amount} damage!***"
                                    em = embedMessage(colour=discord.Colour.red(), description=msg)
                                    await bot.create_embed(em, message)
                        else:
                            heal_amount = oppSpell.heal
                            msg = f"***{opponent.name} has cast {oppSpell.name} and healed for {heal_amount} health points!***"
                            em = embedMessage(colour=discord.Colour.green(), description=msg)
                            await bot.create_embed(em, message)
                            if opponent.health + heal_amount > opponent.max_health:
                                opponent.health = opponent.max_health
                            else:
                                opponent.health += heal_amount
                    else:
                        msg = f"***{opponent.name} has missed the spell!***"
                        em = embedMessage(colour=discord.Colour.blue(), description=msg)
                        await bot.create_embed(em, message)
                else:
                    if random.random() < opponent.prob:
                        msg = f"***{opponent.name} has launched an attack! Type 'dodge' to dodge the attack.***"
                        em = embedMessage(colour=discord.Colour.blue(), description=msg)
                        await bot.create_embed(em, message)
                        await response1.channel.send(opponent.name + " has launched an attack! Type 'dodge' to dodge the attack.")
                        response1 = await bot.recieve(message, check=lambda message1: bot.check(message1, message), timeout=3.0)
                        if response1 != None:
                            if response1.content == "exit":
                                msg = "***Farewell for now, come back again soon!***"
                                em = embedMessage(colour=discord.Colour.blue(), description=msg)
                                await bot.create_embed(em, message)
                                return False
                            if response1.content == "dodge":
                                msg = f"***You have successfully dodged the attack!***"
                                em = embedMessage(colour=discord.Colour.green(), description=msg)
                                await bot.create_embed(em, message)
                            else:
                                msg = f"***{opponent.name}'s attack hit successfully.\nDamage taken = {opponent.damage}***"
                                em = embedMessage(colour=discord.Colour.red(), description=msg)
                                await bot.create_embed(em, message)
                                currUser.health -= opponent.damage
                        else:
                            msg = f"***{opponent.name}'s attack hit successfully.\nDamage taken = {opponent.damage}***"
                            em = embedMessage(colour=discord.Colour.red(), description=msg)
                            await bot.create_embed(em, message)
                            currUser.health -= opponent.damage
                    else:
                        msg = f"***{opponent.name} has missed the attack!***"
                        em = embedMessage(colour=discord.Colour.blue(), description=msg)
                        await bot.create_embed(em, message)

    async def emojis(self, client, currUser, message):
        msg = "***You and your friends snuck out of bed for a midnight stroll around the castle, but came face to face with Peeves!He's now threatening to sell you out to Filch unless you agree to play a game of charades with him. Cuz poltergeists get bored too, you know!***\n***You have no choice but to agree. Anything to escape the wrath of Filch, am I right?***"
        em = embedMessage(colour=discord.Colour.blue(), description=msg, title = ":european_castle: :sparkles: ", image = "https://i.pinimg.com/564x/6a/93/a0/6a93a031e258b391a02bd5e923bb4d64.jpg")
        await client.create_embed(em, message)

        msg = "***Here are the rules:***\n*** Peeves acts out a character and you've to guess who he's mimicking. (Basically, the good old game of guessing the character from the emojis).***\n*** You'll have 7 questions in total. Type 'play' to start playing.***"
        em = embedMessage(colour=discord.Colour.blue(), description=msg, image = "https://i.pinimg.com/564x/f8/f1/47/f8f14754704bd7f89edf32458a376314.jpg")
        await client.create_embed(em, message)

        while True:
            response = await client.wait_for('message', check=lambda message1: client.check(message1, message))
            if response.content == "exit" and response.channel.name == "mini-games":
                msg = "***Farewell for now, come back again soon!***"
                em = embedMessage(colour=discord.Colour.blue(), description=msg)
                await client.create_embed(em, message)
                return False
            elif response.channel.name == "mini-games":
                if response.content == 'play':
                    break
                else:
                    msg = "***I'm sorry, I didn't catch that. Please try again.***"
                    em = embedMessage(colour=discord.Colour.blue(), description=msg)
                    await client.create_embed(em, message)
            else:
                msg = "***A game is already in progress. Do you want to exit Word Chain? (yes/anything else)***"
                em = embedMessage(colour=discord.Colour.blue(), description=msg)
                await client.create_embed(em, message)
                response = await client.wait_for('message', check=lambda message1: client.check(message1, message))
                if response.content == "yes":
                    msg = "***Farewell for now, come back again soon!***"
                    em = embedMessage(colour=discord.Colour.blue(), description=msg)
                    await client.create_embed(em, message)
                    return False

        s = 0
        L = []
        for i in range(7):
            emoji, ans = random.choice(list(d.items()))
            while True:
                if emoji not in L:
                    L.append(emoji)
                    break
                else:
                    emoji, ans = random.choice(list(d.items()))

            await message.channel.send(emoji)
            response = await client.wait_for('message', check=lambda message1: client.check(message1, message))
            if response.content == "exit":
                msg = "***Farewell for now, come back again soon!***"
                em = embedMessage(colour=discord.Colour.blue(), description=msg)
                await client.create_embed(em, message)
                return False
            elif response.channel.name == "mini-games":
                if response.content.title() in ans:
                    msg = "***You're correct!***"
                    em = embedMessage(colour=discord.Colour.blue(), description=msg)
                    await client.create_embed(em, message)
                    s += 1

                else:
                    if len(ans) == 1:
                        msg = f"***That's not right. The correct answer is {ans[0]}***"
                        em = embedMessage(colour=discord.Colour.blue(), description=msg)
                        await client.create_embed(em, message)
                    else:
                        msg = f"***That's not right. The correct answer is {ans[1]}***"
                        em = embedMessage(colour=discord.Colour.blue(), description=msg)
                        await client.create_embed(em, message)
            else:
                msg = "***A game is already in progress. Do you want to exit Word Chain? (yes/anything else)***"
                em = embedMessage(colour=discord.Colour.blue(), description=msg)
                await client.create_embed(em, message)
                response = await client.wait_for('message', check=lambda message1: client.check(message1, message))
                if response.content == "yes":
                    msg = "***Farewell for now, come back again soon!***"
                    em = embedMessage(colour=discord.Colour.blue(), description=msg)
                    await client.create_embed(em, message)
                    return False

        msg = f"***You were right {s}/7 times!***\n***Peeves is now headed to annoy Mrs Norris and you're free to roam the corridors again! Now that you think about it, hanging out with Peeves was actually fun and turned out to be the highlight of your night!***"
        em = embedMessage(colour=discord.Colour.blue(), description=msg, image = "https://i.pinimg.com/564x/14/fb/69/14fb692c99f2c068eafd625a39eb081a.jpg")
        await client.create_embed(em, message)
        msg = f"***You've earned {s*2} galleons and {s} points for your house!***"
        em = embedMessage(colour=discord.Colour.blue(), description=msg)
        await client.create_embed(em, message)
        currUser.wealth += s*2
        eval(currUser.house).add_points(s)
        return s
