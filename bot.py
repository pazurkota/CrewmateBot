# ██████╗██████╗ ███████╗██╗    ██╗███╗   ███╗ █████╗ ████████╗███████╗    ██████╗  ██████╗ ████████╗
#██╔════╝██╔══██╗██╔════╝██║    ██║████╗ ████║██╔══██╗╚══██╔══╝██╔════╝    ██╔══██╗██╔═══██╗╚══██╔══╝
#██║     ██████╔╝█████╗  ██║ █╗ ██║██╔████╔██║███████║   ██║   █████╗      ██████╔╝██║   ██║   ██║   
#██║     ██╔══██╗██╔══╝  ██║███╗██║██║╚██╔╝██║██╔══██║   ██║   ██╔══╝      ██╔══██╗██║   ██║   ██║   
#╚██████╗██║  ██║███████╗╚███╔███╔╝██║ ╚═╝ ██║██║  ██║   ██║   ███████╗    ██████╔╝╚██████╔╝   ██║   
# ╚═════╝╚═╝  ╚═╝╚══════╝ ╚══╝╚══╝ ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝    ╚═════╝  ╚═════╝    ╚═╝   


#--------------------------------------
#       Crewmate Bot main file
#
#         (C) PazurKOTA 2020
#--------------------------------------


#DO NOT DELETE THIS FILE! DELETING THIS FILE WILL OCCUR BOT WILL STOP WORKING!


import discord
import os
from discord.ext import commands, tasks
from itertools import cycle


client = commands.Bot(command_prefix = "c!")
status = cycle(['c!help. Have a very safe day!', 'c!help GitHub project: https://bit.ly/36NmeiN'])

@client.event
async def on_ready():
    change_status.start()
    print('Bot ready to use!')

@tasks.loop(seconds=30)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def load(ctx, extension):
        client.load_extension(f'cogs.{filename}')

@client.command()
async def unload(ctx, extension):
        client.unload_extension(f'cogs.{filename}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event 
async def on_member_join(member):
    print(f'{member} Has joined a server!')

@client.event 
async def on_member_remove(member):
    print(f'{member} Has left a server!')


client.run('NzYxNjEzMjIyMzg5MzUwNDUx.X3dJlg.GqZs3SK-3xwYaST-jXgrEU2U8vU') #BOT TOKEN. WARNING: DO NOT REMOVE OR BOT WILL NOT WORKING!