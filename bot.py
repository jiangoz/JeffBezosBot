import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()

PREFIX = os.getenv('PREFIX')
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX,
                   case_insensitive=True, intents=intents)


@bot.event
async def on_connect():
    appInfo = await bot.application_info()
    print(
        f'Bot Owner: {appInfo.owner.name}#{appInfo.owner.discriminator}  |  Bot Prefix: {PREFIX}')
    print('Successfully connected to Discord...')

    # load the cogs
    cogcount = 0
    coglist = ''
    for filename in os.listdir('./cogs'):
        cogName = filename[:-3]  # without the '.py' part
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{cogName}')
                cogcount += 1
                coglist += cogName + ' | '
            except commands.ExtensionError:
                pass

    print(f'Loaded {cogcount} cogs: {coglist[:-3]}')


@bot.event
async def on_ready():
    # load member count & server list
    serverlist = ''
    for guild in bot.guilds:
        serverlist += guild.name+' | '
    print(f'{len(bot.users)} members total')
    print(f'In {len(bot.guilds)} servers: {serverlist[:-3]}')

    print('\nBOT IS READY!')

# Run the bot
bot.run(TOKEN)
