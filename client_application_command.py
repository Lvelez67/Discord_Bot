import settings
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")

def run():
  intents = discord.Intents.default()
  intents.message_content = True
  intents.members = True
  
  bot = commands.Bot(command_prefix="~", intents=intents)
  
  @bot.event
  async def on_ready():
    logger.info(f"User: {bot.user} (ID: {bot.user.id})")
    logger.info(f"Guild ID {bot.guilds[0].id}")
    bot.tree.copy_global_to(guild=settings.GUILDS_ID)
    await bot.tree.sync(guild=settings.GUILDS_ID)
  
  @bot.hybrid_command(name="pong", description="pings")
  async def pong(ctx):
    await ctx.send("ping")
    
  @bot.tree.command()
  async def ciao(interaction: discord.Interaction):
    await interaction.response.send_message(f"Ciao! {interaction.user.mention}", ephemeral=True)
    
    
  bot.run(settings.DISCORD_API_SECRET, root_logger=True)
  
if __name__ == "__main__":
  run()