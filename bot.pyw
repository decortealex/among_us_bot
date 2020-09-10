import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = discord.ext.commands.Bot(command_prefix='$', help_command=None, description=None)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='mutechannel')
@commands.has_guild_permissions(mute_members=True)
async def mutechannel(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
            
        for member in channel.members:
            await member.edit(mute=True)

        await ctx.send("Voice channel muted.")
    else:
        await ctx.send("You are not connected to a voice channel.")
        return

@bot.command(name='unmutechannel')
@commands.has_guild_permissions(mute_members=True)
async def unmutechannel(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel

        for member in channel.members:
            await member.edit(mute=False)

        await ctx.send("Voice channel unmuted.")
    else:
        await ctx.send("You are not connected to a voice channel.")
        return
        
bot.run(TOKEN)