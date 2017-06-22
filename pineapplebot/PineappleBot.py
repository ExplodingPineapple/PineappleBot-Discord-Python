import sys
import logging
import discord
import config
import botcommands.version
from discord.ext import commands

DESCRIPTION = 'PineappleBot the Best Discord Bot!'
BOT_PREFIX = '!'

logging.basicConfig(level=logging.INFO)

client = commands.Bot(description=DESCRIPTION, command_prefix=BOT_PREFIX)

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



client.run(config.bot_token)
