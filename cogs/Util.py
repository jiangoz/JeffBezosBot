import discord
import asyncio
import os
from discord import app_commands
from discord.ext import commands


class Util(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping")
    @app_commands.checks.cooldown(1, 10, key=lambda i: (i.guild_id, i.user.id))
    async def ping(self, interaction: discord.Interaction) -> None:
        """Is Jeff Bezos still alive? Find out!"""
        await interaction.response.send_message(f'Pong! {round(self.bot.latency*1000)}ms')
    
    @ping.error
    async def on_ping_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.response.send_message(str(error), ephemeral=True)


async def setup(bot):
    await bot.add_cog(Util(bot))