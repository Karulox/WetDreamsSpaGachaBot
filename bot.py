import discord
import random
import os
import json
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot listo como {bot.user}')


@bot.command()
async def personaje(ctx):
    with open("personajes.json") as f:
        data = json.load(f)

    personaje = random.choice(data)

    embed = discord.Embed(
        title=personaje["nombre"],
        description=personaje["descripcion"],
        color=discord.Color.blue()
    )

    file = discord.File(personaje["imagen"], filename="img.png")
    embed.set_image(url="attachment://img.png")

    await ctx.send(embed=embed, file=file)

bot.run("TU_TOKEN_AQUI")