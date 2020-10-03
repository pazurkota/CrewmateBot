# ██████╗██████╗ ███████╗██╗    ██╗███╗   ███╗ █████╗ ████████╗███████╗    ██████╗  ██████╗ ████████╗
#██╔════╝██╔══██╗██╔════╝██║    ██║████╗ ████║██╔══██╗╚══██╔══╝██╔════╝    ██╔══██╗██╔═══██╗╚══██╔══╝
#██║     ██████╔╝█████╗  ██║ █╗ ██║██╔████╔██║███████║   ██║   █████╗      ██████╔╝██║   ██║   ██║   
#██║     ██╔══██╗██╔══╝  ██║███╗██║██║╚██╔╝██║██╔══██║   ██║   ██╔══╝      ██╔══██╗██║   ██║   ██║   
#╚██████╗██║  ██║███████╗╚███╔███╔╝██║ ╚═╝ ██║██║  ██║   ██║   ███████╗    ██████╔╝╚██████╔╝   ██║   
# ╚═════╝╚═╝  ╚═╝╚══════╝ ╚══╝╚══╝ ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝    ╚═════╝  ╚═════╝    ╚═╝   



import discord
import random 
from discord.ext import commands


client = commands.Bot(command_prefix = "c!")

@client.event
async def on_ready():
    print('Bot ready to use!')

@client.event #Show message when someone join the server
async def on_member_join(member):
    print(f'{member} Has joined a server!')

@client.event #Show message when someone left the server
async def on_member_remove(member):
    print(f'{member} Has left a server!')

# COMMAND SECTION #

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ["To pewne.", #c!8ball responses :D
                "Zdecydowanie tak",
                "Bez wątpienia",
                "Tak - zdecydowanie.",
                "Możesz na tym polegać.",
                "Tak, jak ja to widzę.",
                "Najprawdopodobniej.",
                "Dobra perspektywa.",
                "Tak.",
                "Znaki wskazują na tak.",
                "Odpowiedź niewyraźna, spróbuj ponownie.",
                "Zapytaj póżniej.",
                "Lepiej ci teraz nie mówić.",
                "Nie mogę teraz przewidzieć.",
                "Skoncentruj się i zapytaj ponownie.",
                "Nie licz na to.",
                "Moja odpowiedź brzmi: nie.",
                "Moje źródła mówią nie.",
                "Perspektywa niezbyt dobra.",
                "Bardzo wątpliwe."] 
    await ctx.send(f'Pytanie: {question}\nOpdowiedź: {random.choice(responses)}')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Użytkownik {member} został wyrzucony!\nPowód: {reason}')

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Użytkownik {member} został zbanowany!\nPowód: {reason}')

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users: 
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Użytkownik {user.name}#{user.discriminator} został odbanowany!')


client.run('NzYxNjEzMjIyMzg5MzUwNDUx.X3dJlg.vcZeKXYwbFdSJadh7uLN8E2Srxs') #Token required to bot normal working