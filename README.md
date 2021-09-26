# Alex's Annoybot

A simple Discord bot to annoy my friends!

### Functionality
My bot types along with you as you type so that you're never alone:<\br>
![typing](https://user-images.githubusercontent.com/65733434/134791994-2377daf7-87b4-4146-8238-eff3c60bc7bc.PNG)

My bot also repeats your messages with your own username to blare out any messages you send to everyone on the channel using Discord's text to speech engine:<\br>
![peaceful discord](https://user-images.githubusercontent.com/65733434/134791993-f57cf54e-9d9c-4301-a6df-38c7cdf60699.png)

### Tech
My bot is very simple. I store my bot token in a .env file, so I use pyenv to load it, and then from there I simply use the discord.py python library to handle all discord- related events.

I am currently running the bot on an Azure VM (I am using the lowest tier of shared VM, so it is quite laggy and the tts functionality definitely suffers because of this) because it is free with my student bundle. You can add the bot to your own server [here](https://discord.com/api/oauth2/authorize?client_id=891079826021187634&permissions=67181568&scope=bot) (although as it is added to more servers, the functionality will suffer heavily due to lag).
