import asyncio
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

import asyncio
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



    @commands.command()
    async def banco(self, ctx):
        db = cluster["DiscordBot"]
        collection = db["Users"]
        id1 = str(ctx.author.id)
        results1 = collection.find_one({"_id": id1})
        if results1 == None:
            await ctx.send('Primeiro crie um personagem')
        else:
            results1 = collection.find_one({"_id": id1,"BankAccount": False})
            if results1 == None:
                message = await ctx.send("Voce nao tem uma conta deseja criar uma(custa 1000$)")
                await message.add_reaction("✅")
                await message.add_reaction("❌")
                check = lambda r, u: u == ctx.author and str(r.emoji) in "✅❌"  # r=reaction, u=user
                try:
                    reaction, user = await self.client.wait_for("reaction_add", check=check, timeout=30)
                except asyncio.TimeoutError:
                    await message.edit(content="Voce demorou demais timeout!")
                    return
                if str(reaction.emoji) == "✅":
                    
                    await message.edit("Conta criada com sucesso".format(newprefix))
                    collection.update_one({"_id": id1}, {"$set":{"Prefix":newprefix}})
                if str(reaction.emoji) == "❌":
                    await message.edit(content="Ok cancelado")
                else:
                    await ctx.send('')

        

def setup(client):
    client.add_cog(Economia(client))
        

def setup(client):
    client.add_cog(Economia(client))