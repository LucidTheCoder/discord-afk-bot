import discord
from discord import app_commands
from discord.ext import commands

from embeds import success


class AFK(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="startafk", description="Starts the AFK process.")
    async def start_afk(self, interaction: discord.Interaction):

        await interaction.response.send_message(
            embed=success(
                "AFK Started",
                "Afking successfully started."
            )
        )


async def setup(bot):
    await bot.add_cog(AFK(bot))