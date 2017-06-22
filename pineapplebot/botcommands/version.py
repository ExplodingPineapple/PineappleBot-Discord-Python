import sys
import discord

BOT_VERSION = '0.0.1 alpha'

@client.command(pass_context=True)
async def version(ctx):
    await client.say('PineappleBot version : {}'.format(BOT_VERSION))
    await client.say('Running on Python version : {}'.format(sys.version))
