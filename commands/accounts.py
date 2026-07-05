import discord
from discord import app_commands
from discord.ext import commands

from storage import accounts
from embeds import success, info, error


class Accounts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="list", description="Lists all accounts.")
    async def list_accounts(self, interaction: discord.Interaction):

        online = []
        offline = []

        for name, status in accounts.items():
            if status:
                online.append(f"• {name}")
            else:
                offline.append(f"• {name}")

        embed = discord.Embed(
            title="📋 Account List",
            color=discord.Color.blurple()
        )

        embed.add_field(
            name="🟢 Online",
            value="\n".join(online) if online else "None",
            inline=False
        )

        embed.add_field(
            name="🔴 Offline",
            value="\n".join(offline) if offline else "None",
            inline=False
        )

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="addaccount", description="Adds an account.")
    async def add_account(self, interaction: discord.Interaction, account_name: str):

        if account_name in accounts:
            await interaction.response.send_message(
                embed=error("Account Exists", f"`{account_name}` already exists.")
            )
            return

        accounts[account_name] = False

        await interaction.response.send_message(
            embed=success("Account Added", f"`{account_name}` was added.")
        )

    @app_commands.command(name="startaccount", description="Starts an account.")
    async def start_account(self, interaction: discord.Interaction, account_name: str):

        if account_name not in accounts:
            await interaction.response.send_message(
                embed=error("Unknown Account", f"`{account_name}` does not exist.")
            )
            return

        accounts[account_name] = True

        await interaction.response.send_message(
            embed=success("Account Started", f"`{account_name}` is now online.")
        )

    @app_commands.command(name="stopaccount", description="Stops an account.")
    async def stop_account(self, interaction: discord.Interaction, account_name: str):

        if account_name not in accounts:
            await interaction.response.send_message(
                embed=error("Unknown Account", f"`{account_name}` does not exist.")
            )
            return

        accounts[account_name] = False

        await interaction.response.send_message(
            embed=success("Account Stopped", f"`{account_name}` is now offline.")
        )


async def setup(bot):
    await bot.add_cog(Accounts(bot))