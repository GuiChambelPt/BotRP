import discord
import os
from discord.ext import commands
import pymongo
import datetime
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
DB = os.getenv("DB")
cluster = MongoClient(DB)

class Criar(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    @commands.is_owner()
    async def criarcidade(self, ctx):
        guild = str(ctx.guild.id)
        id1 = str(ctx.author.id)
        member = ctx.author
        db = cluster["DiscordBot"]
        collection = db["Guild"]
        results1 = collection.find_one({"_id": guild})
        if results1 == None:
            await ctx.send('Indique o nome da cidade')
            nomecidade = await self.client.wait_for(
                "message", check=lambda message: message.author == member
            )
            namecity = nomecidade.content
            results2 = collection.find_one({"CityName": namecity})
            if results2 == None:
                await ctx.send('Quer que a cidade se chame `' + nomecidade.content + "`")
                confirmmessage = await self.client.wait_for(
                    "message", check=lambda message: message.author == member
                )
                if "sim" in confirmmessage.content:
                    await ctx.send('Criando Cidade!')
                    post = {"_id": guild, "CityName": namecity, "Owner": id1, "Prefix":"r/"}
                    collection.insert_one(post)
                    await ctx.send('Cidade criada com sucesso ✅')
                if "nao" in confirmmessage.content:
                    await ctx.send('Ok!')
            else:
                await ctx.send('Ja existe um cidade com este nome!')
        else:
            await ctx.send('A cidade ja foi criada!')

    @commands.command()
    async def criarpersonagem(self, ctx):
        db = cluster["DiscordBot"]
        collection = db["Users"]
        member = ctx.author
        id1 = str(ctx.author.id)
        results1 = collection.find_one({"_id": id1})
        if results1 == None:
            await ctx.send("Criando personagem!")
            await ctx.send("Nome do personagem?")
            nomemessage = await self.client.wait_for(
                "message", check=lambda message: message.author == member
            )
            await ctx.send("Sobrenome do personagem?")
            sobrenomemessage = await self.client.wait_for(
                        "message", check=lambda message: message.author == member
            )
            await ctx.send("Idade do personagem?")
            idademessage = await self.client.wait_for(
                "message", check=lambda message: message.author == member
            )
            sobrenome=sobrenomemessage.content
            nome = nomemessage.content
            idade = idademessage.content
            empregopadrao = "Desempregado"
            await ctx.send("Confirma este dados? \n Nome:"+ nome+ "\n Sobrenome:"+ sobrenome +"\n Idade:"+ idade + "\n Emprego:"+ empregopadrao)
            confirmmessage = await self.client.wait_for(
                "message", check=lambda message: message.author == member
            )
            if "sim" in confirmmessage.content:
                x = datetime.datetime.now()
                data = x.strftime('%H:%M:%S %d-%m-%Y')
                post = {"_id": id1,"Nome": nome, "Sobrenome": sobrenome, "Idade": idade, "Emprego": "Desempregado", "Dinheiro":500,"Estado-Civil": "Solteiro", "Datadacriacao":data,"Casadocom": None,"BankAccount": "False", "BankAccountMoney": 0, "inventario":''}

                collection.insert_one(post)
                await ctx.send('Personagem Criado')
            if "nao" in confirmmessage.content:
                await ctx.send('Ok, deletando tudo!')
        else:    
            await ctx.send("Conta ja criada")
    @commands.command()
    async def infopersonagem(self, ctx, user: discord.Member=None):
        if user == None:
            user = str(ctx.author.id)
            userfinal1 = user.replace('<', '')
            userfinal2 = userfinal1.replace('!', '')
            userfinal3 = userfinal2.replace('@', '')
            userfinal = userfinal3.replace('>', '')
            user = userfinal
        else:
            user = str(user.id)
        id1 = str(ctx.author.id)
        db = cluster["DiscordBot"]
        collection = db["Users"]
        results1 = collection.find_one({"_id": user})
        if results1 == None:
            await ctx.send('Este usuario nao tem um personagem!')
        else:
            nome = results1['Nome']
            sobrenome = results1['Sobrenome']
            idade = results1['Idade']
            emprego = results1['Emprego']
            numcc = results1['_id']
            embedinfo = discord.Embed(
                title="Informacoes do Personagem",
                description="Nome: {}\n Sobrenome: {}\nIdade: {}\n Emprego: {}".format(nome, sobrenome, idade, emprego),
                colour=discord.Colour(0xFF9900),
                )
            embedinfo.set_footer(
                text=f"Solicitado por {ctx.author.name}",
                icon_url=f"{ctx.author.avatar_url}")
            await ctx.send(embed=embedinfo)
        
def setup(client):
    client.add_cog(Criar(client))
