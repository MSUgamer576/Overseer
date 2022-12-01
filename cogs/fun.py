import nextcord
from nextcord import slash_command, Interaction
from nextcord.ext import commands
import requests
import aiohttp
import random
import os


class Fun(commands.Cog):
    def __init__(self, client, *args, **kwargs):
        self.client = client

    @slash_command(name = "hello", description = "Sends a Hi")
    async def hello(self, interaction: Interaction):
        await interaction.response.send_message("Hello!")


    @slash_command(name = "bye", description = "Sends a bye")
    async def bye(self, interaction: Interaction):
        await interaction.response.send_message("Bye")

    @slash_command(name = "members", description = "members information")
    async def members(self , interaction: Interaction):
        total = len(interaction.guild.members)
        await interaction.send(f"There are {total} people in this server")

    @slash_command(name = "about", description = "about the person who made me")
    async def about(self, interaction: Interaction):
        embed=nextcord.Embed(title="About Me", description="Im Overseer, A Discord Bot With Support For Slash Commands Made By ❄ cold#7720", color=0x00ffbf)
        embed.set_author(name="Cold", url="https://github.com/MSUgamer576", icon_url="https://cdn.discordapp.com/avatars/810400726865412128/8419b2076966826bc263031f80418f58.png?size=1024")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1040890682153386014/d1e31e52de39c2b0947e3f395f80aefd.png?size=1024")
        embed.set_footer(text="Made with ❤️ By cold")
        await interaction.send(embed=embed)

    
    @slash_command(name = "help", description = "Help Command")
    async def help(self, interaction: Interaction):
        embed=nextcord.Embed(title="Command's Of Overseer", color=0x26cb1a)
        embed.add_field(name="/ban", value="Ban A Member(Accessible To Mod's Only)", inline=False)
        embed.add_field(name="/bye", value="Sends a Bye", inline=False)
        embed.add_field(name="/hello", value="Sends a Hello", inline=False)
        embed.add_field(name="/kick", value="Kicks a Member(Accessible to Mod's Only)", inline=False)
        embed.add_field(name="/long", value="suprise", inline=False)
        embed.add_field(name="/members", value="sends how many people are in the server", inline=False)
        embed.add_field(name="/meme", value="gets Memes Form r/whenthe (requested By conspiracy enjoyer)", inline=False)
        embed.add_field(name="/rickroll", value="it Does What it says", inline=False)
        embed.add_field(name="/unban", value="to unban people who where banned(accessible to Mod's Only)", inline=False)
        await interaction.send(embed=embed)


def setup(client):
    client.add_cog(Fun(client))