import discord
from discord.ext import commands
import random
import PIL
from PIL import Image
import numpy as np
import io

class Dangeons(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.command(aliases=['подземелье'])
    async def dangeon(self, ctx):
        #await ctx.send("Начинаем сбор для посещения Deep Dark Dangeon")
        members = list(ctx.guild.members)
        online_members = [member for member in members if member.status != 'offline']
        online_members = [member for member in members if member.bot != True]
        while len(online_members) > 4:
            del online_members[random.randint(0,len(online_members)-1)]  
        online_mentions = ''
        for member in online_members:
            online_mentions = online_mentions + ' ' + member.mention
        #await ctx.send(f"В данжен пойдут {online_mentions}" )
        avatars = []
        img_dangeon = Image.open('cogs/dgs/gachimuchi-4953271.jpeg')
        for member in online_members:
            byte_avatar = io.BytesIO(await member.avatar_url_as(format="jpeg").read())
            avatar = Image.open(byte_avatar)
            avatar = avatar.resize((80,80))
            avatars.append(np.asarray(avatar))
            

def setup(bot):
    bot.add_cog(Dangeons(bot))
    print('Dangeons being loaded!')