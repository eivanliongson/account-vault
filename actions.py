import sqlite3
from generate import Key

class Actions:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.c = self.conn.cursor()
        print("Connected!")

    def create(self): # creates the table accounts
        try:
            self.conn.execute(""" 
            CREATE TABLE accounts(
                platform text,
                username text,
                password text
            )
            """)
        except: print("*" * 5)


    def add_account(self): # add account to the database
        trig = Key()
        platform = input("\nEnter Platform: ")
        username = input("Enter Username: ")
        print("GENERATE new PASSWORD or USE your own PASSWORD?")
        ans = input("GENERATE or USE: ").upper()
        if ans == "GENERATE":
            password = trig.generate()
        elif ans == "USE":
            password = input("Enter password: ")
        

        # sqlite command
        self.c.execute("INSERT INTO accounts VALUES (:platform, :username, :password)", 
        {"platform": platform, "username": username, "password": password})
        # dictionary key => value
        self.conn.commit()
        print("*"*5)
        print ("\nSuccess!")

    def get_all_accounts(self):
        print(self.c.fetchall())