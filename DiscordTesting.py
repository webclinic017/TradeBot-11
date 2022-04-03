# bot.py
import os

import discord
from dotenv import load_dotenv # this line

load_dotenv() #and this line are for more usability for future me to get fucked by.
TOKEN = 'OTYwMjc1MTk1MTcwNTI5Mjkx.YkoD9w.iRvuiq1pvS_ceUK3ZTQIHtFIJlI'
GUILD = 'For TraderMan'


 #IPMORTANT REGEX ^[-_\p{L}\p{N}\p{sc=Deva}\p{sc=Thai}]{1,32}$



client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'buy':
        print("buy request sent")
        response = ("bought!")
        await message.channel.send(response)

client.run(TOKEN)