
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
import nextcord
from nextcord import slash_command, Interaction
from nextcord.ext import commands
import requests
import aiohttp
import random
import os


class memes(commands.Cog):
    def __init__(self, client, *args, **kwargs):
        self.client = client

    @slash_command(name = "rickroll", description = "send a rickroll")
    async def rickroll(self, interaction: Interaction):
            if not interaction.channel.is_nsfw():
                embed = nextcord.Embed(
                    title="rickroll",
                    color=nextcord.Colour.purple()
                )
                embed.set_image(url="https://media.tenor.com/CWgfFh7ozHkAAAAC/rick-astly-rick-rolled.gif")
                await interaction.send(embed=embed)


    @slash_command(name = "meme", description = "send's a meme from r/whenthe")
    async def meme(self, interaction: Interaction):
        embed = nextcord.Embed(title="Meme", description="a meme")
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/whenthe/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await interaction.send(embed = embed)














def setup(client):
    client.add_cog(memes(client))