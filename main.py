import discord, csv
class bot(discord.Client):
    async def on_ready(self):
        print(f"Succesfully logged on {self.user}!")




# ============================commands=============================
    async def on_message(self, msg):
        print(f'{msg.author}: {msg.content}')
        if msg.author == client.user:
            return
        if msg.content.startswith('!admin'):
            adminFile = open('data/admin.csv', 'r')
            admins = csv.DictReader(adminFile)
            admins = list(admins)
            adminFile.close()
            adminCheck = False
            for admin in admins:
                if(admin['perms']=="1" and admin['id']==str(msg.author.id)):
                    adminCheck = True
            if(adminCheck==True):
                await msg.channel.send("You are a admin!")
            else:
                await msg.channel.send("You are not a admin!")



        # register command
        if msg.content.startswith('!register'):
            userFile = open('data/users.csv', 'r')
            users = csv.DictReader(userFile)
            users = list(users)
            userFile.close()
            for user in users:
                if(user['id']==str(msg.author.id)):
                    await msg.channel.send("You are already registered!")
                    return
            userFile = open('data/users.csv', 'a')
            userFile.write(f'\n{msg.author.id},0')
            userFile.close()
            incomeFile = open('data/income.csv', 'a')
            incomeFile.write(f'\n{msg.author.id},1000,150')
            incomeFile.close()
            await msg.add_reaction('👍')

        





# ============================intents============================
intents = discord.Intents.default()
intents.message_content = True

# ============================start bot============================
client = bot(intents=intents)
token = open('data/token.txt', 'r').read()
client.run(token)