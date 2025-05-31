# test_setup.py
import importlib.metadata
import discord
import sqlalchemy
import aiohttp
import PIL

print("Discord.py version:", discord.__version__)
print("SQLAlchemy version:", sqlalchemy.__version__)
print("python-dotenv version:", importlib.metadata.version("python-dotenv"))
print("aiohttp version:", aiohttp.__version__)
print("Pillow version:", PIL.__version__)
print("\nAll required packages are installed correctly!")
