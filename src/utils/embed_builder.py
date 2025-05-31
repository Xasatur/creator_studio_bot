# src/utils/embed_builder.py
import discord

def create_portfolio_embed(user, items):
    """Create an embed to display a user's portfolio"""
    embed = discord.Embed(
        title=f"{user.name}'s Portfolio",
        description="A showcase of creative work",
        color=discord.Color.blue()
    )

    embed.set_author(name=user.name, icon_url=user.avatar.url if user.avatar else None)

    # Add portfolio items
    for i, item in enumerate(items):
        if i >= 5:  # Limit to 5 items per embed
            embed.add_field(
                name="And more...",
                value=f"{len(items) - 5} more items not shown",
                inline=False
            )
            break

        embed.add_field(
            name=item["title"],
            value=item["description"],
            inline=False
        )

        # Add image to the first item only
        if i == 0 and "image_url" in item:
            embed.set_image(url=item["image_url"])

    embed.set_footer(text="Creator Studio Bot • Portfolio System")
    return embed
