import discord, csv
class Client(discord.Client):
    async def on_ready(self):
        print(f"Succesfully logged on {self.user}!")




# ============================commands=============================
    async def on_message(self, message):
        print(f'{message.author}: {message.content}')
        if message.author == client.user:
            return
        if message.content.startswith('!admin'):
            adminFile = open('data/admin.csv', 'r')
            admins = csv.DictReader(adminFile)
            admins = list(admins)
            adminFile.close()
            adminCheck = False
            for admin in admins:
                if(admin['perms']=="1" and admin['id']==str(message.author.id)):
                    adminCheck = True
            if(adminCheck==True):
                await message.channel.send("You are a admin!")
            else:
                await message.channel.send("You are not a admin!")





# ============================intents============================
intents = discord.Intents.default()
intents.message_content = True

# ============================start bot============================
client = Client(intents=intents)
token = open('data/token.txt', 'r').read()
client.run(token)