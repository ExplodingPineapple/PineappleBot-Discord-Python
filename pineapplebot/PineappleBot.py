import sys
import logging
import discord
from discord.ext import commands

description = 'PineappleBot the Best Discord Bot!'
bot_prefix = '!'
bot_version = '0.0.1 alpha'

logging.basicConfig(level=logging.INFO)

client = commands.Bot(description=description, command_prefix=bot_prefix)

@client.event
async def on_ready():
    print('Logged In')
    print('Name : {}'.format(client.user.name))
    print('ID : {}'.format(client.user.id))
    print('Discord Library : {}'.format(discord.__version__))
    print('Python Version : {}'.format(sys.version))

@client.command(pass_context=True)
async def ping(ctx):
    await client.say('Pong!')
    await client.say(ctx.message.author.mention + ' I\'m watching you buddy!')

@client.command(pass_context=True)
async def version(ctx):
    await client.say('PineappleBot version : {}'.format(bot_version))
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
