import nextcord, config, os
from nextcord.ext import commands
from nextcord import Interaction, SlashOption, ChannelType
import requests
import aiohttp
import random
import os
from nextcord.abc import GuildChannel


intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True


client = commands.Bot(command_prefix = '>', intents=intents)

list = ['cogs.moderation']
for item in list:
    client.load_extension(item)

list = ['cogs.fun']
for item in list:
    client.load_extension(item)

list = ['cogs.memes']
for item in list:
    client.load_extension(item)

@client.event
async def on_ready():
    print(f"{client.user} is online!")
    print("------------------------")
    await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="i am a discord bot", url="https://github.com/MSUgamer576"))

client.run('token')