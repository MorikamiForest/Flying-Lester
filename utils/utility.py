import discord
import os
import json
from core.classes import CogExtension
from discord.ext import commands

class Utility(CogExtension):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"{self.bot.latency*1000}(ms)")

    @commands.command()
    async def sayd(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clean(self, ctx, num: int=1, ):
        await ctx.channel.purge(limit=(num+1))
        await ctx.send(f"{num} Message(s) Cleaned")
    
    @commands.command()
    async def voice_clients(self, ctx):
        await ctx.send(self.bot.voice_clients)

def setup(bot):
    bot.add_cog(Utility(bot))