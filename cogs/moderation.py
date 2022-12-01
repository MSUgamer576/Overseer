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
