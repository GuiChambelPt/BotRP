import discord
import random
import os
from discord.ext import commands
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
DB = os.getenv("DB")
cluster = MongoClient(DB)

class Economia(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def trabalhar(self, ctx):
        db = cluster["DiscordBot"]
        collection = db["Users"]
        guild = str(ctx.guild.id)
        member = ctx.author
        id1 = str(ctx.author.id)
        results1 = collection.find_one({"_id": id1})
        if results1 == None:
            await ctx.send('Voce nao tem personagem, cria um com r/criarpersonagem')
        else:
            emprego = results1['Emprego']
            if emprego == "Desempregado":
                await ctx.send('Voce precisa arranjar um emprego!')
            if emprego == "Entregador":
                trabalhar1 = True
                while trabalhar1 == True:
                    await ctx.send('Digite trabalhar para trabalhar e end para terminar')
                    entregadormessage = await self.client.wait_for("message", check=lambda message: message.author == member)
                    if entregadormessage.content == "trabalhar":
                        dinheiro = random.randint(0,100)
                        collection.update_one({"_id": id1}, {"$inc":{"Dinheiro":dinheiro}})
                        await ctx.send('Voce trabalhou e ganhou `' + str(dinheiro) + "`")
                    if entregadormessage.content == "end":
                        await ctx.send('Acabando trabalho')
                        trabalhar1 = False



def setup(client):
    client.add_cog(Economia(client))