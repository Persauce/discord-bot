import discord
from discord.ext import commands

import settings


def run():
    
    ints = discord.Intents.default()
    ints.message_content = True
    bot = commands.Bot(command_prefix="!",intents=ints)
    @bot.event
    async def on_ready():
        print("logged in")
         
    @bot.command()
    async def ping(ctx):
        await ctx.send("pong")
    



    bot.run(settings.DISC_CODE)
if __name__ == "__main__":
    run()