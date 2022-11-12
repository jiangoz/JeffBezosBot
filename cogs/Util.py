import discord
import asyncio
import random
from discord import app_commands
from discord.ext import commands



class Util(commands.Cog):
    '''Various utilities'''

    def __init__(self, bot):
        self.bot = bot
        self.teams = [
            'Amazon Web Services',
            'Amazon.com',
            'Retail',
            'Operations Technology',
            'Amazon Devices',
            'Human Resources',
            'Finance and Global Business Services',
            'eCommerce Foundation',
            'Consumer Payments',
            'Amazon Ads',
            'Amazon Alexa',
            'Student Programs',
            'Consumer Engagement',
            'Shopping',
            'Amazon Entertainment',
            'Amazon Go',
            'Amazonian Experience and Technology',
            'Selling Partner Services',
            'Marketplace',
            'Fulfillment & Operations',
            'Amazon Global Corporate Affairs',
            'Amazon Transportation Services',
            'Amazon Business',
            'Business & Corporate Development',
            'Health Storefront and Tech',
            'Kindle Content',
            'Amazon Customer Service',
            'Customer Experience and Business Trends',
            'Amazon Fresh',
            'Zoox',
            'Audible',
            'Zappos',
            'Whole Foods',
            'Twitch',
            'A9.com',
            'AbeBooks',
            'Amazon Air',
            'Amazon Books',
            'Amazon Games',
            'Amazon Lab126',
            'Amazon Logistics',
            'Amazon Pharmacy',
            'Amazon Publishing',
            'Amazon Robotics',
            'Amazon Studios',
            'Body Labs',
            'Book Depository',
            'ComiXology',
            'Digital Photography Review',
            'Eero LLC',
            'Goodreads',
            'Graphiq',
            'IMDb',
            'MGM Holdings',
            'PillPack',
            'Ring',
            'Souq.com',
            'Woot',
        ]
        self.cities = [
            'Seattle',
            'Bengaluru',
            'Sao Paulo',
            'San Francisco',
            'Austin',
            'Hyderabad',
            'Vancouver',
            'Arlington',
            'New York City',
            'Toronto',
            'Redmond',
            'Bellevue',
            'London',
            'San Diego',
            'Sunnyvale',
            'Dublin',
            'Madrid',
            'Dallas',
            'Boston',
            'Tempe',
            'Jersey City',
            'WestBorough',
            'Bucharest',
            'Northridge',
            'East Palo Alto',
            'Tel Aviv-Yafo',
            'Berlin',
            'Gdansk',
            'Beijing',
            'Cupertino',
            'Luxembourg',
            'Amsterdam',
            'Barcelona',
            'Chennai',
            'Irvine',
            'Mexico City',
            'Minneapolis',
            'Detroit',
            'Gurugram',
            'Haifa',
            'North Reading',
            'Taipei City',
            'Warsaw',
            'Atlanta',
            'Cambridge',
            'Edinburgh',
            'Nashville',
            'Palo Alto',
            'Reading',
            'Herndon',
            'Culver City',
            'Iasi',
            'Santa Clara',
            'Shanghai',
            'Denver',
            'Santa Monica',
            'Sydney',
            'Boulder',
            'Heredia',
            'Los Angeles',
            'San Jose',
            'San Luis Obispo',
            'Cape Town',
            'Helsinki',
            'Houston',
            'Miami',
            'Munich',
            'Paris',
            'Portland',
            'Salt Lake City',
            'Amman',
            'Aurangabad',
            'Cairo',
            'Chantilly',
            'Melbourne',
            'Milan',
            'Niagara-on-the-Lake',
            'Pennsylvania Furnace',
            'Pittsburgh',
            'Pune',
            'Santa Cruz',
            'Shenzhen',
            'Singapore',
            'Aachen',
            'Alberta',
            'Athens',
            'Berkeley',
            'Cagliari',
            'Cracow',
            'Dresden',
            'Durham',
            'Louisville',
            'Miami Beach',
            'Mumbai',
            'Raleigh',
            'Rome',
            'Santa Barbara',
            'Santiago',
            'Swansea',
            'Timisoara',
            'Tokyo',
            'Tubingen',
        ]

    @app_commands.command()
    @app_commands.checks.cooldown(1, 10, key=lambda i: (i.guild_id, i.user.id))
    async def ping(self, interaction: discord.Interaction) -> None:
        """Is Jeff Bezos still alive? Find out!"""
        await interaction.response.send_message(f'Pong! {round(self.bot.latency*1000)}ms')
    
    @ping.error
    async def on_ping_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.response.send_message(str(error), ephemeral=True)

    
    @app_commands.command()
    @app_commands.checks.cooldown(1, 10, key=lambda i: (i.guild_id, i.user.id))
    async def lookup(self, interaction: discord.Interaction, job_id: str):
        """Find out your team and location!"""
        if not job_id.isnumeric() or len(job_id) != 7:
            await interaction.response.send_message('Please provide a valid job ID', ephemeral=True)
        else:
            await interaction.response.send_message(
                f'Job ID: {job_id}\nTeam: {random.choice(self.teams)} | City: {random.choice(self.cities)}')
    
    @lookup.error
    async def on_lookup_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.response.send_message(str(error), ephemeral=True)


async def setup(bot):
    await bot.add_cog(Util(bot))