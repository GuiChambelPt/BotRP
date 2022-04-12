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
        print(results1)
        if results1 == None:
            await ctx.send('Primeiro crie um personagem')
        else:
            results1 = collection.find_one({"_id": id1}, {"BankAccount": 'True'})
            bankaccount = results1['BankAccount']
            if results1 == None:
                embedbank = discord.Embed(
                title="Banco ",
                colour=discord.Colour(0x33DDFF),
                )
                embedbank.add_field(
                    name="Cenas",
                    value="💵-Para ver quanto dinheiro tem \n💳-Para criar um cartao de credito \n📜-Para ver os extra",
                    inline=False
                )
                embedbank.set_footer(
                    text=f"Solicitado por {ctx.author.name}",
                    icon_url=f"{ctx.author.avatar_url}")
                message = await ctx.send(embed=embedbank)
                embedbank = discord.Embed(
                    title="Banco",
                    description="Voce nao tem uma conta deseja criar uma?",
                    colour=discord.Colour(0x33DDFF),
                )
                embedbank.set_footer(
                    text=f"Solicitado por {ctx.author.name}",
                    icon_url=f"{ctx.author.avatar_url}")
                message = await ctx.send(embed=embedbank)
                await message.add_reaction("✅")
                await message.add_reaction("❌")
            
            embedbank = discord.Embed(
                title="Banco ",
                colour=discord.Colour(0x33DDFF),
                )
            embedbank.add_field(
                    name="Cenas",
                    value="💵-Para ver quanto dinheiro tem \n💳-Para criar um cartao de credito \n📜-Para ver os extra",
                    inline=False
            )
            embedbank.set_footer(
                    text=f"Solicitado por {ctx.author.name}",
                    icon_url=f"{ctx.author.avatar_url}")
            message = await ctx.send(embed=embedbank)
            embedbank = discord.Embed(
                title="Banco ",
                colour=discord.Colour(0x33DDFF),
            )
            embedbank.add_field(
                    name="Cenas",
                    value="💵-Para ver quanto dinheiro tem \n💳-Para criar um cartao de credito \n📜-Para ver os extra",
                    inline=False
            )
            embedbank.set_footer(
                    text=f"Solicitado por {ctx.author.name}",
                    icon_url=f"{ctx.author.avatar_url}")
            message = await ctx.send(embed=embedbank)
            await message.add_reaction("💳")
            await message.add_reaction("📜")
            check = lambda r, u: u == ctx.author and str(r.emoji) in "✅❌"  # r=reaction, u=user
                try:
                    reaction, user = await self.client.wait_for("reaction_add", check=check, timeout=30)
                except asyncio.TimeoutError:
                    await message.edit(content="Voce demorou demais timeout!")
                    return
                if str(reaction.emoji) == "✅":
                    results2 = collection.find_one({"_id": id1})
                    dinheiro = results2("Dinheiro")
                    print(dinheiro)

                    await message.edit("Conta criada com sucesso".format())
                if str(reaction.emoji) == "❌":
                    await message.edit(content="Ok cancelado")

            results1 = collection.find_one({"_id": id1}, {"BankAccount": 'True'})
            print(type(results1))
            bankaccount = results1['BankAccount']
            if results1 == False:
                message = await ctx.send("Voce nao tem uma conta deseja criar uma(custa 1000$)")
                await message.add_reaction("✅")
                await message.add_reaction("❌")
                


def setup(client):
    client.add_cog(Economia(client))