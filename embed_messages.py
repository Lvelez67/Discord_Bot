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
    logger.info(f"User: {bot.user} (ID: {bot.user.id})")
    
  @bot.command()
  async def ping(ctx):
    embed = discord.Embed(
      colour=discord.Colour.dark_teal(),
      description="This is the description",
      title="This is the footer"
      
    )
    
    embed.set_footer(text="this is the footer")
    embed.set_author(name="Luis", url="https://github.com/Lvelez67?tab=repositories")
    
    embed.set_thumbnail(url="https://th.bing.com/th/id/OIG.hSKc.XhLnL7SPxOdkRsU")
    embed.set_image(url="https://png.pngtree.com/png-vector/20230831/ourmid/pngtree-3d-penguin-model-illustration-png-image_9199122.png")
    
    embed.add_field(name="Git Repo", value="https://github.com/Lvelez67?tab=repositories",inline=False)
    embed.add_field(name="Site", value="https://www.youtube.com")
    embed.insert_field_at(1, name="Test insert", value="https://www.google.com")
    
    
    await ctx.send(embed=embed)
    
  
  bot.run(settings.DISCORD_API_SECRET, root_logger=True)
  
if __name__ == "__main__":
  run()