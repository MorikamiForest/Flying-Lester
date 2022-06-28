import discord
import os
from core.classes import CogExtension
from discord.ext import commands

class Reacts(CogExtension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def flying(self, ctx):
        pic = discord.File('./image/flying.jpg')
        await ctx.send("I'm Flying!!!", file=pic)

    @commands.command()
    async def dancing(self, ctx):
        pic = discord.File('./image/dancing.jpg')
        await ctx.send("I'm Dancing", file=pic)

    @commands.command()
    async def hello(self, ctx):
        pic = discord.File('./image/greeting.jpg')
        await ctx.send(u"我带你们打", file=pic)


def setup(bot):
    bot.add_cog(Reacts(bot))