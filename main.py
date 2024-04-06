import discord
from utilities import *


class bot(discord.Client):
    def __init__(self, dataHandle: dataHandler, intents=discord.Intents.all(), **options):
        super().__init__(intents=intents, ** options)
        self.userDataHandler = dataHandle('user_data.json')
        self.houseDataHandler = dataHandle('house_data.json')
        self.games = games()
        self.categ = None
        self.userDataHandler.read(readAmajeDataUser)
        self.houseDataHandler.read(readAmajeDataHouse)
        self.notFree = []

    def check(self, m1, m2):
        '''
        Checks if author of message 1 is the same as message 2.
        '''
        return m1.author == m2.author

    def save(self, currUser: user):
        '''
        This saves the user.
        '''
        user.users[user.names.index(currUser.name)] = currUser
        self.userDataHandler.dump(
            data=user.users, func=getDumpUser, key='users')
        self.houseDataHandler.dump(
            data=[Slytherin, Gryffindor, Ravenclaw, Hufflepuff], func=getDumpHouse, key='house')

    def getUser(self, message: discord.Message):
        '''
        Gets the user object of the message author.
        '''
        try:
            return user.ids[message.author.id]
        except:
            print(f"{user.users}")
            return None

    async def send(self, message: discord.Message, content: str):
        '''
        Sends a message to the channel of the message.
        '''
        await message.channel.send(content)

    async def send_embed(self, message: discord.Message):
        pass

    async def recieve(self, message: discord.Message, check=None, timeout=None):
        '''
        Recieves a message from the channel of the message.
        '''
        try:
            return await self.wait_for('message', check=check, timeout=timeout)
        except:
            return None

    async def on_ready(self):
        """
        Does the following whenever bot starts up.
        """
        print(f'Logged in as {self.user}')
        print(self.user.id)

        self.guild = self.get_guild(1217366468908290118)

        y = False
        for x in self.guild.categories:
            if x.name == 'PotterBot':
                y = True

        if not y:
            await self.on_guild_join(self.guild)

    async def on_guild_join(self, guild: discord.Guild):
        categ = await guild.create_category('PotterBot')
        await guild.create_voice_channel("chill", category=categ)
        await guild.create_text_channel('potterbot-general', category=categ)
        await guild.create_text_channel('potterbot-newts', category=categ)
        await guild.create_text_channel('potterbot-dueling-club', category=categ)
        await guild.create_text_channel('potterbot-forbidden-forest', category=categ)
        await guild.create_text_channel('potterbot-mini-games', category=categ)
