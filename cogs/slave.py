from discord.ext import commands


class Slave(commands.Cog):
    """

    """

    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    """

    :param bot:
    """
    bot.add_cog(Slave(bot))
    print("Slave being loaded!")
