import random

from discord import utils
from discord.ext import commands


class Slave(commands.Cog):
    """

    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def slave(self, ctx):
        members = list([member for member in ctx.guild.members if not member.bot])
        slave = random.choice(members)
        await ctx.send(f'А Fucking Slave сегодня: {slave.mention}')
        slave_role = utils.get(ctx.guild.roles, name='Slave')
        await slave.add_roles(slave_role)


def setup(bot):
    """

    :param bot:
    """
    bot.add_cog(Slave(bot))
    print("Slave being loaded!")
