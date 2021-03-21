# Импорты
import discord
from discord.ext import commands
from config import settings
import os

intents = discord.Intents(members=True, presences=True)
bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)


# Основные кооманды

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print(bot.guilds)


@bot.command(aliases=['Привет', 'привет'])
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f'Привет Дружок-пирожок, {author.mention}! Ты ошибся дверью')


@bot.command()
async def load(ctx, extension):
    if ctx.author.id == 510786265311084544:
        bot.load_extension(f"cogs.{extension}")


@bot.command()
async def reload(ctx, extension):
    if ctx.author.id == 510786265311084544:
        bot.reload_extension(f"cogs.{extension}")


@bot.command()
async def unload(ctx, extension):
    if ctx.author.id == 510786265311084544:
        bot.unload_extension(f"cogs.{extension}")


for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(settings['token'])
