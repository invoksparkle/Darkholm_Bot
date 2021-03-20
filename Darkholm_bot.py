##Импорты
import discord
from discord.ext import commands
from config import settings

##Тело бота
bot = commands.Bot(command_prefix= settings['prefix'])

##Основной код
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f'Привет, {author.mention}!')

##Запуск
bot.run(settings['token'])