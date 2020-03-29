# hope someone could help me improve this
import generate
import commands

key = generate.Key()
MASTER_PASSWORD = key.code

auth = input("Master Password: ")


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
        elif cmnd == "show all":
            print("Accounts")
            for items in action.get_all_accounts():
                print(items)
        elif cmnd.upper() == "LIST":
            print(action.list_all_platforms())
        elif cmnd.upper() == "SHOW ACCOUNT":
            print(action.get_account(input("Enter Platform: ")))
else:
    print("DENIED")
    
    