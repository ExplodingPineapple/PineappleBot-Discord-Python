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

