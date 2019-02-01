# Work with Python 3.6
import discord
from mytoken import TOKEN
from demineur import get_minesweeper

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith("!play"):
        command = message.content.split()
        print(command)
        msg = get_minesweeper(int(command[1]),  int(command[2]), int(command[3]))
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
