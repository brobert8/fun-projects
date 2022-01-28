import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '.')

#for testing

@client.event
async def on_ready():
    print('Logged on as {0}!')

#alert for member join

@client.event
async def on_member_join(member):
    print(f'{member} is a has joined')

#alert for kick or remove

@client.event
async def on_member_remove(member):
    print('probobly got kicked')

#clear messages

@client.command()
async def clear(ctx, amount=5):
    if amount > 10:
        await ctx.send('no more than 10 at a time')
    else:
        await ctx.channel.purge(limit = amount)

#listCommands

@client.command()
async def helpMe(ctx):
    await ctx.send('Options are: \n .clear (amt) \n .ping \n .coinFlip \n .mike')

#for testing

@client.command()
async def ping(ctx):
    await ctx.send('pong')

#coinflip 50/50

@client.command()
async def coinFlip(ctx):
    responses = ['heads', 'tails']
    await ctx.send(f'{random.choice(responses)}')

#Mutes a Member From The server

@client.command(pass_context = True)
async def mute(ctx, *, member : discord.Member):
    '''Mutes A Memeber'''
    user_roles = [r.name.lower() for r in ctx.message.author.roles]

    if "admin" not in user_roles:
        return await client.say("You do not have the role: Admin")
    pass

    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    await client.edit_channel_permissions(ctx.message.channel, member, overwrite)

    await client.say("**%s** is now Muted! Wait For an Unmute.."%member.mention)

#Unmutes a member

@client.command(pass_context = True)
async def unmute(ctx, *, member : discord.Member):
    '''Unmutes The Muted Memeber'''
    user_roles = [r.name.lower() for r in ctx.message.author.roles]

    if "admin" not in user_roles:
        return await client.say("You do not have the role: Admin")
    pass

    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = True
    await client.edit_channel_permissions(ctx.message.channel, member, overwrite)

    await client.say("**%s** Times up...You are Unmuted!"%member.mention)


client.run(token)



client.run('hidden')
