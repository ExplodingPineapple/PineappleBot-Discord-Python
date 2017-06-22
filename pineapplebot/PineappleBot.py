import sys
import logging
import random
import asyncio
import config
import plugins.stream_alerts
import discord
from discord.ext import commands

DESCRIPTION = 'Pineapplebot the Best Discord bot!'
BOT_PREFIX = '!'
BOT_VERSION = '0.0.1 alpha'

logging.basicConfig(level=logging.INFO)

bot = commands.Bot(description=DESCRIPTION, command_prefix=BOT_PREFIX)

@bot.event
async def on_ready():
    print('Logged In')
    print('Name : {}'.format(bot.user.name))
    print('ID : {}'.format(bot.user.id))
    print('Discord Library : {}'.format(discord.__version__))
    print('Python Version : {}'.format(sys.version))

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say('Pong!')
    await bot.say(ctx.message.author.mention + ' I\'m watching you buddy!')

@bot.command(pass_context=True)
async def version(ctx):
    await bot.say('PineappleBot version : {}'.format(BOT_VERSION))
    await bot.say('Running on Python version : {}'.format(sys.version))

@bot.command()
async def add(left: int, right: int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command()
async def addadd(text: str):
    """Adds Add to the input text."""
    await bot.say("Add " + text)

@bot.command()
async def addnaddadd(left: int, right: int):
    """Adds two numbers together and adds Add."""
    await bot.say("Add " + str(left + right))

@bot.command()
async def addnaddaddnadd(left: int, right: int, text: str):
    """Adds two numbers together and adds Add, then adds that to the input text."""
    await bot.say("Add {0} {1}".format(str(left + right), text))


bot.run(config.bot_token)
