from lib2to3.pgen2 import token
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("TOKEN")
prefix = 'r/'
client = commands.Bot(command_prefix = prefix)

@client.event
async def on_ready():
    print("Estou Pronto")
    print(f"Ping {round(client.latency*1000)}ms")

for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        print('Carregando com sucesso o '+filename[:-3])
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)