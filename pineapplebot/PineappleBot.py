import sys
import logging
import random
import asyncio
import time
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
    """Prints to terminal when bot is ready"""
    print('Logged In')
    print('Name : {}'.format(bot.user.name))
    print('ID : {}'.format(bot.user.id))
    print('Discord Library : {}'.format(discord.__version__))
    print('Python Version : {}'.format(sys.version))

@bot.command(pass_context=True)
async def ping(ctx):
    """Simple ping pong command to test the bot"""
    await bot.say('Pong!')
    await bot.say(ctx.message.author.mention + ' I\'m watching you buddy!')

@bot.command(pass_context=True)
async def version():
    """Replys in chat with bot's version info"""
    await bot.say('PineappleBot version : {}'.format(BOT_VERSION))
    await bot.say('Running on Python version : {}'.format(sys.version))

@bot.command()
async def add(left: int, right: int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command()
async def count():
    """Counts to ten."""
    COUNT = 1
    while COUNT <= 5:
        await bot.say(COUNT)
        COUNT = COUNT + 1
        time.sleep(1)
    await bot.say("Finished!")

bot.run(config.bot_token)
