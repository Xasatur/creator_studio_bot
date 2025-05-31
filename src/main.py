# main.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from src.data.db import init_db

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
COMMAND_PREFIX = os.getenv('COMMAND_PREFIX', '!')

# Set up intents (permissions)
intents = discord.Intents.default()
intents.message_content = True  # Needed to read message content
intents.members = True  # Needed for user-related features

# Initialize the bot
class CreatorStudioBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=COMMAND_PREFIX,
            intents=intents,
            help_command=None,  # We'll create our own help command
            description="A Discord bot for content creators"
        )

    async def setup_hook(self):
        # Load all cogs
        for filename in os.listdir('./src/cogs'):
            if filename.endswith('.py'):
                await self.load_extension(f'src.cogs.{filename[:-3]}')
                print(f'Loaded extension: {filename[:-3]}')

        # Initialize database
        init_db()
        print("Database initialized")

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

        # Set bot status
        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="for creator commands"
            )
        )

# Run the bot
bot = CreatorStudioBot()

if __name__ == '__main__':
    bot.run(TOKEN, log_handler=None)
