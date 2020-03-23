# main program
import generate
import commands

key = generate.Key()
MASTER_PASSWORD = key.code

# auth = input("Master Password: ")

auth = "123456"

list_of_commands = [
    "add - add account to storage",
    "list - list all platforms saved",
    "show account - get a specified account",
    "quit - quit"
]

if auth == MASTER_PASSWORD:
    action = commands.Commands()
    action.create()
    while True:
        print("\n"*2 + "Commands")
        for item in list_of_commands:
            print(item)
        cmnd = input("\ncmnd:  ")

        if cmnd.upper() == "QUIT":
            break
        elif cmnd.upper() == "ADD":
            action.add_account()
        elif cmnd.upper() == "SHOW ALL":
            action.get_all_accounts()
        elif cmnd.upper() == "SHOW ACCOUNT":
            action.get_account(input("Enter Platform: "))
else:
    print("DENIED")
    
    