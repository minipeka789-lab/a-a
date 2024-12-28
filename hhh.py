import discord
from discord.ext import commands
from hola import a
intensiones=discord.Intents.default()
intensiones.message_content=True
bot=commands.Bot(command_prefix="/",intents=intensiones)
@bot.event
async def on_ready():
    print("el bot esta en linea")
@bot.command()
async def hola(ctx):
    await ctx.send("hola")
@bot.command()
async def adios(ctx):
    await ctx.send("adios")
@bot.command()
async def generador(ctx):
    b=a(8)
    await ctx.send(f"aqui esta tu contraseña {b}")
bot.run("")

