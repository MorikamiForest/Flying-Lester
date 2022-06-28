import discord
import os
import requests
import json
from core.classes import CogExtension
from discord.ext import commands
import core.bilibiliaudio as bili

convert_headers = {
    "Host" : "api.bilibili.com",
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36'
}


class Music(CogExtension):
    def __init__(self, bot):
        self.bot = bot
        self.current_playing = None # bv
        self.source_queue = [] # source
        self.bv_queue = [] # bv
        self.looping = False

    def clear_queue(self):
        for i in self.bv_queue:
            if os.path.isfile(f"temp/{i}.mp3"):
                os.remove(f"temp/{i}.mp3")
                print(f"temp/{i}.mp3 Removed")

    def check_queue(self):
        if self.current_playing and os.path.isfile(f"temp/{self.current_playing}.mp3"):
            os.remove(f"temp/{self.current_playing}.mp3")
            print(f"temp/{self.current_playing}.mp3 Removed")
            self.current_playing = None
        
        if self.source_queue != []:
            source = self.source_queue.pop(0)
            self.current_playing = self.bv_queue.pop(0)
            print(f"Playing {self.current_playing}")
            
            self.voice_client.play(source, after=lambda error: self.check_queue())

    @commands.command()
    async def join(self, ctx):
        channel = ctx.message.author.voice.channel
        self.voice_client = await channel.connect()
        await ctx.send(f'Connected to {channel}')

    @commands.command()
    async def leave(self, ctx):
        user_channel = ctx.message.author.voice.channel
        bot_channel =  ctx.guild.voice_client.channel
        if user_channel == bot_channel:
            client = ctx.guild.voice_client
            self.clear_queue()
            await client.disconnect()
            await ctx.send("Disconnected")
        else:
            await ctx.send('You have to be connected to the same voice channel to disconnect me.')

    @commands.command()
    async def pause(self, ctx):
        self.voice_client.pause()
        await ctx.send("Music Paused")

    @commands.command()
    async def resume(self, ctx):
        self.voice_client.resume()
        await ctx.send("Music Resumed")

    @commands.command()
    async def stop(self, ctx):
        self.clear_queue()
        self.voice_client.stop()
        await ctx.send("Music Stopped")
    
    @commands.command()
    async def skip(self, ctx):
        if not self.voice_client.is_playing:
            await ctx.send('Not playing any music right now')
        else:
            self.voice_client.stop()
            await ctx.send(f"{self.current_playing} skipped")
            self.check_queue()
            
    
    @commands.command()
    async def playb(self, ctx, bv):

        bv = str(bv).strip()
        if bv[0:2] == "av":
            convert_url = f"http://api.bilibili.com/x/web-interface/archive/stat?aid={bv[2:]}"
            data = requests.get(url=convert_url, headers=convert_headers)
            info = json.loads(data.content.decode('utf-8'))
            if info["code"] != -400:
                bv = str(info["data"]["bvid"])

        if not ctx.guild.voice_client or ctx.guild.voice_client.channel != ctx.message.author.voice.channel:
            await ctx.invoke(self.join)
        else:
            self.voice_client = ctx.guild.voice_client

        title = await bili.get_url(f"{bv}")
        source = await discord.FFmpegOpusAudio.from_probe(f"temp/{bv}.mp3")

        self.source_queue.append(source)
        self.bv_queue.append(bv)
        
        if not self.voice_client.is_playing():
            self.check_queue()
            await ctx.send(f'Now playing {title} https://www.bilibili.com/video/{bv}')
        else:
            await ctx.send(f'{title} in queue position {len(self.source_queue)} https://www.bilibili.com/video/{bv}')

def setup(bot):
    bot.add_cog(Music(bot))