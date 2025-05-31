# src/cogs/error_handler.py
import discord
from discord.ext import commands
import traceback
import sys

class ErrorHandlerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """Handle command errors"""
        if isinstance(error, commands.CommandNotFound):
            return  # Ignore command not found errors

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Missing required argument: {error.param.name}")
            return

        if isinstance(error, commands.BadArgument):
            await ctx.send(f"Bad argument: {error}")
            return

        # Log all other errors
        print(f'Ignoring exception in command {ctx.command}:', file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

        await ctx.send("An error occurred while processing your command.")

    @commands.Cog.listener()
    async def on_application_command_error(self, interaction, error):
        """Handle slash command errors"""
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.response.send_message(
                f"This command is on cooldown. Try again in {error.retry_after:.2f} seconds.",
                ephemeral=True
            )
            return

        # Log all other errors
        print(f'Ignoring exception in application command {interaction.command.name}:', file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

        # If the interaction hasn't been responded to yet
        if not interaction.response.is_done():
            await interaction.response.send_message(
                "An error occurred while processing your command.",
                ephemeral=True
            )

async def setup(bot):
    await bot.add_cog(ErrorHandlerCog(bot))
