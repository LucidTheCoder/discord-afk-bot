import os
import discord

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    await bot.load_extension("commands.accounts")
    await bot.load_extension("commands.afk")

    synced = await bot.tree.sync()

    print(f"Synced {len(synced)} commands")


bot.run(TOKEN)