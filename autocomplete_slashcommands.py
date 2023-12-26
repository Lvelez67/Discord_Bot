import typing
import settings
import discord
from discord.ext import commands
from discord import app_commands

logger = settings.logging.getLogger("bot")

def run():
  intents = discord.Intents.all()
  
  bot = commands.Bot(command_prefix="~", intents=intents)
  
  @bot.event
  async def on_ready():
    logger.info(f"User: {bot.user} (ID: {bot.user.id})")
    
    bot.tree.copy_global_to(guild=settings.GUILDS_ID)
    await bot.tree.sync(guild=settings.GUILDS_ID)
  
  @bot.tree.command()  
  @app_commands.describe(text_to_send="Simon say this..")
  @app_commands.rename(text_to_send="message")
  async def say(interaction: discord.Interaction, text_to_send: str):
    await interaction.response.send_message(f"{text_to_send}", ephemeral=True)
  
  async def drink_autocomplettion(
    interaction: discord.Interaction,
    current: str
  ) -> typing.List[app_commands.Choice[str]]:
    data=[]
    for drink_choice in ['beer','milk','tea', 'coffee', 'juice']:
      if current.lower() in drink_choice.lower():
        data.append(app_commands.Choice(name = drink_choice, value=drink_choice))
    return data

  @bot.tree.command()
  @app_commands.autocomplete(item=drink_autocomplettion)  
  async def drink(interaction: discord.Interaction, item: str):
    await interaction.response.send_message(f"{item}", ephemeral=True)

#     Way 1 for autocomplete (Max list size is 25)
#    @drink.autocomplete("item")
#   async def drink_autocomplettion(
#     interaction: discord.Interaction,
#     current: str
#   ) -> typing.List[app_commands.Choice[str]]:
#     data=[]
#     for drink_choice in ['beer','milk','tea', 'coffee', 'juice']:
#       if current.lower() in drink_choice.lower():
#         data.append(app_commands.Choice(name = drink_choice, value=drink_choice))
#     return data
  
  bot.run(settings.DISCORD_API_SECRET, root_logger=True)
  
if __name__ == "__main__":
  run()