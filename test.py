import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    # ignore its own messages
    if message.author == client.user:
        return

    print(message.author)
    await message.channel.send("Happy Birthday! 🎈🎉")

client.run(TOKEN)