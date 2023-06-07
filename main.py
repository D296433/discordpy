import discord
class Client(discord.Client):
    async def on_ready(self):
        print(f"Succesfully logged on {self.user}!")





    async def on_message(self, message):
        print(f'{message.author}: {message.content}')
        if message.author == client.user:
            return
        if message.content.startswith('!ping'):
            await message.channel.send('Pong!')





# intents
intents = discord.Intents.default()
intents.message_content = True

# start bot
client = Client(intents=intents)
token = open('token.txt', 'r').read()
client.run(token)