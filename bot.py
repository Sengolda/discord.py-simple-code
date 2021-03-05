import discord
from discord.ext import commands
client = commands.Bot(command_prefix = ".", intents =discord.Intents.all(),case_insensitive = True,help = None)
@client.event 
async def on_ready():
    print("ready boss")
    


@client.command()
async def hello(ctx):
    await ctx.send("hi")


@client.command()
async def ping(ctx):
    await ctx.send("pong")

@client.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=1):
 await ctx.channel.purge(limit = amount)

@client.command()
@commands.has_permissions(manage_messages = True)
async def purge(ctx,amount=1):
  await ctx.channel.purge(limit = amount)

@client.command()
@commands.has_permissions(kick_members = True)
async def whois(ctx, member : discord.Member):
  embed = discord.Embed(title = member.name , description = member.mention , color = discord.Colour.green())
  embed.add_field(name = "ID" , value = member.id , inline = True)
  embed.set_thumbnail(url = member.avatar_url)
  await ctx.send(embed=embed)

client.run("TOKEN HERE")
