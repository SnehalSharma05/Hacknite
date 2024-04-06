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
        await bot.send(message, "Greetings! Welcome to the whimsical world of PotterBot, where the whispers of ancient spells and the flicker of wands weave tales of wonder reminiscent of Dumbledore's office. Here, amid the hallowed halls of Hogwarts, where portraits come to life and enchanted creatures roam, embark on a journey beyond the pages of the Marauder's Map, where mischief and magic await your command!")
        msg = "If you wish to leave at any point in the game, just type 'exit'."
        em = embedMessage(colour=discord.Colour.blue(), description=msg)
        await bot.send(message, "If you wish to leave at any point in the game, just type 'exit'.")
        await bot.create_embed(em, message)

        if message.author.id in user.ids:
            em = embedMessage(colour = discord.Colour.blue())
            msg = "Welcome back to Hogwarts, " + user.ids[message.author.id].name + "!"
            await bot.create_embed(em, msg)
            return user.ids[message.author.id]

        currUser = await self.new_user(bot, message)

        return currUser

    async def new_user(self, bot, message):
        '''
        Function to initiate a new user.
        '''
        await bot.send(message, "Welcome, new user! Please choose your username.")
        while True:
            response = await bot.recieve(message, check=lambda message1: bot.check(message1, message))
            if response.content == "exit" and response.channel.name == "general":
                await bot.send(response, "Farewell for now, come back again soon!")
                return None
            elif response.channel.name == "general":
                if response.content in user.names:
                    await bot.send(response, "I'm sorry, that username is already taken. Please try again.")
                    return await bot.new_user(message)

                u = user(response.content, response.author.id)
                await bot.send(response, "Welcome to Hogwarts, " + response.content + "!")

                return u
            else:
                await bot.send(response, "A game is already in progress in the channel 'general'. Do you want to exit the game? (yes/anything else)")
                response = await bot.recieve(message, check=lambda message1: bot.check(message1, message))
                if response.content == "yes":
                    await bot.send(response, "Farewell for now, come back again soon!")
                    return None
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
            if response.content == "exit" and response.channel.name == "general":
                await bot.send(response, "Farewell for now, come back again soon!")
                return False
            elif response.channel.name == "general":
                if response.content == "a":
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
            else:
                await bot.send(response, "A game is already in progress in the channel 'general'. Do you want to exit the game? (yes/anything else)")
                response = await bot.recieve(message, check=lambda message1: bot.check(message1, message))
                if response.content == "yes":
                    await bot.send(response, "Farewell for now, come back again soon!")
                    return False
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
            if response.content == "exit" and response.channel.name == "general":
                await bot.send(response, "Farewell for now, come back again soon!")
                return False
            elif response.channel.name == "general":
                if response.content == "wand":
                    break
                else:
                    await bot.send(response, "I'm sorry, I didn't catch that. Please try again.")
            else:
                await bot.send(response, "A game is already in progress in the channel 'general'. Do you want to exit the game? (yes/anything else)")
                response = await bot.recieve(message, check=lambda message1: bot.check(message1, message))
                if response.content == "yes":
                    await bot.send(response, "Farewell for now, come back again soon!")
                    return False

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
            response = await bot.recieve(message)
            if response.author.id == int(opponent_id) and response.channel.name == "dueling-club" and response.content == "yes":
                accepted = True
                bot.notFreeUser.append(int(opponent_id))
                opponent = bot.getUser(response)
                break
            elif response.author.id == int(opponent_id) and response.channel.name == "dueling-club" and response.content == "no":
                await message.channel.send("The duel has been declined.")
                return None
            elif response.channel.name == "dueling-club":
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
            if response1.content == "exit" and response1.channel.name == "dueling-club":
                await response1.channel.send("Farewell for now, come back again soon!")
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
                else:
                    await response1.channel.send("You do not have that spell.")
            else:
                await response1.channel.send("A game is already in progress in the channel 'dueling-club'. Do you want to exit the duel? (yes/anything else)")
                response1 = await bot.recieve(message, check=lambda message1: bot.check(message1, message))
                if response1.content == "yes":
                    await response1.channel.send("Farewell for now, come back again soon!")
                    break
        currUser.health = currUser.max_health
        opponent.health = opponent.max_health
        opponent.update_level()
        bot.notFreeUser.remove(int(opponent.id))
        bot.save(opponent)
    async def staircase(self, client, currUser, message):
        total_stairs = 20
        moves_left = total_stairs//2
        stairs_left = total_stairs
        cap_steps = total_stairs//3

        await message.channel.send(f"You're running late to class and you've just stepped onto the moving staircases. You now get {moves_left} moves to climb up {total_stairs} stairs to make it to your Transfiguration lesson on time. \nHere's what you have to do: \nType in the number of stairs you wanna climb at a time and then play a game of 7 up 7 down to see if you were successful. Mind your step! You don't wanna step onto a trick stair which will cause you to get stuck on that stair for the next move.\nConsecuently that move will be skipped (total moves reduces by 2)")
        await message.channel.send(f"Max steps that can be crossed per move is {cap_steps}. All the best!")
        await message.channel.send("If you don't know how 7 Up 7 Down works, enter '7' to learn now. Otherwise, type 'play' to start the game.")

        while True:
            response = await client.wait_for('message', check=lambda message1: client.check(message, message1))
            if response.channel.name == "general":
                if response.content == "exit":
                    await response.channel.send("Farewell for now, come back again soon!")
                    return False

                elif response.content == "play":
                    break

                elif response.content == "7":
                    await message.channel.send("The random number generator generates a number between 1 to 12. You have to guess if the number is >=7 or <7 (Enter a number >=7 or <7 to guess respectively). If your guess is correct, you move up your chosen number of steps; but if your guess is wrong, you fall down the chosen number of steps.")
                    await message.channel.send("Now that the rules are , type 'play' to proceed to the game.")
                    break

                else:
                    await response.channel.send("I'm sorry, I didn't catch that. Please try again.")
            else:
                await response.channel.send("A game is already in progress in the channel 'general'. Do you want to exit the game? (yes/anything else)")
                response = await client.wait_for('message', check=lambda message1: client.check(message1, message))
                if response.content == "yes":
                    await response.channel.send("Farewell for now, come back again soon!")
                    return False

        trick = False

        while moves_left > 0 and stairs_left > 0:
            trick = random.choice([True, False, False, False, False, False])

            while True:
                await message.channel.send("How many steps do you wanna take at a time?")
                response = await client.wait_for('message', check=lambda message1: client.check(message1, message))
                n = response.content
                if n.isdigit() and int(n) > 0 and int(n) <= cap_steps:
                    break
                else:
                    await message.channel.send(f"Please enter a valid number from 1-{cap_steps}.")

            while True:
                await message.channel.send("Let's see if the odds are in your favour! Pick a number between 1 to 12 (both included).")
                response = await client.wait_for('message', check=lambda message1: client.check(message1, message))
                guess = response.content

                if response.content == "exit":
                    await response.channel.send("Farewell for now, come back again soon!")
                    return False

                elif guess.isdigit():
                    if int(guess) >= 1 and int(guess) <= 12:
                        break
                    else:
                        await message.channel.send("Please enter a valid guess from 1-12.")

                else:
                    await message.channel.send("Please enter a valid guess.")

            random_no = random.randint(1, 12)

            if trick == True:
                increment_steps = random.randint(1, int(n))
                await message.channel.send(f"Oh no! You stepped on a trick step on the {increment_steps} step.")
                stairs_left = min(stairs_left + increment_steps, total_stairs)
                moves_left -= 1

            if not trick and ((random_no >= 7 and int(guess) >= 7) or (random_no < 7 and int(guess) < 7)):
                await message.channel.send(f"Congrats! You have climbed {n} steps.")
                stairs_left = max(0, stairs_left - int(n))

            elif not trick:
                await message.channel.send(f"Alas! You have fallen down {n} steps. Better luck next time.")
                stairs_left = min(stairs_left + int(n), total_stairs)

            moves_left -= 1
            await message.channel.send(f"You now have to climb {stairs_left} stairs in {moves_left} moves.")

            if (moves_left*cap_steps < stairs_left):
                await message.channel.send(f"Oh no, you don't have enough moves!")
                break

        if stairs_left == 0:
            await message.channel.send(f"Phew! You've managed to maneuver the magical staircases to reach class on time. Now Professor McGonagall won't transfigure you into a pocket watch!")
            return True

        else:
            await message.channel.send(f"L! You couldn't maneuver the staircases on time and now you're late to class. Your excuse was lame and Professor McGonagall has deducted 5 house points from {currUser.house.get_name()}.")
            currUser.house.add_points(-5)
            return True

    async def key(self, client, currUser, message):
        await message.channel.send("Would you like to buy a key for 50 Galleons to continue the game?")
        while True:
            response = await client.wait_for('message', check=lambda message1: client.check(message1, message))
            if response.channel.name == message.channel.name:
                if response.content == "exit":
                    await response.channel.send("Farewell for now, come back again soon!")
                    return False

                elif response.content.lower() == "yes":
                    if currUser.wealth < 50:
                        await response.channel.send(
                            f"Uh oh! You only have {currUser.wealth} Galleons in your Gringotts account. You lose.")
                        key = 0
                        break
                    else:
                        currUser.wealth -= 50
                        key = 1
                        await response.channel.send(
                            "Congrats! You have successfully purchased the key and are now free to continue the game.")
                        break
                elif response.content.lower() == "no":
                    key = 0
                    await response.channel.send("Good game, see you soon!")
                    break

                else:
                    await response.channel.send("Please answer with only yes or no.")
            else:
                await response.channel.send("A game is already in progress in another channel. Do you want to exit the game? (yes/anything else)")
                response = await client.wait_for('message', check=lambda message1: client.check(message1, message))
                if response.content == "yes":
                    await response.channel.send("Farewell for now, come back again soon!")

        return key

    async def WordChain(self, client, currUser, message):
        words = terms + spells + characters + creatures
        done = []
        await message.channel.send("Welcome to WordChain, a game where you put your vocabulary of the Wizarding World to the test!")
        await message.channel.send("Basically, you've to type a Harry Potter related word that starts with the ending letter of the last word. You and the Potterbot take turns. Be careful to not repeat any word.")
        await message.channel.send("You get to start! Please type your word.")
        while True:
            response = await client.wait_for('message', check=lambda message1: client.check(message1, message))
            if response.content == "exit" and response.channel.name == "mini-games":
                await response.channel.send("Farewell for now, come back again soon!")
                return False
            elif response.channel.name == "mini-games":
                if response.content.title() not in words:
                    await response.channel.send("That word is not related to Harry Potter. You lose.")
                    key = await self.key(client, currUser, message)
                    if key == 0:
                        break

                elif response.content.title() in done:
                    await response.channel.send("Oops! That word is already done. You lose.")
                    key = await self.key(client, currUser, message)
                    if key == 0:
                        break

                elif len(done) > 0:
                    if response.content[0].lower() != myword[-1]:
                        await response.channel.send(
                            f"Your word does not start with '{myword[-1].upper()}'. You've lost.")
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
                await response.channel.send("A game is already in progress. Do you want to exit Word Chain? (yes/anything else)")
                response = await client.wait_for('message', check=lambda message1: client.check(message1, message))
                if response.content == "yes":
                    await response.channel.send("Farewell for now, come back again soon!")
                    return False
                continue
        await message.channel.send(f"You've earned {len(done)//2} galleons and {len(done) // 2} points for your house!")
        currUser.house.points += len(done) // 2
        currUser.wealth += len(done) // 2
        return True

    async def Trivia(self, client, currUser, message):
        await message.channel.send("7 years of calling Hogwarts home and here you are...\n Finally putting all your years of top level magical eductaion to the test!")
        await message.channel.send("And not just any test - the most important one of 'em of all, the test that'll decide your future in the Wizarding World - the NEWTs!")
        await message.channel.send("I hope you've done your revision! Good luck!")
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
                await response.channel.send("Farewell for now, come back again soon!")
                return False
            elif response.channel.name == "newts":
                if response.content.title() in ans:
                    await response.channel.send("You're correct!")
                    s += 1

                else:
                    await response.channel.send(f"That's not right. The correct answer is {ans[0]}.")
                    key = await self.key(client, currUser, message)
                    if key == 0:
                        break
            else:
                await response.channel.send("A game is already in progress. Do you want to exit trivia? (yes/anything else)")
                response = await client.wait_for('message', check=lambda message1: client.check(message1, message))
                if response.content == "yes":
                    await response.channel.send("Farewell for now, come back again soon!")
                    return False
                continue

        await response.channel.send(f"You were right {s} times!")
        await message.channel.send(f"You've earned {s} points for your house!")
        currUser.house.points += s
        return True

    async def crossword(self, client, currUser, message):

        chosen_one = random.choice(list(cross.keys()))
        await message.channel.send("Here's your crossword!\n Please don't put a space between 2 words in your answer.",
                                   file=discord.File(chosen_one))
        await message.channel.send(
            "You can type your answers in any order, but the format must be 'question_number answer'. For example, if the answer to the first question is Harry Potter, type '1 HarryPotter'. The answers are not case sensitive.")
        await message.channel.send(
            "For the crosswords that have both across and down on the same number, follow the following format: For example, if the answer for 1 across is HarryPotter, type '1a HarryPotter'. And '1d Hermione' if the answer for 1 down is Hermione.")
        await message.channel.send("Type 'I'm done' when you wish to end the game and reveal the answers.")

        user_answers = {}
        for i in cross[chosen_one]:
            user_answers[i] = ''

        while True:
            response = await client.wait_for('message', check=lambda message1: client.check(message1, message))
            if user_answers == cross[chosen_one]:
                await message.channel.send("Congrats! You've successfully solved the crossword.")
                await message.channel.send(f"You've earned {len(user_answers)} galleons and {user_answers} points for your house!")
                currUser.house.add_points(len(user_answers))
                currUser.wealth+=len(user_answers)*2
                return True
            elif response.channel.name == "mini-games":
                if response.content == "exit":
                    await response.channel.send("Farewell for now, come back again soon!")
                    return False

                elif response.content.lower() == "i'm done":
                    for i in cross[chosen_one]:
                        await response.channel.send(f"{i} : {cross[chosen_one][i]}")
                    await message.channel.send(f"You've earned {user_answers} points for your house!")
                    currUser.house.add_points(len(user_answers))
                    return True

                n = response.content.find(' ')

                try:
                    if response.content[n + 1:].title() == cross[chosen_one][response.content[0:n]]:
                        await response.channel.send("You're right, of course!")
                        user_answers[response.content[0:n]
                        ] = response.content[n + 1:].title()
                    else:
                        await response.channel.send(f"That's not right. Try again.")
                        user_answers[response.content[0:n]
                        ] = response.content[n + 1:].title()

                except KeyError:
                    if (n == -1):
                        await response.channel.send(f"There is no {response.content}")

                    elif (response.content[n - 1].isdigit()):
                        await response.channel.send(
                            f"{response.content[0:n]} has both across and down. Please specify which one you're answering.")

                    else:
                        await response.channel.send(f"There is no {response.content[0:n]}")
            else:
                await response.channel.send("A game is already in progress. Do you want to exit crossword? (yes/anything else)")
                response = await client.wait_for('message', check=lambda message1: client.check(message1, message))
                if response.content == "yes":
                    await response.channel.send("Farewell for now, come back again soon!")
                    return False
    async def botDuel(self, bot, currUser, message):
        opponent = enemies[currUser.enemiesDefeated]
        await message.channel.send(f'''Your opponent is {opponent.name}''')
        while True:
            await message.channel.send(f"{currUser.name}'s health points: {currUser.health}")
            await message.channel.send(f'''{"|||||" + "|" * (0 if currUser.health < 0 else currUser.health) * 3} \n {currUser.name}'s spells: {",".join(currUser.spells)}\n ''')
            await message.channel.send(f"{opponent.name}'s health points: {opponent.health}")
            if opponent.name not in ["Basilisk", "Werewolf", "Acromantula"]:
                await message.channel.send(f'''{"|||||" + "|" * (0 if opponent.health < 0 else opponent.health) * 3} \n {opponent.name}'s spells: protego,{",".join(spell.name for spell in opponent.spells)}\n ''')
            else:
                await message.channel.send(f'''{"|||||" + "|" * (0 if opponent.health < 0 else opponent.health) * 3} \n {opponent.name}'s damage: {opponent.damage}\n ''')
                await message.channel.send(f"Type 'dodge' to dodge an attack.")
            print(currUser.id)
            if currUser.health <= 0:
                await message.channel.send(f"Oh no, you have been defeated! Better luck next time.")
                return False
            elif opponent.health <= 0:
                await message.channel.send(f"Merlin's beard! {opponent.name} has been defeated! You have won the duel!")
                currUser.enemiesDefeated += 1
                currUser.health = currUser.max_health
                currUser.points += 10
                currUser.level = currUser.points // 30
                currUser.house.points+=5
                return True
            response1 = await bot.recieve(message, check=lambda message1: bot.check(message1, message))
            if response1.content == "exit":
                await response1.channel.send("Farewell for now, come back again soon!")
                return None
            if response1.content in currUser.spells:
                spell = eval(f"{response1.content}")
                if random.random() < opponent.prob:
                    if opponent.name not in ["Basilisk", "Werewolf", "Acromantula"]:
                        await response1.channel.send(opponent.name + " has cast Protego and blocked the spell!")
                    else:
                        await response1.channel.send(opponent.name + " has dodged the spell!")
                else:
                    await response1.channel.send("You have cast " + response1.content + " successfully!")
                    damage_amount = spell.damage
                    heal_amount = spell.heal
                    if damage_amount > 0:
                        opponent.health -= damage_amount
                        await response1.channel.send(opponent.name + " has taken " + str(damage_amount) + " damage!")
                    if heal_amount > 0:
                        await response1.channel.send("You have healed for " + str(heal_amount) + " health points!")
                        if currUser + heal_amount > currUser.max_health:
                            currUser.health = currUser.max_health
                        else:
                            currUser.health += heal_amount
                    if currUser.health <= 0:
                        await message.channel.send(f"Oh no, you have been defeated! Better luck next time.")
                        return False
                    elif opponent.health <= 0:
                        await message.channel.send(f"Merlin's beard! {opponent.name} has been defeated! You have won the duel!")
                        currUser.enemiesDefeated += 1
                        currUser.health = currUser.max_health
                        currUser.points += 10
                        currUser.level = currUser.points // 30
                        currUser.house.points+=5
                        return True
                if opponent.name not in ["Basilisk", "Werewolf", "Acromantula"]:
                    oppSpell = random.choice(opponent.spells)
                    if random.random() < opponent.prob:
                        await response1.channel.send(opponent.name + " : " + oppSpell.name)
                        if oppSpell.heal == 0:
                            response1 = await bot.recieve(message, check=lambda message1: bot.check(message1, message), timeout=3.0)
                            if response1 != None:
                                if response1.content == "exit":
                                    await response1.channel.send("Farewell for now, come back again soon!")
                                    return False
                                elif response1.content == "protego":
                                    await response1.channel.send("You have cast Protego and blocked the spell!")
                                else:
                                    await response1.channel.send(opponent.name + " has cast " + oppSpell.name + " successfully!")
                                    damage_amount = oppSpell.damage
                                    if damage_amount > 0:
                                        currUser.health -= damage_amount
                                        await response1.channel.send("You have taken " + str(damage_amount) + " damage!")

                            else:
                                await message.channel.send(opponent.name + " has cast " + oppSpell.name + " successfully!")
                                damage_amount = oppSpell.damage
                                if damage_amount > 0:
                                    currUser.health -= damage_amount
                                    await message.channel.send("You have taken " + str(damage_amount) + " damage!")
                        else:
                            heal_amount = oppSpell.heal
                            await response1.channel.send(opponent.name + " has healed for " + str(heal_amount) + " health points!")
                            if opponent.health + heal_amount > opponent.max_health:
                                opponent.health = opponent.max_health
                            else:
                                opponent.health += heal_amount
                    else:
                        await response1.channel.send(opponent.name + " has missed the spell!")
                else:
                    if random.random() < opponent.prob:
                        await response1.channel.send(opponent.name + " has launched an attack! Type 'dodge' to dodge the attack.")
                        response1 = await bot.recieve(message, check=lambda message1: bot.check(message1, message), timeout=3.0)
                        if response1 != None:
                            if response1.content == "exit":
                                await response1.channel.send("Farewell for now, come back again soon!")
                                return False
                            if response1.content == "dodge":
                                await response1.channel.send("You have successfully dodged the attack!")
                            else:
                                await response1.channel.send(opponent.name + "'s attack hit successfully.")
                                currUser.health -= opponent.damage
                        else:
                            await message.channel.send(opponent.name + "'s attack hit successfully.")
                            currUser.health -= opponent.damage
                    else:
                        await response1.channel.send(opponent.name + "'s attack missed.")

    async def emojis(self, client, currUser, message):
        await message.channel.send("You and your friends snuck out of bed for a midnight stroll around the castle, but came face to face with Peeves!")
        await message.channel.send("He's now threatening to sell you out to Filch unless you agree to play a game of charades with him. Cuz poltergeists get bored too, you know!")
        await message.channel.send("You have no choice but to agree. Anything to escape the wrath of Filch, am I right? ")
        await message.channel.send("Here are the rules: Peeves acts out a character and you've to guess who he's mimicking. (Basically, the good old game of guessing the character from the emojis). You'll have 7 questions in total. Type 'play' to start playing.")
        while True:
            response = await client.wait_for('message', check=lambda message1: client.check(message1, message))
            if response.content == "exit" and response.channel.name == "mini-games":
                await response.channel.send("Farewell for now, come back again soon!")
                return False
            elif response.channel.name == "mini-games":
                if response.content == 'play':
                    break
                else:
                    await response.channel.send("I'm sorry, I didn't catch that. Please try again.")
            else:
                await response.channel.send("A game is already in progress. Do you want to exit Word Chain? (yes/anything else)")
                response = await client.wait_for('message', check=lambda message1: client.check(message1, message))
                if response.content == "yes":
                    await response.channel.send("Farewell for now, come back again soon!")
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
                await response.channel.send("Farewell for now, come back again soon!")
                return False
            elif response.channel.name == "mini-games":
                if response.content.title() in ans:
                    await response.channel.send("You're correct!")
                    s += 1

                else:
                    if len(ans) == 1:
                        await response.channel.send(f"That's not right. The correct answer is {ans[0]}")
                    else:
                        await response.channel.send(f"That's not right. The correct answer is {ans[1]}")
            else:
                await response.channel.send("A game is already in progress. Do you want to exit Word Chain? (yes/anything else)")
                response = await client.wait_for('message', check=lambda message1: client.check(message1, message))
                if response.content == "yes":
                    await response.channel.send("Farewell for now, come back again soon!")
                    return False

        await response.channel.send(f"You were right {s}/7 times!")
        await response.channel.send("Peeves is now headed to annoy Mrs Norris and you're free to roam the corridors again! Now that you think about it, hanging out with Peeves was actually fun and turned out to be the highliight of your night!")
        await message.channel.send(f"You've earned {s*2} galleons and {s} points for your house!")
        currUser.wealth+=s*2
        currUser.house.points += s
        return s