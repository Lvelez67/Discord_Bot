import discord
from discord.ext import commands

class Greetings(commands.Cog):
  #useful link for creating events in cogs
  #https://stackoverflow.com/questions/67078658/discord-greetings-with-cogs-on-member-join-doent-work
  
  
  def __init__(self,bot):
    self.bot = bot
    
  # @commands.Cog.listener()
  # async def on_message(self, message: discord.Message):
  #   await message.add_reaction("\U0001F44D")
    
  @commands.Cog.listener()
  async def on_member_join(self, member:discord.Member):
    print(member)
    #await member.send("hello") sends dm
    guild = self.bot.get_guild(151725034644307968)
    channel = discord.utils.get(member.guild.channels, id=1184930527267012688)
    if guild:
      print('guild ok')
    else:
      print('guild not found')
      
    if channel is not None:
      await channel.send(f"{member.mention} has join the server.")
    else:
      print('id channel wrong')
      
  @commands.Cog.listener()
  async def on_member_remove(self, member: discord.Member):
    print('member')
    guild = self.bot.get_guild(151725034644307968)
    channel = discord.utils.get(member.guild.channels, id=1184930527267012688)
    await channel.send(f"{member.mention} has left the server.")
  
  @commands.Cog.listener()
  async def on_member_update(self, member: discord.Member):
    print('member')
    guild = self.bot.get_guild(151725034644307968)
    channel = discord.utils.get(member.guild.channels, id=1184930527267012688)
    await channel.send(f"{member.mention} has left the server.")
  
  
  @commands.command()
  async def hello(self, ctx, *, member:discord.Member):
    await ctx.send(f"Hello {member.name}")
    
async def setup(bot):
  await bot.add_cog(Greetings(bot))