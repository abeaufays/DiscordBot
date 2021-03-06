# Work with Python 3.6
import discord
from mytoken import TOKEN
from demineur import get_minesweeper
from command_handler import handle

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!'):
        msg = handle(message)
        print(msg)
        print(message.content)
        if msg is not None:
            await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
