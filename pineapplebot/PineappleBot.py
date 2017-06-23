import sys
import logging
import random
import asyncio
import time
import urllib.request
import config
import plugins.stream_alerts
import discord
from discord.ext import commands

DESCRIPTION = 'Pineapplebot the Best Discord bot!'
BOT_PREFIX = '!'
BOT_VERSION = '0.0.1 alpha'

logging.basicConfig(level=logging.INFO)

client = commands.Bot(description=DESCRIPTION, command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    """Prints to terminal when bot is ready"""
    print('Logged In')
    print('Name : {}'.format(client.user.name))
    print('ID : {}'.format(client.user.id))
    print('Discord Library : {}'.format(discord.__version__))
    print('Python Version : {}'.format(sys.version))

@client.command(pass_context=True)
async def ping(ctx):
    """Simple ping pong command to test the bot"""
    await client.say('Pong!')
    await client.say(ctx.message.author.mention + ' I\'m watching you buddy!')

@client.command(pass_context=True)
async def version():
    """Replys in chat with client's version info"""
    await client.say('PineappleBot version : {}'.format(BOT_VERSION))
    await client.say('Running on Python version : {}'.format(sys.version))

@client.command()
async def add(left: int, right: int):
    """Adds two numbers together."""
    await client.say(left + right)

@client.command()
async def count():
    """Counts up."""
    COUNT = 1
    while COUNT <= 5:
        await client.say(COUNT)
        COUNT = COUNT + 1
        time.sleep(1)
    await client.say("Finished!")

@client.command(pass_context=True)
async def randomword(ctx):
    """Posts random word from world site"""
    await client.send_typing(ctx.message.channel)
    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = urllib.request.urlopen(word_site)
    txt = response.read()
    WORDS = txt.splitlines()
    word = random.choice(WORDS)
    await client.say(word)

@client.command(pass_context=True)
async def triggered(ctx):
    """Posts triggered meme"""
    em = discord.Embed(title='Triggered')
    em.set_image(url='https://media.giphy.com/media/vk7VesvyZEwuI/giphy.gif')
    await client.send_message(ctx.message.channel, embed=em)

client.run(config.bot_token)
