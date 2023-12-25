import random
import settings
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")

def run():
  intents = discord.Intents.default()
  intents.message_content = True
  
  bot = commands.Bot(command_prefix="~", intents=intents)
  
  @bot.event
  async def on_ready():
    logger.info(f'User:{bot.user} (ID: {bot.user.id})')
    print('___________________')
  
  @bot.command(
    aliases=['p'],
    help="This is help",
    description="This is description",
    brief = "This is brief",
    enabled=True,
    hidden=True
  )
  async def ping(ctx):
    await ctx.send("Pong!") 
    """Answers with Pong""" 
    
  @bot.command()
  async def say(ctx, what = "Umm I think you're supposed to put something here?"):
     await ctx.send(what)
     """This will take in only one argument so hello world will
     not work you need 'hello world' or anything in quotes"""
  
  @bot.command()
  async def say2(ctx, *what):
     await ctx.send(" ".join(what))
  
  @bot.command()
  async def say3(ctx, what = "WHAT?", why = "WHY?"):
     await ctx.send(what+why)
     
  @bot.command()
  async def choices(ctx, *options):
     await ctx.send(random.choice(options))
     
  @bot.command()
  async def add(ctx, one : int, two : int):
    await ctx.send(one + two)
  
  bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
  run()
  