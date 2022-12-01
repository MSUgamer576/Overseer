
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


class Moderation(commands.Cog):
    def __init__(self, client, *args, **kwargs):
        self.client = client
    
    @slash_command(name='kick', description='kicks a member')
    async def kick(
        self,
        interaction: Interaction,
        member: nextcord.Member = nextcord.SlashOption(name='member', description='please select a member'),
        reason: str = nextcord.SlashOption(name='reason', description='please provide a reason', required=False)
    ):
        if not reason: reason="no reason"
        await member.kick(reason=reason)
        await interaction.response.send_message(f"{member} has been kicked for reason: {reason}")
    
    @slash_command(name='ban', description='Bans a member')
    async def ban(
        self,
        interaction: Interaction,
        member: nextcord.Member = nextcord.SlashOption(name='member', description='please provide a member'),
        reason: str = nextcord.SlashOption(name='reason', description='please enter a reason', required=False)
    ):
        if not reason: reason="No reason"
        await member.ban(reason=reason)
        await interaction.response.send_message(f"{member} has been banned for reason: {reason}")

    @slash_command(name='unban', description='Unban a member')
    async def unban(
        self,
        interaction: Interaction,
        member: nextcord.User = nextcord.SlashOption(name='memberid', description=' please provide a member id')

    ):
        await interaction.guild.unban(user=member)
        await interaction.response.send_message(f"{member} has been unban by {interaction.user.mention}")

def setup(client):
    client.add_cog(Moderation(client))
