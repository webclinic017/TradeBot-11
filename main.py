import alpaca_trade_api as tradeapi
import numpy as np
import time
import discord

#discord var
TOKEN = 'OTYwMjc1MTk1MTcwNTI5Mjkx.YkoD9w.iRvuiq1pvS_ceUK3ZTQIHtFIJlI'
GUILD = 'For TraderMan'
#alpaca var
SEC_KEY = 'xeTVHjYvfDkabRXqCa0iRGZ7K9V8nn8TTHnjboC4'  # Secret key here
PUB_KEY = 'PK9MJ9WIT9BMA0SGANPC'  # public key here

BASE_URL = 'https://paper-api.alpaca.markets' # This is the base URL for paper trading
#BASE_URL = 'https://data.alpaca.markets/v2' # swap this one for past market data


api = tradeapi.REST(key_id=PUB_KEY, secret_key=SEC_KEY, base_url=BASE_URL) # For real trading, don't enter a base_url




# buy function
def buy():
    api.submit_order(
        symbol='SPY',
        qty=100,
     side='buy',
        type='market',
        time_in_force='gtc'  # good till cancelled
)

client = discord.Client()
"""
this part is just general connection info for dev
"""

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


"""
how to send buy requests from discord
"""
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'buy':
        print("INFO:buy request sent")
        response = ("bought!")
        await message.channel.send(response)
        buy()




client.run(TOKEN) #this seems important but i dont know what it does.