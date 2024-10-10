# bot.py
import os

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
    
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


TOKEN = input("Token:")
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client = discord.Client()
client.run(TOKEN)
