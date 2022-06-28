import discord
import os
import re
from core.classes import CogExtension
from discord.ext import commands

class Event(CogExtension):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        # channel = self.bot.get_channel(673203933698719749)
        # await channel.send('>> Lester is Ready to Fly!!!!!')
        print('Bot online')
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        keywords = msg.content.split()
        if (msg.content == "Lester" or msg.content == "lester") and msg.author != self.bot.user:
            await msg.channel.send("啊，谁叫我")
        elif ("lester" in keywords or "Lester"in keywords) and ("eat" in keywords and "shit" in keywords):
            await msg.channel.send("屎真好吃")


def setup(bot):
    bot.add_cog(Event(bot))