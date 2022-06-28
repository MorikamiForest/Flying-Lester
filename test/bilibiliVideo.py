import discord
import os
from core.classes import CogExtension
from discord.ext import commands

class Music(CogExtension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(invoke_without_subcommand=True)
    async def join(self, ctx):
        destination = ctx.author.voice.channel
        if ctx.voice_state.voice:
            await ctx.voice_state.voice.move_to(destination)
            return

        ctx.voice_state.voice = await destination.connect()

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def summon(self, ctx, *, channel=None):
        destination = channel or ctx.author.voice.channel
        if ctx.voice_state.voice:
            await ctx.voice_state.voice.move_to(destination)
            return

        ctx.voice_state.voice = await destination.connect()

'''    @commands.command()
    async def play(self, ctx, *, search: str):
        if not ctx.voice_state.voice:
            await ctx.invoke(self.join)

        async with ctx.typing():
            try:
                source = await YTDLSource.create_source(ctx, search, loop=self.bot.loop)
            except YTDLError as e:
                await ctx.send('An error occurred while processing this request: {}'.format(str(e)))
            else:
                song = Song(source)

                await ctx.voice_state.songs.put(song)
                await ctx.send('Enqueued {}'.format(str(source)))
'''

def setup(bot):
    bot.add_cog(Music(bot))