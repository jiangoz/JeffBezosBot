import asyncio
from typing import List
import yfinance as yf
import plotly.express as px
import string
import random
import os
import discord
from discord import app_commands
from discord.ext import commands



class Stocks(commands.Cog):
    '''Stocks information and graphs'''

    def __init__(self, bot):
        self.bot = bot

        # maps a period to a reasonable interval
        self.periods = {
            '1d': '5m',
            '5d': '30m',
            '1mo': '1d',
            '3mo': '1d',
            '6mo': '1d',
            'ytd': '1d',
            '1y': '1d',
            '2y': '5d',
            '5y': '1wk',
            '10y': '1mo',
            'max': '1mo',
        }
        
    
    @app_commands.command()
    @app_commands.checks.cooldown(1, 30, key=lambda i: (i.guild_id, i.user.id))
    async def stocks(self, 
        interaction: discord.Interaction, 
        ticker_symbol: str = 'AMZN', 
        period: str = '1mo',
        ):
        """Look up a stock and graph it"""
        
        stock = yf.Ticker(ticker_symbol.upper())
        stock_info = stock.info

        if (stock_info['regularMarketPrice'] is None):
            await interaction.response.send_message('Please provide a valid ticker symbol', ephemeral=True)
            return

        current_price = stock_info['currentPrice']
        market_cap = stock_info['marketCap']

        history_df = stock.history(period, self.periods[period])
        fig = px.line(history_df, y='Close', template='plotly_dark')
        fig.update_traces(line_color='#FF9900')

        rand_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))
        file_name = f'stocks{rand_str}.png'
        fig.write_image(file_name)

        await interaction.response.send_message(
            f'**{ticker_symbol.upper()}** Current Price: `${current_price}`\nMarket Cap: `${market_cap:,}`',
            file=discord.File(file_name))
        
        if os.path.exists(file_name):
            os.remove(file_name)

    @stocks.autocomplete('period')
    async def stocks_autocomplete(
        self,
        interaction: discord.Interaction,
        current: str,
    ) -> List[app_commands.Choice[str]]:
        periods = self.periods.keys()
        return [
            app_commands.Choice(name=p, value=p)
            for p in periods if current.lower() in p.lower()
        ]
    
    @stocks.error
    async def on_stocks_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.response.send_message(str(error), ephemeral=True)


async def setup(bot):
    await bot.add_cog(Stocks(bot))
