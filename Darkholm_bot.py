##Импорты
import discord
from discord import FFmpegPCMAudio
from discord.ext import commands, tasks
from config import settings
import youtube_dl
import ffmpeg
 
##Youtube

YDL_OPTIONS = {'format': 'worstaudio/best',
    'noplaylist': 'True',
    'simulate': 'True',
    'preferredquality': '192',
    'preferredcodec': 'mp3',
    'key': 'FFmpegExtractAudio'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}


##Тело бота
     
bot = commands.Bot(command_prefix= settings['prefix'])
client = discord.Client()

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

##Radio

@bot.command()
async def start(ctx, arg):
    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(arg, download=False)
    URL = info['formats'][0]['url']
    chanel = discord.utils.get(ctx.guild.channels, name='Radio')
    vc = await chanel.connect()
    vc.play(discord.FFmpegPCMAudio(executable="C:\\ffmpeg\\bin\\ffmpeg.exe", source = URL, **FFMPEG_OPTIONS))
    

## Запуск
bot.run(settings['token'])