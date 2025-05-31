# test_setup.py
import discord
import sqlalchemy
import dotenv
import aiohttp
import PIL

print("Discord.py version:", discord.__version__)
print("SQLAlchemy version:", sqlalchemy.__version__)
print("python-dotenv version:", dotenv.__version__)
print("aiohttp version:", aiohttp.__version__)
print("Pillow version:", PIL.__version__)
print("\nAll required packages are installed correctly!")
