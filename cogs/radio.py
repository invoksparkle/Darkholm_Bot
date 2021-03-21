import discord
from discord.ext import commands
import youtube_dl
import ffmpeg


class Radio(commands.Cog):
    YDL_OPTIONS = {
        'format': 'worstaudio/best',
        'noplaylist': 'True',
        'simulate': 'True',
        'preferredquality': '192',
        'preferredcodec': 'mp3',
        'key': 'FFmpegExtractAudio'
    }
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    def __init__ (self, bot):
        self.bot = bot
        
    @commands.command()
    async def start(self, ctx, arg):
        with youtube_dl.YoutubeDL(Radio.YDL_OPTIONS) as ydl:
            info = ydl.extract_info(arg, download=False)
        URL = info['formats'][0]['url']
        if ctx.voice_client is None:
            chanel = discord.utils.get(ctx.guild.channels, name='Radio')
            await chanel.connect()
        ctx.voice_client.play(discord.FFmpegPCMAudio(executable="C:\\ffmpeg\\bin\\ffmpeg.exe", source = URL, **Radio.FFMPEG_OPTIONS))

def setup(bot):
    bot.add_cog(Radio(bot))
    print('Radio being loaded!')