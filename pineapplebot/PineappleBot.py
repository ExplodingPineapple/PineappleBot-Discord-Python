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



client.run(bot_token)
