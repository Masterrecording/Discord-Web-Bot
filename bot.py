import discord
from discord.ext import commands
from random import randint

async def getRandom(ctx, *args):
    try:
        await ctx.send(str(randint(int(args[0]), int(args[1]))))
    except Exception as e: 
        await ctx.reply(embed=discord.Embed(colour=discord.Colour.from_rgb(255,100,100), description="Error, expected command usage:\n!random `<min>` `<max>`\n\nIt gives a random number "))

def start(token, PREFIX):
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix=PREFIX, intents=intents)


    @bot.command()
    async def random(ctx):
        args = ctx.message.content.lower().replace(PREFIX+"random ", "").split(" ")
        await getRandom(ctx, *args)
        
    bot.run(token)