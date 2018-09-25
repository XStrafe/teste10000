import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print("The bot is online!")

@bot.command
async def on_message(message):
    if  message.author == client.user:
        return
    elif message.content.startswith("!help"):
        await client.send_message(message.channel, "!fornite, !hulu, !spotify, !netflix, !pornhub")

lines = open(r'Fortnite.txt').read().splitlines()

@bot.command(pass_context=True)
async def fortnite (ctx):
    userName = ctx.message.author.name
    userID = ctx.message.author.id

    if ctx.message.server:
        myline = random.choice(lines)
    split = myline.partition(":")
    
    embed=discord.Embed(title="Fornite Account", color=0xff00b6)
    embed.set_thumbnail(url="https://png.icons8.com/color/1600/fortnite.png")
    embed.add_field(name="Email:", value=split[0], inline=True)
    embed.add_field(name="Password:", value=split[2], inline=False)
    await bot.send_message(ctx.message.author, embed=embed)

    print("{} Typed !gen fortnite".format(userName))
    
lines = open(r'Spotify.txt').read().splitlines()

@bot.command(pass_context=True)
async def spotify (ctx):
    userName = ctx.message.author.name
    userID = ctx.message.author.id

    if ctx.message.server:
        myline = random.choice(lines)
    split = myline.partition(":")
    
    embed=discord.Embed(title="Spotify Account", color=0x00ff00)
    embed.set_thumbnail(url="https://image.flaticon.com/icons/png/512/232/232413.png")
    embed.add_field(name="Email:", value=split[0], inline=True)
    embed.add_field(name="Password:", value=split[2], inline=False)
    await bot.send_message(ctx.message.author, embed=embed)

    print("{} Typed !gen spotify".format(userName))

lines = open(r'Netflix.txt').read().splitlines()

@bot.command(pass_context=True)
async def netflix (ctx):
    userName = ctx.message.author.name
    userID = ctx.message.author.id

    if ctx.message.server:
        myline = random.choice(lines)
    split = myline.partition(":")
    
    embed=discord.Embed(title="Netflix Account", color=0xf00000)
    embed.set_thumbnail(url="https://mbtskoudsalg.com/images/netflix-icon-png-3.png")
    embed.add_field(name="Email:", value=split[0], inline=True)
    embed.add_field(name="Password:", value=split[2], inline=False)
    await bot.send_message(ctx.message.author, embed=embed)

    print("{} Typed !netflix".format(userName))

lines = open(r'Pornhub.txt').read().splitlines()

@bot.command(pass_context=True)
async def pornhub (ctx):
    userName = ctx.message.author.name
    userID = ctx.message.author.id

    if ctx.message.server:
        myline = random.choice(lines)
    split = myline.partition(":")
    
    embed=discord.Embed(title="Pornhub Account", color=0xffff00)
    embed.set_thumbnail(url="https://mbtskoudsalg.com/image/pornhub-logo-png/740542.html")
    embed.add_field(name="Email:", value=split[0], inline=True)
    embed.add_field(name="Password:", value=split[2], inline=False)
    await bot.send_message(ctx.message.author, embed=embed)

    print("{} Typed !gen pornhub".format(userName))

lines = open(r'Hulu.txt').read().splitlines()

@bot.command(pass_context=True)
async def hulu (ctx):
    userName = ctx.message.author.name
    userID = ctx.message.author.id

    if ctx.message.server:
        myline = random.choice(lines)
    split = myline.partition(":")
    
    embed=discord.Embed(title="Hulu Account", color=0x80ff00)
    embed.set_thumbnail(url="https://mbtskoudsalg.com/images250_/hulu-icon.png")
    embed.add_field(name="Email:", value=split[0], inline=True)
    embed.add_field(name="Password:", value=split[2], inline=False)
    await bot.send_message(ctx.message.author, embed=embed)

    print("{} Typed !hulu".format(userName))

lines = open(r'Minecraft.txt').read().splitlines()

@bot.command(pass_context=True)
async def minecraft (ctx):
    userName = ctx.message.author.name
    userID = ctx.message.author.id

    if ctx.message.server:
        myline = random.choice(lines)
    split = myline.partition(":")
    
    embed=discord.Embed(title="Minecraft Account", color=0x2ffd6c)
    embed.set_thumbnail(url="https://pre00.deviantart.net/2640/th/pre/f/2016/133/0/d/minecraft_hd_logo_by_nuryrush-da2aumi.png")
    embed.add_field(name="Email:", value=split[0], inline=True)
    embed.add_field(name="Password:", value=split[2], inline=False)
    await bot.send_message(ctx.message.author, embed=embed)

bot.run('NDkzODQ2NTY0MTgwMzI4NDc1.Doq89g.DGtitK6oCc2wFzVfDY38WXQQLao')
