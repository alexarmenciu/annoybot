import os
import discord
import time
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

intents = discord.Intents.all()
client = discord.Client()


@client.event
async def on_typing(channel, user, when):
    if client.user != user:
        async with channel.typing():
            time.sleep(5)


client.run(TOKEN)
