import discord
from discord.ext import commands
from utils import *

intents = discord.Intents.default()
intents.message_content = True
intents.guild_messages = True
intents.members = True

bot = commands.Bot(command_prefix="!a", intents=intents)

bot.run(token)
