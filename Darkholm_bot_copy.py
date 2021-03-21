##Импорты
import os
import discord
from discord import FFmpegPCMAudio
from discord.ext import commands, tasks
from config import settings
import youtube_dl
import ffmpeg
 
##Youtube




##Тело бота
     
bot = commands.Bot(command_prefix= settings['prefix'])


##Основные кооманды

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

bot.run(settings['token'])