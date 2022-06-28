import discord
import os
import json
import asyncio
import time
from core.classes import CogExtension
from discord.ext import commands

class Task(CogExtension):
    
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command()
    async def bgtask(self, ctx):
        async def testtask():
            await self.bot.wait_until_ready()
            while not self.bot.is_closed():
                await ctx.send('b')
                await asyncio.sleep(1)

        self.bgtask = self.bot.loop.create_task(testtask())

def setup(bot):
    bot.add_cog(Task(bot))