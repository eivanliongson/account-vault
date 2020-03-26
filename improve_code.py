# improved code
import sqlite3

class Account:
    def __init__(self,platform,username,password):
        self.platform = platform
        self.username = username
        self.password = password

class Commands:
    def add_account(self, account):
        pass
        
def connect_sqlite():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    try:
        c.execute(""" 
        create table accounts (
            platform text,
            username text,
            password text
        )
        """)
    except:
        pass

print('List of Commands')
for items in ['view', 'add']:
    print(items)
enter = input(': ').upper()