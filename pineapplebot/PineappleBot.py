"""A dumb bot."""
import sys
import logging
from urllib import request
import random
import discord
from discord.ext import commands
import config
import addingcommands

DESCRIPTION = 'PineappleBot the Best Discord Bot!'
BOT_PREFIX = '?'
BOT_VERSION = '0.0.1 alpha'

logging.basicConfig(level=logging.INFO)

client = commands.Bot(description=DESCRIPTION, command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    """Function to handle the bot entering a ready state."""
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

@client.command(pass_context=True)
async def randomword(ctx):
    """Posts random word from world site"""
    await client.send_typing(ctx.message.channel)
    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = request.urlopen(word_site)
    txt = response.read()
    words = txt.splitlines()
    word = random.choice(words).decode('UTF-8')
    await client.say(word)

addingcommands.registeraddingcommands(client)

client.run(config.BOT_TOKEN)
