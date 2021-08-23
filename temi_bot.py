import discord
from dotenv import load_dotenv
import os


load_dotenv()

print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


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

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}!'
            await guild.system_channel.send(to_send)

intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)


client.run(TOKEN)