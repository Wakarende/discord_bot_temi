import discord
from dotenv import load_dotenv
import os
from discord import member
from discord.ext.commands import has_permissions, MissingPermissions


load_dotenv()

print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():

# Functionality
  general_channel = client.get_channel(878219278376124421)

  await general_channel.send('Bot is online')

@client.event
async def on_message(message):
  
  if message.content == 'what is the version':
    general_channel = client.get_channel(878219278376124421)

    myEmbed = discord.Embed(title='Current Version', description='The bot is in version 1.0', color=0x00ff00,)
    myEmbed.add_field(name='Version Code',value='v1.0',inline=False)
    myEmbed.add_field(name='Date Released', value='20/08/21', inline=False)
    myEmbed.set_footer(text='This is a sample footer')
    myEmbed.set_author(name='Temi')

    await general_channel.send(embed=myEmbed) 

# New Member 
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    # async def on_member_join(self, member):
    #     guild = member.guild
    #     if guild.system_channel is not None:
    #         to_send = f'Welcome {member.mention} to {guild.name}!'
    #         await guild.system_channel.send(to_send)

# Welcome New Users 
@client.event
async def on_member_join(member):
  guild = client.get_guild(878219278376124416)
  channel = guild.get_channel(878219278376124418)
  await channel.send(f'Welcome to Play with Temi Community {member.mention} ! :partying_face:, Ensure you read the rules and have a blast!')
  await member.send(f'Welcome to {guild.name}, {member.name} :partying_face:')


# Kick and Ban Members 
@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send(f'User {member} has been kicked')

@kick.error
async def kick_error(ctx,error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("You don't have persmission to kick people!")

@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member:discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await ctx.send(f'User {member} has been banned')

@ban.error
async def ban_error(ctx,error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("You don't have persmission to ban people!")



client.run(TOKEN)