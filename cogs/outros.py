import asyncio
import discord
import os
from discord.ext import commands
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
DB = os.getenv("DB")
cluster = MongoClient(DB)

class Outros(commands.Cog):
    def __init__(self, client):
        self.client = client


    # @commands.command(name="Prefixo")
    # @commands.is_owner()
    # async def prefix(self, ctx):
    #     guild = str(ctx.guild.id)
    #     db = cluster["DiscordBot"]
    #     collection = db["Guild"]
    #     member = ctx.author
    #     results1 = collection.find_one({"_id": guild})
    #     if results1 == None:
    #         await ctx.send('Voce tem que primeiro criar uma cidade primeiro r/criarcidade')
    #     else:
    #         prefixoatual = results1["Prefix"]
    #         await ctx.send('O prefixo atual e {} digite para qual voce quer mudar'.format(prefixoatual))
    #         prefixmessage = await self.client.wait_for("message", check=lambda message: message.author == member)
    #         newprefix = prefixmessage.content
    #         message = await ctx.send("Queres que o prefixo seja {}?".format(newprefix))
    #         await message.add_reaction("✅")
    #         await message.add_reaction("❌")
    #         check = lambda r, u: u == ctx.author and str(r.emoji) in "✅❌"  # r=reaction, u=user
    #         try:
    #             reaction, user = await self.client.wait_for("reaction_add", check=check, timeout=30)
    #         except asyncio.TimeoutError:
    #             await message.edit(content="Voce demorou demais timeout!")
    #             return
    #         if str(reaction.emoji) == "✅":
    #             await message.edit("Prefixo alterado para {}!!!".format(newprefix))
    #             collection.update_one({"_id": guild}, {"$set":{"Prefix":newprefix}})
    #         if str(reaction.emoji) == "❌":
    #             await message.edit(content="Ok cancelado")
            



def setup(client):
    client.add_cog(Outros(client))