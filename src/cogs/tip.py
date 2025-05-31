# src/cogs/tip.py
import discord
from discord import app_commands
from discord.ext import commands

class TipCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="tip_setup",
        description="Set up your tip system"
    )
    async def tip_setup(self, interaction: discord.Interaction, platform: str, link: str):
        """Set up your tip system"""
        # Validate the platform and link
        valid_platforms = ["paypal", "kofi", "buymeacoffee"]
        if platform.lower() not in valid_platforms:
            await interaction.response.send_message(f"Invalid platform. Please use one of: {', '.join(valid_platforms)}")
            return

        # This would save the tip link in the database
        await interaction.response.send_message(f"Tip system set up with {platform}!")

    @app_commands.command(
        name="tip",
        description="Tip a creator"
    )
    async def tip(self, interaction: discord.Interaction, user: discord.User):
        """Tip a creator"""
        # This would fetch the user's tip links from the database
        # For now, we'll use a placeholder

        embed = discord.Embed(
            title=f"Support {user.name}",
            description="If you enjoy their work, consider supporting them!",
            color=discord.Color.gold()
        )

        embed.set_thumbnail(url=user.avatar.url if user.avatar else None)
        embed.add_field(name="PayPal", value="[Donate via PayPal](https://paypal.me/example)", inline=False)
        embed.add_field(name="Ko-fi", value="[Buy them a coffee](https://ko-fi.com/example)", inline=False)

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(TipCog(bot))
