# main program
from generate import Key
from actions import Actions

key = Key()
MASTER_PASSWORD = key.code

auth = input("Master Password: ")

if auth == MASTER_PASSWORD:
    action = Actions()
    action.create()
    while True:
        print("\n"*2)
        print("Commands")
        print("add - Add Account to Storage")
        print("view - Display Saved Account")
        print("quit - Exit")
        cmd = input("\nEnter command: ")

        if cmd.upper() == "QUIT":
            break
        elif cmd.upper() == "ADD":
            action.add_account()
        elif cmd.upper() == "VIEW":
            action.get_all_accounts() # currently it can only view all all accounts
else:
    print("DENIED")
    
    