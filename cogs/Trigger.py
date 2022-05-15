import asyncio
import discord
from discord.ext import commands


class Trigger(commands.Cog):
    '''Keywords that trigger bot responses'''

    def __init__(self, bot):
        self.bot = bot
        self.triggerDict = {
            "dress code": "the dress code is to shower and wear clothes",
            "please keep trolling": "<:chillin:966826207750524949>"
        }

    @commands.Cog.listener()
    async def on_message(self, msg: str):

        # ignore self sent messages and DMs
        if msg.author == self.bot.user or msg.guild is None:
            return

        for trigger, response in self.triggerDict.items():
            if trigger in msg.content.lower():
                await msg.channel.send(response)
                return


def setup(bot):
    bot.add_cog(Trigger(bot))
