import discord
from discord.ext import commands

description = 'PineappleBot the Best Discord Bot!'
bot_prefix = '!'

client = commands.Bot(description=description, command_prefix=bot_prefix)

@client.event
async def on_ready():
    print('Logged In')
    print('Name : {}'.format(client.user.name))
    print('ID : {}'.format(client.user.id))
    print(discord.__version__)

    @client.command(pass_context=True)
    async def ping(ctx):
        await client.say('Pong!')

client.run(token)