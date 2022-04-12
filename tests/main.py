import discord
import os
import datetime
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("TOKEN")
prefix = 'r/'
client = commands.Bot(command_prefix = prefix)

@client.event
async def on_ready(ctx):
    guild = str(ctx.guild)
    print(guild)
    print("Estou Pronto")
    print(f"Ping {round(client.latency*1000)}ms")

x = datetime.datetime.now()
print(x.strftime('%H:%M:%S %d-%m-%Y'))

client.run(TOKEN)