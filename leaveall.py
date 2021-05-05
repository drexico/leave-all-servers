import discord
from discord.ext import commands, tasks





balls = discord.Client()   
balls= commands.Bot(command_prefix="nigga", self_bot=True)
balls.remove_command("help")
token = "token here"




@balls.event
async def on_connect():
    for guild in balls.guilds:
        try: 
             await guild.leave()
        except:
            print("Cannot Leave Server")

balls.run(token, reconnect=True, bot=False)
