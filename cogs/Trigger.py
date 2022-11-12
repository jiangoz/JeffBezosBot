import asyncio
import discord
from discord.ext import commands


class Trigger(commands.Cog):
    '''Keywords that trigger bot responses'''

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg: str):

        # ignore self sent messages and DMs
        if msg.author == self.bot.user or msg.guild is None:
            return

        if 'dress code' in msg.content.lower():
            await msg.channel.send('the dress code is to shower and wear clothes')


async def setup(bot):
    await bot.add_cog(Trigger(bot))
