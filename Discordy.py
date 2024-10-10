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
    id = int('450867169581072394')
    member = discord.utils.get(message.guild.members, name='Korra122')

    print(member)

    """on_presence_update(before=Member.status, after=Member.status):
      if after.id == my_Member_id:
        print('{} changed status to {}'.format(
            after.display_name,
            after.status
        ))"""

Token = input("Token:")
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('MTI5Mjk2MzY2Mzc2NjA5ODAxMw.GaheI3.VKE5ISWmJ1Gwi5ksf1TlGsq9tapC60rZKe42gg')
