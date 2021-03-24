import discord
from discord.ext import commands
import youtube_dl

from config import waves


class Radio(commands.Cog):
    YDL_OPTIONS = {
        'format': 'worstaudio/best',
        'noplaylist': 'True',
        'simulate': 'True',
        'preferredquality': '192',
        'preferredcodec': 'mp3',
        'key': 'FFmpegExtractAudio'
    }
    FFMPEG_OPTIONS = {'options': '-vn'}

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def radio(self, ctx, arg='gachi'):
        chose = waves[arg]
        with youtube_dl.YoutubeDL(Radio.YDL_OPTIONS) as ydl:
            info = ydl.extract_info(chose, download=False)
        url = info['formats'][0]['url']
        if ctx.voice_client is None:
            channel = discord.utils.get(ctx.guild.channels, name='Radio')
            await channel.connect()
        ctx.voice_client.stop()
        ctx.voice_client.play(
            discord.FFmpegPCMAudio(source=url, **Radio.FFMPEG_OPTIONS))


def setup(bot):
    bot.add_cog(Radio(bot))
    print('Radio being loaded!')
