import discord
import random

from bot_settings import TOKEN
from bot_mantik import gen_pass
from bot_mantik import flip_coin
# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# istemci (client) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık')
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send("Hi!")

    elif message.content.startswith('!password'):
        await message.channel.send(gen_pass(5))

    elif message.content.startswith('!bye'):
        await message.channel.send(":pensive:")

    elif message.content.startswith('!yt'):
        await message.channel.send(flip_coin())

    else:
        await message.channel.send("Yanlış Yazdın Tekrar Dene")

client.run(TOKEN["TOKEN"])