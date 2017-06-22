

@client.command(pass_context=True)
async def version(ctx):
    await client.say('PineappleBot version : {}'.format(bot_version))
    await client.say('Running on Python version : {}'.format(sys.version)