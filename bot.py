import discord
from discord.ext import commands

bot = discord.Client(command_prefix="")

@bot.event
async def on_message(message):
    if message.content.lower().startswith("purge"):
        arr=message.content.split(" ")
        amount = int(arr[0])
        await message.channel.purge(limit=amount)
        await message.channel.send(str(amount)+" "+"messages have deleted successfully")
bot.run('token')
