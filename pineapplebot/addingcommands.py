"""all the add, add and adding commands for the bot"""
import discord
from discord.ext import commands

def registeraddingcommands(client: commands.Bot):
    """Creates and registers all of the adding commands to the specified bot client"""
    async def add(left: int, right: int):
        """Adds two numbers together."""
        await client.say("{0} + {1} = {2}".format(left, right, left + right))
    client.command()(add)
    async def addadd(text: str):
        """Adds Add to the input text."""
        await client.say("Add " + text)
    client.command()(addadd)
    async def addnaddadd(left: int, right: int):
        """Adds two numbers together and adds Add."""
        await client.say("Add " + str(left + right))
    client.command()(addnaddadd)
    async def addnaddaddnadd(left: int, right: int, text: str):
        """Adds two numbers together and adds Add, then adds that to the input text."""
        await client.say("Add {0} {1}".format(str(left + right), text))
    client.command()(addnaddaddnadd)
