import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

    async def on_presence_update(before: discord.Member, after: discord.Member):
        if after.id == my_Member_id:
            print('{} changed status to {}'.format(
                after.display_name,
                after.status
            ))

import os

import discord
from dotenv import load_dotenv

load_dotenv()
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

client.run(TOKEN)


mytoken = input("Token:")
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(mytoken)
