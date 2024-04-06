from discord import Embed


class embedMessage(Embed):
    '''
    A class that inherits from discord.Embed to create a custom embed message.

    Attributes
    -----------

    title: Optional[:class:`str`]
        The title of the embed.
        This can be set during initialisation.
        Can only be up to 256 characters.

    type: :class:`str`
        The type of embed. Usually "rich".
        This can be set during initialisation.
        Possible strings for embed types can be found on discord's
        :ddocs:`api docs <resources/channel#embed-object-embed-types>`

    description: Optional[:class:`str`]
        The description of the embed.
        This can be set during initialisation.
        Can only be up to 4096 characters.

    url: Optional[:class:`str`]
        The URL of the embed.
        This can be set during initialisation.

    timestamp: Optional[:class:`datetime.datetime`]
        The timestamp of the embed content. This is an aware datetime.
        If a naive datetime is passed, it is converted to an aware
        datetime with the local timezone.

    colour: Optional[Union[:class:`Colour`, :class:`int`]]
        The colour code of the embed. Aliased to ``color`` as well.
        This can be set during initialisation.

    image: Optional[:class:`str`]
    '''

    def __init__(
        self,
        *,
        colour=None,
        color=None,
        title=None,
        type='rich',
        url=None,
        description=None,
        timestamp=None,
        footer=None,
        footer_url=None,
        image=None,
        thumbnail=None,
        author=None,
        author_url=None,
        fields=None,
        inline=True,
        view=None
    ):
        super().__init__(colour=colour, color=color, title=title, type=type,
                         url=url, description=description, timestamp=timestamp)

        if (image):
            self.set_image(url=image)

        if (thumbnail):
            self.set_thumbnail(url=thumbnail)

        if (fields):
            for field in fields:
                self.add_field(name=field['name'],
                               value=field['value'], inline=inline)

        if (footer):
            self.set_footer(text=footer, icon_url=footer_url)

        if (author):
            self.set_author(name=author, icon_url=author_url)

    async def send(self, message):
        '''
        A method that sends the embed message to the channel of the message.
        '''
        await message.channel.send(embed=self)
