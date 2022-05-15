import asyncio
import discord
from discord.ext import commands

# NO COMMANDS HERE, only 1 listener for on_message()
# Designed specifically for Amazon server


class Trigger(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg: str):

        # ignore self sent messages
        if msg.author == self.bot.user:
            return

        # if msg was sent in DM (not in a guild)
        if msg.guild == None:
            return

        if 'dress code' in msg.content.lower():
            await msg.channel.send('the dress code is to shower and wear clothes')


def setup(bot):
    bot.add_cog(Trigger(bot))
