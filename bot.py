#coding: utf-8
import os
import json
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='lester>')

@bot.event
async def on_ready():
    channel = bot.get_channel(673203933698719749)
    await channel.send('>> Lester is Ready to Fly!!!!!')
    
    print('>> Bot online')

@bot.command()
async def ping(ctx):
    await ctx.send(f"{bot.latency*1000}(ms)")

@bot.command()
async def flying(ctx):
    pic = discord.File(os.path.abspath('image/flying.jpg'))
    await ctx.send(f"I'm Flying!!!", file=pic)

@bot.command()
async def dancing(ctx):
    pic = discord.File(os.path.abspath('image/dancing.jpg'))
    await ctx.send(f"I'm Dancing", file=pic)

@bot.command()
async def greeting(ctx):
    pic = discord.File(os.path.abspath('image/greeting.jpg'))
    await ctx.send(f"I'm Greeting", file=pic)


with open('setting.json', 'r', encoding='utf8') as f:
    setting = json.loads(f.read())

bot.run(setting['TOKEN'])