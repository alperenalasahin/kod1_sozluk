import discord
from bot_settings import TOKEN
from lol_samp import *
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def lol(ctx, deger1):
    await ctx.send(lol_fun(deger1))        

bot.run(TOKEN["TOKEN"])    