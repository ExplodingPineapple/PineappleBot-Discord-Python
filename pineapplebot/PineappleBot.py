"""A dumb bot."""
import sys
import logging
import discord
from discord.ext import commands

DESCRIPTION = 'PineappleBot the Best Discord Bot!'
BOT_PREFIX = '!'
BOT_VERSION = '0.0.1 alpha'

logging.basicConfig(level=logging.INFO)

client = commands.Bot(description=DESCRIPTION, command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    """Function to handle the bot becoming ready."""
    print('Logged In')
    print('Name : {}'.format(client.user.name))
    print('ID : {}'.format(client.user.id))
    print('Discord Library : {}'.format(discord.__version__))
    print('Python Version : {}'.format(sys.version))

@client.command(pass_context=True)
async def ping(ctx):
    """Simple command to check if the bot is alive."""
    await client.say('Pong!')
    await client.say(ctx.message.author.mention + ' I\'m watching you buddy!')

@client.command(pass_context=True)
async def version():
    """Check the bot version."""
    await client.say('PineappleBot version : {}'.format(BOT_VERSION))
    await client.say('Running on Python version : {}'.format(sys.version))

@client.command()
async def addadd(text: str):
    """Adds Add to the input text."""
    await client.say("Add " + text)

@client.command()
async def addnaddadd(left: int, right: int):
    """Adds two numbers together and adds Add."""
    await client.say("Add " + str(left + right))

@client.command()
async def addnaddaddnadd(left: int, right: int, text: str):
    """Adds two numbers together and adds Add, then adds that to the input text."""
    await client.say("Add {0} {1}".format(str(left + right), text))

client.run('token')
