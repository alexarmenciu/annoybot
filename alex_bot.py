import os
import discord
import time
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

intents = discord.Intents.all()
client = discord.Client()


# function to define how the bot types when a user begins typing
@client.event
async def on_typing(channel, user, when):

    #check that user is not the bot, otherwise we would enter an infinite "typing..." loop
    if client.user != user:
        # channel.typing() is a generalized way to indicate the bot is typing in the specified channel
        async with channel.typing():
            time.sleep(5)


# function defines how the bot creates a tts message
@client.event
async def on_message(message):
    await message.guild.me.edit(nick="typelex")
    #first check the user is not the bot
    if client.user != message.author:
        #change the bot's username in the server to the sender's username to create a funnier text to speech
        await message.guild.me.edit(nick=message.author.display_name)

        #type while the bot runs (but this shouldn't take too long in most cases)
        async with message.channel.typing():

            #send a message then delete it soon after for cleanup
            await message.channel.send(content=message.content,
                                       tts=True,
                                       delete_after=10)

        #change username back to bot username
        await message.guild.me.edit(nick="typelex")


#begin the client runtime
client.run(TOKEN)
