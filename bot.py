import discord
from discord.ext import commands

bot = discord.Client(command_prefix="")

@bot.event
async def on_message(message):
    if message.content.lower().startswith("siler misin"):
        liste=message.content.split(" ")
        sayi = int(liste[0])
        await message.channel.purge(limit=sayi)
        await message.channel.send(str(sayi)+" "+"mesaj başarıyla silindi.")
bot.run('token')
