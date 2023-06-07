import os, csv

isRunning = True
while(isRunning):
    os.system("cls")
    print("1. Add a new user")
    print("2. Delete a user")
    print("n. Forward a turn")
    choice = input("\nMake a choice: ").lower()
    if(choice=="1"):
        os.system("cls")
        print("1. Add a default user")
        print("2. Add a custom user")
        choose = input("\nMake a choice: ")
        if(choose=="1"):
            os.system("cls")
            name = input("Enter the user ID: ")
            usersFile = open("data/users.csv", "a")
            usersFile.write(name + ",1000,1000,y" + "\n")
            usersFile.close()
        elif(choose=="2"):
            os.system("cls")
            name = input("Enter the user ID: ")
            balance = input("Enter the balance: ")
            base = input("Enter the base: ")
            capital = input("Enter the capital: ")
            usersFile = open("data/users.csv", "a")
            usersFile.write(name + "," + balance + "," + base + "," + capital + "\n")
            usersFile.close()
        else:
            print("Invalid choice")
            input("\nPress enter to continue...")
    elif(choice=="2"):
        os.system("cls")
        name = input("Enter the user ID: ")
        usersFile = open("data/users.csv", "r")
        reader = csv.DictReader(usersFile)
        users = list(reader)
        usersFile.close()
        for user in users:
            if(user['id']==name):
                users.remove(user)
                break
        usersFile = open("data/users.csv", "w")
        usersFile.write("id,bal,base,capital\n")
        for user in users:
            usersFile.write(user['id'] + "," + user['bal'] + "," + user['base'] + "," + user['capital'] + "\n")
        usersFile.close()
    elif(choice=="n"):
        os.system("cls")
        usersFile = open("data/users.csv", "r")
        reader = csv.DictReader(usersFile)
        users = list(reader)
        usersFile.close()
        for user in users:
            if(user['capital']=="y"):
                user['bal'] = str(int(user['bal']) + int(user['base']) + 150)
            else:
                user['bal'] = str(int(user['bal']) + int(user['base']))
        usersFile = open("data/users.csv", "w")
        usersFile.write("id,bal,base,capital\n")
        for user in users:
            usersFile.write(user['id'] + "," + user['bal'] + "," + user['base'] + "," + user['capital'] + "\n")
        usersFile.close()