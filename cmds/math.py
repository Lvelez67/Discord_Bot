from discord.ext import commands


@commands.group()
async def math(ctx):
  if ctx.invoked_subcommand is None:
    await ctx.send(f"No, {ctx.subcommand_passed} does not belong to math")

@math.command()
async def add(ctx, one : int, two : int):
  await ctx.send(one + two)
  
async def setup(bot):
  bot.add_command(math)
  bot.add_command(add)#This allows the add command to be used as ~add and ~math add 
 #Useful if you want to create a shortcut for a comma
  