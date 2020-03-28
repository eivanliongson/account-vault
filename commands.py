import sqlite3
from generate import Key

# hope someone could help me improve this

class Commands:
    def __init__(self):
        self.hold = ["Platform: ", "Username: ", "Password: "]
        self.conn = sqlite3.connect('database.db')
        self.c = self.conn.cursor()
        print("Connected! Hi there!")

    def create(self): # creates the table accounts
        try:
            self.conn.execute(""" 
            CREATE TABLE accounts(
                platform text,
                username text,
                password text
            )
            """)
        except: return 0


    def add_account(self): # add account to the database
        trig = Key()
        platform = input("\nEnter Platform: ").upper()
        username = input("Enter Username: ")
        print("GENERATE new PASSWORD or USE your own PASSWORD?")
        ans = input("GENERATE or USE: ").upper()
        if ans == "GENERATE":
            password = trig.generate()
        elif ans == "USE":
            password = input("Enter password: ")
            
        # sqlite command
        with self.conn:
            self.c.execute("insert into accounts values (:platform, :username, :password)", 
            {"platform": platform, "username": username, "password": password})
            # dictionary key => value
            self.conn.commit()
            print("*"*5)
            print ("\nSuccess!")

    def get_all_accounts(self):
        with self.conn:
            data = self.c.execute("select * from accounts").fetchall()
            return data
                

    def get_account(self, platform):
        get = platform
        with self.conn:
            data = self.c.execute("select * from accounts where platform = :platform", 
            {"platform": get.upper()}).fetchone()
            return data


    def list_all_platforms(self):
        with self.conn:
            data = self.c.execute("select platform from accounts").fetchall()
            return [items[0] for items in data]

    
    def add_account_gui(self, data):
        print(data)
        with self.conn:
            self.c.execute("insert into accounts values (:platform, :username, :password)", 
            {"platform": data[0], "username": data[1], "password": data[2]})
            # dictionary key => value
            self.conn.commit()
            print("*"*5)
            print ("\nSuccess!")

        
