
'''MIT License

Copyright (c) [2022] [Shayaan]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''
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