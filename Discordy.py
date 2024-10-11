# This example requires the 'message_content' intent.

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
    
    async def on_presence_update(before, after):
        print(after)
        


intents = discord.Intents.default()
intents.message_content = True
intents.presences = True 
intents.members = True

Token = input("Token:")
client = MyClient(intents=intents)
client.run(Token)
