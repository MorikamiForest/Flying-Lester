#coding: utf-8
import os
import json
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.command()
async def load(ctx, extension):
    try:
        bot.load_extension(f'utils.{extension}')
        await ctx.send(f"Loaded {extension}")
    except FileExistsError:
        await ctx.send(f"No Extension names {extension}")

@bot.command()
async def unload(ctx, extension):
    try:
        bot.unload_extension(f'utils.{extension}')
        await ctx.send(f"Unloaded {extension}")
    except FileExistsError:
        await ctx.send(f"No Extension names {extension}")

@bot.command()
async def reload(ctx, extension):
    try:
        bot.reload_extension(f'utils.{extension}')
        await ctx.send(f"Re - Loaded {extension}")
    except FileExistsError:
        await ctx.send(f"No Extension names {extension}")



if __name__ == "__main__":
    with open('setting.json', 'r', encoding='utf8') as f:
        setting = json.loads(f.read())

    for f in os.listdir('./utils'):
        if f.endswith('.py'):
            bot.load_extension(f'utils.{f[:-3]}')

    bot.run(setting['TOKEN'])