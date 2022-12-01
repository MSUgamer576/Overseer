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