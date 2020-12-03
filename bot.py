import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    """
    docstring
    """
    print('>> Lester is Ready to Fly!!!!!')

bot.run('NzgzODkxODUyMDk1OTE0MDI1.X8hWLQ.bhps3Jak116fCHekKMvc_zuoCnw')