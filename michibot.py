import discord
from discord.ext import commands
import datetime
bot = commands.Bot(command_prefix='_', description="this is a testing bot")


#Ping-pong
@bot.command()
async def ping(ctx):
     await ctx.send('pong')

bot.run('OTAyMzg5Nzc5NjY3MjUxMjAx.YXdt-Q.FgShCaHEuoa4FDSPn_AKs8zmkAE')
