import io
import random

import numpy as np
from PIL import Image, ImageDraw
from discord.ext import commands


class Dungeons(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['подземелье'])
    async def dungeon(self, ctx):
        # await ctx.send("Начинаем сбор для посещения Deep Dark Dungeon")
        members = list(ctx.guild.members)
        online_members = []
        for member in members:
            print(member.status)
            if str(member.status) != 'offline' and not member.bot:
                online_members.append(member)
        print(online_members)
        while len(online_members) > 4:
            del online_members[random.randint(0, len(online_members) - 1)]
        online_mentions = ''
        for member in online_members:
            online_mentions = online_mentions + ' ' + member.mention
        # await ctx.send(f"В данжен пойдут {online_mentions}" )
        avatars = []
        size = (80, 80)
        mask = Image.new('L', size)
        ImageDraw.Draw(mask).ellipse((0, 0, 80, 80), fill=255)
        for member in online_members:
            byte_avatar = io.BytesIO(await member.avatar_url_as(format="png").read())
            avatar = Image.open(byte_avatar)
            avatar = avatar.resize(size)
            avatar.putalpha(mask)
            avatar.show()
            avatars.append(np.asarray(avatar))
        img_dungeon = Image.open('img/dungeon.jpeg')
        # for i in avatars:
        #    if i = 0:


def setup(bot):
    bot.add_cog(Dungeons(bot))
    print('Dungeons being loaded!')
