import discord, csv
class bot(discord.Client):
    async def on_ready(self):
        print(f"Succesfully logged on {self.user}!")




# ============================commands=============================
    async def on_message(self, msg):
        ctx = msg.channel
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
                await ctx.send("You are a admin!")
            else:
                await ctx.send("You are not a admin!")



        # register command
        if msg.content.startswith('!register'):
            userFile = open('data/users.csv', 'r')
            users = csv.DictReader(userFile)
            users = list(users)
            userFile.close()
            for user in users:
                if(user['id']==str(msg.author.id)):
                    await ctx.send("You are already registered!")
                    return
            userFile = open('data/users.csv', 'a')
            userFile.write(f'\n{msg.author.id},0')
            userFile.close()
            incomeFile = open('data/income.csv', 'a')
            incomeFile.write(f'\n{msg.author.id},1000,150')
            incomeFile.close()
            await msg.add_reaction('👍')


        # balance command
        if msg.content.startswith('!balance') or msg.content.startswith('!bal'):
            userFile = open('data/users.csv', 'r')
            users = csv.DictReader(userFile)
            users = list(users)
            userFile.close()
            for user in users:
                if(user['id']==str(msg.author.id)):
                    embed = discord.Embed(
                        title="Balance",
                        description=f"🪙 {user['bal']}",
                        color=discord.Color.red()
                    )
                    await ctx.send(embed=embed)
                    return
            await ctx.send("You are not registered!")


        # earn command
        if msg.content.startswith('!earn'):
            userFile = open('data/users.csv', 'r')
            users = csv.DictReader(userFile)
            users = list(users)
            userFile.close()
            for user in users:
                if(user['id']==str(msg.author.id)):
                    incomeFile = open('data/income.csv', 'r')
                    income = csv.DictReader(incomeFile)
                    income = list(income)
                    incomeFile.close()
                    for i in income:
                        if(i['id']==str(msg.author.id)):
                            user['bal'] = int(user['bal']) + int(i['base']) + int(i['capital'])
                            userFile = open('data/users.csv', 'w')
                            userFile.write('id,bal\n')
                            for user2 in users:
                                userFile.write(f'{user2["id"]},{user2["bal"]}\n')
                            userFile.close()
                            embed = discord.Embed(
                                title="Balance",
                                description=f"+ 🪙 {int(i['capital'])+int(i['base'])}",
                                color=discord.Color.green()
                            )
                            await ctx.send(embed=embed)
                            return
            await ctx.send("You are not registered!")

        





# ============================intents============================
intents = discord.Intents.default()
intents.message_content = True

# ============================start bot============================
client = bot(intents=intents)
token = open('data/token.txt', 'r').read()
client.run(token)