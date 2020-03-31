import random
import sqlite3


MASTERPASSWORD = 'supersecret'
prompt = input('MASTER PASSWORD: ')
if prompt != MASTERPASSWORD:
    print('Access Denied')
else:
    print('\n'*5 + 'Welcome!\nConnected..')

    connect = sqlite3.connect('database.db')
    c = connect.cursor()
    try:
        c.execute(""" 
        create table accounts(
            platform text,
            username text,
            password text
        )
        """)
    except:
        pass

    def add_account(accounts):
        with connect:
            c.execute("insert into accounts values (:platform, :username, :password)", 
                {"platform": accounts[0], "username": accounts[1], "password": accounts[2]})
                # dictionary key => value
            connect.commit()
        return '\nAccount Stored!'

    def view_account(platform):
        with connect:
            return c.execute("select * from accounts where platform = :platform", 
            {"platform":platform.upper()}).fetchall()

    def view_all():
        with connect:
            return c.execute("select * from accounts").fetchall()

    def update_password(platform, new):
        with connect:
            c.execute("update accounts set password = :password where platform = :platform",
                {"password": new, "platform": platform})
            connect.commit()
            return f'Updated Password!'

    def display(data, title):
        print(title)
        for items in data:
            print(items)

    while True:
        print('\nCommands:')
        for items in ['add', 'view','view all','update','quit']:
            print(items)
        
        command = input(': ').upper()
        if command == 'ADD':
            accounts = [input('\nPlatform: ').upper(),input('Username: '),input('Password: ')]
            print(add_account(accounts))
        elif command == 'VIEW':
            display(view_account(input("Platform: ").upper()), "Account Info")
        elif command == 'VIEW ALL':
            display(view_all(), 'All Accounts Saved')
        elif command == 'UPDATE':
            print(update_password(input("Platform: ").upper(), input("New Password: ")))
        elif command == 'QUIT':
            print('Goodbye!')
            break
        else:
            print('\nCommand not existing')
