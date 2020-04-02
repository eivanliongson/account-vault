import random
import sqlite3
import string
from pyfiglet import Figlet

style = Figlet(font='slant')
MASTERPASSWORD = 'supersecret'
prompt = input('MASTER PASSWORD: ')
if prompt != MASTERPASSWORD:
    print('Access Denied')
else:
    print(style.renderText('The Vault!'))
    print('Welcome, Admin..')

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
        return f'\nAccount Stored for {accounts[0]}!'

    def view_account(platform):
        print("\nAccount Info\n")
        with connect:
            return c.execute("select * from accounts where platform = :platform", 
            {"platform":platform.upper()}).fetchall()

    def view_all():
        print("\nAll Accounts Saved\n")
        with connect:
            return c.execute("select * from accounts").fetchall()

    def update_password(platform, new):
        with connect:
            c.execute("update accounts set password = :password where platform = :platform",
                {"password": new, "platform": platform})
            connect.commit()
            return f'Updated Password for {platform}!'

    def delete_account(platform):
        with connect:
            c.execute("delete from accounts where platform = :platform",
                {"platform": platform})
            connect.commit()
            return f'{platform} Account Deleted'

    def generate_pass():
        code = string.ascii_letters + '123456789' + '!@#$%^&*'
        generated = [code[random.randint(0,len(code)-1)] for x in range(12)] # change 8 to how long your password
        return ''.join(generated)

    def display(data):
        for items in data:
            print(items[0] +'-'+ items [1] +'-'+ items[2])
            print('\n' + '-'*10)

    while True:
        print('\nCommands:')
        for items in ['add', 'view','view all','update','delete','generate','quit']:
            print(items)
        
        command = input(': ').upper()
        if command == 'ADD':
            accounts = [input('\nPlatform: ').upper(),input('Username: '),input('Password: ')]
            print(add_account(accounts))
        elif command == 'VIEW':
            display(view_account(input("Platform: ").upper()))
        elif command == 'VIEW ALL':
            display(view_all())
        elif command == 'DELETE':
            print(delete_account(input("Platform: ").upper()))
        elif command == 'UPDATE':
            print(update_password(input("Platform: ").upper(), input("New Password: ")))
        elif command == 'GENERATE':
            print('\nGenerated Password: ' + generate_pass())
        elif command == 'QUIT':
            print('Goodbye!')
            break
        else:
            print('\nCommand not existing')
