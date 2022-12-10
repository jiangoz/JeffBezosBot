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
from datetime import datetime, timezone, timedelta
from dateutil.relativedelta import relativedelta


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
    

    @app_commands.command()
    @app_commands.checks.cooldown(1, 30, key=lambda i: (i.guild_id, i.user.id))
    async def rsu(self, 
        interaction: discord.Interaction,
        amount_usd: int, 
        ticker_symbol: str = 'AMZN', 
        ):
        """Calculate RSU vesting based on the average price in past 30 days"""

        if amount_usd <= 0:
            await interaction.response.send_message(
                'Please provide a positive amount of stocks in USD', 
                ephemeral=True)
            return

        if amount_usd > 100000000000:
            await interaction.response.send_message(
                'You ain\'t a multibillionaire, skill issue!', 
                ephemeral=True)
            return

        stock = yf.Ticker('AMZN')
        stock_info = stock.info

        if (stock_info['regularMarketPrice'] is None):
            await interaction.response.send_message('Please provide a valid ticker symbol', ephemeral=True)
            return

        history_df = stock.history('1mo', '1d')
        avg = round(history_df['Close'].mean(), 7)
        shares = amount_usd / avg

        today = datetime.now(timezone(-timedelta(hours=8))) # PST
        y1 = today + relativedelta(years=1)
        y2 = y1 + relativedelta(years=1)
        y2_6mo = y2 + relativedelta(months=6)
        y3 = y2_6mo + relativedelta(months=6)
        y3_6mo = y3 + relativedelta(months=6)
        y4 = y3_6mo + relativedelta(months=6)

        await interaction.response.send_message(
            f"**{ticker_symbol.upper()}** past 30 day average: `${avg}`\n"
            + f"{y1.strftime('%x')} | `{round(0.05*shares, 7)}` units | `${0.05*shares*avg}`\n"
            + f"{y2.strftime('%x')} | `{round(0.15*shares, 7)}` units | `${0.15*shares*avg}`\n"
            + f"{y2_6mo.strftime('%x')} | `{round(0.2*shares, 7)}` units | `${0.2*shares*avg}`\n"
            + f"{y3.strftime('%x')} | `{round(0.2*shares, 7)}` units | `${0.2*shares*avg}`\n"
            + f"{y3_6mo.strftime('%x')} | `{round(0.2*shares, 7)}` units | `${0.2*shares*avg}`\n"
            + f"{y4.strftime('%x')} | `{round(0.2*shares, 7)}` units | `${0.2*shares*avg}`\n"
            + f"Total | `{round(shares, 7)}` units | `${amount_usd}`| TZ: PST"
        )
    
    @rsu.error
    async def on_rsu_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.response.send_message(str(error), ephemeral=True)


async def setup(bot):
    await bot.add_cog(Stocks(bot))
