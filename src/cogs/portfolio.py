# src/cogs/portfolio.py
import discord
from discord import app_commands
from discord.ext import commands
import os
from src.data.models import Portfolio, PortfolioItem
from src.utils.embed_builder import create_portfolio_embed

class PortfolioCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="portfolio",
        description="View your or someone else's portfolio"
    )
    async def portfolio(self, interaction: discord.Interaction, user: discord.User = None):
        """View a user's portfolio"""
        target_user = user or interaction.user

        # Placeholder for database query
        # In a real implementation, you would fetch from the database
        portfolio_items = [
            {"title": "Sample Artwork", "description": "A beautiful landscape", "image_url": "https://example.com/image.png"},
            {"title": "Character Design", "description": "Fantasy character concept", "image_url": "https://example.com/character.png"}
        ]

        # Create an embed to display the portfolio
        embed = create_portfolio_embed(target_user, portfolio_items)

        await interaction.response.send_message(embed=embed)

    @app_commands.command(
        name="portfolio_create",
        description="Create a new portfolio"
    )
    async def portfolio_create(self, interaction: discord.Interaction, name: str):
        """Create a new portfolio"""
        # Placeholder for database creation
        # In a real implementation, you would create in the database

        await interaction.response.send_message(f"Created portfolio: {name}")

    @app_commands.command(
        name="portfolio_add",
        description="Add an item to your portfolio"
    )
    async def portfolio_add(
        self,
        interaction: discord.Interaction,
        title: str,
        description: str,
        image: discord.Attachment
    ):
        """Add an item to your portfolio"""
        # Check if image is valid
        if not image.content_type.startswith('image/'):
            await interaction.response.send_message("Please upload an image file.")
            return

        # Placeholder for saving the image and database entry
        # In a real implementation, you would save the image and create a database entry

        await interaction.response.send_message(f"Added '{title}' to your portfolio!")

async def setup(bot):
    await bot.add_cog(PortfolioCog(bot))
